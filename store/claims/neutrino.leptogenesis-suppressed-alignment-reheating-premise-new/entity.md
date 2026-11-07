---
id: neutrino.leptogenesis-suppressed-alignment-reheating-premise-new
kind: claim
version: 8
title: 'Leptogenesis suppressed: the alignment, the reheating premise, and a new stance'
status: proved
region: neutrino
subject: neutrinos
tags: [matter-asymmetry, flavour-and-mixing, live-prediction]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 8
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - neutrino.imported-ceiling-under-hypothesis-u-arrow@6
  - neutrino.imported-indifference-faces-democratic-alignment-rank@6
  - neutrino.invariant-symmetric-matrices@2
  - neutrino.rank-one-seesaw-ordering-sum-double@8
  assumes:
  - neutrino.r-descent-reheats-below-lower-heavy@1
  - dark-matter.hyp-u-equal-rank-one-eigenvalues@3
  - neutrino.real-breaking-assumption@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T15.py
  tags:
  - label:prop:leptogenesis
- kind: check
  ref: check.py::check_alignment_kills_decay_asymmetries
- kind: check
  ref: check.py::check_washout_strength_and_resonant_pair
- kind: check
  ref: check.py::check_real_breaking_kills_interference
- kind: check
  ref: check.py::check_unification_above_heavy_scale
locators:
  paper: T15
  number: Prop 5.3
  label: prop:leptogenesis
  line: 733
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the complex breaking phase in the proof, step (3), is written as I_4 (numbers read in span{1, I_4}): e^{I_4 theta} = (3 + 4 I_4)/5; nothing stays.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'Im of products of Yukawa matrix entries and the Gaussian rational e^{i theta} = (3 + 4i)/5: complex matrix entries and numbers'
    - 'every subscript i (heavy-neutrino index)'
  env: proposition
  context_refs:
  - neutrino.breaking-relation
  - neutrino.imported-ceiling-under-hypothesis-u-arrow
  - neutrino.imported-indifference-faces-democratic-alignment-rank
  - neutrino.invariant-symmetric-matrices
  - neutrino.rank-one-seesaw-ordering-sum-double
  unresolved_refs:
  - rem:branch
  - rem:valuation
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - neutrino.imported-ceiling-under-hypothesis-u-arrow
    - neutrino.imported-indifference-faces-democratic-alignment-rank
    - neutrino.invariant-symmetric-matrices
    - neutrino.rank-one-seesaw-ordering-sum-double
    - neutrino.r-descent-reheats-below-lower-heavy
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
    note: 'the proof existed after the premise environment and was copied verbatim (without the \sloppy
      layout command); (R) is assumed, the breaking lemma only names delta and was not added, and the
      real-breaking assumption of (3) has no store postulate, so that conditionality is carried only in
      the text. Hypothesis pass: assumes dark-matter.hyp-u-equal-rank-one-eigenvalues added because the
      paper names Hypothesis (U) as a condition of this result. Levels pass: all three levels now name
      Hypothesis (U), and the lay level labels Premise (R) and says it also blocks the resonant pair.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - neutrino.imported-ceiling-under-hypothesis-u-arrow
    - neutrino.imported-indifference-faces-democratic-alignment-rank
    - neutrino.invariant-symmetric-matrices
    - neutrino.rank-one-seesaw-ordering-sum-double
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Assumes the real-breaking assumption, a new postulate (the typing note recorded that it had no store postulate, so the conditionality of step (3) and of the registered CP stance was carried only in the text). Cited in the proof at step (3). The statement is unchanged."
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: eigenspaces of M_R and vanishing off-diagonal Y_D^dag Y_D in five eigenbases, K in (43, 48), the delta-independent resonant ratio, zero interference under real breaking, and M_U above M_3. Version 5 -> 6. Check strengthened: K ends, the pair ratio''s closed form and the leading O(delta^2) coefficient pinned by hand; phases asserted unit modulus; samples moved to module level. Version 6 -> 7.'
---

