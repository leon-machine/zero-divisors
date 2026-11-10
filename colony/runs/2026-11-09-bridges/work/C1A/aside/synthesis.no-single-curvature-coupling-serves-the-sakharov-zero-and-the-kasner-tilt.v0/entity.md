---
id: synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt
kind: claim
version: 1
title: No single curvature coupling serves the Sakharov zero and the Kasner tilt
status: proved
region: synthesis
subject: quantum-fields
tags: [kasner, curvature-and-field-equations, no-go, undetermined-input, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
derivations:
- name: main
  uses:
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@3
  - synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike@3
  - synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off@2
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling@3
  - synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point@4
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@5
  - synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_attachment_scalar_spectrum_is_the_conformal_one_only
- kind: check
  ref: check.py::check_induced_coefficient_is_negative_over_the_tilt_window
- kind: check
  ref: check.py::check_no_generation_number_has_zero_coefficient_and_the_measured_tilt
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
  - synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off
extraction:
  open_problem: op.curvature-coupling-across-subjects
  note: >-
    The open problem asks whether the scalar curvature coupling that enters the induced quadratic coefficient, the
    fit of the primordial tilt on a Kasner approach and the rung field's doublets is one value of one field or
    several. Result. (a) Where a scalar is the attachment's helicity-zero module its coupling is forced to the
    conformal value by the spectrum, so it is not a free datum there. (b) The unreviewed figures recorded in the
    open problem reproduce: the coefficient is between -66.31 and -65.08 over the tilt window at three generations
    and its zero sits at 7.07 to 7.14 generations. (c) Eliminating the coupling between a vanishing coefficient and
    the tilt formula gives the index 3 - sqrt(2 n_g - 5) for two doublets, which meets the measured window at no
    integer; seven generations is exact scale invariance, 8.4 standard deviations from the measurement. (d) The
    positive coefficient that the stored matching clause needs requires a coupling below the conformal one. So
    under the one-field reading no value serves two of the three uses. Which fields the three stored statements
    are about is a reading of their texts and is labelled argued: the cancellation is stated for attachment
    modules, the weights for the scalars of the content with one coupling each, the tilt fit for an unspecified
    curvature-coupled scalar at the isotropic point before the descent. Not decided here: the coupling of the rung
    field's doublets (the stored action, written on a flat background, has no curvature term; the attachment gives
    the conformal value if the doublets are attachment modules), the gauge on which the vector's weight depends,
    and the running of the coupling, whose one-loop form (a multiple of the departure from the conformal value,
    cited from memory and not derived) would make the conformal value a fixed point. The coincidence that the
    zero at seven generations is the scale-invariant coupling 3/2 is arithmetic of the two formulas and is not
    given a meaning. Transport-absent: arithmetic on stored one-loop weights and a spectrum on the three-sphere.
---

