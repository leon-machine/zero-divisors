---
id: dark-matter.unit-ball-rule
kind: claim
version: 6
title: The unit-ball rule
status: proved
region: dark-matter
subject: dark-matter
tags:
- dark-matter-ratio
- counting-rules
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Fable 5.2
  role: 'the two registered conditions (single-ideal clause, population of the odd towers) assumed; the sourcing lemma used; statement of what the total rests on'
  version: 6
  source: maintainer pass of 2026-11-10
review: typed
derivations:
- name: main
  uses:
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.towers-are-residues-single-clock-filter@5
  assumes:
  - dark-matter.odd-towers-populated@1
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  - dark-matter.r3-one-cell-per-unshared-direction@2
  - dark-matter.single-ideal-at-residues-zero-and-four@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_shares
- kind: check
  ref: check.py::check_dark_towers_and_dimensions
- kind: check
  ref: check.py::check_total
locators:
  paper: T14
  number: Prop 7.6
  label: prop:rule
  line: 821
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 5 -> 6. Leon''s decision 5 of 10 November 2026: assumes edges added to the two conditions registered that day, dark-matter.single-ideal-at-residues-zero-and-four and dark-matter.odd-towers-populated, which the closed form held only as text. A uses edge to the sourcing lemma dark-matter.projection-every-towers-content-dilutes-ones is added: the proof and R3 are phrased in the sourcing rule, and without the edge P1 was missing from the cone. A paragraph ''What the total rests on'' states what the audit of the cone found (the postulates under the closed form, R2 entering twice, the total a fit of two shares against one measured number, and which ingredients were chosen with the number known, quoting dark-matter.status-rule and dark-matter.which-towers-are-populated only). R3 repinned 1 -> 2 after its unit was stated (each tower''s own cell radius; under R2 the common unit used here), the use holding as cited. Arithmetic and check unchanged; coverage.yaml records the three new premises as untouched.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the shares V_3/V_D under R1 to R3, the five dark towers'' dimensions, and the total (11 pi + 16)/(3 pi) against the record. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    - dark-matter.r3-one-cell-per-unshared-direction
    - dark-matter.towers-are-residues-single-clock-filter
    note: 'R1 to R3 added as assumes since the statement is under them; the residue census added as the
      source of the representatives'' dimensions in the sum, a judgement call since the paper does not
      cite it in the proof. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.towers-are-residues-single-clock-filter
  small_findings_pass:
    by: ai-small-findings-pass
    date: '2026-10-22'
    finding: CONTRADICTIONS_VALUES M11
    note: 'Every level now says the agreement with 5.364 is a fit, as dark-matter.status-rule records
      (found by solving for the observed value; one of fourteen equally simple candidates). The arithmetic
      is unchanged: V3/V2 = 4/3, V3/V4 = 8/(3 pi), 1 + 8/3 + 16/(3 pi) = (11 pi + 16)/(3 pi). Suggested
      maintainer edge: dark-matter.status-rule comments_on this rule.'
    open_problem: op.small-findings
  open_problem: op.small-findings
---

## formal
Under R1 to R3, with the four odd towers populated (Premise \claimref{dark-matter.odd-towers-populated}) and residues $0$ and $4$ empty (Premise \claimref{dark-matter.single-ideal-at-residues-zero-and-four}), the share of a tower whose space has $D$ dimensions is $f = \tfrac{V_{3}}{V_{D}}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; V_{3}\sum_{\text{dark }r}\frac{1}{V_{D_{r}}}
\;=\; \frac{V_{3}}{V_{3}} + 2\,\frac{V_{3}}{V_{2}} + 2\,\frac{V_{3}}{V_{4}}
\;=\; 1 + \frac{8}{3} + \frac{16}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.36432\ldots
\]
against the observed $5.364 \pm 0.065$. The agreement is built in, not predicted: the relation was found by solving for the observed value, and its clauses were chosen with it known, and the closed form is one of fourteen equally simple candidates within the error bar (Observation \claimref{dark-matter.status-rule}).

