---
id: synthesis.residues-zero-four-real-chirality-anomaly
kind: claim
version: 2
title: 'Real chirality at residues 0 and 4, and the spinor-ideal anomaly'
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, chirality, pseudoscalar-and-centre, hypercharge-and-anomalies, dark-tower-premises]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.oriented-causal-towers-mirror-pair-every-window@2
  - transport.sign@3
  - dark-tower-matter.constituents-field@2
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.thickness-not-gravitational-quantity@5
  - dark-matter.sourcing-rule-forced-not-chosen@3
  - standard-model.imported-anomaly-coefficients@1
  proof: proof-main.tex
about:
- obj.dark-tower-matter.ideals-fields-momentum
checked_by:
- kind: check
  ref: check.py::check_real_chirality_window_free
- kind: check
  ref: check.py::check_anomaly_polynomials
- kind: check
  ref: check.py::check_two_dimensional_fields
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.lowest-causal-residues-zero-four-content
  - dark-matter.p3-nearest-dimension-representatives
outside_ga:
  kind: other
  why: 'in the proof, at residues 2 and 6, chirality is the splitting into the +-i eigenspaces of the complex structure I itself, so the i is an eigenvalue of that pseudoscalar and cannot be written as it'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): in the proof, at residues 2 and 6, chirality is the splitting into the +-i eigenspaces of the complex structure I itself, so the i is an eigenvalue of that pseudoscalar and cannot be written as it.'
  open_problem: op.window-p3
  note: >-
    Second clause of P3 (residues 0 and 4 empty). Residues 0 and 4 are, in every window, exactly
    the causal towers whose dimension is 2 mod 4, where the pseudoscalar squares to +1 and the
    single spinor ideal has a real chirality (the lemma of the result filed alongside,
    synthesis.reversion-pairing-vanishes-residues-zero-four, and of the stored oriented-causal
    result); this is also exactly where local anomalies of one chirality cannot cancel. The
    anomaly forms are exact power-series algebra (transport-absent). The anomaly theorems
    (Alvarez-Gaume and Witten 1984; Bardeen and Zumino 1984; the covariant two-dimensional form of
    Iso, Umetsu and Wilczek 2006) are cited from memory and are not in the store: clauses (ii) to
    (iv) are conditional on them. The single-ideal definition is a costed clause chosen with the
    fit known, and (G6) is a reading, also chosen knowing that the unit-ball fit needs residue 4
    empty.
---