## formal
Units of one minimally coupled real scalar. For $n_{g}$ generations of sixteen Weyl components, twelve gauge vectors and $N_{S} = 4n_{h}$ real scalar components of one curvature coupling $\xi_{R}$ (normalised so that $\tfrac16$ is conformal), the stored induced quadratic coefficient is $B = 16n_{g} - 48 + N_{S}(1 - 6\xi_{R})$ in the Feynman gauge (\claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off}(i)), with $12(\alpha - 5)$ in place of $-48$ under the heat-kernel cut-off with gauge parameter $\alpha$ (\claimref{synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike}(ii)); the recorded content has $n_{h} = 2$ (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}). The stored index of a curvature-coupled scalar that exits at the isotropic Kasner point is $n - 1 = 3 - \sqrt{6\xi_{R}}$, and the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ within three standard deviations is the window $\xi_{R} \in [1.5225, 1.5481]$ (\claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}(ii), (iii), (vi)).
\begin{enumerate}
\item[(i)] \emph{(The attachment's scalar is conformally coupled; proved, given the two stored spectra.)} The attachment's helicity-$0$ module has conformal energies $k = l + 1$, $l \ge 0$, with multiplicity $k^{2}$ (\claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}). A real scalar obeying $(\Box + \xi_{R}R)\phi = 0$ on the Einstein static field of unit radius, where $R = 6$ and the Laplace operator of the three-sphere has eigenvalues $l(l + 2)$ with multiplicity $(l + 1)^{2}$, has squared frequencies $l(l + 2) + 6\xi_{R}$ with the same multiplicities. The two spectra agree if and only if $\xi_{R} = \tfrac16$, and any single level decides it. So a scalar that is the attachment's helicity-$0$ module has no free curvature coupling; this is the value of the first and second readings of the stored dictionary at the conformal weight $w = -1$ (\claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}(i)).
\item[(ii)] \emph{(The coefficient over the tilt window; computed.)} At $n_{g} = 3$, $n_{h} = 2$: $B = 8(1 - 6\xi_{R})$, which is $0$ at $\xi_{R} = \tfrac16$, $8$ at $\xi_{R} = 0$, and runs from $-65.08$ to $-66.3088$ over the window. The zero of $B$ in $n_{g}$ is at $\tfrac52 + 3\xi_{R}$, between $7.0675$ and $7.1443$ over the window. With the gauge parameter free, $B = 12\alpha - 4 - 48\xi_{R}$ is negative for $\alpha < \tfrac13 + 4\xi_{R}$, a bound between $6.4233$ and $6.5258$ over the window; with the stored weight $-(3 + 6\xi_{R}\alpha)$ of a massive vector, $B = 20 - 48\xi_{R} - 72\xi_{R}\alpha$ is negative for every $\alpha \ge 0$. The stored matching of the induced coupling to Newton's constant needs $B > 0$, which at this content is $\xi_{R} < \tfrac16$.
\item[(iii)] \emph{(Elimination; proved, as arithmetic on the two stored formulas.)} If one multiplet of $n_{h}$ doublets carries the same $\xi_{R}$ in both formulas and $B = 0$ in the Feynman gauge, then $6\xi_{R} = 1 + 4(n_{g} - 3)/n_{h}$ and the index is
\[
n - 1 = 3 - \sqrt{1 + \frac{4(n_{g} - 3)}{n_{h}}}, \qquad\text{for } n_{h} = 2:\quad n - 1 = 3 - \sqrt{2n_{g} - 5} .
\]
For $n_{h} = 2$ this is $2$ at three generations, exactly $0$ at seven (where $\xi_{R} = \tfrac32$) and $3 - \sqrt{11}$ at eight; the window requires $9.1355 \le 2n_{g} - 5 \le 9.2885$ and contains no integer. For every $n_{h} \le 13$ no integer $n_{g} \ge 1$ meets the window; the first content that does has $n_{h} = 14$, $n_{g} = 32$. Exact scale invariance is $8.36$ standard deviations from the measured tilt.
\item[(iv)] \emph{(The stored values; computed.)} The conformal value gives index $2$, and every real tree-level coupling of the stored dictionary, $0 \le \xi_{R} \le \tfrac12$, gives $6\xi_{R} \le 3$, below the window's $9.1355$.
\end{enumerate}
\emph{Reading (argued, from the texts of the stored statements).} The three statements do not name one field. The stored cancellation at three generations is a statement about attachment modules, where by (i) the coupling is $\tfrac16$, and its coefficient does not depend on the number of scalars. The weights of the induced coefficient attach one coupling to each scalar of the content. The tilt fit concerns an unspecified curvature-coupled scalar at the isotropic Kasner point before the descent. If the three are read as one coupling of the rung field's doublets, no value serves two uses: the zero needs $\tfrac16$, the matching a value below $\tfrac16$, the tilt a value near $1.53$ at which $B$ is about $-65$. If they are different fields the uses are independent and the open datum is the doublets' coupling alone. Scope: one-loop weights as stored, the isotropic Kasner point, three standard deviations, the conversion of the scalar's spectrum into the curvature perturbation not treated (as in the stored tilt result).

## technical
A scalar field's coupling to the scalar curvature appears in three stored results: the one-loop coefficient of the induced Einstein-Hilbert term, the spectral index of a scalar leaving a Kasner approach, and the open coupling of the Higgs-like doublets. This result recomputes the coefficient over the range of couplings that fits the measured tilt (it is about $-65$, of the sign that forbids matching Newton's constant), eliminates the coupling between the two formulas (a vanishing coefficient with two doublets gives the index $3 - \sqrt{2n_{g} - 5}$, which never lands in the measured window; seven generations would be exactly scale invariant), and shows that the massless scalar of the twistor attachment has the conformal coupling forced on it by its spectrum on the three-sphere. Read as one coupling of one field, the three uses exclude each other pairwise; read as different fields they are independent.

## lay
How strongly a scalar field feels the curvature of spacetime is a number the series leaves open, and it shows up in three places: in whether quantum fluctuations could generate gravity's strength, in the colour of the primordial ripples, and in the Higgs sector. Could one value do all three jobs? No. The value that makes the induced-gravity coefficient cancel at three families is nine times smaller than the value that would give the observed ripple colour, and at the latter value the coefficient has the wrong sign for generating gravity at all. Forcing both conditions at once would need about seven families, and even exactly seven gives a colour that the data exclude. The result also shows that for the simplest massless scalar of the series the value is not open: its vibration frequencies on a round universe fix it.

## one-liner
With one curvature coupling $\xi_{R}$ for $n_{h}$ doublets, a vanishing induced quadratic coefficient gives the Kasner index $3 - \sqrt{1 + 4(n_{g} - 3)/n_{h}}$, which meets the measured three-sigma window for no integer $n_{g}$ when $n_{h} \le 13$ (seven generations with two doublets is exact scale invariance); over the tilt window the coefficient at three generations is between $-66.31$ and $-65.08$; and the attachment's helicity-$0$ module has $\xi_{R} = \tfrac16$ forced by its spectrum.
