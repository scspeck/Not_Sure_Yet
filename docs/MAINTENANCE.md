# Maintenance guide

## Routine
Keep `main` deployable; use issues for substantive bugs/features; regression-test every filtering/rendering change; re-test the large example dataset; check the browser console; periodically verify external services; and update docs when behavior changes.

## Versioning
Use semantic versioning: patch for compatible bug fixes, minor for compatible features, major for breaking changes.

## Example data
Preserve raw provenance separately. Rebuild the web example through a documented transformation script and update query/export dates, row counts, exclusions, and changelog.

## Services and keys
Optional services must fail without breaking core functions. Never commit private API keys.

## Release
Complete `RELEASE_CHECKLIST.md`, update version/changelog, validate `CITATION.cff`, tag/publish the GitHub release, archive it, and verify archival metadata.
