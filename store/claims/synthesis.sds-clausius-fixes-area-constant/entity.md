---
id: synthesis.sds-clausius-fixes-area-constant
kind: claim
version: 4
title: 'Clausius on Schwarzschild-de Sitter fixes the area constant'
status: proved
region: synthesis
subject: entropy
tags: [hawking-temperature, horizons, cosmological-constant, the-number-n, needs-continuum]
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
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.quarter-from-temperature@1
  - synthesis.de-sitter-temperature-frozen-point-norm@5
  - standard-model.imported-frozen-point-dictionary@7
  - synthesis.boundary-mode-thermal-entropy@2
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - synthesis.imported-wald-noether-charge-entropy@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_sds_clausius
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.de-sitter-entropy-pi-n-squared
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the Jacobson-Myers entropy of a Gauss-Bonnet term, cited from memory in clause (v), is now the imported Fact synthesis.imported-wald-noether-charge-entropy, added to uses and cited in the statement, proof and check; reading it as horizon entropy stays a hypothesis of clause (v). Version 1 -> 2.'
  open_problem: ein.series-action-area-law
  note: >-
    The series' action as written gives every spherical horizon the Einstein-Hilbert area law
    plus the constant of its Gauss-Bonnet term. This result shows that the series' own
    thermodynamics (horizon temperatures from the regularity premises, Hawking's Clausius
    argument on each horizon) fixes the coefficient 1/4 on both horizons of the
    Schwarzschild-de Sitter family and leaves exactly one constant per horizon, that two
    normalisations already used in the store fix both constants at zero, and that the de Sitter
    value pi N^2 then follows without the imported Gibbons-Hawking law. Transport-convenient:
    the temperatures come from the series' premises, the rest is standard horizon
    thermodynamics. The Gauss-Bonnet value of the constant rests on reading horizon entropy as the Wald entropy, whose
    Jacobson-Myers form is the imported Fact synthesis.imported-wald-noether-charge-entropy; it is computed under that reading in a result filed
    alongside, synthesis.euler-term-horizon-entropy-shift, and clause (v) here is stated for any
    constant. Fix round 2026-10-22-toe: title states the hypotheses; constants are independent of M
    (they may depend on Lambda); the Gauss-Bonnet value and the SdS black-hole bound are cited
    rather than restated.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Schwarzschild-de Sitter field on flat spacetime in the Painleve-Gullstrand gauge hb = 1 - beta P, beta^2 = 2M/r + r^2/l^2, with Q(K) = f for K = hb^{-1}(e_t); horizons are horizon loci, areas are those of cross-sections in the chart, the Killing flow is the flow of K. Hypotheses (T), (Cl) and clauses (i)-(v) unchanged.'
---

