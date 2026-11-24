---
id: synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
kind: claim
version: 2
title: 'First-order gravitational field: two free directions at null momentum, four constraints'
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, curvature-and-field-equations, radiation-spectrum]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
- name: Claude Fable 5.2
  role: 'the Reading, the technical and lay levels and the one-liner say which of the two options the decision of 24 November 2026 takes and which burst ratio then holds; no clause, proof or check changed'
  version: 2
  source: 'maintainer pass of 2026-11-24 (run 2026-11-24-three-routes)'
amendments:
- version: 2
  kind: restatement
  defect: 'the Reading said that whether the series gives the two free directions any existence of their own is open and listed two burst ratios without saying which holds; since 24 November 2026 the series posits a canonical pair on them at first order, and the ratio that holds is the first, with a proviso on the state near the hole'
  evidence: check.py::check_burst_ratio_under_the_options_for_the_gravitational_term
review: draft
derivations:
- name: main
  uses:
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@2
  - field-theory.operator-newtonian-coupling@4
  - field-theory.fock-space-maxwell-modes@5
  - synthesis.dimmed-burst-time-rescaled-copy@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_kernel_at_null_momentum_is_displacements_plus_two_transverse_trace_free_maps
- kind: check
  ref: check.py::check_image_at_null_momentum_is_the_sources_without_transverse_trace_free_part
- kind: check
  ref: check.py::check_pole_at_the_null_cone_is_in_the_transverse_trace_free_part
- kind: check
  ref: check.py::check_constraint_components_carry_no_second_power_of_the_frequency
- kind: check
  ref: check.py::check_free_directions_are_exchanged_by_the_pseudoscalar
- kind: check
  ref: check.py::check_static_coupling_does_not_separate_the_channels_and_pair_production_does
- kind: check
  ref: check.py::check_burst_ratio_under_the_options_for_the_gravitational_term
lineage:
  motivated_by:
  - pred.dimmed-evaporation-bursts
  - synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation
extraction:
  maintainer_pass_2026_11_24_three_routes:
    by: maintainer-2026-11-24
    date: '2026-11-24'
    note: >-
      Version 1 -> 2, on Leon's decision of 24 November 2026 (the canonical pair on the two free directions adopted
      as Premise (TT), at first order: synthesis.premise-canonical-pair-on-the-two-null-directions). The Reading now
      says that the question it left open was decided by adoption on that date, that the first of its two options
      is the one taken, and that of the two burst ratios of clause (viii) the first, (2 + g + o)/(1 + g), then
      holds, provided the state of the pair near a hole is the one from which the standard derivation takes the
      emission, which the premise does not select. The technical and lay levels and the one-liner say the same.
      Clauses (i) to (viii), the proof and the checks are unchanged; clause (viii) still lists both options, as a
      computed statement of what each gives. No assumes edge is added: no clause needs the premise. The note below
      is kept as filed; its sentence that nothing here decides whether the series gives the two directions states
      remains true of this result.
  open_problem: op.gravitational-field-at-null-momentum
  note: >-
    Filed against the fourth attack item of the problem (what the free part is, and what each option does to the
    burst baseline) and against the trace-free channel item of op.einstein-from-the-field-theory read with the
    operator source. The count of the stored results (kernel of dimension six at null momentum against four
    displacements) is sharpened to an identification with a general proof: which two directions, what the image
    is, where the pole of the curvature is, and what the stored bilinear is on the cone. The stored first-order
    theorem (its clause (ii), version 1) already names the two transverse trace-free directions N_p at a null
    momentum and the class G_p + N_p as invariant, computed at one null momentum; clause (i) here is the general,
    proved form of that statement (the kernel of the Einstein map at every nonzero null momentum), and the rest
    is new. Nothing here decides
    whether the series gives the two directions states: clause (viii) lists what the burst ratio is under each
    option and chooses none. The number 2 percent of clause (viii) is from the abstract of Page's paper, read on
    the web on 18 November 2026 (its tables were not read); it holds for a hole emitting only massless neutrinos, photons
    and the two helicity-two components, and for a hot hole emitting the whole Standard Model's content the
    fraction is smaller (argued, not computed). Clause (vii) uses the hypothesis (OS) of the stored rate result as
    that result states it, and adds no premise. The standard facts named in the Reading (the vacuum state as the
    source of emission from a hole; the transverse trace-free decomposition; the compact-support solutions of the
    linearised constraints) are cited from memory and are not used in a proof step. Decisions for the maintainer:
    the wording of the burst prediction's sentence on g = 0, which gives the ratio to a baseline that is not the
    standard expectation (clause (viii)); whether the note on where stored text names a graviton takes this
    result's clause (vi) as the reading of its group (a).
