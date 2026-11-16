---
id: synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio
kind: claim
version: 1
title: 'Conditional inheritance of $B - L$ and the conversion coefficient as a Gram ratio'
status: proved
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, hypercharge-and-anomalies, seesaw-and-majorana]
proposed_by:
  kind: ai
  session: 2026-11-16-anomaly
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-anomaly
review: draft
derivations:
- name: main
  uses:
  - standard-model.hyp-s-slot-statistics@10
  - synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them@1
  - synthesis.baryon-number-centraliser-in-the-five-mode-algebra@1
  - standard-model.majorana-element@7
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.imported-anomaly-coefficients@1
  - dark-tower-matter.mirrors-composition@3
  - synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch@5
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_stored_terms_carry_b_minus_l_except_the_majorana_element
- kind: check
  ref: check.py::check_neutral_colour_singlet_mass_forms
- kind: check
  ref: check.py::check_conserved_charges_of_the_equilibrated_interactions
- kind: check
  ref: check.py::check_gram_ratio_in_the_symmetric_phase
- kind: check
  ref: check.py::check_gram_ratio_in_the_broken_phase_and_the_bracket
- kind: check
  ref: check.py::check_lepton_flavour_does_not_enter_the_ratio
- kind: check
  ref: check.py::check_doublets_carry_one_charge_and_the_count_at_freeze_out
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.matter-asymmetry-registered-free-input
  - synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them
  - neutrino.r-descent-reheats-below-lower-heavy
extraction:
  open_problem: op.matter-asymmetry-origin
  note: >-
    Third attack item of op.matter-asymmetry-origin (the conditional inheritance theorem, with every premise
    named) and the algebraic part of its item (a) (the coefficient, the doublet count). A partial settlement
    with named premises, not a settlement: the theorem is conditional on six hypotheses, of which two are stored
    postulates (Premise (R), real breaking), one is the stored naming decision, and three are not stored
    (the anomalous weak process and its rate; a washout bound; the thermal description of the descent's state).
    Proved here, with exact checks: the weights of the stored terms under B - L, the classification of the
    bilinear forms on the sixteen invariant under colour and electric charge, the conserved spaces of the
    equilibrated interactions in the two phases, the Gram-ratio formula and its closed forms, flavour
    independence. Argued: the doublet count on the level branch, the size of the washout. Literature, checked at
    source during the run and not imported (each is a decision for the maintainer): the two closed forms of the
    coefficient (Harvey and Turner, Phys. Rev. D 42 (1990) 3344, as quoted in hep-ph/0511059, equation (13a), and
    in Khlebnikov and Shaposhnikov, hep-ph/9607386, equations (18), (19)); the interpolation between them
    (Khlebnikov and Shaposhnikov, equation (17)); the freeze-out of the weak process at 131.7 +- 2.3 GeV, below
    the crossover at 159 +- 1 GeV (D'Onofrio, Rummukainen and Tranberg, arXiv:1404.3565). Cited from memory and
    not checked: the anomaly of the baryon current ('t Hooft 1976), the equilibrium above the weak scale
    (Kuzmin, Rubakov and Shaposhnikov 1985), the washout bound on scatterings through the heavy neutral singlet
    (Fukugita and Yanagida 1990). The coefficient and its derivation are standard and transport-absent; new for
    the store are the form of the result (a Gram ratio on the stored space of charges, which makes each
    equilibrated interaction a named condition), the completeness clause over bilinear forms, and the doublet
    count. Postulates the statement is conditional on are cited in the text and are not added as assumes edges
    (maintainer only). Overlap: clause (vi) of the first cited claim holds the five conditions and four values of
    the closed form; this result derives them and does not restate that clause. Not done: any rate; the heavy
    pair's split and widths; the mirror's ratio; channels outside the bilinear terms of one family's mode algebra.
---

## formal
Under Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}) take the five-mode module, the sixteen (its even states) with the species $Q$, $u^{c}$, $d^{c}$, $L$, $e^{c}$, $\nu^{c}$, the charges $B - L$, $n_{B}$, $n_{L}$, $Y$, the weak isospin $T_{3}$ and the electric charge $Q_{\mathrm{em}} = T_{3} + Y$, the pairing $B(\cdot, \cdot)$ (\claimref{standard-model.invariant-pairing-five-modes}), the Majorana element $T$ (\claimref{standard-model.majorana-element}) and the mixed coefficients $A_{2}$, $A_{3}$, all as in \claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}. The \emph{fifteen} is the sixteen without $\nu^{c}$. A \emph{weight vector} of $B - L$ is an element $x$ of the mode algebra with $[B - L, x] = c\,x$.

