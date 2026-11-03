# legacy/

Snapshots of the series' verify scripts (`verify_*.py`) that store claims cite as `legacy`
evidence, with the `GA.py` they import. They belong to the papers and are maintained in
TP_Papers_Suite (most at its root, a few under `Claude outputs/`); the copies here let the store
be checked anywhere, including in CI.

When a paper's verify script changes, copy the new version here in the same commit as any store
change that depends on it. To check against the live copies instead, set TP_LEGACY_DIR to the
folder that holds them.
