---
id: synthesis.injection-freshness-is-pair-purity
kind: claim
version: 3
title: 'Freshness of injection is the purity of the injected pair'
status: proved
region: synthesis
subject: entropy
tags: [entropy-premises, boundary-modes, car-algebra]
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
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - singularity.modular-descent@8
  - singularity.chains-state-class-stability@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pure_pair_is_fresh
- kind: check
  ref: check.py::check_ghz_counter_model
- kind: check
  ref: check.py::check_schmidt_rigidity
- kind: check
  ref: check.py::check_zero_weight_form_not_forced
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.rate-models-kinematic-inputs-l-u
  - singularity.eviction-window-thermal-product-radiation-entropy
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U1) the abstract qubit spaces H_W = H_R = C^2 have their numbers read in span{1, I_4}, stated once in the formal level, so the thermofield form is psi = c|00> + e^{I_4 phi} s|11>; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the phase e^{i phi} and C^2 are the abstract qubit Hilbert spaces of the window mode and emitted quantum, not built here from GA modes; declared (version and levels unchanged).'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'check_pure_pair_is_fresh: freshness derived for every rho on W, R, X from three linear identities checked on all 64 matrix units (positivity step argued); check_schmidt_rigidity: complex amplitude scan over 12 rational unit phases (144 hits, all diagonal) and TF implies Pure at those phases; docstrings (a), (c) reworded. Version 1 -> 2.'
  open_problem: pr.minimal-premise-basis
  note: >-
    Premise-basis bookkeeping inside one postulate. Clause (I) of the rate model lists the pair
    form (from the modular descent theorem) and freshness (an independent assumption). Given the
    thermal marginals, the pair form is purity of the pair's state, purity implies freshness, and
    under clause (U) freshness implies purity: the clause carries one assumption, not two, and it
    is not supplied by the cited results (an even, globally pure counter-model has the marginals
    and violates it). At zero weight purity no longer fixes the number-basis form. The rate model
    is described, not assumed, so it enters as lineage. Transport-absent (finite quantum
    information).
---

## formal
Consider one injection step of the rate model of Premise \claimref{singularity.rate-models-kinematic-inputs-l-u}: the window mode $W$ and emitted quantum $R$ of the $k$-th pair, and a finite system $X$ holding everything already present, in a state $\varrho$ on $\mathcal{H}_W \otimes \mathcal{H}_R \otimes \mathcal{H}_X$ with $\mathcal{H}_W = \mathcal{H}_R = \C^{2}$, abstract qubit spaces whose numbers are read in $\mathrm{span}\{1, I_4\}$ (conventions, the unit principle, U1). Let (M) say that both single-mode marginals are the thermal marginal $\operatorname{diag}(c^{2}, s^{2})$, $c, s > 0$, $c^{2} + s^{2} = 1$, that Theorem \claimref{singularity.modular-descent} and Corollary \claimref{singularity.chains-state-class-stability} supply; (Pure) that the pair state $\varrho_{WR}$ is pure; (F) freshness, $\varrho_{WRX} = \varrho_{WR} \otimes \varrho_X$; and (TF) the thermofield form $\varrho_{WR} = |\psi\rangle\langle\psi|$, $\psi = c|00\rangle + e^{I_4\phi}s|11\rangle$. Then:
\begin{enumerate}
\item[(i)] (Pure) implies (F), for every $\varrho$;
\item[(ii)] if $\varrho_{WRX}$ is pure, clause (U) restricted to this step, then (F) implies (Pure);
\item[(iii)] under (M) with $c \neq s$, (Pure) holds if and only if (TF) does; at zero weight, $c = s$, (Pure) with (M) gives a maximally entangled pair which need not be of the form (TF), for example $(|01\rangle + |10\rangle)/\sqrt2$;
\item[(iv)] (M), (U) and the evenness (P) of Premise \claimref{singularity.p-univalence} do not imply (Pure), (F) or (TF): the state $c|00\rangle_{WR}|00\rangle_X + s|11\rangle_{WR}|11\rangle_X$, with $X$ two earlier modes, is globally pure and even, has both marginals $\operatorname{diag}(c^{2}, s^{2})$ and an even, number-diagonal pair state, and its pair state is mixed, $\tr\varrho_{WR}^{2} = c^{4} + s^{4} < 1$, and correlated with $X$.
\end{enumerate}
So for $c \neq s$ clause (I) of the rate model has exactly one content beyond the derived marginals: the pair's state is pure, equivalently (under (U)) fresh, equivalently of thermofield form. The pair form is no more supplied by the cited results than freshness is; it is the same assumption. Indeed (Pure) is hypothesis (i) of Theorem \claimref{singularity.modular-descent}, so applying that theorem to the injected pair already assumes the pair pure, hence (by (i)) fresh: clause (I) states one assumption twice. At zero weight, where the eviction theorem's maximally entangled idealisation lives (Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}(4)), the number-basis form needs an input beyond purity, which is hypothesis (ii) of the same theorem, invariance of the pair state under the pair's boost flow.

## technical
The rate model's injection clause says that each emitted quantum enters in a thermofield pair $c|00\rangle + s|11\rangle$ with a fresh window mode, taking the pair form from the modular descent theorem and adding freshness, the absence of correlation with everything already present, as a separate assumption. A pair in a pure joint state cannot be correlated with anything else, so purity gives freshness; and when the whole description is pure, a pair uncorrelated with the rest must itself be pure. With the thermal marginals fixed and unequal, a pure pair is forced into the thermofield form by the uniqueness of the Schmidt decomposition. So the three statements coincide, and the clause holds one assumption. That assumption is hypothesis (i), purity, of the modular descent theorem from which the clause takes its pair form: the theorem does not supply the purity of the pair, it presupposes it. That assumption is not a consequence of the cited theorems: a globally pure, even state with the right marginals can hold the pair in a mixed state correlated with earlier modes. At zero weight the marginals are maximally mixed and purity alone allows other maximally entangled pairs; the theorem's second hypothesis, boost invariance of the pair, is what selects the number-basis form there.

## lay
In the series' simple model of black-hole evaporation, every emitted particle is born together with a partner inside the hole, in a definite entangled pair, and the pair is assumed to arrive with no links to anything already there. These sound like two assumptions. They are one: a pair in a definite joint state cannot be linked to anything else, and, if the whole description is in a definite state, a pair with no outside links must be in a definite state itself. The assumption is not supplied by the theorems the model cites, as an explicit example shows.

## one-liner
Given global purity and thermal marginals $\operatorname{diag}(c^{2}, s^{2})$ with $c \neq s$, the rate model's freshness, the purity of the injected pair and its thermofield form are equivalent under global purity, so clause (I) holds one assumption; an even, globally pure state with those marginals and a mixed, correlated pair shows the cited results do not supply it.
