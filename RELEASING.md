# Releasing the Physics Graph

`main` changes whenever a pull request is merged or the maintainer edits the store. That is not a
release: nothing is archived and the public site does not change. A release is a deliberate step,
taken when enough has been merged to be worth a new version.

## What a release does

- **Zenodo:** publishing a GitHub release archives a snapshot of the repository at its tag as a
  new version of the Zenodo record "Zero Divisors: Physics Graph" (metadata in `.zenodo.json`).
  All versions share one DOI for the record as a whole, and each version has its own. Files marked
  `export-ignore` in `.gitattributes` are left out of the snapshot. A published version's files
  cannot be changed; only its description can.
- **The public site** is built from the release tag, so it shows exactly what was archived. Its
  Documents page names the release it was built from.

## One-off set-up

1. The repository is public (Zenodo archives public repositories).
2. On zenodo.org, sign in with GitHub, open the account's GitHub page and switch the repository on.
3. Optional: rehearse on sandbox.zenodo.org first; versions on Zenodo cannot be deleted.

## Each release

1. On `main`: `python -m tp check --store store --keep-going`, the unit tests, `python -m tp build`,
   `python -m tp.layout`, `python -m tp.site`; commit anything they change.
2. On GitHub, Releases, Draft a new release:
   - a new tag, `vMAJOR.MINOR.PATCH`: `v1.0.0` for the first release; raise MINOR when results are
     added or changed in substance; raise PATCH for corrections of wording, notation or citations;
   - Generate release notes (the merged pull requests since the last release), and add a line on
     the main changes;
   - Publish. Zenodo issues the new version's DOI within minutes.
3. Build and publish the public site from the tag (with `site_url` in `store/config.yaml` set to the
   site's public address, so shared links and link previews use it and each result gets its share
   page `site/r/<id>.html`):
   `git checkout vX.Y.Z && python -m tp.site`, then deploy `site/`, then `git checkout main`.
4. If the papers' deposits changed in the same period, record them first with
   `python -m tp.deposits record <code> --tex FILE --doi DOI --version V`, so the release carries them.

The history of the repository before its first public release is not kept.