\emph{The hypotheses, each named, with its standing in the store.}
\begin{itemize}
\item[(R)] Premise (R), a stored postulate (\claimref{neutrino.r-descent-reheats-below-lower-heavy}): the descent reheats below the lower heavy scale, so no heavy neutral singlet is in the plasma and the fermions of the plasma are $N_{f}$ copies of the fifteen.
\item[(W)] No washout, not stored: after the descent, the processes of second order in the Majorana element between states of the fifteen (exchange of a heavy neutral singlet; they change $B - L$ by $\pm 2$) are slower than the expansion. (R) does not imply (W); the standard estimate of the rate, cited from memory and not computed here, puts it below the expansion rate for temperatures well under about $10^{13}$ GeV.
\item[(I)] No injection: the non-thermal injection of $B - L$ by descent-populated heavy states vanishes or lies below the inherited value. It vanishes under the real-breaking assumption, a stored postulate (\claimref{neutrino.real-breaking-assumption}); without it this is a bound on a phase that has not been computed.
\item[(N)] The naming, a stored decision: the inherited datum is the total $B - L$ (\claimref{synthesis.matter-asymmetry-registered-free-input}).
\item[(A)] The anomalous weak process, literature and not stored: the weak field's four-form drives a process that changes a charge $X$ of the fermions in proportion to $A_{2}(X)$ per family, and it is in equilibrium between a freeze-out temperature $T_{*}$ near the weak scale and a temperature far above it (about $10^{12}$ GeV in the literature, from memory). Likewise the colour four-form and $A_{3}(X)$.
\item[(T)] The descent's state for the purpose, a hypothesis: the descent reheats above $T_{*}$ to a homogeneous plasma with vanishing densities of the gauge charges and small asymmetries, in which the gauge interactions and the Dirac pairings of every family are in equilibrium at $T_{*}$; densities respond linearly, $n_{X} = \tfrac{T^{2}}{6}\chi(X, \mu)$ for an assignment $\mu$ of chemical potentials, with the massless susceptibility form $\chi$ of (v).
\end{itemize}
\begin{enumerate}
\item[(i)] \emph{(Every stored term but one carries $B - L$.)} Each of the $40$ off-diagonal mode bilinears $v_{a}v_{b}$, $v_{a}w_{b}$, $w_{a}v_{b}$, $w_{a}w_{b}$ ($a < b$) is a weight vector of $B - L$, with weight $0$ (ten of them), $\pm\tfrac23$ (twelve each, the $24$ slot-pair generators) and $\pm\tfrac43$ (three each); the five $N_{a}$ have weight $0$. So each generator of the chain's gauge algebras changes $B - L$ by a fixed weight, which its gauge field carries. The slot vectors, in particular the rung vectors, have weight $0$. $A_{2}(B - L) = A_{3}(B - L) = 0$ and $B - L$ has trace zero on the sixteen. The Majorana element has $[B - L, T] = -2T$ and is a fixed direction, so nothing carries its weight. (Assembled from the two cited claims of 12 November; the count of weights is rechecked.)
\item[(ii)] \emph{(Completeness over bilinear terms.)} The bilinear forms on the sixteen invariant under colour $\su(3)$ and the electric charge, the forms a fixed vacuum direction can multiply after electroweak breaking, form a space of dimension $10$. Eight have $B - L$ weight $0$: the Dirac forms on $(Q, u^{c})$, $(Q, d^{c})$, $(L, \nu^{c})$, $(L, e^{c})$ and their transposes. Exactly two have nonzero weight: the form on $(\nu^{c}, \nu^{c})$, of weight $+2$ and weak isospin $0$, which is $B(\psi, T\varphi)$, and the form on $(\nu, \nu)$, of weight $-2$ and weak isospin $1$, which is not invariant under the Standard Model algebra and is not among the stored terms. So among terms bilinear in one family's sixteen with a fixed coefficient, the Majorana element is the only stored one that changes $B - L$, and the only other possible one is the weak-triplet neutrino form.
\item[(iii)] \emph{(Conditional inheritance.)} Assume (R), (W), (I), (A), and that the interactions of the plasma after the descent are those of (i), the anomalous processes of (A), and the Majorana element only through (W) and (I). Then every one of them conserves the total $B - L$, the gauge fields carrying the weights of (i), so the total $B - L$ after the descent equals its value at the descent: under (N), the registered datum. This is a statement about the listed interactions; it is as complete as (ii), that is over bilinear terms of one family's mode algebra with family multiplicity, and no further.
\item[(iv)] \emph{(The charges an equilibrium can carry.)} Describe an abelian charge on states by $16$ numbers, the charges of the four slot operators and the charge of the weak root vector $v_{4}w_{5}$. Those conserved by colour, the weak root vectors and the Dirac pairings with one doublet and its conjugate form a space of dimension $4$, spanned by $T_{3}$, $Y$, $n_{B}$, $n_{L}$; with the weak anomalous condition, the sum of the charge over the doublet states vanishing, a space of dimension $3$, spanned by $T_{3}$, $Y$, $B - L$. If the electrically neutral slot operators are a fixed vacuum direction, carrying no charge (the broken phase), the two spaces have dimensions $3$ and $2$, spanned by $Q_{\mathrm{em}}$, $n_{B}$, $n_{L}$ and by $Q_{\mathrm{em}}$, $B - L$. The colour anomalous condition $A_{3} = 0$ holds on all of them, and by clause (ii) of the first cited claim it is what removes the one further charge that independent charges of the slot creation and contraction operators would allow: every doublet in the plasma carries the same charge.
\item[(v)] \emph{(The coefficient as a Gram ratio.)} Let $\chi(X, X') = N_{f}\,\tr_{15}(XX') + 2\sum_{b}X(b)X'(b)$, the trace over the fifteen and the sum over the complex boson states in the plasma (the components of $N_{H}$ doublets, of hypercharge $\tfrac12$; the weak bosons, two helicities each). Under (T), with $G$ the neutral gauge charges of the phase and $\mu$ in the space of (iv) with $\chi(g, \mu) = 0$ for $g \in G$, $\mu$ is unique up to scale, and with $g$ the single charge of $G$ not orthogonal to $B - L$ ($Y$ in the symmetric phase, where $T_{3}$ is $\chi$-orthogonal to $Y$, $n_{B}$ and $B - L$; $Q_{\mathrm{em}}$ in the broken phase)
\[
c = \frac{n_{B}}{n_{B-L}} = \frac{\chi(n_{B}, B - L)\,\chi(g, g) - \chi(n_{B}, g)\,\chi(g, B - L)}{\chi(B - L, B - L)\,\chi(g, g) - \chi(g, B - L)^{2}} .
\]
Per family $\chi(Y, Y) = \tfrac{10}{3}$, $\chi(Y, B - L) = \chi(Q_{\mathrm{em}}, B - L) = \tfrac83$, $\chi(B - L, B - L) = \tfrac{13}{3}$, $\chi(n_{B}, B - L) = \tfrac43$, $\chi(n_{B}, Y) = \chi(n_{B}, Q_{\mathrm{em}}) = \tfrac23$, $\chi(Q_{\mathrm{em}}, Q_{\mathrm{em}}) = \tfrac{16}{3}$; the bosons add $N_{H}$ to $\chi(Y, Y)$ and $4 + 2N_{H}$ to $\chi(Q_{\mathrm{em}}, Q_{\mathrm{em}})$. Hence
\[
c_{\mathrm{sym}} = \frac{8N_{f} + 4N_{H}}{22N_{f} + 13N_{H}}, \qquad c_{\mathrm{br}} = \frac{8N_{f} + 4(N_{H} + 2)}{24N_{f} + 13(N_{H} + 2)},
\]
at $N_{f} = 3$: $c_{\mathrm{sym}} = \tfrac{28}{79}$, $c_{\mathrm{br}} = \tfrac{12}{37}$ for $N_{H} = 1$, and $\tfrac{8}{23}$, $\tfrac{10}{31}$ for $N_{H} = 2$. These are the closed forms of the literature, and $c_{\mathrm{sym}}$ agrees with the kernel of the five conditions of the check of Computation \claimref{dark-tower-matter.mirrors-composition}. With the neutral singlet in the plasma, against (R), $\chi(B - L, B - L)$ would be $\tfrac{16}{3}$ per family and the coefficient another number.
\item[(vi)] \emph{(Flavour.)} If the three charges $\tfrac13 n_{B} - L_{f}$ of the lepton flavours are conserved separately, the equilibrium space of (iv) grows by two dimensions and $n_{B}/n_{B-L}$ is the same $c$ for every distribution of the asymmetry over the flavours.
\item[(vii)] \emph{(The doublet count on the working branch; argued.)} The covariant coupling $Yc + \tilde{Y}c^{*}$ (\claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}) couples both doublets of the rung field to both quark types, so by (iv) both carry the same charge and $N_{H}$ counts the doublets light at $T_{*}$. On the level branch the second doublet lies at or above about $2.5$ TeV (\claimref{synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch}), nineteen times $T_{*}$ for the literature's $T_{*} \approx 132$ GeV, so $N_{H} = 1$ at freeze-out; the two-doublet values would apply only to a plasma hotter than the second doublet's mass and leave no trace, baryon number following its equilibrium value down to $T_{*}$. The literature places $T_{*}$ below the weak crossover, so the value lies between the two one-doublet limits,
\[
\tfrac{12}{37} \le c \le \tfrac{28}{79}, \qquad \tfrac{79}{28} \le \frac{(B - L)/s}{n_{B}/s} \le \tfrac{37}{12},
\]
along the literature's interpolation $(28m_{D}^{2} + 72m_{W}^{2})/(79m_{D}^{2} + 222m_{W}^{2})$, a mediant of the two limits; with $n_{B}/s = 8.7 \times 10^{-11}$ the datum $(B - L)/s$ lies between $2.45 \times 10^{-10}$ and $2.68 \times 10^{-10}$. The value $\tfrac{8}{23}$ is not the working-branch value.
\end{enumerate}
\emph{What this settles and what it does not.} Under (R), (W), (I), (N), (A), (T): the total $B - L$ after the descent is the inherited datum, and baryon number is the fraction $c$ of it, with $c$ a Gram ratio on the stored charges and $N_{H} = 1$. That is the conditional theorem the open problem asked for, with its premises named; it is not a proof that no stored dynamics generates the asymmetry. Not shown: (W) and (I) as bounds (no rate is computed); that the descent reheats above $T_{*}$; the value of $c$ within the bracket, which needs the ratio of the Higgs expectation value to the temperature at $T_{*}$; the mirror's ratio, whose plasma the cited Computation finds degenerate, so that (T) fails there; completeness beyond bilinear terms of one family (terms of higher order, instantons of the larger groups).

