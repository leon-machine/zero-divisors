---
id: synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt
kind: claim
version: 1
title: At gauge parameter one no curvature coupling gives the Sakharov zero and the Kasner tilt
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
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@4
  - synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike@3
  - synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off@2
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling@4
  - synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point@4
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@5
  - synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free@2
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@3
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
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'By decisions 7 and 10 of 9 November 2026: the Krein premise is an assumes edge, with the sentence that under its clause (K1) the gauge parameter is one, so the no-go at gauge parameter one is the stored statement and the free-gauge-parameter clause is recorded as the counter-statement outside the premise; the stored reading of the rung doublets'' curvature coupling is the tree-level value 0, and the Sakharov zero at three generations is a property of the attachment modules only. Version kept: the entity was accepted in the same pass.'
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
    under the one-field reading, at gauge parameter one, no value serves the zero and the tilt, or the matching and
    the tilt. Restated after review: the exclusion is scoped to gauge parameter one (the value clause (K1) of the
    Krein premise selects); under the stored heat-kernel cut-off with the gauge parameter free the zero and the tilt
    are met together at alpha = 1/3 + 4 xi, between 6.42 and 6.53, so the no-go fails there. By decision 7 of 9 November 2026 the gauge
    parameter is fixed at one by clause (K1) of the Krein premise
    (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields, an assumes edge of this result) for
    every statement about B: the no-go at gauge parameter one is therefore the stored statement, and the clause
    with the gauge parameter free is kept as the counter-statement outside the premise. The tilt formula holds under
    hypothesis (P1) of the stored tilt results. Which fields the three stored statements
    are about is a reading of their texts and is labelled argued: the cancellation is stated for attachment
    modules, the weights for the scalars of the content with one coupling each, the tilt fit for an unspecified
    curvature-coupled scalar at the isotropic point before the descent. The store already records the tree-level value 0 for the rung field's doublets, and by decision 10 of
    9 November 2026 that value is the stored reading of the doublets' coupling: the Sakharov zero at three
    generations is a property of the attachment modules (coupling 1/6 by their spectrum) and not of the content,
    on which B = 8 at gauge parameter one. Both readings are now stated by the cited results themselves:
    version 4 of the attachment-modules result carries the scope of the cancellation, and version 2 of the
    generation-number result says that under clause (K1) the zeros of B in the gauge parameter are not
    admissible. So the open problem's phrase
    'fixed by none' holds beyond tree level only; the elimination of clause (iii) is a test of the one-field
    hypothesis, not an identification of the pre-descent scalar with the weak-scale doublets. Not decided here:
    the doublets' coupling beyond tree level, which scalar the tilt fit is about,
    and the running of the coupling, whose one-loop form (a multiple of the departure from the conformal value,
    cited from memory and not derived) would make the conformal value a fixed point. The coincidence that the
    zero at seven generations is the scale-invariant coupling 3/2 is arithmetic of the two formulas and is not
    given a meaning. Transport-absent: arithmetic on stored one-loop weights and a spectrum on the three-sphere.
---