---

## formal
Units, signature and conventions of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}: $\Cl(1,3)$ with $(+,-,-,-)$, symmetric linear maps $h$ of the vectors (ten dimensions), the first-order curvature $\mathcal{R}_{k}[h](B) = -\tfrac12\,k \wedge h(B \cdot k)$ of Theorem \claimref{synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel}, its Einstein map $\mathcal{G}_{k}$, the displacements $G_{k} = \{a \mapsto (a \cdot k)\xi + (a \cdot \xi)k\}$, the pairing $\ip{h_{1}}{h_{2}} = \sum_{a} h_{1}(e_{a}) \cdot h_{2}(e^{a})$, conserved sources $\mathcal{T}(k) = 0$, and $B(\mathcal{T}_{1}, \mathcal{T}_{2}) = \ip{\mathcal{T}_{1}}{\mathcal{T}_{2}} - \tfrac12\,\tr\mathcal{T}_{1}\,\tr\mathcal{T}_{2}$. For a nonzero null $k$ let $m_{1}, m_{2}$ be orthogonal unit spacelike vectors orthogonal to $k$, and
\[
n_{+}(a) = (a \cdot m_{1})m_{1} - (a \cdot m_{2})m_{2}, \qquad n_{\times}(a) = (a \cdot m_{1})m_{2} + (a \cdot m_{2})m_{1}, \qquad N_{k} = \mathrm{span}\{n_{+}, n_{\times}\},
\]
the transverse trace-free maps; replacing $m_{i}$ by $m_{i} + c_{i}k$ changes $n_{+}, n_{\times}$ by displacements, and a rotation of $m_{1}, m_{2}$ by an angle rotates $n_{+}, n_{\times}$ by twice that angle, and $\ip{n_{+}}{n_{+}} = \ip{n_{\times}}{n_{\times}} = 2$, $\ip{n_{+}}{n_{\times}} = 0$.
\begin{enumerate}
\item[(i)] \emph{(Kernel; proved.)} At every nonzero null $k$, $\ker\mathcal{G}_{k} = \{h : h(k) = \tfrac12\,\tr(h)\,k\} = G_{k} \oplus N_{k}$, of dimension six.
\item[(ii)] \emph{(Image; proved.)} $\mathcal{G}_{k}$ is symmetric for the pairing at every $k$. At null $k$ its image is $\{\mathcal{T} : \mathcal{T}(k) = 0,\ \ip{\mathcal{T}}{n_{+}} = \ip{\mathcal{T}}{n_{\times}} = 0\}$, of dimension four. So the first-order field equation with source $\mathcal{T}$ has a solution at a null momentum exactly when the source has no transverse trace-free part there, and the solution is then fixed up to $G_{k} \oplus N_{k}$.
\item[(iii)] \emph{(The pole; proved.)} For a conserved source at null $k$ put $P_{k}\mathcal{T} = \tfrac12\ip{\mathcal{T}}{n_{+}}n_{+} + \tfrac12\ip{\mathcal{T}}{n_{\times}}n_{\times}$. Then $\mathcal{T} - \tfrac12\,\id\,\tr\mathcal{T} - P_{k}\mathcal{T} \in G_{k}$. Consequently, in a frame with timelike unit $e_{0}$, for $k = \omega e_{0} + \kappa$ with fixed spatial $\kappa \neq 0$, $m_{1}, m_{2}$ orthogonal to $e_{0}$ and $\kappa$, and sources $\mathcal{T}(\omega)$ polynomial in $\omega$ and conserved at $k$, the curvature of the field $h = \lambda\,(\mathcal{T} - \tfrac12\,\id\,\tr\mathcal{T})/Q(k)$ of the stored result's clause (i) is
\[
\mathcal{R}_{k}[h] = \lambda\,\frac{\mathcal{R}_{k}[P\mathcal{T}]}{Q(k)} + \text{a polynomial in } \omega, \qquad P\mathcal{T} = \tfrac12\ip{\mathcal{T}}{n_{+}}n_{+} + \tfrac12\ip{\mathcal{T}}{n_{\times}}n_{\times} :
\]
its only pole on the null cone is in the two transverse trace-free components.
\item[(iv)] \emph{(The bilinear on the cone; proved.)} On conserved sources at null $k$, $B(\mathcal{T}_{1}, \mathcal{T}_{2}) = \tfrac12\ip{\mathcal{T}_{1}}{n_{+}}\ip{\mathcal{T}_{2}}{n_{+}} + \tfrac12\ip{\mathcal{T}_{1}}{n_{\times}}\ip{\mathcal{T}_{2}}{n_{\times}}$: positive semidefinite of rank two, with the image of (ii) as its radical. The residue at the cone of the stored first-order interaction $8\pi G\,B/Q(k)$ is $8\pi G$ times this form: for a source with itself, a sum of two squares, one for each free direction. On conserved sources at the sampled timelike momenta $B$ has signature $(5,1)$, the negative direction being the trace, and at the sampled spacelike momenta $(3,3)$ (computed).
\item[(v)] \emph{(Four constraints; proved.)} With $k = \omega e_{0} + \kappa$, the component $e_{0} \cdot \mathcal{G}_{k}[h](e_{0})$ does not depend on $\omega$ and the components $e_{i} \cdot \mathcal{G}_{k}[h](e_{0})$ are of degree at most one in $\omega$, for every $h$; the spatial components are of degree two. So four of the ten first-order equations carry no second derivative in the time of the frame.
\item[(vi)] \emph{(One mode per null momentum; computed.)} For $m_{1}, m_{2}, \kappa/\omega$ right-handed, $I_{4}\,\mathcal{R}_{k}[n_{+}](B) = -\mathcal{R}_{k}[n_{\times}](B)$ and $I_{4}\,\mathcal{R}_{k}[n_{\times}](B) = \mathcal{R}_{k}[n_{+}](B)$ for every bivector $B$ (signs reversed for the other handedness), with $\mathcal{R}_{k}[n](I_{4}B) = I_{4}\mathcal{R}_{k}[n](B)$: the curvatures of the two free directions span one line over $\mathrm{span}\{1, I_{4}\}$, as the bivectors $f$ with $kf = 0$ do for the photon in Proposition \claimref{field-theory.fock-space-maxwell-modes}(2). In $\Cl(1,2)$ the kernel at null momentum is $G_{k}$ alone, and in $\Cl(1,4)$ it has five further directions (computed).
\item[(vii)] \emph{(What, among the stored results, tests the trace-free channel; proved for the bilinears, computed for the rates given (OS) as the stored result states it; the reading of $B_{N}$ as the interaction of a field varied within the Weyl-flat class is argued.)} At non-null $k$, with $\theta_{k}(a) = a - (a \cdot k)k/Q(k)$ and $\mathcal{T}^{\circ} = \mathcal{T} - \tfrac13\,\tr\mathcal{T}\,\theta_{k}$ for a conserved source, $B(\mathcal{T}_{1}, \mathcal{T}_{2}) = \ip{\mathcal{T}_{1}^{\circ}}{\mathcal{T}_{2}^{\circ}} - \tfrac16\,\tr\mathcal{T}_{1}\,\tr\mathcal{T}_{2}$, a trace-free part and a trace part. For two bodies at rest these are $\tfrac23 m_{1}m_{2}$ and $-\tfrac16 m_{1}m_{2}$, and the comparison bilinear, defined as $B_{N} = \tfrac12\,\tr\mathcal{T}_{1}\,\tr\mathcal{T}_{2}$, gives the same $\tfrac12 m_{1}m_{2}$. ($B_{N}$ is the bilinear of a first-order interaction $8\pi G\,B_{N}/Q(k)$ through the trace alone; that this is the interaction of a field varied only within the Weyl-flat class, with its constant fixed by the same Newtonian limit, is argued from clause (iii) of the stored first-order theorem and is not used in what is proved here.) So, among the stored results, the static coupling (Proposition \claimref{field-theory.operator-newtonian-coupling}) and the registered entangling phase do not test the trace-free channel. Pair production does: with $B_{N}$ in place of $B$ the channel weights of the stored result become $W_{ij} = \tfrac{\pi}{180}\cdot 45\,\tau_{i}\tau_{j}$, zero for chiral fermions, vectors and conformally coupled scalars; from the Standard Model's content with $\xi = 0$ the coefficient for a real scalar is $\pi^{3}/21600$, which is $3840/5789$ of the stored one, and for a copy of that content $\pi^{3}/5400$, which is the fraction $15360/1519247 \approx 0.0101$ of the stored total, about one percent; for massless vectors it is zero.
\item[(viii)] \emph{(The burst ratio under each option; computed from the stored theorem.)} In Theorem \claimref{synthesis.dimmed-burst-time-rescaled-copy} let $g_{\mathrm{h}}$ be the emission of the hole into the two free directions and $g_{\mathrm{s}}$ the same quantity in the standard expectation against which a burst is compared, both relative to this tower's emission. The theorem's ratio is $D = (2 + g_{\mathrm{h}} + o)/(1 + g_{\mathrm{s}})$. If the free directions emit as in standard physics, $g_{\mathrm{h}} = g_{\mathrm{s}} = g$ and $D = (2 + g + o)/(1 + g)$, the stored form. If the hole does not emit into them, $g_{\mathrm{h}} = 0$ and $D = (2 + o)/(1 + g)$ against the standard expectation; $D = 2 + o$ is the ratio to a baseline from which the term has also been removed, which is not the standard expectation. The two options differ by $g/(1 + g)$ for every $o$: with $g = 2/98$ (a hole emitting only massless neutrinos, photons and the helicity-two components, \cite{Page1976}), $D = 99/50$ against $49/25$ at $o = 0$.
\end{enumerate}
\emph{Reading (argued).} Clauses (i) to (v) say where a free part of the gravitational gauge field can sit and what it is: of the six components of the first-order field modulo displacements, four are fixed by the source through equations with no pole on the cone, the constraint equations of (v) among them, and two satisfy $Q(k)\,h = $ source, solvable at the cone only for a source with no component there. The first-order equation has solutions without source only in those two components, and by (vi) they form, at each null momentum, one mode over $\mathrm{span}\{1, I_{4}\}$, of helicity two in the sense of the Setting (a rotation of $m_{1}, m_{2}$ rotates $n_{+}, n_{\times}$ by twice the angle, proved under (i)), the counterpart of the stored photon mode. Whether the series gives these solutions any existence of their own was open when this result was stored (18 November 2026), and nothing here decides it. It was decided by adoption on 24 November 2026: by Leon's decision of that date the series posits, at first order, a canonical pair on the two directions at each nonzero null momentum (Premise \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}, called (TT)), the first of the two options that follow; clauses (i) to (viii) do not depend on it. If the series gives the free part states in the way it gives the photon states, the construction is that of Proposition \claimref{field-theory.fock-space-maxwell-modes} on these modes, a canonical pair on polynomials and not an element of a floor of the tower; (iv) says the sign is the healthy one. If it does not, (ii) is the price: the first-order equation with an operator source has no solution of this form at a null momentum where the source's transverse trace-free part is nonzero, and a rule is needed there (retarded, advanced or symmetric), the three differing by elements of $N_{k}$. Clause (viii) says what each option does to the burst baseline. Under (TT) the ratio that holds is the first, $D = (2 + g + o)/(1 + g)$ with $g_{\mathrm{h}} = g_{\mathrm{s}} = g$, provided the state of the pair near a hole is the ground state from which the standard derivation takes the emission, which (TT) does not select; the second, $(2 + o)/(1 + g)$, is the ratio of the option not taken. The standard derivation of emission from a hole takes it from the ground state of the emitted field; for the helicity-two channels that is a state of the free part, so $g_{\mathrm{h}} = g$ needs such a state, and without one the emission into the two directions is what the operator source of the matter excites there, of relative order $G\,T^{2}$ and negligible until the hole's last Planck times (standard, cited from memory, not computed here). At $g = 2/98$ the two options differ by $0.02$ in $D$, by less when the whole Standard Model's content is emitted (argued), and by more for a hole so cold that it emits photons alone; the prediction's kill condition, an undimmed burst, does not distinguish them. Clause (vii) is what the operator-source result says of the trace-free channel item of the Einstein problem: (OS) takes the whole stress map as source and so assumes the clause that the trace-free stress is a source, at the level of operators; it does not derive it. What it adds is a place where the clause matters inside the series: of the stored results, the static coupling and the entangling phase are blind to it (outside the series the deflection of light already tests that channel classically, light having a trace-free stress; standard, cited from memory), and the gravitational heating of the dark towers is, for all but one percent of the mirror's rate and for all of the vectors' rate, a process in the trace-free channel. Since the mean stress of an isotropic bath sources a Weyl-flat field (the stored result's clause (vii)), that process is carried by the fluctuations of the trace-free stress about a mean that has none.

