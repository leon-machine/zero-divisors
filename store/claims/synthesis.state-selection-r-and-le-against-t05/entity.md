---
id: synthesis.state-selection-r-and-le-against-t05
kind: claim
version: 4
title: 'The folded note''s (R) and (L$_E$) against T05''s'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, entropy-premises, modular-theory, finite-models, ledger-audit]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.singularity.geometric-modular-condition-g
derivations:
- name: main
  uses:
  - singularity.kms-uniqueness-factor@6
  - hawking.modular-structure-completed-pair@3
  - scrambling.boundary-mode-space-matrix@4
  - singularity.number-diagonal-dynamics-models-scrambling-derived@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_single_mode_readings
- kind: check
  ref: check.py::check_two_mode_counter_models
- kind: check
  ref: check.py::check_le_pair_same_generators
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.r-regularity-fixed-locus
  - singularity.l-boundary-mode-locality
  - singularity.q-joint-quasi-freeness-s-wave
  - singularity.p-univalence
  - singularity.rate-discharge-hypothesis-iii
  - state-selection.rate-discharge-hypothesis-iii
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The window is built from completed pairs of the radial atom (U2): its numbers are read in span{1, J}, J = e_2 e_3 (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the formal level), the source unit i read as J; the Killing flow Ad(e^{J t sum omega_k K_k}), the ladder phases e^{+-J omega t} and the continuation F_{a,b}(t + Jp) are written with J (with the signs of that result, F(t + Jp) = omega(alpha_t(b) a) being its KMS relation). No i remains; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the window is built from completed pairs of the hyperbolic atom (Proposition hawking.modular-structure-completed-pair), and on the atom of the spacetime radial plane I_4 anticommutes with the mode operators (conventions, known limit 1), so the store does not show I_4 to be the unit; i stays in the Killing flow, the ladder phases and the continuation F(t + i p) (declared complex-analysis).'
  maintainer_pass_2:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  open_problem: op.folded-state-selection-note
  note: >-
    Settles the content relation of the two premise pairs among the folded note's same-title
    pairs, on the boundary-mode algebra. The note's (R) has three readings there; only one is
    satisfiable and contentful, and in it the note's (R) is T05's (R) plus vanishing inter-mode
    two-point functions, strictly between T05's (R) and (R) with (Q), with exact even
    counter-models both ways. The two (L_E) premises name the same generator class. Supplies
    the reductions for pr.minimal-premise-basis: the note's (L_E) is a restatement; the note's
    (R) is not, but its one consumer uses only its single-mode content, which T05's (R)
    supplies. Retyping either needs an assumes change, a maintainer decision. Transport-absent
    (finite CAR algebra), except that the modes are the transport's completed pairs.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 2: on the strength of this result the note''s (R) and (L_E) (state-selection.r-regularity-fixed-locus,
      state-selection.l-ledger-locality) and the note''s duplicates of T05 entities were retired to tombstones.yaml. The
      claimrefs to the retired ids in the formal level became plain references to the note''s Premise 5.1, Premise 7.3 and
      Proposition 7.4 (the first two recorded under extraction.merged_from of the T05 premises), the lineage links to them
      were dropped, and the about link to the note''s copy of the geometric modular condition was dropped (the T05
      definition, kept, is the same set of states). Statement and checks unchanged.'
---

