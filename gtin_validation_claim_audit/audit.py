"""Offline documentation and Python source audit."""
import ast
import os
import re
from pathlib import Path

from .phrases import GTINVALIDATION, NOGTINVALIDATION, GENERIC_NAMES


def normalize(text):
    return ' '.join(text.lower().replace("n't", ' not').replace('-', ' ').split())


def _pattern(phrases):
    return re.compile(r'(?<!\w)(?:' + '|'.join(re.escape(p) for p in sorted(phrases, key=lambda x: (-len(x), x))) + r')(?!\w)')

YES = _pattern(GTINVALIDATION)
NO = _pattern(NOGTINVALIDATION)


def claims(text):
    lines = []
    fence = None
    for line in text.splitlines():
        m = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        lines.append(line)
    yes = no = False
    for paragraph in re.split(r'\n\s*\n', '\n'.join(lines)):
        value = normalize(paragraph)
        no |= bool(NO.search(value))
        yes |= bool(YES.search(NO.sub(' ', value)))
    return yes, no


def evidence(source):
    try:
        tree = ast.parse(source)
    except (SyntaxError, ValueError):
        return False
    imports = {}
    defined = set()
    bound = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            defined.add(node.name)
        elif isinstance(node, ast.Import):
            for a in node.names:
                imports[a.asname or a.name.split('.')[0]] = a.name if a.asname else a.name.split('.')[0]
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for a in node.names:
                imports[a.asname or a.name] = node.module + '.' + a.name
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.NamedExpr)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                bound.update(n.id for n in ast.walk(target) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store))
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            for item in node.items:
                if item.optional_vars:
                    bound.update(n.id for n in ast.walk(item.optional_vars) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store))
    shadow = defined | bound
    routes = {'stdnum.ean.validate', 'stdnum.ean.is_valid', 'gtin.validator.is_valid_GTIN', 'gtin.has_valid_check_digit', 'gtin.validate_check_digit'}
    def resolve(expr):
        if isinstance(expr, ast.Name):
            return imports.get(expr.id, '') if expr.id not in shadow else ''
        if isinstance(expr, ast.Attribute):
            base = resolve(expr.value)
            return base + '.' + expr.attr if base else ''
        return ''
    def root(expr):
        while isinstance(expr, ast.Attribute):
            expr = expr.value
        return expr.id if isinstance(expr, ast.Name) else None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Name):
            resolved = resolve(func)
            if resolved in routes or (resolved and resolved.rsplit('.', 1)[-1] in GENERIC_NAMES and func.id not in defined and resolved.rsplit('.', 1)[-1] not in defined):
                return True
        elif isinstance(func, ast.Attribute):
            base = root(func)
            if base in imports and base in shadow:
                continue
            if func.attr in defined:
                continue
            if resolve(func) in routes or func.attr in GENERIC_NAMES:
                return True
    return False


def audit(root, ignore=()):
    root = Path(root)
    if not root.is_dir():
        raise OSError('repository is not a readable directory: ' + str(root))
    docs = []
    production = []
    tests = []
    for current, dirs, files in os.walk(str(root), followlinks=False, onerror=lambda e: (_ for _ in ()).throw(e)):
        dirs[:] = sorted(d for d in dirs if not (Path(current) / d).is_symlink() and not any((Path(current) / d).relative_to(root).as_posix().startswith(p) for p in ignore))
        for name in sorted(files):
            path = Path(current) / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() or any(rel.startswith(p) for p in ignore):
                continue
            parts = path.relative_to(root).parts
            if (rel == 'README.md' or ('docs' in parts[:-1] and name.endswith('.md'))):
                docs.append(path)
            if name.endswith('.py') and not any(p in ('fixtures', 'docs', 'examples') for p in parts[:-1]):
                target = tests if 'tests' in parts[:-1] or name.startswith('test_') or name.endswith('_test.py') else production
                target.append(path)
    yes = no = False
    for path in docs:
        a, b = claims(path.read_text(encoding='utf-8'))
        yes |= a
        no |= b
    prod = any(evidence(p.read_text(encoding='utf-8')) for p in production)
    test = any(evidence(p.read_text(encoding='utf-8')) for p in tests)
    findings = []
    if yes and not prod:
        findings.append({'id': 'documented-gtin-validation-claim-false', 'severity': 'MEDIUM' if test else 'HIGH', 'message': 'Documented claim has ' + ('only test evidence' if test else 'no production evidence')})
    if no and prod:
        findings.append({'id': 'documented-no-gtin-validation-claim-false', 'severity': 'HIGH', 'message': 'Documented denial conflicts with production evidence'})
    return findings