## technical
The stored results count: the first-order Einstein map has kernel of dimension four (the displacements) at non-null momentum and six at null momentum. This result says which two directions are added and what follows.

At a nonzero null momentum $k$ the kernel is the set of symmetric maps with $h(k) = \tfrac12\tr(h)k$, which is the displacements together with the two transverse trace-free maps. The map is symmetric for the stored pairing, so its image at null $k$ is the conserved sources with no transverse trace-free part: the first-order equation is solvable there exactly for those. For a conserved source at null $k$, $\mathcal{T} - \tfrac12\id\tr\mathcal{T}$ differs from its transverse trace-free part by a displacement, so the pole of the first-order curvature at the cone is in the two transverse trace-free components only, and the stored bilinear $B$ restricted to the cone is the sum of two squares.

In a frame, four of the ten equations (those with one index along $e_{0}$) carry no second power of the frequency: they are constraints.

The pseudoscalar $I_{4}$ exchanges the curvatures of the two free directions: one mode over $\mathrm{span}\{1, I_{4}\}$ per null momentum, as for the photon. In three dimensions there is no free direction; in five there are five.

The static Newtonian coupling splits as $\tfrac23 - \tfrac16$ between the trace-free and trace channels and equals the trace-only bilinear normalised to Newton's law: it does not test the trace-free channel. The stored production rate does: with a trace-only source a copy of the Standard Model's content would be produced at one percent of the stored rate, and vectors not at all.