## technical
Two things are assembled. First, the statement that the total $B - L$ is inherited: every stored interaction other than the Majorana element changes $B - L$ by a weight that the corresponding gauge field carries, or not at all, and among all terms bilinear in one family's sixteen that respect colour and electric charge, only two can change it, the Majorana form on $\nu^{c}\nu^{c}$ and a weak-triplet form on $\nu\nu$ that the series does not hold. So if no heavy neutral singlet is in the plasma (Premise (R)), if its virtual exchange is slow (a separate condition, here called (W)), and if no non-thermal injection occurred (real breaking), $B - L$ after the descent is the datum of the descent.

Second, the fraction of it that is baryon number. In equilibrium the chemical potentials form a charge conserved by every fast interaction. On the stored classification those charges are the combinations of $T_{3}$, $Y$ and $B - L$ in the symmetric phase and of the electric charge and $B - L$ in the broken phase. Requiring the plasma to be neutral selects the one combination orthogonal to the gauge charges in the susceptibility form, and the baryon fraction is then a ratio of two Gram determinants of that form. With one per fermion state and two per boson state it reproduces the known closed forms: $28/79$ and $12/37$ for one doublet above and below the weak transition, $8/23$ and $10/31$ for two. On the working branch of the rung field the second doublet is far too heavy to be present when the weak process freezes out, so the count is one, and since the freeze-out lies below the crossover the value lies between $12/37$ and $28/79$.