## formal
Let $\Lambda = 3/\ell^{2} > 0$, in units $\hbar = c = G = 1$, and for $0 < M < M_{N} := \ell/(3\sqrt{3})$ consider the Schwarzschild-de Sitter gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$, $\beta^{2} = 2M/r + r^{2}/\ell^{2}$, whose static Killing field $K = \hb^{-1}(e_t)$ has $Q(K) = f(r) = 1 - 2M/r - r^{2}/\ell^{2}$. The positive zeros of $f$ are the black-hole horizon locus $r_{b}$ and the cosmological horizon locus $r_{c}$, with $0 < r_{b} < \ell/\sqrt{3} < r_{c} < \ell$ (the third zero is $-(r_{b} + r_{c})$), whose cross-sections in the chart have areas $A_{h} = 4\pi r_{h}^{2}$. Suppose
\begin{enumerate}
\item[(T)] each horizon is at the temperature $T_{h} = |f'(r_{h})|/4\pi$ of the Killing flow $\partial_{t}$ (the flow of $K$), the value that (R) gives at $\Lambda = 0$ (Theorem \claimref{synthesis.quarter-from-temperature}) and (R$_{\Lambda}$) gives at $M = 0$ (Theorem \claimref{synthesis.de-sitter-temperature-frozen-point-norm}), here assumed on both horizons of the whole family;
\item[(Cl)] each horizon obeys the Clausius relation along the family at fixed $\Lambda$, $dM = T_{b}\,dS_{b}$ and $dM = -T_{c}\,dS_{c}$ (the cosmological horizon shrinks as $M$ grows), as in Hawking's argument.
\end{enumerate}
Then:
\begin{enumerate}
\item[(i)] $S_{b} = A_{b}/4 + c_{b}$ and $S_{c} = A_{c}/4 + c_{c}$ with $c_{b}$, $c_{c}$ independent of $M$ (they may depend on $\Lambda$), and every pair of such constants is compatible with (T) and (Cl): the temperatures fix the coefficient $\tfrac14$ on both horizons and nothing else.
\item[(ii)] (Z) $S_{b} \to 0$ as $M \to 0$, the normalisation of Theorem \claimref{synthesis.quarter-from-temperature}, holds if and only if $c_{b} = 0$.
\item[(iii)] (N) Continuity at the Nariai merger, $\lim S_{b} = \lim S_{c}$ as $M \to M_{N}$, where both radii tend to $\ell/\sqrt{3}$, holds if and only if $c_{c} = c_{b}$.
\item[(iv)] Under (Z) and (N), as $M \to 0$ the cosmological horizon's entropy tends to $\pi\ell^{2} = \pi N^{2}$, with $N^{2} = M_{P}^{2}/Q(I_{\Lambda})$ (Fact \claimref{standard-model.imported-frozen-point-dictionary}): the value of Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared} is reached from the series' temperatures and the black hole's normalisation, without the imported area law.
\item[(v)] An entropy that adds one constant $c \neq 0$ to every spherical horizon of the family satisfies (T), (Cl) and (N) and violates (Z). Since $S_{b} \to c$ as $M \to 0$, nonnegativity of the black hole's entropy alone excludes every $c < 0$; an entropy that is the von Neumann entropy of the horizon's boundary modes is nonnegative (each mode carries $s \ge 0$, Theorem \claimref{synthesis.boundary-mode-thermal-entropy}). (Z) fixes $c = 0$ exactly. The Gauss-Bonnet term of the MacDowell-Mansouri action as written (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}) contributes a negative constant of this kind under the hypothesis that horizon entropy is the Wald entropy, whose Jacobson-Myers form is Fact \claimref{synthesis.imported-wald-noether-charge-entropy}; its value and the resulting bound on Schwarzschild-de Sitter black holes are computed in the result filed alongside, synthesis.euler-term-horizon-entropy-shift. Under (T), (Cl) and (Z), or under nonnegativity, that contribution must be removed from horizon entropy.
\end{enumerate}

## technical
The Schwarzschild-de Sitter gravitational field on flat spacetime has two horizon loci in its Painlev\'e-Gullstrand chart, the black hole's and the cosmological one. Assume (T) that each sits at the temperature the series' regularity premises give at the ends of the family (surface gravity over $2\pi$), here assumed for every mass, and (Cl) that each obeys Hawking's Clausius relation as the mass varies at fixed $\Lambda$. Then each horizon's entropy is a quarter of the area of its cross-section plus a constant, one constant per horizon, independent of the mass, and the temperatures say nothing about the constants. Two normalisations fix them: (Z) the black hole's entropy vanishes as its mass goes to zero (Hawking's normalisation, already used for the quarter), and (N) the two entropies agree where the two horizons merge (the Nariai limit). Under (T), (Cl), (Z) and (N) both constants are zero, and the cosmological horizon of pure de Sitter space has entropy $\pi\ell^{2} = \pi N^{2}$, derived from these four hypotheses rather than from the imported area law.

A constant added to every spherical horizon passes (T), (Cl) and (N) and fails (Z); a negative one also makes small black holes' entropy negative, which a count of boundary modes cannot be. The series' MacDowell-Mansouri action as written adds such a negative constant through its Gauss-Bonnet term, under the Wald entropy hypothesis; its value is computed in a result filed alongside. Under (Z), or under nonnegativity, the topological contribution has to be removed.

## lay
A black hole in a universe with a cosmological constant has two horizons: its own and the universe's. Assuming the framework's horizon temperatures hold all along this family, and the ordinary law linking heat and entropy, each horizon's entropy comes out as a quarter of its area plus an unknown constant. Requiring a vanishing black hole to carry no entropy, and the two horizons to agree where they merge, sets both constants to zero, which gives the universe's horizon its standard entropy from these assumptions rather than from the standard area law. The framework's own form of the gravitational action instead subtracts a fixed amount from every horizon, which would make small black holes' entropy negative; if horizon entropy counts quantum modes, that subtraction cannot stand.

## one-liner
Under the series' horizon temperatures (T) and Clausius on each horizon locus of the Schwarzschild-de Sitter field on flat spacetime, $S_{h} = A_{h}/4 + c_{h}$ with $c_{h}$ independent of $M$; zero entropy at zero mass and continuity at the Nariai merger force $c_{b} = c_{c} = 0$ and give $\pi N^{2}$ for de Sitter, so a constant topological shift, such as the Gauss-Bonnet term's, must be removed.