The burst ratio is $(2 + g_{\mathrm{h}} + o)/(1 + g_{\mathrm{s}})$: $(2 + g + o)/(1 + g)$ if the two directions emit as in standard physics, $(2 + o)/(1 + g)$ if they do not (under the premise (TT) adopted on 24 November 2026, \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}, the first holds, provided the state of the pair near the hole is the standard one, which the premise does not select); the difference is $g/(1 + g)$, which is two percent for a hole hot enough to emit massless neutrinos, photons and the two components and no more (the mix for which the fraction was read), less for a hotter hole emitting more species, and larger for a hole so cold that it emits photons alone.

Ledger: transport-absent. This is the linear algebra of linearised gravity (the transverse trace-free decomposition, the constraint equations, the helicity-two mode), carried out in the spacetime algebra on the stored first-order map; the series contributes the reading against its own results.

## lay
The series treats gravity as a classical field and has recorded as open whether that field has any freedom of its own. Earlier results counted: at first order the field is completely fixed by matter, except in two components at the momenta that light has, which the source does not fix.

This result identifies those two components. In standard physics they are the two polarisations of a gravitational wave; whether the series gives them any existence of their own is open, and this result does not decide it. Everything else in the field, at first order, is tied to matter by equations of the kind that fix the electric field of a charge, with nothing left over. The two components form a single mode for each such momentum, in the same way as the mode of light does in the series.

