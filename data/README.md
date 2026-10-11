# Mirrored basis payloads

This directory is the direct-use side of the database contract. A set is
copied here only after the database marks it `publishable` and records a
reciprocal calculation with public inputs, final outputs, full ABACUS and
LibRPA commits, and redistribution terms. The current release manifest is
empty because the imported historical records still lack at least one of
those requirements. Historical PP/NAO/ABF files remain in the database for
auditing and are not silently promoted to downloadable recommendations.

When the first set is released, store its payload under
`payloads/<set-id>/`, add its role, source database path, and SHA-256 to
`release-manifest.json`, update `database_commit`, and run the release
validator against that database checkout.
