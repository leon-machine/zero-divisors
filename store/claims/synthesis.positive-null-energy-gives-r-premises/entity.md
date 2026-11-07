---
id: synthesis.positive-null-energy-gives-r-premises
kind: claim
version: 7
title: 'Positive null energy gives the (R) premises'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, modular-theory, horizons, hawking-temperature, car-algebra, forcing-and-uniqueness, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: the analysis of (i) and (ii) split out into synthesis.null-vacuum-on-a-horizon-generator, which the proof now cites
  version: 6
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: unit conventions per Leon's rulings of 7 November 2026 (R4)
  version: 6
  source: maintainer pass 2026-11-07 (unit rulings)
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 7
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.hawking.continuum-mode-space
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - hawking.i-state-continuum@5
  - hawking.imported-quasi-free-kms-reduces-two@2
  - hawking.imported-ideal-fermi-gas-uniqueness@2
  - singularity.euclidean-section-period@5
  - synthesis.de-sitter-static-boost-frozen-point@5
  - synthesis.local-boost-temperature-is-local-regularity@3
  - synthesis.point-spectrum-boost-admits-no-half-sided-translations@3
  - angle.imported-theorems-deliver-their-hypotheses@2
  - mass.chart-form-spin-isomorphism@5
  assumes:
  - synthesis.n-plus-null-ground-state@11
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_half_generator_strip_is_kms_at_two_pi
- kind: check
  ref: check.py::check_past_half_is_kms_for_the_future_boost
- kind: check
  ref: check.py::check_mellin_symbol_is_the_i_state_at_two_pi
- kind: check
  ref: check.py::check_horizon_boosts_dilate_affine_generators
- kind: check
  ref: check.py::check_boost_and_dilation_conjugate_null_translations
- kind: check
  ref: check.py::check_point_spectrum_carries_no_dilated_translation
