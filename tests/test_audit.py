import tempfile
import unittest
from pathlib import Path
from gtin_validation_claim_audit.audit import audit, claims, evidence
from gtin_validation_claim_audit.phrases import GTINVALIDATION, NOGTINVALIDATION, GENERIC_NAMES

class AuditTests(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((len(set(GTINVALIDATION)), len(set(NOGTINVALIDATION)), len(set(GENERIC_NAMES))), (50, 24, 24))
        for phrase in GTINVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NOGTINVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate gtin\n```\n\n`validate gtin`'), (True, False))
        self.assertEqual(claims('xvalidate gtinx'), (False, False))

    def test_library_routes(self):
        for module, functions in [('stdnum.ean', ['validate', 'is_valid']), ('gtin.validator', ['is_valid_GTIN']), ('gtin', ['has_valid_check_digit', 'validate_check_digit'])]:
            for fn in functions:
                shapes = ['import %s\n%s.%s(x)' % (module, module, fn), 'import %s as m\nm.%s(x)' % (module, fn), 'from %s import %s as f\nf(x)' % (module, fn)]
                if '.' in module:
                    package, child = module.split('.')
                    shapes += ['from %s import %s\n%s.%s(x)' % (package, child, child, fn), 'import %s\n%s.%s.%s(x)' % (package, package, child, fn)]
                for shape in shapes:
                    with self.subTest(shape=shape): self.assertTrue(evidence(shape))

    def test_generic_routes_and_shadows(self):
        for name in GENERIC_NAMES:
            for source in ['obj.%s(x)' % name, 'from other import %s as f\nf(x)' % name, 'obj = thing()\nobj.%s(x)' % name]:
                with self.subTest(source=source): self.assertTrue(evidence(source))
            self.assertFalse(evidence('def %s(x): pass\nobj.%s(x)' % (name, name)))
        for source in ['import stdnum.ean\nstdnum = 1\nstdnum.ean.validate(x)', 'import gtin as g\nwith x as g: pass\ng.validate_check_digit(x)', 'from stdnum.ean import validate as v\ndef v(x): pass\nv(x)']:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_not_evidence(self):
        cases = ['import stdnum.ean', 'validate(x)', 'is_valid(x)', 'validate_gtin(x)', 'x.validate(x)', 'x.is_valid_GTIN(x)', 'stdnum.ean.validate', 'import stdnum.ean\nstdnum.ean.compact(x)', 'import stdnum.ean\nstdnum.ean.calc_check_digit(x)', 'import gtin\ngtin.calculate_check_digit(x)', 'import gtin\ngtin.append_check_digit(x)', 'import gtin\ngtin.get_gcp(x)', 'import gtin\ngtin.GTIN(x)', 'import stdnum.isbn\nstdnum.isbn.validate(x)', 'import stdnum.issn\nstdnum.issn.to_ean(x)', 'barcode.EAN13(x)', 'barcode.EAN8(x)', 'barcode.EAN14(x)', 're.match(pattern, x)', 're.search(pattern, x)', 're.fullmatch(pattern, x)', 'len(x) == 13', 'x[:3] in prefixes', 'registry.lookup(x)', 'isbn.to_gtin(x)', 'registry.issue(x)', 'obj.validate_ean(x)', 'obj.validate_upc(x)', 'validators.url(x)', 'subprocess.run(["validate gtin"])', '"gtin validation"', 'def broken(']
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); readme = root / 'README.md'
            readme.write_text('validate gtin')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'tests').mkdir(); (root / 'tests/test_x.py').write_text('x.validate_gtin(a)')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')
            (root / 'code.py').write_text('x.validate_gtin(a)')
            self.assertEqual(audit(root), [])
            readme.write_text('no gtin validation')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'code.py').unlink(); self.assertEqual(audit(root), [])

    def test_exclusions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); (root / 'README.md').write_text('validate gtin')
            for folder in ('docs', 'fixtures', 'examples'):
                (root / folder).mkdir(); (root / folder / 'x.py').write_text('x.validate_gtin(a)')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'real.py').write_text('x.validate_gtin(a)')
            self.assertEqual(audit(root, ['real.py'])[0]['severity'], 'HIGH')
            self.assertEqual(audit(root), [])