\emph{What the total rests on.} On the stored dependence edges the past cone of this closed form holds these postulates of the dark-matter subject: R1, R2 and R3; P1 (\claimref{dark-matter.p1-single-frozen-point}), through the sourcing rule in which the shares are read (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}); P2 and P3, through the census of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}; and the two conditions registered as premises on 10 November 2026, the single-ideal clause \claimref{dark-matter.single-ideal-at-residues-zero-and-four} and the population of the odd towers \claimref{dark-matter.odd-towers-populated}. R2 enters twice, as the number density and as the unit of R3's thickness, which is each tower's own cell radius. The democracy premise (\claimref{dark-matter.d-democracy-total-mass}) is not among them: it belongs to the de Sitter reading. The total remains a fit. The mirror's share of one is derived separately (Proposition \claimref{dark-matter.population-count-one-share-half-percent}), so the closed form fixes two shares, $\tfrac{4}{3}$ and $\tfrac{8}{3\pi}$, against one measured number, the remainder $4.36 \pm 0.07$. Chosen with that number known, by the store's own record: the relation was found by solving for the observed value (Observation \claimref{dark-matter.status-rule}(i)); the clauses of the contact mechanism that returns R3's value were chosen with it known (the same, (ii)); the single-ideal clause was chosen knowing that the fit needs it (the same, (vi)); and the population of the odd towers is inferred from the remainder itself (Observation \claimref{dark-matter.which-towers-are-populated}). P1, P2 and P3 belong to the paper's earlier sections, written before the rule was proposed (Remark \claimref{note.dark-matter.setting-dark-matter-ratio-unit-ball}).

## technical
Under premises R1 (equal mass per quantum), R2 (one quantum per unit ball of a tower's own space) and R3 (one cell per unshared direction), a tower whose space has $D$ dimensions has number density $1/V_{D}$ and so contributes a share $f = V_{3}/V_{D}$ of our matter per unit of our volume, with $V_{n}$ the volume of the unit $n$-ball. Summing over the five dark towers at their nearest-dimension representatives (the four odd ones taken as populated and residues $0$ and $4$ as empty, two conditions now registered as premises), the mirror with $D = 3$, two three-dimensional towers with $D = 2$ and two five-dimensional towers with $D = 4$, gives
$$\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} = 1 + \frac{8}{3} + \frac{16}{3\pi} = \frac{11\pi + 16}{3\pi} = 5.36432\ldots,$$
against the observed $5.364 \pm 0.065$. The agreement is a fit, not a prediction: the relation was found by solving for the observed value, its clauses chosen with it known, and it is one of fourteen equally simple values in the error bar (Observation \claimref{dark-matter.status-rule}).

What the total rests on, on the stored edges: R1, R2 (twice: the density, and the unit of R3's thickness), R3, P1 through the sourcing rule, P2 and P3 through the census, the single-ideal clause and the population of the odd towers; not the democracy premise. It remains a fit: two shares, $4/3$ and $8/(3\pi)$, against one measured remainder, with the relation found by solving for the value, the contact clauses and the single-ideal clause chosen with it known, and the population of the odd towers inferred from the remainder itself.

## lay
This rule assigns every dark tower one particle of a common mass per unit-sized ball of its own space, and compares that density with ours. Towers with fewer or more spatial dimensions then contribute different amounts, fixed by the volumes of balls in two, three and four dimensions. Under its three premises, together with the assumptions that the four odd hidden sectors hold matter and that two further sectors hold none, the rule gives a dark-to-ordinary matter ratio of about 5.364, the observed value. The formula sets two shares against one measured number, and the assumption that the four sectors are filled is itself read off from that number; but the relation was found by solving for that value, and many equally simple formulas land inside the measurement's error, so the agreement is a fit rather than a prediction.

## one-liner
Under premises R1 to R3, with the odd towers populated and residues 0 and 4 empty (both registered premises), a tower with $D$-dimensional space has share $V_{3}/V_{D}$, and the dark-to-baryon ratio is $(11\pi + 16)/(3\pi) \approx 5.3643$, against the observed $5.364 \pm 0.065$, an agreement built in by fitting, not predicted.
