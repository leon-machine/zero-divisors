---
id: obj.sheaf.log-completion
kind: object
version: 1
title: The log completion
status: defined
region: sheaf
subject: walls
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.variable-order-algebra-strict-diagonal-data
locators:
  paper: T04
  number: Def 9.8
  label: def:logcompletion
  line: 1252
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [sheaf.differential-closure-filtration-conormality]
    added_about: []
    verdict: connected
    note: 'The one result stated in the log completion is the differential-closure theorem.'
---

## formal
$\mathcal{A}^{\log}$ is the algebra of sums $\sum_{j,\ell} f_{j,\ell}(x,\tau)\,\tau^{e_j(x)}(\log\tau)^{\ell}$ over admissible exponent families (Definition \claimref{obj.sheaf.variable-order-algebra-strict-diagonal-data}), with $f_{j,\ell}$ smooth up to $\tau = 0$ and the log powers $\ell$ locally bounded (the index letter avoiding the radical section $k$).

## technical
The log completion $\mathcal{A}^{\log}$ enlarges the variable-order algebra by allowing powers of $\log\tau$. Its elements are sums $\sum_{j,\ell} f_{j,\ell}(x,\tau)\,\tau^{e_j(x)}(\log\tau)^{\ell}$ over admissible exponent families $\{e_j\}$, with coefficients $f_{j,\ell}$ smooth up to $\tau = 0$ and the log powers $\ell$ locally bounded.

## lay
Near the boundary, functions are described as sums of powers of the distance to it, with exponents that may vary from point to point. The log completion also allows each power to be multiplied by a power of the logarithm of that distance, with only a bounded number of logarithms in any region.

## one-liner
$\mathcal{A}^{\log}$ is the algebra of sums $\sum_{j,\ell} f_{j,\ell}\,\tau^{e_j(x)}(\log\tau)^{\ell}$ over admissible exponent families, with coefficients smooth up to $\tau = 0$ and locally bounded log powers.