## formal
Let a window of $n$ boundary modes, completed pairs $(a_{k}, a_{k}^{*})$ obeying the canonical anticommutation relations (Proposition \claimref{scrambling.boundary-mode-space-matrix}), carry the Killing flow $\alpha_{t} = \operatorname{Ad}(e^{Jt\sum_{k}\omega_{k}K_{k}})$, $K_{k} = N_{k} - \tfrac12$ (Proposition \claimref{hawking.modular-structure-completed-pair}), its numbers read in $\mathrm{span}\{1, J\}$ with $J = e_{2}e_{3}$ the complex unit of the completed pair's radial atom (Theorem \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}), which commutes with the radial plane and with every vector orthogonal to spacetime, hence with every mode (the continuation $t + Jp$ is in that field), with period $p = 2\pi/\kappa$ and $Q_{k} = e^{\omega_{k}p}$. For mode operators $a, b$ write $F_{a,b}(t) = \omega(a\,\alpha_{t}(b))$, a finite sum of exponentials in $t$. Premise (R) of the state-selection note (its Premise 5.1, now retired from the store; its statement is recorded with \claimref{singularity.r-regularity-fixed-locus}) asks that the state's two-point functions, continued in the rapidity of the boost flow, be single valued and regular at its fixed locus; T05's Premise (R) (\claimref{singularity.r-regularity-fixed-locus}) asks that each single-mode correlator continue to the Euclidean section with its two orderings glued across the cut, $F_{a,b}(t + Jp) = \omega(\alpha_{t}(b)\,a)$.
\begin{enumerate}
\item[(i)] (one mode, three readings) on a mode of nonzero weight: regularity alone is vacuous (every $F_{a,b}$ is entire); single-valuedness read as strict periodicity, $F_{a,b}(t + Jp) = F_{a,b}(t)$ for both orderings of the ladder, holds for no state (it forces the occupancy to be both $1$ and $0$); single-valuedness read with the orderings glued, as T05 reads it, holds exactly when the occupancy is $n = 1/(Q + 1)$, which is T05's (R) on that mode; the ladder correlators do not see $\omega(a)$, and with $\omega(a) = 0$, as (P) (\claimref{singularity.p-univalence}) gives, the marginal is the Gibbs state at $\beta = p$ (Theorem \claimref{singularity.kms-uniqueness-factor}). At zero weight strict periodicity is vacuous and the glued reading forces $n = \tfrac12$ at every period;
\item[(ii)] (the glued reading on the whole window) write (R$_{\mathrm{reg}}$) for the glued reading imposed on every two-point function of mode operators. On mixed correlators, $i \ne j$, it reads $Q^{\mp 1}\omega(a_{i}b_{j}) = -\omega(a_{i}b_{j})$ for $b_{j} \in \{a_{j}^{*}, a_{j}\}$, so (R$_{\mathrm{reg}}$) holds if and only if T05's (R) holds on every mode and every inter-mode two-point function vanishes;
\item[(iii)] (strictly between) T05's (R) with the two-point clause of (Q) (\claimref{singularity.q-joint-quasi-freeness-s-wave}) implies (R$_{\mathrm{reg}}$), and (R$_{\mathrm{reg}}$) implies T05's (R); neither converse holds. On two modes with Gibbs marginals: adding a coherence $c \ne 0$ between $\ket{10}$ and $\ket{01}$ gives an even state satisfying T05's (R) with $\omega(a_{1}a_{2}^{*}) = -c$, so (R$_{\mathrm{reg}}$) fails; adding instead a density correlation $d \ne 0$ gives an even state satisfying (R$_{\mathrm{reg}}$) with $\omega(N_{1}N_{2}) - n_{1}n_{2} = d$, so it is not quasi-free and (Q) fails;
\item[(iv)] (the note's rate theorem) on each mode, the Gibbs form at $\beta = 2\pi/\kappa$ with occupancy in $(0,1)$, hence faithful marginals, follows from (R$_{\mathrm{reg}}$) and (P) by (i), without the geometric modular condition, as T05's Theorem \claimref{singularity.rate-discharge-hypothesis-iii} obtains it from T05's (R); the single-mode conclusions of the note's Theorem \claimref{state-selection.rate-discharge-hypothesis-iii} therefore need only T05's (R);
\item[(v)] (the two (L$_E$)) T05's Premise \claimref{singularity.l-boundary-mode-locality} and the note's Premise 7.3 (now retired from the store as a restatement of T05's) generate the dynamics by the boost bivectors $\sigma_{k}$ and their products, the abelian algebra $\mathcal{A}_{\sigma}$ of dimension $2^{n}$, which commutes with every $N_{k}$, contains the cross-point products $\sigma_{j}\sigma_{k}$, and excludes the hopping $a_{j}^{*}a_{k}$ and the pairing $a_{j}^{*}a_{k}^{*}$ ($j \ne k$). The note's clause that no generator couples the ladder at one point to the ladder at another, read as excluding every generator that involves two points, would exclude $\sigma_{j}\sigma_{k}$, which its own first clause admits and its Proposition 7.4, merged into \claimref{singularity.number-diagonal-dynamics-models-scrambling-derived}, uses (the controlled-$Z$); read as excluding transfer of occupation, it is T05's clause. The two premises name one generator class.
\end{enumerate}
So the note's (L$_E$) restates T05's, and the note's (R), in its one satisfiable contentful reading on the boundary-mode algebra, is T05's (R) plus vanishing inter-mode two-point functions.

## technical
The note folded into T05 states two premises under T05's names. On the boundary-mode algebra the note's (R), regularity of the state's two-point functions continued in rapidity, can be read three ways on a single mode: regularity alone constrains nothing, strict periodicity in imaginary time is satisfied by no state, and the reading T05 uses, with the two operator orderings glued across the cut, fixes the mode's occupancy at its thermal value for the geometric period, and with univalence (P) makes the mode exactly thermal (KMS). Imposed on every two-point function of the window, the glued reading also forces all correlations between different modes' ladders to vanish. It therefore sits strictly between T05's (R), which constrains single modes only, and T05's (R) together with the quasi-free premise (Q); two small even states show both gaps. The single-mode conclusions of the note's rate theorem need only T05's (R) with (P).

The two locality premises (L$_E$) describe the same generators: products of the boost bivectors at each point, which commute with every occupation number, include the cross-point products used for the controlled-$Z$ scrambling, and exclude hopping and pairing between points. The note's wording, taken literally, would also exclude the cross-point products its own proposition uses, so T05's wording is the consistent one.

## lay
Two assumptions of the series appear twice, once in the main paper on black-hole states and once in a shorter note later folded into it, under the same names. This result compares them exactly. The two locality assumptions turn out to say the same thing. The two regularity assumptions do not: read in the only way that makes it both meaningful and satisfiable, the note's version asks for everything the main paper's version asks, plus the absence of correlations between different modes, while still asking less than the main paper's version combined with its separate assumption that the state is the simplest (quasi-free) one. Small explicit examples show both differences. What the note actually uses its version for needs only the main paper's, together with the univalence assumption both papers make.

## one-liner
On the boundary-mode algebra the note's (R) is satisfiable and contentful only in its glued reading, where it equals T05's (R) plus vanishing inter-mode two-point functions, strictly between (R) and (R) with (Q); the two (L$_E$) premises admit the same generators.
