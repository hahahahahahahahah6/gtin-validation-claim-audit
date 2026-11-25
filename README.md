# Global Trade Item Number claim audit

This offline static audit compares documented capability claims with Python source patterns. It reads the root README and Markdown under docs, excluding fenced blocks. It parses source without executing it and separates production and test evidence.

```sh
python3 -m pip install gtin-validation-claim-audit
gtin-validation-claim-audit audit . --fail-on high
python3 -m gtin_validation_claim_audit audit . --json
```

Use `--ignore PREFIX` repeatedly to exclude paths, and `--verbose` for a count. The default threshold is high; medium also fails on test-only evidence. Exit status is 0 for success, 2 for findings at the threshold, and 1 for usage or I/O errors. The version option prints the release number.

```text
documented-gtin-validation-claim-false
documented-no-gtin-validation-claim-false
```

A positive claim without production evidence is high severity, or medium when evidence exists only in tests. A denial conflicting with production evidence is high severity. A positive claim without any source files is high severity; a denial without source files passes.

## Differentiation

This audit does not cover checking whether input is checked at all (the generic validation family).

This audit does not cover checking whether a book number passes the ISBN-10 / ISBN-13 check digit (the ISBN-validation family).

This audit does not cover checking whether a serial number passes the ISSN check digit (the ISSN-validation family).

This audit does not cover checking whether a bank account number passes the IBAN check digit (the IBAN-validation family).

This audit does not cover checking whether a universally unique identifier string is well-formed (the UUID-validation family).

This audit does not cover checking whether a version string is a well-formed semantic version (the semver-validation family).

This audit does not cover checking whether a hardware address string is well-formed (the MAC-address-validation family).

This audit does not cover checking whether a bank identifier code is well-formed (the BIC-validation family).

This audit does not cover judging whether a schedule string is well-formed (the cron-expression-validation family).

This audit does not cover turning a schedule string into a human-readable sentence (the cron-expression-description family).

This audit does not cover running a job on a schedule (the scheduled-execution family).

This audit does not cover checking whether a date value is a real calendar date (the date-validation family).

This audit does not cover limiting how long a call may run (the timeout family).

This audit does not cover taking a payment from a card (the payment-processing family).

This audit does not cover reading card details out of a document (the credit-card-extraction family).

This audit does not cover proving who holds an account with a one-time code or a confirmation link (the auth family).

This audit does not cover verifying a password against a stored hash (authentication, not a judgement about a Global Trade Item Number string).

This audit does not cover hashing a password for storage (the password hashing libraries).

This audit does not cover minting a random password (password generation).

This audit does not cover password-protecting a PDF file (the PDF-encryption family).

This audit does not cover sending mail (the email family).

This audit does not cover sending a text to a number (the SMS family).

This audit does not cover reading data out of a document (the extraction families).

This audit does not cover decoding a code from an image (the barcode family).

This audit does not cover checking whether an email address is well-formed or deliverable (the email-validation family).

This audit does not cover checking whether a phone number is well-formed or valid for a region (the phone-number-validation family).

This audit does not cover judging how strong a password is (the password-strength family).

This audit does not cover judging whether JSON data conforms to a JSON Schema (the JSON-schema-validation family).

This audit does not cover checking whether a card number is a well-formed, Luhn-valid number of a recognised card brand (the credit-card-validation family).

This audit does not cover checking whether a bare host name is a well-formed domain name (the domain-validation family).

This audit does not cover checking whether a web address is well-formed (the URL-validation family).

This audit does not cover checking whether a numeric address is well-formed (the IP-address-validation family).

This audit does not cover decoding JSON text into a value.

This audit does not cover matching a pattern with a regex.

This audit does not cover splitting a web address into its parts (parsing, not a judgement about a Global Trade Item Number string).

This audit does not cover fetching a web address over the network.

This audit does not cover looking a name up in the DNS (resolution, not a judgement about a Global Trade Item Number string).

This audit does not cover encoding an account number into a barcode strip (the barcode-generation family).

This audit does not cover reading an account number out of a document (the extraction families).

This audit does not cover reading a vehicle number out of a registration document or an image (the extraction families — reading a number out is not judging whether it is well-formed).

This audit does not cover splitting a vehicle number into its manufacturer, descriptor, and identifier sections or looking up its make, model, and model year (decoding a number is not judging whether it is well-formed).

This audit does not cover asking a history service what a vehicle number's past is (a lookup is not a judgement about the string itself).

This audit does not cover judging whether a hexadecimal color string is well-formed (the hex-color-validation family).