## formal
The heavy neutrinos of Proposition \claimref{neutrino.rank-one-seesaw-ordering-sum-double} are the textbook mechanism of leptogenesis, and had that mechanism operated it would have generated the asymmetry in this tower alone, breaking the universality on which the dark-tower count and the arrow's accounting stand (Fact \claimref{neutrino.imported-ceiling-under-hypothesis-u-arrow}). The mechanism is suppressed in three steps, and the danger was double.
\begin{enumerate}
\item \emph{(The alignment result; proved.)} The decay asymmetry of the heavy state $N_{i}$ requires interference \cite{FukugitaYanagida1986, DavidsonNardiNir2008}, $\epsilon_{i} \propto \sum_{j \neq i}\mathrm{Im}\bigl[\bigl((Y_{D}^{\dagger}Y_{D})_{ij}\bigr)^{2}\bigr]\,f(M_{j}/M_{i})$, with $Y_{D}$ written in the heavy-mass eigenbasis. With $Y_{D} = y\J$ (Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank}) and $M_{R} = \alpha\mathbf{1} + \beta\J$ (Lemma \claimref{neutrino.invariant-symmetric-matrices}), every heavy eigenbasis contains $u'$ (for $\beta \neq 0$, which the branch supplies; at $\beta = 0$ every basis is an eigenbasis and the conclusion holds a fortiori), and in any such basis the representation of $Y_{D}^{\dagger}Y_{D} = 3|y|^{2}\J$ has exactly one nonzero entry, on the diagonal at $u'$; every off-diagonal entry vanishes identically, so $\epsilon_{i} = 0$ for every $i$ at leading order, and the pair $N_{\perp}$ has no Dirac coupling at all. What this suppresses is the state $N_{u'}$; the pair is suppressed at leading order only because it does not couple.
\item \emph{(The degenerate pair, and the reheating premise.)} The graver threat was erasure, not production: the rank-one coupling washes exactly one lepton-flavour direction, the democratic one, with strength $K = m_{3}/m_{*} \approx 45$ for the equilibrium mass $m_{*} \in (1.06, 1.15)$ meV \cite{DavidsonNardiNir2008}, and a flavour-democratic descent asymmetry lies entirely in that direction; had the plasma ever reached $T \sim M_{3}$, the framework's own neutrinos would have erased the arrow's imprint. And the pair $N_{\perp}$, exactly degenerate at $\alpha$ at leading order, is the resonant configuration \cite{PilaftsisUnderwood2004}: after the breaking its couplings are $O(\delta)$ but the interference combination that controls its asymmetry, an off-diagonal entry of $Y_{D}^{\dagger}Y_{D}$ normalised by the two diagonal entries it connects, is $O(1)$ in $\delta$, so the pair's asymmetry is not switched off by the smallness of the breaking, and its value depends on the pair's split and widths, which this paper does not compute. What protects both is a premise, stated as such at the scale that does so:
\end{enumerate}
\begin{premise}[R: the descent reheats below the lower heavy scale]
$T_{\mathrm{desc}} \le \alpha = \min(\alpha, M_{3})$, with $\alpha$ on the branch of Remark \ref{rem:branch}. This is a reading of the dark-matter paper's own assumption (Fact \claimref{neutrino.imported-ceiling-under-hypothesis-u-arrow}: $T_{\mathrm{desc}}$ at the ceiling or below it) at "below"; under it no heavy state ever thermalised, the washout of $N_{u'}$ is Boltzmann-suppressed, the pair $N_{\perp}$ was never produced thermally, and the descent's $B - L$ is untouched. The natural justification, that the frozen phase's description dissolves above the rung scale, identifies $M_{3}$ with that scale, which is Hypothesis (U) and the valuation of Remark \ref{rem:valuation}, not a theorem; and (R) at $\alpha$ asks more of the descent than that, since $\alpha$ lies nearly two orders below $M_{3}$ on the branch taken. A derivation of $M$ and of $\alpha$ (successor problems (2) and (3)) would decide it.
\end{premise}
\begin{enumerate}
\setcounter{enumi}{2}
\item \emph{(The phases.)} Non-thermal decays of descent-populated heavy states inject asymmetry at order $\delta^{2}\sin\varphi$ from $N_{u'}$, and with an $O(1)$ prefactor times $\sin\varphi$ from the pair by (2), with $\delta$ the breaking of Lemma \claimref{neutrino.breaking-relation} and $\varphi$ a relative phase between the Dirac and Majorana matrices after it. Both matrices are built from one real geometric vacuum and one flavour-independent flag; the orientation is the only CP-violating mechanism the framework itself supplies (Fact \claimref{neutrino.imported-ceiling-under-hypothesis-u-arrow}, uniqueness not claimed there); that it is flavour-independent, one bit of the descent with no face index, as is the relaxing $\theta$-angle that Fact names as unexcluded, is this paper's reading of that object at observation level, and under it neither can generate a \emph{relative} phase between two family matrices; if the breaking is real in the vacuum's basis the relative phases vanish and the injection is zero to all orders in it. Under (R) a consistency consequence follows: the unification scale, on either of the Standard-Model paper's branches (Remark \ref{rem:valuation}), lies above $M_{3}$ at either end of Hypothesis (U), so the universe never revisited unification after the descent, and the meeting of the couplings, where there is one, is structural, not thermal history.
\end{enumerate}
The corollary is registered as the framework's fifth stance: the Dirac phase of lepton mixing is trivial, $\delta_{CP} \in \{0, \pi\}$. The current record leaves this allowed and, notably, allowed precisely in the ordering the framework predicts: the joint long-baseline analysis finds CP conservation allowed within the three-sigma interval for \emph{normal} ordering while excluding it at three sigma under \emph{inverted} ordering \cite{T2KNOvA2025}, so the stance's survival and the framework's ordering prediction are now the same experimental question. Should $\delta_{CP}$ prove nontrivial with normal ordering established, the real-breaking assumption fails, the double-beta values of Proposition \claimref{neutrino.rank-one-seesaw-ordering-sum-double}(3) revert to their hull, and subdominance would demand the injected asymmetry, $\delta^{2}\sin\varphi$ from $N_{u'}$ and $O(\sin\varphi)$ from the pair, below the asymmetry a successful leptogenesis needs, of order $10^{-7}$ in the standard treatments \cite{DavidsonNardiNir2008}, a tuning this framework would then have to record. (1) is proved at leading order; (2) is a premise; (3) is conditional on the real-breaking assumption.