## lay
The series takes the excess of matter over antimatter as given at the beginning, in the form of a conserved quantity: baryon number minus lepton number. This result states exactly under which assumptions that quantity survives unchanged to today, and names each assumption: the early universe never became hot enough to make the heavy neutrinos; their indirect effects were slow; nothing injected an extra excess. It also derives how much of the conserved quantity ends up as ordinary matter: a fixed fraction, between $12/37$ and $28/79$, about a third. The fraction is a known result of particle cosmology, rederived here from the series' own list of charges, and the series' Higgs sector is shown to select the version of it with one light Higgs doublet.

## one-liner
Under Premise (R), no washout, no injection, the naming, the imported anomalous weak process and a thermal descent state, the total $B - L$ is inherited (the Majorana element is the only stored bilinear term that changes it, and the only other possible one is the weak-triplet $\nu\nu$ form) and $n_{B} = c\,(B - L)$ with $c$ a Gram ratio of the susceptibility form on $\mathrm{span}\{g, B - L\}$: $(8N_{f} + 4N_{H})/(22N_{f} + 13N_{H})$ for $g = Y$, $(8N_{f} + 4(N_{H} + 2))/(24N_{f} + 13(N_{H} + 2))$ for $g = Q_{\mathrm{em}}$; on the level branch $N_{H} = 1$ and $\tfrac{12}{37} \le c \le \tfrac{28}{79}$.