- kind: check
  ref: check.py::check_spectrum_condition_gives_positive_null_generators
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.cost-r-dictionary
  - singularity.r-regularity-fixed-locus
  - synthesis.r-lambda-regularity-cosmological-horizon
  - synthesis.c-loc-local-horizon-premise
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.twistor-form-states-only-off-the-real-slice
  - singularity.exact-equilibrium-over-determines-boundary-modes
  - synthesis.c-loc-modular-clause-moves-no-nested-patch
  - synthesis.einstein-equations-from-c-loc-and-clausius
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. The last bare i, in the Borchers relation quoted in the proof of (v) from the imported Fact angle.imported-theorems-deliver-their-hypotheses, is written with the field unit (U1): Delta^{I_4 s} U(a) Delta^{-I_4 s} = U(e^{-2 pi s} a), the unit of an abstract complex Hilbert space being I_4, as for the continuum mode space h. The window commutator [K, P] = i c P of the obstruction lives in check.py only (not edited). No i remains in the levels or proofs; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_unit_rulings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Leon''s rulings R1-R4 of 7 November 2026, folded into version 6 of this pass: R4: the contour rotation x = r e^{-I_4 pi} of the remark in (iii) written with I_4; i stays only in the Borchers relation quoted from the imported Fact, now declared imported'
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee fix folded into version 6: the Bratteli-Robinson reference in the proof of (i) is Definition 5.3.18 and Proposition 5.3.19. Version 5 -> 6, at Leon''s decision of 7 November 2026: the analysis behind (i) and (ii) (the null vacuum as the unique gauge-invariant quasi-free ground state of the null translations, its kernel, and its thermality at rapidity period 2 pi on either half-generator), which uses no premise once the state is given, is now the separate result synthesis.null-vacuum-on-a-horizon-generator, its clauses (ii) and (iii), with the setup''s weight and dilation statements its (i); the proofs of (i) and (ii) cite it (under (N+) the state is a gauge-invariant quasi-free ground state, hence the null vacuum), so that results needing only the null vacuum no longer inherit (N+) through this one. Statement unchanged; assumes edge to (N+) kept; the checks of (ii) are kept and also record the new premise. Notation as the sweep left it (I_4 in the statement and in (i)); the outside_ga reason updated to where i now stays.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the continuum mode space is written as the field unit I_4 at every level (P = I_4 d/du, the translations e^{I_4 a P}, the null-vacuum kernel (I_4/2 pi)(u - v + I_4 0)^{-1}, the Mellin modes u^{-1/2 + I_4 w}, the rotated ray e^{I_4 theta}R_+) and in the proof of (i); i stays in the complex analysis of the proof of (ii) (Mellin multiplier, contour rotation, strip continuation, Gaussian-rational check points) and in the Borchers relation quoted from the imported Fact (declared complex-analysis).'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2 adds the assumes edge to the new postulate synthesis.n-plus-null-ground-state: the formal statement states (N+) as its hypothesis and draws every clause from it, the pattern of the Einstein derivation''s assumes edge to the local-horizon premise, so holds_given now tracks (N+); the formal statement and the proof name the premise. Label: (iii) and the proof now name the weight clause of (Q) version 3, kappa(k + 1/2), beside version 2''s kappa k, as not given by (N+). Statement unchanged otherwise. Version 1 -> 2.'
  open_problem: op.r-premises-external
  note: >-
    Restates the thermal premises on the continuum and derives their common content from one premise. (N+)
    asks that a gauge-invariant quasi-free state on the continuum mode space of a horizon's generators be a
    ground state for the affine null translations along them; it contains no temperature, period or Euclidean
    section. The derivation is the null-plane form of the Bisognano-Wichmann, Hislop-Longo, Sewell and Kay-Wald
    results (standard; transport-absent), executed on the continuum mode space with the store's CAR conventions,
    the route the stored point-spectrum no-go left open. What it costs: the carrier becomes the continuum (the
    stored point-spectrum wordings are discretisations); at a Killing horizon (N+) is regularity across the
    bifurcation surface on the whole generator of the extended solution, so it covers the eternal hole and not a
    hole formed by collapse; the thermal import is relocated to that regularity condition, not removed; and the
    state has the exact joint product form, stronger than (R) on marginals. Literature cited from memory:
    Euler's integral, Mellin-Plancherel, the ground-state characterisation (Bratteli and Robinson, Vol. 2,
    5.3.19). Numerical confirmation of the symbol is in the proof text only.
  flags:
  - 'beyond one flat chart: the whole generator of the eternal horizon and of the de Sitter cosmological horizon, through its bifurcation surface'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces, exception): case (c) named as flat spacetime with vanishing gravitational field; the curved-spacetime local form read in a gauge with hb(x0) = 1, Omega(x0) = 0. Cases (a) and (b) keep their text (the whole generator u in R through the bifurcation surface) and carry the Section 14 flag. Clauses (i)-(v) unchanged; proof given a one-sentence pointer for the Christoffel computation of (iii).'
---