## formal
\emph{Premise.} The statement is made under Premise (KF), \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}: under its clause (K1) the one-particle form of the polarisations is the Minkowski metric (the Gupta-Bleuler form), which is the Feynman gauge, so the gauge parameter is one, $\alpha = 1$. Under the premise the no-go of clause (iii) and of the Reading is the stored statement; the clause of (ii) with the gauge parameter free is recorded as the counter-statement outside the premise. Units of one minimally coupled real scalar. For $n_{g}$ generations of sixteen Weyl components, twelve gauge vectors and $N_{S} = 4n_{h}$ real scalar components of one curvature coupling $\xi_{R}$ (normalised so that $\tfrac16$ is conformal), the stored induced quadratic coefficient is $B = 16n_{g} - 48 + N_{S}(1 - 6\xi_{R})$ in the Feynman gauge (\claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off}(i)), with $12(\alpha - 5)$ in place of $-48$ under the heat-kernel cut-off with gauge parameter $\alpha$ (\claimref{synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike}(ii)); the recorded content has $n_{h} = 2$ (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}). The stored index of a curvature-coupled scalar that exits at the isotropic Kasner point is $n - 1 = 3 - \sqrt{6\xi_{R}}$, and the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ within three standard deviations is the window $\xi_{R} \in [1.5225, 1.5481]$ (\claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}(ii), (iii), (vi)).
\begin{enumerate}
\item[(i)] \emph{(The attachment's scalar is conformally coupled; classical; proved given the two stored spectra.)} The attachment's helicity-$0$ module has conformal energies $k = l + 1$, $l \ge 0$, with multiplicity $k^{2}$ (\claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}). A real scalar obeying $(\Box + \xi_{R}R)\phi = 0$ on the Einstein static field of unit radius, where $R = 6$ and the Laplace operator of the three-sphere has eigenvalues $l(l + 2)$ with multiplicity $(l + 1)^{2}$, has squared frequencies $l(l + 2) + 6\xi_{R}$ with the same multiplicities. The two spectra agree if and only if $\xi_{R} = \tfrac16$, and any single level decides it. So a scalar that is the attachment's helicity-$0$ module has no free curvature coupling: a property of the module, not a constraint on the action of a scalar field of the content. It is the value of the first and second readings of the stored dictionary at the conformal weight $w = -1$ (\claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}(i)).
\item[(ii)] \emph{(The coefficient over the tilt window; computed.)} At $n_{g} = 3$, $n_{h} = 2$: $B = 8(1 - 6\xi_{R})$, which is $0$ at $\xi_{R} = \tfrac16$, $8$ at $\xi_{R} = 0$, and runs from $-65.08$ to $-66.3088$ over the window. The zero of $B$ in $n_{g}$ is at $\tfrac52 + 3\xi_{R}$, between $7.0675$ and $7.1443$ over the window. These numbers at $\alpha = 1$ restate the arithmetic recorded in the open problem. \emph{Counter-statement with the gauge parameter free.} Under the heat-kernel cut-off $B = 12\alpha - 4 - 48\xi_{R}$ is negative for $\alpha < \tfrac13 + 4\xi_{R}$, a bound between $6.4233$ and $6.5257$ over the window; so with the gauge parameter free, $B = 0$ and the tilt window are met together at $\alpha = \tfrac13 + 4\xi_{R} \in [6.4233, 6.5257]$ (for example $\xi_{R} = 1.53$, $\alpha = 6.4533$), and $B > 0$ with the tilt for larger $\alpha$; the exclusions below are statements at $\alpha = 1$. The stored matching of the induced coupling to Newton's constant needs $B > 0$, which at this content is $\xi_{R} < \tfrac16$.
\item[(iii)] \emph{(Elimination under the one-field hypothesis, at gauge parameter one; proved, as arithmetic on the two stored formulas.)} The hypothesis under test, which no stored statement makes, is that the scalar of the tilt fit is the multiplet of $n_{h}$ doublets of the content, with one $\xi_{R}$ in both formulas. Under it, if $B = 0$ in the Feynman gauge, then $6\xi_{R} = 1 + 4(n_{g} - 3)/n_{h}$ and the index is
\[
n - 1 = 3 - \sqrt{1 + \frac{4(n_{g} - 3)}{n_{h}}}, \qquad\text{for } n_{h} = 2:\quad n - 1 = 3 - \sqrt{2n_{g} - 5} .
\]
For $n_{h} = 2$ this is $2$ at three generations, exactly $0$ at seven (where $\xi_{R} = \tfrac32$; an arithmetic coincidence, the scale-invariant $6\xi_{R} = 9$ being odd, given no meaning) and $3 - \sqrt{11}$ at eight; the window requires $9.1355 \le 2n_{g} - 5 \le 9.2885$ and contains no integer. For every $n_{h} \le 13$ no integer $n_{g} \ge 1$ meets the window; the first content that does has $n_{h} = 14$, $n_{g} = 32$. Exact scale invariance is $8.36$ standard deviations from the measured tilt.
\item[(iv)] \emph{(The stored values; restates clause (iv) of the tree-level result.)} The conformal value gives index $2$, and every real tree-level coupling of the stored dictionary, $0 \le \xi_{R} \le \tfrac12$, gives $6\xi_{R} \le 3$, below the window's $9.1355$.
\end{enumerate}
\emph{Reading (argued, from the texts of the stored statements).} The three statements do not name one field. The stored cancellation at three generations is a statement about attachment modules, where by (i) the coupling is $\tfrac16$, and its coefficient does not depend on the number of scalars. The weights of the induced coefficient attach one coupling to each scalar of the content, and for the rung field's doublets the store records $\xi_{R} = 0$ at tree level (clause (ii) of the tree-level result; the stored example $B = 8$ is that value). That value is the stored reading of the doublets' coupling: the vanishing of the coefficient at three generations is a property of the attachment modules, where $\xi_{R} = \tfrac16$ by (i), and not of the content, on which $B = 8$ at gauge parameter one. The tilt fit concerns a curvature-coupled scalar at the isotropic Kasner point before the descent, which is no stored field. If the three are read as one coupling of the rung field's doublets, then at $\alpha = 1$ no value serves the zero and the tilt, or the matching and the tilt (the zero needs $\tfrac16$, the matching a value below $\tfrac16$, the tilt a value near $1.53$ at which $B$ is about $-65$); the zero and the matching are alternatives by definition; and with the gauge parameter free under the heat-kernel cut-off neither exclusion holds, by (ii). So at gauge parameter one the one-field reading is excluded by (ii) to (iv), and at every gauge parameter it contradicts the stored tree-level value $0$ of the doublets; as different fields the uses are independent, and what stays open is the doublets' coupling beyond tree level. Scope: gauge parameter one (Premise (KF), clause (K1)) unless stated; hypothesis (P1) of the stored tilt results (the pre-descent Kasner stage); one-loop weights as stored, the isotropic Kasner point, three standard deviations, the conversion of the scalar's spectrum into the curvature perturbation not treated (as in the stored tilt result).

## technical
A scalar field's coupling to the scalar curvature appears in three stored results: the one-loop coefficient of the induced Einstein-Hilbert term, the spectral index of a scalar leaving a Kasner approach, and the open coupling of the Higgs-like doublets. This result recomputes the coefficient over the range of couplings that fits the measured tilt (it is about $-65$, of the sign that forbids matching Newton's constant), eliminates the coupling between the two formulas (at gauge parameter one a vanishing coefficient with two doublets gives the index $3 - \sqrt{2n_{g} - 5}$, which never lands in the measured window; seven generations would be exactly scale invariant), and shows that the massless scalar of the twistor attachment has the conformal coupling forced on it by its spectrum on the three-sphere. Read as one coupling of one field at gauge parameter one, the value that clause (K1) of the Krein premise fixes, the zero and the tilt exclude each other and the tilt excludes a positive coefficient; with the gauge parameter free under the heat-kernel cut-off neither exclusion holds, both conditions being met at a gauge parameter between $6.42$ and $6.53$; that case lies outside the premise and is recorded as the counter-statement. Read as different fields the uses are independent, and the stored reading is that they are different: the doublets have coupling $0$ at tree level and the cancellation at three generations belongs to the attachment modules.