This audit does not cover judging whether a researcher identifier string is a well-formed ORCID iD (the ORCID-validation family).

This audit does not cover judging whether a 16-digit International Standard Name Identifier is well-formed (the ISNI-validation family — a different identifier that shares a standards body with this family's identifier and nothing else).

This audit does not cover judging whether a digital object identifier names a work and resolves (DOI validation and resolution — a DOI names a work, never a trade item).

This audit does not cover judging whether a 9-character national identifier is well-formed on its own (CUSIP validation — the national part of a US security identifier, not a Global Trade Item Number).

This audit does not cover judging whether a 7-character London identifier is well-formed (SEDOL validation — a different identifier with its own check digit).

This audit does not cover judging whether a 12-character securities identifier string is well-formed (the ISIN-validation family — a different identifier that also uses a check digit, over a letter-expanded digit string and a different shape).

This audit does not cover fetching a security's record from a market-data service over the network (a record lookup, not a judgement about the string itself).

This audit does not cover reading a securities identifier out of a document (extraction, not a judgement about the string).

This audit does not cover judging whether a 15-digit device identifier string is well-formed (IMEI validation — a different identifier for mobile devices, with its own Luhn check digit).

This audit does not cover judging whether a 14-digit hexadecimal mobile identifier is well-formed (MEID validation — a different identifier for CDMA devices, with its own check digit).

This audit does not cover judging whether any serial number is well-formed in general (serial-number validation — wider than this family, with no check-digit leg).

This audit does not cover judging whether a 20-character legal-entity identifier string is well-formed (the LEI-validation family — a different identifier that also uses a check digit, over a different shape and a different algorithm).

This audit does not cover judging whether an EAN string is well-formed (the EAN-validation family — an EAN-13 code is the same numbering as a GTIN-13, but claims phrased with the EAN name are a separate family).

This audit does not cover judging whether a UPC string is well-formed (the UPC-validation family — a UPC-A code is a GTIN-12, but claims phrased with the UPC name are a separate family).

This audit does not cover translating a book number into a Global Trade Item Number or the reverse (identifier conversion, not a judgement about whether either string is well-formed).

This audit does not cover reading a GS1-128 barcode strip (barcode scanning, not a judgement about whether a Global Trade Item Number string is well-formed).

This audit does not cover reading the company prefix out of a Global Trade Item Number (prefix extraction, not a judgement about whether the string is well-formed).

This audit does not cover computing the final digit for a number without one (calculation, not a judgement about a complete string).

This audit does not cover appending a computed final digit to a number (construction, not a judgement about a complete string).

This audit does not cover encoding a number into an EAN-13 barcode strip (barcode generation, not a judgement about whether the number is well-formed).

This audit does not cover fetching a trade item's record from a GS1 registry service over the network (a record lookup, not a judgement about the string itself).

This audit does not cover fetching a legal entity's record from the GLEIF database or any registry service over the network (an entity lookup, not a judgement about the string itself).

This audit does not cover translating a securities identifier into a legal-entity identifier or the reverse (identifier conversion, not a judgement about whether either string is well-formed).

This audit does not cover issuing a new legal-entity identifier through a Local Operating Unit (registration, not a judgement about a given string).

This audit does not cover reading a legal-entity identifier out of a document or a photo (extraction, not a judgement about the string).

This audit does not cover the other claim-audit families in general (spreadsheet reading, spreadsheet generation, word-document reading, word-document generation, presentation reading, presentation generation, PDF extraction, PDF generation, PDF merging, PDF splitting, PDF rotation, PDF form-filling, PDF watermarking, PDF redaction, PDF compression, PDF annotation, table extraction, OCR, document extraction, e-signature, screen recording, video generation, QR code generation, barcode generation, barcode scanning, audio mixing, audio generation, audio editing, source separation, speech recognition, text-to-speech, noise suppression, music generation, and music transcription claims are NOT in the matching lists: this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only).

## Limitations

```text
validate gtin
```

The wording above can describe the capability being audited. But the wording above can also name a manual step in a runbook (the wording above), not code. A doc that means that is a false positive.

```text
gtin validation
```

The wording above can describe the capability being audited. But the wording above can also name a validation feature listed in a roadmap, not one the tool implements. A doc that means that is a false positive.

```text
gtin validator
```

The wording above can describe the capability being audited. But the wording above can also name a hosted web page that checks a pasted value, not the tool's own code. A doc that means that is a false positive.

```text
gtin check
```

The wording above can describe the capability being audited. But the wording above can also name a submission-system lint rule that only checks that an identifier field is present, not that it is well-formed. A doc that means that is a false positive.

```text
check gtin
```

The wording above can describe the capability being audited. But the wording above can also name a manual step in a runbook, not code. A doc that means that is a false positive.

```text
verify gtin
```

The wording above can describe the capability being audited. But the wording above can also name confirming that a displayed product is the right trade item, a visual step rather than a judgement about the string. A doc that means that is a false positive.

```text
gtin code validation
```

The wording above can describe the capability being audited. But the wording above can also name checking that a GTIN field is filled in at all, with no check-digit judgement behind it. A doc that means that is a false positive.

```text
valid gtin
```

The wording above can describe the capability being audited. But the wording above can also name an example value in docs (the wording above), with no validation capability at all. A doc that means that is a false positive.

```text
gtin is valid
```

The wording above can describe the capability being audited. But the wording above can also name example output text in docs, with no validation call behind it. A doc that means that is a false positive.

```text
gtin is invalid
```

The wording above can describe the capability being audited. But the wording above can also name example error text in docs, with no validation call behind it. A doc that means that is a false positive.

```text
gtin validity
```

The wording above can describe the capability being audited. But the wording above can also name a config flag or a column name, with no validation call behind it. A doc that means that is a false positive.

```text
gtin format validation
```

The wording above can describe the capability being audited. But the wording above can also name a format description in docs, with no validation code behind it. A doc that means that is a false positive.

```text
validate gtin number
```

The wording above can describe the capability being audited. But the wording above can also name judging whether any 14-digit string is well-formed, which is shape alone without the GS1 leg. A doc that means that is a false positive.

```text
gtin number validation
```

The wording above can describe the capability being audited. But the wording above can also name a spec section with no validation code behind it. A doc that means that is a false positive.

```text
validate gtin code
```

The wording above can describe the capability being audited. But the wording above can also name a manual step in a runbook, not code. A doc that means that is a false positive.

```text
check gtin code
```

The wording above can describe the capability being audited. But the wording above can also name a manual step in a runbook, not code. A doc that means that is a false positive.

```text
validate gtin identifier
```

The wording above can describe the capability being audited. But the wording above can also name a manual step in a runbook, not code. A doc that means that is a false positive.

```text
gtin identifier validation
```

The wording above can describe the capability being audited. But the wording above can also name a spec section with no validation code behind it. A doc that means that is a false positive.

```text
gtin product validation
```

The wording above can describe the capability being audited. But the wording above can also name a spec section with no validation code behind it. A doc that means that is a false positive.

```text
gtin number check
```

The wording above can describe the capability being audited. But the wording above can also name a checklist item in an onboarding guide, with no validation call behind it. A doc that means that is a false positive.

```text
gtin validation
```

The wording above can describe an external service rather than the project’s own code, producing a false positive. A human must judge the context.

```text
gtin
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
gtin number
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
validate identifier
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
check digit
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
mod 10
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
gs1
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
gs1 prefix
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
gcp
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
ean
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
upc
```

The wording above is not in the matching list because it alone does not establish the capability.

```text
barcode
```

The wording above is not in the matching list because it alone does not establish the capability.

A stdnum.ean compact call is NOT evidence: it strips separators and never raises and never returns a boolean — re-formatting a string is not judging it. That is a deliberate choice; the call shape is the fingerprint.

A stdnum.ean calc_check_digit call on its own is NOT evidence: computing a check digit for a number without one never judges a complete string. That is a deliberate choice; the call shape is the fingerprint.

A gtin calculate_check_digit / append_check_digit call on its own is NOT evidence: computing or appending a check digit never judges a complete string. That is a deliberate choice; the call shape is the fingerprint.

A gtin.get_gcp call on its own is NOT evidence: reading the company prefix out of a number never judges whether the number is well-formed. That is a deliberate choice; the call shape is the fingerprint.

A gtin.GTIN class construction on its own is NOT evidence: the published description shows construction normalising and padding numbers rather than rejecting an invalid check digit, so its invalid-input behaviour is not established from the published text. That is a deliberate choice; the call shape is the fingerprint.

A digit string with an unassigned GS1 prefix is judged valid by the library when its check digit is correct: stdnum.ean.validate does not check whether a known GS1 prefix or company identifier is referenced, so a number such as 9999999999994 passes when its final digit matches the computed check digit, even though no such prefix is assigned. That is a deliberate limitation of the evidence route, not of this tool.

The library accepts only the four GTIN lengths: stdnum.ean.validate raises InvalidLength for any other length, so a 7-digit string such as 9780471 and a 15-digit string such as 978047111709456 are rejected even though a check digit could be computed for them. That is a deliberate property of the evidence route, not of this tool.

A GS1 registry lookup call is NOT evidence: it fetches a trade item's record from a GS1 service or any registry service over the network, and a lookup says the number exists in a database, not whether the string itself is well-formed. That is a deliberate choice; the call shape is the fingerprint.

An ISBN-to-GTIN conversion call is NOT evidence: it translates one identifier into another and never judges whether either is well-formed. That is a deliberate choice; the call shape is the fingerprint.

A GTIN registration / issuance call is NOT evidence: a GS1 member organisation issuing a new GTIN creates an identifier, never judges whether a given string is well-formed. That is a deliberate choice; the call shape is the fingerprint.

A lone length check on the number is NOT evidence: checking that the string is 8, 12, 13, or 14 characters without the check digit is a length check, not a validity judgement. That is a deliberate choice; the call shape is the fingerprint.

A lone GS1-prefix membership check is NOT evidence: checking that the first digits are a known GS1 prefix without the check digit is a membership check, not a validity judgement. That is a deliberate choice; the call shape is the fingerprint.

A lone mod-10 checksum call on a string with no GTIN leg is NOT evidence: a bare mod-10 check judges any digit string, never a GTIN on its own. That is a deliberate choice; the call shape is the fingerprint.

A re.match call on a GTIN pattern alone is NOT evidence: matching characters accepts malformed strings and rejects nothing by library validation, because a regex never validates through a library call. That is a deliberate choice; the call shape is the fingerprint.

A .validate call on a base that is not a stdnum-ean base is missed, even when the base holds an identifier object built in another module or through a helper the tracer cannot follow. The tool checks the call shape, not the value.

A bare import of a capability library with no call is not evidence, even when the import is the only thing the module does.

A doc that claims the checked capability in a roadmap, changelog, or TODO is still a claim: the tool reads prose, not intent.

A doc that denies the checked capability with a phrase outside the denial list (for example a paraphrase the list does not contain) is not recognised as a denial and the claim side still fires if a claim phrase is present.

A claim in a file that is not the root README.md and has no `docs` path component is not read at all (for example a claim in a top-level CHANGELOG.md is invisible to the tool).

Evidence split across two modules is not evidence: each route must sit in a single module, even when the two halves obviously belong together.

A route call on a name the module locally defines (a function, method, or class with the same name) is shadowed and does not count, even when the local definition is a thin wrapper around the real library call.

Dead code counts: a validation route in a function that is never called is still evidence, because the tool reads code, not execution.

A subprocess call that shells out to an external identifier checker is NOT evidence by design: a shell command name in a string literal is never evidence.

A single generic input check with no GTIN leg is not evidence, even when the checked input happens to be a GTIN string: checking that input exists says nothing about judging whether it is well-formed, and this family covers the capability only.

A single email validation call with no GTIN leg is not evidence, even when the validated address sits next to a GTIN field: email addresses are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single phone number validation call with no GTIN leg is not evidence, even when the validated number sits next to a GTIN field: phone numbers are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single URL validation call with no GTIN leg is not evidence, even when the validated address contains a GTIN string: web addresses are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single IP address validation call with no GTIN leg is not evidence, even when the validated address sits next to a GTIN field: numeric addresses are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single domain validation call with no GTIN leg is not evidence, even when the validated name sits next to a GTIN field: host names are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single ISBN validation call with no GTIN leg is not evidence, even when the validated number sits next to a GTIN field: book numbers are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single ISSN validation call with no GTIN leg is not evidence, even when the validated number sits next to a GTIN field: serial numbers are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single IBAN validation call with no GTIN leg is not evidence, even when the validated number sits next to a GTIN field: bank account numbers are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single ISIN validation call with no GTIN leg is not evidence, even when the validated number sits next to a GTIN field: securities identifiers are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single IMEI validation call with no GTIN leg is not evidence, even when the validated identifier sits next to a GTIN field: device identifiers are a different capability, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

A single EAN-named generic call with no GTIN leg is not evidence, even when the validated number is a GTIN-13: EAN-named claims belong to a separate family, and this family covers GTIN-named claims only.

A single UPC-named generic call with no GTIN leg is not evidence, even when the validated number is a GTIN-12: UPC-named claims belong to a separate family, and this family covers GTIN-named claims only.

A single barcode-generation EAN-13 encoding call with no GTIN leg is not evidence, even when the encoded number is a GTIN-13: encoding a number into a barcode strip prints it, never judges whether it is well-formed, and this family covers judging whether a Global Trade Item Number string is a well-formed GTIN only.