## technical
The heavy neutrinos of the rank-one seesaw are the textbook mechanism of leptogenesis, and had it operated it would have made an asymmetry in this tower alone, breaking the universality on which the dark-tower count and the arrow's accounting rest. Step (1), proved at leading order: with $Y_{D} = y\J$ and $M_{R} = \alpha\mathbf{1} + \beta\J$, every heavy eigenbasis contains $u'$ and $Y_{D}^{\dagger}Y_{D} = 3|y|^{2}\J$ has no off-diagonal entry there, so every decay asymmetry $\epsilon_{i} \propto \sum_{j \neq i}\mathrm{Im}\bigl[((Y_{D}^{\dagger}Y_{D})_{ij})^{2}\bigr]f(M_{j}/M_{i})$ vanishes, and the pair $N_{\perp}$ has no Dirac coupling.

Step (2): the washout of the democratic flavour direction, of strength $K \approx 45$, and the resonant degenerate pair, whose asymmetry is not switched off by small breaking, are avoided only under Premise (R), that the descent reheats below $\alpha$. Step (3), conditional on the real-breaking assumption: with both matrices built from one real vacuum and one flavour-independent flag (the paper's reading at observation level), no relative phase arises and the non-thermal injection vanishes; under (R) the unification scale lies above $M_{3}$ at either end of Hypothesis (U) and is never revisited. The corollary is registered as a stance, $\delta_{CP} \in \{0, \pi\}$.

## lay
Heavy neutrinos are the standard explanation of why the universe has more matter than antimatter, but in this framework that imbalance must be inherited, not made here. The paper shows that at first approximation these heavy neutrinos cannot create an imbalance, that they would neither have erased the inherited one nor made a new one provided the early universe never got hot enough to make them (Premise (R), an assumption), and that if the small symmetry breaking is real no CP-violating phase arises. With the heavy scale set under Hypothesis (U), the same premise also means the universe never got back to the temperature at which the forces unify. That gives a testable stance: the leptonic CP phase should be trivial.

## one-liner
Leptogenesis is suppressed by the alignment at leading order, by Premise (R) against washout and the resonant pair, and by real breaking for the phases, giving, with the scales of Hypothesis (U), the stance $\delta_{CP} \in \{0, \pi\}$.
