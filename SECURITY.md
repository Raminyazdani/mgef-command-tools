# Security scope

The new CLI uses explicit input, validates IDs and refuses output overwrite.
Tests use fictional records and temporary directories. No record collections,
credentials, environment files or generated command outputs belong in this repo.
The preserved legacy scripts have less restrictive file behavior and should only
be used in an isolated scratch directory. No game-engine behavior is verified.