## lay
How strongly a scalar field feels the curvature of spacetime is a number the series leaves open, and it shows up in three places: in whether quantum fluctuations could generate gravity's strength, in the colour of the primordial ripples, and in the Higgs sector. Could one value do all three jobs? Not in the gauge the series' premise selects. There the value that makes the induced-gravity coefficient cancel at three families is nine times smaller than the value that would give the observed ripple colour, and at the latter value the coefficient has the wrong sign for generating gravity at all. Forcing both conditions at once would need about seven families, and even exactly seven gives a colour that the data exclude. The coefficient, however, depends on a technical choice in how the force fields are treated (the gauge parameter), and for an unusual value of that choice, about six and a half, the two conditions can be met together; so the exclusion holds only once that choice is fixed, as the series' premise on gauge fields fixes it. The result also shows that for the simplest massless scalar of the series the value is not open: its vibration frequencies on a round universe fix it.

## one-liner
In the Feynman gauge, which clause (K1) of the Krein premise selects (gauge parameter one), with one curvature coupling $\xi_{R}$ for $n_{h}$ doublets, a vanishing induced quadratic coefficient gives the Kasner index $3 - \sqrt{1 + 4(n_{g} - 3)/n_{h}}$, which meets the measured three-sigma window for no integer $n_{g}$ when $n_{h} \le 13$, and over the tilt window the coefficient at three generations is between $-66.31$ and $-65.08$; with the gauge parameter free under the heat-kernel cut-off, outside the premise, the zero and the tilt are met together at $\alpha = \tfrac13 + 4\xi_{R}$, between $6.42$ and $6.53$; the attachment's helicity-$0$ module has $\xi_{R} = \tfrac16$ forced by its spectrum.
