---
id: synthesis.imported-pinsker-inequality
kind: claim
version: 1
title: 'Imported: Pinsker''s inequality'
status: imported
region: synthesis
subject: entropy
tags: [entanglement, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'M. S. Pinsker, Information and Information Stability of Random Variables and Processes, Holden-Day, San Francisco (1964).'
  key: Pinsker1964
- citation: 'I. Csiszar, Information-type measures of difference of probability distributions and indirect observations, Studia Sci. Math. Hungar. 2 (1967), 299--318.'
  key: Csiszar1967
- citation: 'J. H. B. Kemperman, On the optimum rate of transmitting information, Ann. Math. Statist. 40 (1969), 2156--2177.'
  key: Kemperman1969
- citation: 'S. Kullback, A lower bound for discrimination information in terms of variation, IEEE Trans. Inform. Theory 13 (1967), 126--127.'
  key: Kullback1967
extraction:
  note: >-
    Imported for the eviction-deficit result, which uses the two-outcome case. That Pinsker proved
    the inequality with a weaker constant and that the sharp constant was found independently by
    Kullback, Csiszar and Kemperman was checked against the Wikipedia article on Pinsker's
    inequality; the bibliographic data of the four references are cited from memory, not checked
    against the source. The two-outcome case also has a one-line proof: f(p) = D((p, 1 - p) || (q, 1
    - q)) - 2 (p - q)^2 has f(q) = f'(q) = 0 and f''(p) = 1/(p(1 - p)) - 4 >= 0.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the eviction-deficit result can pin the two-outcome Pinsker inequality it cited from memory; history verified, references cited from memory.'
---

## formal
For probability distributions $P = (p_{i})$, $Q = (q_{i})$ on a finite set, with $D(P\|Q) = \sum_{i}p_{i}\ln(p_{i}/q_{i})$ in nats,
\[
D(P\,\|\,Q) \;\ge\; \tfrac12\Bigl(\sum_{i}|p_{i} - q_{i}|\Bigr)^{2},
\]
and the constant $\tfrac12$ is best possible. For two outcomes, $D\bigl((p, 1 - p)\,\|\,(q, 1 - q)\bigr) \ge 2(p - q)^{2}$ for all $p \in [0, 1]$ and $q \in (0, 1)$. \emph{Provenance:} \cite{Pinsker1964}, with the sharp constant from \cite{Csiszar1967, Kullback1967, Kemperman1969}.

## technical
Pinsker's inequality bounds the relative entropy of two probability distributions from below by the square of their total-variation distance: $D(P\|Q) \ge \tfrac12\|P - Q\|_{1}^{2}$ in nats, with the best constant. For two outcomes it reads $D \ge 2(p - q)^{2}$. Pinsker proved it with a weaker constant; the sharp form is due independently to Csiszár, Kullback and Kemperman.

## lay
Relative entropy measures how distinguishable two probability distributions are. Pinsker's inequality says it is at least half the square of the total difference between their probabilities, so distributions that differ noticeably always have a noticeable relative entropy. It is a standard result of information theory taken from the literature.

## one-liner
$D(P\|Q) \ge \tfrac12\|P - Q\|_{1}^{2}$ in nats with the best constant; for two outcomes $D((p, 1 - p)\|(q, 1 - q)) \ge 2(p - q)^{2}$.
