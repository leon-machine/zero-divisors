---
id: obj.sheaf.relatively-admissible-perturbation
kind: object
version: 2
title: Relatively admissible perturbation
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
  number: Def 9.4
  label: def:reladm
  line: 1210
extraction:
  env: definition
  context_refs:
  - sheaf.variable-weight-boundary-tameness-completion-forced
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [sheaf.stability-reduction-strict-diagonal-case]
    added_about: [obj.sheaf.variable-order-algebra-strict-diagonal-data]
    verdict: connected
    note: 'About from the stability theorem, the one result quantified over relatively admissible perturbations; the definition is stated in the variable-order algebra.'
---

## formal
Let $G$ be the weighted Gram of Theorem \claimref{sheaf.variable-weight-boundary-tameness-completion-forced}, dying slot $1$, nondegenerate slots $\{0,2,3\}$. A symmetric $\mathcal{A}$-bilinear perturbation $\Xi_\bullet$ (the letter avoiding the boundary $E$) is \emph{relatively admissible} if, for some $\delta > 0$: the entries on the nondegenerate slots lie in $\tau^\delta\mathcal{A}$; the mixed entries (dying slot against a nondegenerate slot) lie in $\varrho^{1/2}\tau^\delta\mathcal{A}$ (note $\varrho^{1/2} = \tau^{-p_1(x)} \in \mathcal{A}$); and the dying entry lies in $\varrho\,\tau^\delta\mathcal{A}$.

## technical
Take the weighted Gram $G$ of the variable-weight theory, with dying slot $1$ and nondegenerate slots $0, 2, 3$. A symmetric $\mathcal{A}$-bilinear perturbation $\Xi_\bullet$ is relatively admissible if, for some $\delta > 0$, each entry carries a factor $\tau^\delta$ beyond the weight of its slots: entries on the nondegenerate slots lie in $\tau^\delta\mathcal{A}$, mixed entries of the dying slot against a nondegenerate slot lie in $\varrho^{1/2}\tau^\delta\mathcal{A}$, and the dying entry lies in $\varrho\,\tau^\delta\mathcal{A}$, where $\varrho^{1/2} = \tau^{-p_1(x)}$ belongs to $\mathcal{A}$.

## lay
This definition says when a change to the weighted geometry near the singularity counts as small. Each entry of the change must be smaller, by a definite positive power of the distance to the boundary, than the natural size attached to its pair of directions. The dying direction carries a different natural size from the others.

## one-liner
A symmetric perturbation of the weighted Gram is relatively admissible when, for some $\delta > 0$, its entries lie in $\tau^\delta\mathcal{A}$, $\varrho^{1/2}\tau^\delta\mathcal{A}$ or $\varrho\,\tau^\delta\mathcal{A}$ according as they are nondegenerate, mixed or dying.