It also says what would and would not notice a decision about them. Among the series' own results, the predicted entanglement of two masses by gravity would not notice, and nor would Newton's law. The predicted dimming of the last flash of an evaporating black hole changes by about two percent between the options, for a hole that emits the lightest particles. The heating of the dark sectors by the early universe's plasma does not depend on the two components, but it does depend on a separate assumption, that all of matter's stress and not only part of it acts as a source of gravity, and this result shows that almost all of that heating would be absent without the assumption.

The result does not decide whether the two components have quantum states. It lays out the consequences of each answer.

Since 24 November 2026 the series assumes, for weak fields, that the two components do have quantum states of their own, as light does. That is an assumption adopted by decision, not something this result shows; of the two figures for the dimming of the last flash it is then the first that applies, as long as the black hole emits into the two components in the standard way.

## one-liner
At null momentum the stored first-order Einstein map has kernel the displacements plus the two transverse trace-free maps and image the conserved sources with no transverse trace-free part, the curvature's only pole on the cone is in those two components (one mode over $\mathrm{span}\{1, I_{4}\}$ per null momentum) and four equations are constraints; the static coupling does not test the trace-free channel while the stored production rate, given its hypothesis (OS), does (a trace-only source gives one percent of the mirror's rate), and the burst ratio is $(2 + g + o)/(1 + g)$ or $(2 + o)/(1 + g)$ according as the two components emit or not (the first under Premise (TT), adopted on 24 November 2026, which gives the two components states at first order and selects no state near the hole).
