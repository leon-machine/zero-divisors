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

## The review service (stage 2)

`tp/review_server.py` is the page a reviewer uses. It runs on the standard library, like the
MCP server.

    python -m tp.review_server --store store --host 0.0.0.0 --port 8090

How a review is made:

1. **Review this result** on the site opens `/review/<result id>`: the result, and a form for
   the verdict, scope, depth, an objection's location and defect, conflicts, a note, the Zenodo
   opt-in, a contact email and acceptance of the reviewer terms (`docs/REVIEW_TERMS.md`).
2. **Sign in with ORCID to submit.** The server builds the signed part, recomputing the
   fingerprint from the store (a review of an out-of-date page is refused), takes its hash and
   sends the browser to ORCID with the hash as the nonce. It uses the authorisation-code flow,
   so the client secret never leaves the server, and a random state also set as a short-lived
   cookie, so the sign-in completes only in the browser that started it.
3. **ORCID returns** to `/callback`. The server exchanges the code for ORCID's id_token, checks
   its signature against `store/orcid_keys/`, its issuer, its audience and that its nonce is the
   hash, then runs the qualification check (`tp/qualify.py`).
4. **Published**: the entry goes to the open review log first, then the signed part goes to a
   new branch of the Physics Graph with a pull request (`tp/review_publish.py`). The contact
   email is kept only in the server's state folder, never in either repository.

Withdrawal (`/withdraw/<hash>`) and the maintainer's answer to an objection (`/answer/<hash>`)
work the same way; a withdrawal is accepted only from the reviewer's own iD and an answer only
from an iD in `reviews.maintainer_orcids`.

### Qualification rule version 1 (`tp/qualify.py`)

Any one route: a current employment whose source on the ORCID record is an organisation; or at
least `min_works` works that carry a DOI, were added by a client rather than typed in, have an
OpenAlex primary subfield in `subfields`, and (with `require_author_match`) list the reviewer's
iD among their authors in OpenAlex, so that linking someone else's paper does not count; or an
invitation (`invited`). The subfields are OpenAlex ids: Mathematical Physics 2610, Astronomy and
Astrophysics 3103 (where general relativity is filed), Nuclear and High Energy Physics 3106,
Atomic and Molecular Physics, and Optics 3107, Algebra and Number Theory 2602, Geometry and
Topology 2608. The record is read once per submission; ORCID's terms forbid polling.

### Configuration

`reviews.server` in `store/config.yaml`: `base_url` (the service's public address; the site
shows **Review this result** only once it is set), `orcid_base` (`https://orcid.org`, or
`https://sandbox.orcid.org` for a trial), `graph_repo`, `log_repo`, `privacy_contact`.
Secrets come from the environment only:

| Variable | What |
|---|---|
| `TP_ORCID_CLIENT_ID`, `TP_ORCID_CLIENT_SECRET` | the ORCID Public API client registered for `base_url` + `/callback` |
| `TP_GITHUB_TOKEN` | a token that can write the open review log and open pull requests on the Physics Graph (without it the service writes to local folders, for trials) |
| `TP_REVIEW_STATE` | the folder for contact emails (default `review-state`); keep it on a persistent volume |

The client id also goes in `reviews.orcid.client_ids`, so that `tp reviews check` accepts the
tokens.

### Before going live

- Register the production ORCID client for `base_url/callback`; add its id to the config.
- Create the open review log repository (`log_repo`) and give the service's token write access
  to it alone, plus pull-request access on the Physics Graph; check the log out beside the lab
  in CI (`reviews.log`).
- Show ORCID's official iD icon beside each iD (the site shows the full https://orcid.org/ link).
- Publish the privacy notice (`docs/PRIVACY.md`) with the privacy contact, and run the launch
  admin in the design document (ICO fee check, legitimate-interests assessment).
- Pending sign-ins are held in memory for 30 minutes: run one instance.
- Not yet built (stage 3): adjudication, lapse and reminder emails.
