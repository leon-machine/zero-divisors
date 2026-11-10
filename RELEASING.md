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
   `python -m tp.layout`; commit anything they change.
2. Choose the tag, `vMAJOR.MINOR.PATCH`: `v1.0.0` for the first release; raise MINOR when results
   are added, corrected or restated; raise PATCH for corrections of wording, notation or citations.
3. Draft the release notes: `python -m tp release-notes vX.Y.Z`. It writes `releases/vX.Y.Z.md`,
   listing the results added, the corrections and restatements (each with the defect it fixed and
   who made it), other revisions, the results retired and everyone credited for the first time,
   all compared with the previous release. The same command adds every person credited in the
   store, other than the creators, to `contributors` in `.zenodo.json` (type Researcher, with the
   ORCID iD from their credit entry), leaving AI models out and keeping the entries already there;
   it prints the names it added, so check them. Add a line or two on the main changes where the
   comment says, then `python -m tp.site` and commit the notes, `.zenodo.json` and the site. The site shows every file in `releases/` on its
   Release notes page (from the Physics Graph menu).
4. On GitHub, Releases, Draft a new release: the tag from step 2, on `main`; paste the notes file
   (without its first line) as the description, and optionally Generate release notes below it for
   the list of merged pull requests; Publish. Zenodo issues the new version's DOI within minutes
   and keeps the description with the version.
5. Build and publish the public site from the tag (with `site_url` in `store/config.yaml` set to the
   site's public address, so shared links and link previews use it and each result gets its share
   page `site/r/<id>.html`):
   `git checkout vX.Y.Z && python -m tp.site`, then deploy `site/`, then `git checkout main`.
6. If the papers' deposits changed in the same period, record them first (before step 3) with
   `python -m tp.deposits record <code> --tex FILE --doi DOI --version V`, so the release carries them.

The history of the repository before its first public release is not kept.
