# Expert reviews

A qualified physicist or mathematician can review one result under their verified name:
endorse it or object to it, for one exact version, saying what they checked. Every review is
sealed by ORCID, so nobody, the author included, can forge, edit or bury it. The full design,
with the reasons for each rule, is the design document "Physics Graph: Expert Sign-off
Design".

This page covers the core that is built: the records, how they are checked, and the switch
that keeps them hidden until launch. The review page, the sign-in server and the open review
log's hosting are stage 2.

## The switch

```yaml
# store/config.yaml
reviews:
  enabled: false
```

With `enabled: false` (the default) nothing about reviews appears on the site or through
MCP: no reviews section, no disputed flag, and trust levels come from the front matter as
before. The records are still validated by `tp check` and in CI, so the core is exercised
before launch. Set it to `true` to show them.

## Where a review lives

Each record has two parts.

- The **signed part** is what the reviewer submitted: `store/reviews/<result id>/<hash>.yaml`,
  where `<hash>` is the SHA-256 of its canonical form (sorted-key, whitespace-free UTF-8
  JSON). Fields: `kind` (review, withdrawal, answer, ruling), `result`, `version`,
  `fingerprint`, `verdict`, `scope`, `depth`, `location`, `defect`, `conflicts`, `note`,
  `refers_to`, `terms`, `zenodo_credit`.
- The **attached part** holds everything identifying: the iD and name, ORCID's id_token and
  the qualification check. It lives only in the **open review log**, a separate repository
  (`reviews.log` in the config) with one file per record, `records/<hash>.json`, holding
  `signed`, `orcid`, `by`, `orcid_token`, `qualification` and `submitted`. Keeping it out of
  this repository means an identity can be removed on request without rewriting the Physics
  Graph's history.

The **fingerprint** is the SHA-256 of the result's substantive content with every premise pin
kept at its version: what the reviewer was shown. `tp reviews fingerprint <id>` prints it.

## What is checked (layer 1, every run)

| Code | Rule |
|---|---|
| E130 | the signed part has the right fields and values for its kind |
| E131 | the file is named by the hash of its signed part, under the result it concerns |
| E132 | the result exists, at or above the record's version |
| E133 | the open review log has a matching entry |
| E134 | ORCID's token verifies (RS256) against a key in `store/orcid_keys/` |
| E135 | the token's issuer and audience are accepted, its subject is the record's iD, and its nonce is the hash of the signed part |
| E136 | a withdrawal, answer or ruling refers to a record about the same result; a withdrawal comes from the same iD |
| E137 | an answer answers an objection and comes from an iD in `reviews.maintainer_orcids` |
| E138 | no accepted record has changed or gone (append-only) |
| E119 | front-matter `signoffs` (the retired `tp sign`) |
| E120 | a human trust level set by hand in the front matter |

The RSA check uses Python's own integers, with no third-party package. Token expiry is ignored
on purpose: the token attests what ORCID confirmed at submission.

## Append-only

`tp lock` writes `store/.tp-reviews-lock.json`: every accepted record and the SHA-256 of its
file. CI takes that lock, and `store/orcid_keys/`, from the base branch, so a pull request can
add reviews but cannot change or remove one, nor add an ORCID key of its own (a new ORCID key
is added in a pull request of its own, merged first). The only exceptions are records listed
in `store/reviews/redactions.yaml` (`hash`, `what: identity|text`, `date`, `reason`): an
identity removed on request, or abusive text removed from view.

## What a review means for a result

- A review is **current** when it is for the result's current version and its fingerprint
  matches; otherwise **stale**. A valid withdrawal by the same iD makes it **withdrawn**. A
  log entry marked `removed` makes it **removed** (no identity shown, no longer counted).
- **human-read**: a current endorsement. **human-checked**: a current endorsement from a
  qualified reviewer with `proof` in scope at depth `line-by-line`. A level earned by reviews
  replaces the front-matter level, except that `published` stays.
- A reviewer is **qualified** when the attached `qualification` names a route (employment,
  publications, invitation) under a rule version listed in `reviews.rule_versions`. The
  review server runs that check (stage 2).
- A result is **disputed** while a current objection from a qualified reviewer stands.
  Answers are recorded and checked; adjudication, lapse and their effect on the disputed flag
  are stage 3.

## Commands

    python -m tp reviews check        every record, the append-only rule, and whether reviews are shown
    python -m tp reviews hash FILE    the hash of a signed part (JSON or YAML)
    python -m tp reviews fingerprint ID
    python -m tp reviews add ENTRY    record by hand what the review server will write: the
                                      signed part into the store, the entry into the log,
                                      refused unless ORCID's token checks

`tp sign` is retired: it printed a name anyone could type.

## ORCID keys

`store/orcid_keys/orcid.org.json` is ORCID's published key set (https://orcid.org/oauth/jwks),
archived on 13 November 2026, with an `issuer` field added. When ORCID rotates its key, add the
new key set as another file and keep the old one, so that older tokens stay checkable.

## Before launch (stage 2)

- Register the production ORCID client and add its id to `reviews.orcid.client_ids`.
- Create the open review log repository; check it out beside the lab in CI (`reviews.log`).
- Show ORCID's official iD icon beside each iD, per ORCID's display guidelines (the core
  shows the full https://orcid.org/ link only).
- The review page, the sign-in server (authorisation-code flow), the qualification check,
  reminder emails, the privacy notice and the reviewer terms.
