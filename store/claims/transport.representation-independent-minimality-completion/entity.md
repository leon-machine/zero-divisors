---
id: transport.representation-independent-minimality-completion
kind: claim
version: 4
title: Representation-independent minimality of the completion
status: proved
region: transport
subject: completion
tags: [conformal-model, transport-algorithm, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.normalised-conformal-chart
derivations:
- name: main
  uses:
  - transport.conformal-gram-matrix@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_chart_in_the_model_equality_case
- kind: check
  ref: check.py::check_larger_hosts_split_off_the_chart
- kind: check
  ref: check.py::check_smaller_hosts_admit_no_chart
locators:
  paper: T01
  number: Thm 4.19
  label: thm:chartmin
  line: 987
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the chart in the model with signature (p+1,q+1), splitting in larger hosts, and the inertia exclusion of smaller hosts. Version 2 -> 3. Check strengthened: chart rank n + 2 and extra-block rank m asserted, so the block is the whole complement; ambient Gram built from sq directly; samples moved to module level. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise, the conformal Gram matrix lemma, which the proof uses for the rank and signature count.'
---

## formal
Let $(\mathbb{V}'', Q'')$ be nondegenerate of signature $(p'', q'')$ and suppose its null cone admits a normalised conformal chart of $(\mathbb{V}, Q)$. Then
\[
p'' \geq p + 1 \quad \text{and} \quad q'' \geq q + 1 ;
\]
in particular $\dim \mathbb{V}'' \geq n + 2$, and in case of equality the signature is exactly $(p{+}1, q{+}1)$ and $\Cl(\mathbb{V}'') \cong \Cl(p{+}1, q{+}1)$. Consequently the minimality of the completion is a property of the ambient quadric alone: no Clifford algebra whose quadratic space is smaller than, or differently balanced than, $(p{+}1, q{+}1)$ can host the point-level resolution, \emph{however} $\Cl(p,q)$ is embedded in it as an algebra.

## technical
Let $(\mathbb{V}'', Q'')$ be nondegenerate of signature $(p'', q'')$, and suppose its null cone carries a normalised conformal chart of $(\mathbb{V}, Q)$, a map $\Phi$ with $\Phi(x) \cdot \Phi(y) = -\frac12 Q(x - y)$. Then $p'' \geq p + 1$ and $q'' \geq q + 1$, so $\dim \mathbb{V}'' \geq n + 2$, and in the equality case the signature is exactly $(p{+}1, q{+}1)$ and $\Cl(\mathbb{V}'') \cong \Cl(p{+}1, q{+}1)$.

The minimality of the completion is thus a property of the ambient quadric alone: no Clifford algebra whose quadratic space is smaller than, or differently balanced than, $(p{+}1, q{+}1)$ can host the point-level resolution, however $\Cl(p,q)$ is embedded in it as an algebra.

## lay
One might hope to repair a geometry inside some smaller algebra by placing the original algebra in it in an unusual way. This result rules that out. What the repair needs is room for the points of the geometry together with their separations, and that requires at least one extra positive and one extra negative direction, whatever the embedding.

## one-liner
Any nondegenerate quadratic space whose null cone carries a normalised conformal chart of $(\mathbb{V}, Q)$ has $p'' \geq p + 1$ and $q'' \geq q + 1$, so the minimality of the completion does not depend on how $\Cl(p,q)$ is embedded.