## formal
Let $\mathcal{H}$ be one of: (a) the future event horizon of the eternal (Kruskal-extended) Schwarzschild solution of mass $M$; (b) the future cosmological horizon of the static patch of de Sitter space with $\Lambda = 3H^{2}$; (c) a local Rindler horizon $\mathcal{H}_{p,\ell}$ of Premise \claimref{synthesis.c-loc-local-horizon-premise} in Minkowski space, flat spacetime with vanishing gravitational field ($\hb = 1$, $\Omega = 0$; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). Let $\xi$ be its boost (the Killing flow in (a), (b); the local boost in (c), with time measured in rapidity) and $\kappa$ its surface gravity: $\kappa = 1/(4M)$, $H$, $1$. On each generator let $u$ be the affine parameter with $u = 0$ on the bifurcation (edge) surface, defined on the whole generator $u \in \R$ of the extended solution, and normalised so that $\xi = \kappa u\,\partial_{u}$ on $\mathcal{H}$. Let $\mathfrak{h} = L^{2}(\R, du)\otimes K$ ($K$ the transverse and internal labels) and $\CAR(\mathfrak{h})$ the continuum mode space of Definition \claimref{obj.hawking.continuum-mode-space}, generated by the fields $\psi(u)$ with $\{\psi(u), \psi^{*}(v)\} = \delta(u - v)\otimes\id_{K}$, carrying the null translations $\nu_{a}(\psi(u)) = \psi(u + a)$ and the boost $\beta_{t}(\psi(u)) = e^{\kappa t/2}\psi(e^{\kappa t}u)$ (the weight $\tfrac12$ is the one for which $\beta_{t}$ preserves the anticommutator). Hypothesis (N$_{+}$), Premise \claimref{synthesis.n-plus-null-ground-state}: the state $\omega$ is gauge-invariant and quasi-free (assumed, not derived), invariant under $\nu$, and the generator of $\nu$ in its GNS representation is positive.
\begin{enumerate}
\item[(i)] \emph{(The null vacuum.)} Under (N$_{+}$) the symbol of $\omega$ is $\chi_{(-\infty,0)}(P)\otimes\id_{K}$ (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii)), where $P = I_{4}\,d/du$ is the one-particle generator of $\nu$, $\nu_{a}(a(f)) = a(e^{I_{4}aP}f)$ (the unit of $\mathfrak{h}$ is $I_{4}$; numbers are read in $\mathrm{span}\{1, I_{4}\}$): $\omega(\psi^{*}(v)\psi(u)) = \dfrac{I_{4}}{2\pi}\dfrac{1}{u - v + I_{4}0}\otimes\id_{K}$. No other gauge-invariant quasi-free state satisfies (N$_{+}$).
\item[(ii)] \emph{(The factor $2\pi$.)} The subalgebra $\CAR(L^{2}(\R_{+}, du)\otimes K)$ of the modes beyond the edge is $\beta$-invariant, and the restriction of $\omega$ to it is the continuum I-state of Theorem \claimref{hawking.i-state-continuum} for the one-particle boost generator $h$ at $\beta = 2\pi/\kappa$ (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(iii)): on $u^{-1/2 + I_{4}w}$, $h$ acts as $-\kappa w$ and the symbol is $(1 + e^{-2\pi w})^{-1} = (1 + e^{\beta h})^{-1}$. It is jointly KMS on the whole subalgebra and even, and it is the unique $\beta$-KMS state there. The same holds on the past half $\CAR(L^{2}(\R_{-}, du)\otimes K)$ for the boost that is future-directed there, $\beta_{-t}$, with symbol $(1 + e^{2\pi w})^{-1}$ on $|u|^{-1/2 + I_{4}w}$; the reflection $u \mapsto -u$ exchanges the two statements. Positivity fixes the sign (the opposite sign gives $-2\pi/\kappa$), and the one-sided support is needed (on the full generator the boost-continued two-point function has a pole at imaginary rapidity $\pi$, and the restriction of $\omega$ there is pure); the period $2\pi$ is the first return of the rotated half-generator $e^{I_{4}\theta}\R_{+}$ to itself.
\item[(iii)] \emph{(The continuum restatements follow.)} Hence: on (a), the modes of the generators are jointly KMS for the Killing flow at $\beta = 8\pi M$, Fermi-Dirac with density $(1 + e^{2\pi\varpi/\kappa})^{-1}$ in Killing frequency $\varpi$: the continuum restatement of (R) (Premise \claimref{singularity.r-regularity-fixed-locus}) for the eternal hole, (N$_{+}$) being there a Hartle-Hawking-type regularity condition on the whole Kruskal generator; a hole formed by collapse is not covered (its horizon generators have no $u < 0$ half, and its physical state is not a ground state for $\nu$ on the horizon). On (b), the same at $\beta = 2\pi/H$: the continuum restatement of (R$_{\Lambda}$) (Premise \claimref{synthesis.r-lambda-regularity-cosmological-horizon}). On (c), on the past half of the generators, which is the half the premise's patch uses, joint KMS for the future-directed local boost at rapidity period $2\pi$ on the patch's whole mode algebra: the continuum restatement of (R$_{\mathrm{loc}}$). In each case the state is jointly KMS and even: the joint KMS part of (Q) (Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}); its quasi-freeness is a hypothesis of (N$_{+}$), and its weight clause ($\omega_{k} = \kappa(k + \tfrac12)$ in version 3 of (Q), $\kappa k$ in version 2) is not given.
\item[(iv)] \emph{(Only on the continuum.)} (N$_{+}$) needs a nontrivial strongly continuous translation group dilated by the boost at rate $\kappa$; by Theorem \claimref{synthesis.point-spectrum-boost-admits-no-half-sided-translations} there is none when the boost acts by phases on a generating set of modes, so (N$_{+}$) cannot be posed on the windows, the countable mode space or the array of (Q). The stored wordings of (R), (R$_{\Lambda}$) and (R$_{\mathrm{loc}}$), on point-spectrum mode sets with phase-acting flows, are discretisations of the statements in (iii): the boost has no eigenvectors on the continuum, a normalisable mode $f$ has occupation $\int|\hat f(w)|^{2}m(w)\,dw$, and the ladder values $m(w_{j})$ are recovered only for modes of vanishing Mellin width.
\item[(v)] \emph{(Positivity from the spectrum condition.)} If a representation of the spacetime translations has spectrum in the closed forward cone, every future null translation has a positive generator: $\ip{\ell}{p} \ge 0$ for $p$ in the closed forward cone and $\ell$ future null, with equality only on the ray of $\ell$. In the conformal model $\Cl(2,4)$ the null translation $1 + \tfrac{\alpha}{2}\ell\nInf$ along a generator, the boost and the dilation (both unit boosts) satisfy the $ax{+}b$ relation of the Borchers form of Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}, the boost and the dilation agreeing on the generator and differing off it.
\end{enumerate}