## formal
Use the spinor ideal $S = \Cl^{0}(V)f$ of Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum}, one ideal per tower, with $f = \tfrac12(1 + e_{t}e_{a})$ at $(1,1)$ and $f = \tfrac14(1 + e_{t}e_{a})(1 + cI)$, $c = \pm 1$, at $(1,5)$ and $(5,1)$, $I$ the pseudoscalar of $V$; the single ideal is the series' costed clause for residues $0$ and $4$, chosen with the fit known. Call a causal tower \emph{really chiral} if $I^{2} = +1$ and $I$ is central in $\Cl^{0}(V)$. Let a tower share with this one its time and up to three space directions, as in the sourcing rule (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}). Write (A) for the local-anomaly theorem and the two-dimensional covariant anomaly form, imported from the literature and not in the store; clauses (ii) to (iv) are conditional on (A).
\begin{enumerate}
\item[(i)] \emph{(Every window; proved.)} A causal tower is really chiral if and only if its dimension is $n \equiv 2 \pmod 4$, if and only if its residue is $0$ or $4$ (the splitting is that of Theorem \claimref{synthesis.oriented-causal-towers-mirror-pair-every-window}(ii); its form for the single ideal is the lemma of the result filed alongside, synthesis.reversion-pairing-vanishes-residues-zero-four). There $S$ is an eigenspace of left multiplication by $I$ with a real eigenvalue ($+1$ at $(1,1)$, $c$ at $(1,5)$ and $(5,1)$), the two eigenvalues give non-isomorphic $\Cl^{0}(V)$-modules, and any conjugation keeps the eigenvalue.
\item[(ii)] \emph{(Anomaly forms; computed, conditional on (A).)} The pure rotation-gauge anomaly form of one chiral spin-$\tfrac12$ field in dimension $n$ is the degree-$(n+2)$ part of $\hat{A} = \prod_{i}(x_{i}/2)/\sinh(x_{i}/2)$, nonzero exactly when $n \equiv 2 \pmod 4$: $-p_{1}/24$ for $n = 2$, $(7p_{1}^{2} - 4p_{2})/5760$ for $n = 6$. The pure-gauge part is $\mathrm{tr}_{R}\,F^{(n+2)/2}/((n+2)/2)!$, an even power exactly when $n \equiv 2 \pmod 4$. In a really chiral tower the single-ideal content and its conjugates have one chirality, so these forms add: the rotation-gauge part is $N$ times that of one field and the gauge part is positive on every nonzero element of a gauge algebra acting nontrivially. Gauge vectors are not chiral, and the content has no gravitino and no two-form field, so nothing cancels them.
\item[(iii)] \emph{(Residue $0$, lowest-causal window.)} At $(1,1)$, $I = e_{t}e_{a}$ is the bivector of the tower's own plane, both of whose directions are shared; on the sourcing rule's reading the tower's matter lives on planes of this tower's spacetime and meets the field of the one metric induced on them. Such fields have non-constant scalar curvature: in conformal time, $R = -2\eta^{-4}$ (radiation era) and $R = -4\eta^{-6}$ (matter era) on a coordinate plane of a spatially flat expanding field, and $R = 4M/r^{3}$ on the $t$-$r$ plane of the Schwarzschild field (de Sitter's $R = 2H^{2}$ is constant). Where $R$ varies the anomaly makes the covariant divergence of the stress nonzero, so single-ideal tower matter of residue $0$ at $(1,1)$, massive or massless, has no conserved rotation-covariant stress and cannot source the field equations, whose left side is divergence-free identically (Proposition \claimref{dark-matter.sourcing-rule-forced-not-chosen}). The clause concerns the tower's single-ideal matter only: content with equal chiral weight on the two sheets of an edge has $c_{L} = c_{R}$ and no anomaly.
\item[(iv)] \emph{(Residue $4$, lowest-causal window.)} At $(1,5)$ and $(5,1)$, on $S$ the pseudoscalar $I_{4}$ of the four shared directions equals $-cJ$, $J$ the unit bivector of the two unshared directions, $J^{2} = -1$. The one metric rotates only shared directions (the unshared ones are not gravitational, Proposition \claimref{dark-matter.thickness-not-gravitational-quantity}), and in four dimensions the rotation-gauge anomaly form vanishes, so the one metric's field meets no obstruction at residue $4$. Under (G6), the reading that the tower's own gauge fields are fields on its six-dimensional space and act nontrivially on its constituents, the gauge part of (ii) is nonzero and single-ideal matter of residue $4$ is anomalous. Without (G6) nothing here empties residue $4$.
\end{enumerate}
Consequently, in the lowest-causal window and given (A), the single-ideal clause empties residue $0$ through the one metric alone and residue $4$ through (G6). At higher causal members of residue $0$, such as $(1,9)$ and $(9,1)$, only four directions are shared and, as in (iv), the one metric meets no obstruction; at the non-causal representatives of Premise \claimref{dark-matter.p3-nearest-dimension-representatives} nothing here applies. The result filed alongside shows that with one ideal the emptiness of residues $0$ and $4$ holds under the pairing reading of mass and fails at residue $4$ under the momentum reading; under (G6), (iv) closes that escape at residue $4$. If both ideals are admitted at $n \equiv 2 \pmod 4$, the content of residues $0$ and $4$ is vector-like and anomaly-free.

## technical
Take the single spinor ideal in every causal tower. For a causal signature of even dimension $n$ the pseudoscalar squares to $+1$ exactly when $n \equiv 2 \pmod 4$, which is exactly residues $0$ and $4$ in every window; there the single ideal is one of two non-isomorphic chiral modules and a constituent and its conjugate have the same chirality. Granting the imported anomaly theorems, dimension $2 \bmod 4$ is also exactly where local anomalies of one chirality exist and cannot cancel: the rotation-gauge form is the degree-$(n+2)$ part of the $\hat{A}$ genus, nonzero only in those dimensions, and the pure-gauge form is an even power of the field strength, positive on any nontrivially acting algebra, with no two-form field in the content to cancel it.

In the lowest-causal window, at residue $0$, in dimension two, both directions are shared, the one metric induces fields of varying curvature on the tower's planes (the radiation and matter eras of an expanding field, the Schwarzschild $t$-$r$ plane), and the anomaly makes the stress of single-ideal tower matter non-conserved, so that matter cannot be a source of the field equations; content with equal weight on both sheets of an edge is not affected. At residue $4$ the shared pseudoscalar equals the unshared-plane rotation on the ideal, so against the one metric the content is four-dimensional and meets no gravitational obstruction; it is anomalous only under (G6), the reading that the tower's own gauge fields live on its six-dimensional space and act on its constituents, a reading chosen knowing that the unit-ball fit needs residue $4$ empty. Higher causal members of residue $0$ share only four directions and meet no obstruction from the one metric.

## lay
The dark-matter paper leaves two of its eight families of worlds empty by assumption. In every possible number of dimensions, these two families are exactly the ones in which matter of a single handedness keeps its handedness when matter is swapped for antimatter. Granting standard results of quantum theory that are not yet recorded in the series, a world built from one handedness of matter then has broken bookkeeping of energy or of charge that its other particles cannot repair. If the family's matter has one handedness, as the series' definition says, and lives on two-dimensional slices of our spacetime, as the series' rule for how hidden matter feeds gravity implies, then in the smallest member of the first family this breakdown happens in the ordinary gravitational field of our universe, and that member is empty of matter and of radiation. In the smallest six-dimensional member of the second family it happens only through that world's own forces, and only if those forces spread through all six of its dimensions, an assumption chosen knowing that the paper's dark-matter count needs this family empty. If both handednesses are allowed, both families could hold matter.

## one-liner
Causal towers have a real chirality exactly at residues 0 and 4 ($n \equiv 2 \pmod 4$) in every window; given the imported anomaly theorems, in the lowest-causal window one spinor ideal is anomalous at $(1,1)$ in the one metric's field, and at $(1,5)$, $(5,1)$ only under (G6), a reading chosen knowing that the unit-ball fit needs residue 4 empty.