\emph{Beyond one flat chart.} The whole generator of the eternal horizon (case (a)) and of the de Sitter cosmological horizon (case (b)), through its bifurcation surface, is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in GTG, and the whole generator, through its bifurcation surface, is read on the manifold assembled from the derived metric's charts.

## technical
The series carries three thermal premises of one shape: (R) at the black-hole horizon, (R$_{\Lambda}$) at the cosmological horizon, and (R$_{\mathrm{loc}}$) on every local Rindler horizon. Each asserts that boundary modes are KMS for a boost at the period where the boost's Euclidean section is smooth. This result restates them on the continuum of a horizon's null generators and derives that restated content from one premise with no temperature in it. Place the modes on the generators, with the affine null translations along them. Premise (N$_{+}$) asks that a gauge-invariant quasi-free state be a ground state for those translations: invariant, with positive generator. That fixes the state as the filled sea of every generator. Restricted to either side of the edge, it is the continuum I-state at rapidity period exactly $2\pi$ for the boost that is future-directed on that side. The local-horizon premise and the Einstein derivation use the past side, the generators ending on the edge.

The computation is one line in the Mellin basis $u^{-1/2 + I_{4}w}$, which diagonalises the boost: the compressed sea projection has symbol $(1 + e^{-2\pi w})^{-1}$. Equivalently, the boost-continued two-point function is analytic across the strip of width $2\pi$ in imaginary rapidity, with the KMS boundary values. Positivity fixes the sign of the period, and restriction to one side of the edge is needed (on the whole generator the state is pure). The weight $\tfrac12$ of the field is forced by the anticommutator, not chosen; integer-weight (bosonic) fields give the same $2\pi$. Every horizon of the three kinds acts on its generators' affine parameter as the dilation $u \mapsto e^{\kappa t}u$. This is the null-plane form of the results of Bisognano-Wichmann, Hislop-Longo, Sewell and Kay-Wald (Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}), transport-absent in its analytic core. What is new for the store is its execution on the continuum mode space with the store's conventions, where the point-spectrum no-go left the route open.

What the restatement costs, and what it does not cover. First, the carrier is the continuum: (N$_{+}$) cannot be posed on the point-spectrum mode sets, and the stored wordings become discretisations, recovered only for modes of vanishing Mellin width. The carrier must change in any case. On point-spectrum mode sets with phase-acting flows, (R$_{\mathrm{loc}}$) as worded is satisfiable at nonzero weight only if no mode is shared by two local horizons whose boosts act by inverse flows (filed alongside, synthesis.r-loc-needs-sheet-labelled-modes). The continuum carrier meets this automatically: the past halves of the two sheets of one edge are different null half-planes, the past and future halves of one generator are disjoint half-line algebras, and the edge is a null set that carries no mode. Second, at a Killing horizon (N$_{+}$) is the regularity of the state across the bifurcation surface, posed on the whole generator of the extended solution: the Hartle-Hawking-type state of the eternal hole. A hole formed by collapse has no $u < 0$ half, and its physical state is not a null-translation ground state on the horizon, so it is not covered. Third, the thermal input is relocated, not removed: the regularity condition is the one the stored remark on the cost of (R) lists as the import every derivation of the Hawking temperature makes. Fourth, (N$_{+}$) is strictly stronger than (R): it forces the exact joint product form over boost modes. Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} shows that this form removes the inter-mode correlations the chain's later steps need, which is why (R) was imposed on marginals; those correlations become deviations from (N$_{+}$), as they are from (Q). Where the gravitational field strength is nonzero, case (c) needs a local form of (N$_{+}$): at leading order about the point $x_0$, in a gauge with $\hb(x_0) = 1$ and $\Omega(x_0) = 0$, the state is a ground state for the null translations of the background along the generator. That is a premise, argued and not derived here. The whole generator of the eternal and de Sitter horizons, through the bifurcation surface, which cases (a) and (b) use, is global and is not carried by the store's one-chart fields, so it is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

Remarks (argued). On this continuum the edges at different $u_{0}$ give nested half-generator algebras $\CAR(L^{2}((u_{0}, \infty))\otimes K)$, which the translations $\nu_{a}$, $a \ge 0$, move properly into one another. This is the half-sided structure that Theorem \claimref{synthesis.c-loc-modular-clause-moves-no-nested-patch} shows impossible on point spectrum. (N$_{+}$) is a condition on the state, not a choice of the windows' dynamics: the null translations shift the Mellin weight, so they lie outside the number-diagonal class (L$_{E}$) admits. The stored exclusion of (R) by a unique ground state under (L$_{E}$) concerns ground states of the boost dynamics, not of the translations. Along the imaginary boost, the strip $0 < \theta < \pi$ on which the twistor form is definite (Theorem \claimref{synthesis.twistor-form-states-only-off-the-real-slice}(iii), reflection at $\theta = \pi$) is the $\Delta^{1/2}$ half of the two-point KMS strip $0 < \theta < 2\pi$, with midpoint $\theta = \pi/2$ the $\Delta^{1/4}$ point; the Mellin contour rotation through the angle $\pi$ used in the proof is the imaginary rapidity $\pi$ of that reflection.

## lay
Black holes, the horizon of an expanding universe, and the small horizons an accelerating observer sees all have a temperature. The series has so far assumed each of these temperatures with a separate premise of the same kind, each fixing a period of $2\pi$ by hand. This result shows that a single assumption with no temperature in it gives all three, once the quantum modes are taken to run continuously along each horizon's light rays. The assumption is that these modes are in their lowest-energy state with respect to sliding along the rays. Looked at from one side of the horizon, that state is exactly thermal, and the $2\pi$ comes out of the calculation, because energy is positive and the observer sees only half of each ray. There are costs. The finite lists of modes the series counts become an approximation. For a black hole the assumption describes an eternal hole in equilibrium, not one formed by collapse. And the assumption is still an input: it says the state is smooth across the point where the horizon's two halves meet, which is what every derivation of black-hole temperature assumes in some form.

## one-liner
A gauge-invariant quasi-free ground state for the affine null translations of a horizon's generators (premise (N$_{+}$), no temperature) restricts on either side of the edge to the continuum I-state at rapidity period exactly $2\pi$ for the boost future-directed there. So the continuum restatements of (R) for the eternal hole (a Hartle-Hawking-type regularity, collapse not covered), of (R$_{\Lambda}$) and of (R$_{\mathrm{loc}}$) in Minkowski space, with the joint KMS part of (Q), follow from one premise. The stored point-spectrum wordings are its discretisations, and the import is relocated to regularity across the bifurcation surface.
