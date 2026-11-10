---
id: synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages
kind: claim
version: 1
title: 'A light ray''s continuum is the twist integral of arrays; boost-ordered values are averages'
status: proved
region: synthesis
subject: entropy
tags: [thermal-premises, boundary-modes, mode-counting, needs-continuum, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - hawking.i-state-continuum@5
  - synthesis.positive-null-energy-gives-r-premises@9
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  - synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r@1
  - synthesis.residue-from-mode-entropy@4
  - synthesis.q-splits-maximum-entropy-affine-weights@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_frequencies_split_into_twisted_ladders
- kind: check
  ref: check.py::check_long_window_is_a_product_of_twisted_arrays
- kind: check
  ref: check.py::check_twist_averages_reach_the_continuum_values
- kind: check
  ref: check.py::check_entropy_across_the_twist_circle
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.window-reading-array-killing-energy
  - synthesis.positive-null-energy-gives-r-premises
  - synthesis.half-integer-weight-array-carries-half-ln2
  - synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version kept at 1. The intended citation of the free-spacing result left in the note is now a named comparison with a lineage entry; it is not a uses edge, since that result cites clause (iii) of this one.'
  open_problem: op.residue-killing-weights
  note: >-
    Attack item 4 of op.residue-killing-weights asks for a construction of the arrays out of the continuum modes
    of a light ray and the entropy of the constructed object (the construction that refutation condition (a) of
    the window reading names for energy). Registered before computing: the stored verdict "different objects"
    would be dead if a natural construction gave the Gibbs array of (Q) version 3 as a subsystem of the continuum
    in the I-state without inserting the antiperiodic condition and the Gibbs state by hand; and the conjecture
    that the twist average of the array's entropy is the continuum's pi r/6 would be dead if the exact
    computation gave another value. Outcome: no construction gives a Killing-invariant subsystem (subalgebras that are not invariant can carry the
    same occupations, for any twist, and select none); the array is one fibre of the
    continuum's decomposition by the one-window flow; the conjecture holds, with a finite exact form. Clauses (i),
    (iii) and the averaging identity of (iv) are elementary and use no premise beyond the stored spectral form of
    the continuum; the values pi r/6, pi r/12 in (iv) and the M-point values are those of the stored base comparison
    (the antiperiodic array against the continuum at window length r), cited for its clauses (ii) to (iv), and so
    hold given the imported theta identities on which the base rests; the dual-form derivation is not repeated.
    Named for comparison and recorded in lineage, not a premise:
    synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter, which cites clause (iii)
    here for its half-arrays and shows that at half a thermal period the fibres one quarter and three quarters pass
    both energy equalities. Clause (ii) is the classical description of the self-adjoint
    realisations of a first-order operator on an interval (J. von Neumann's extension theory; M. Reed and B.
    Simon, Methods of Modern Mathematical Physics II, section X.1; cited from memory), with the boundary-form
    computation given. The remark on restriction is argued and uses, from memory, the criterion of R. Powers and
    E. Stormer for quasi-equivalence of quasi-free states (Commun. Math. Phys. 16 (1970) 1) and the interval
    entropy of a thermal chiral field (P. Calabrese and J. Cardy, J. Stat. Mech. (2004) P06002; H. Casini and M.
    Huerta for the free fermion); none is a premise of a clause. That the clauses do not depend on Premise (Q), (N+) or the window
    reading being true is argued, a clause-level judgement and not a cone audit: the declared cone contains them
    through the cited theorems (the cited null-ordering theorem assumes the window reading only for its clause
    (iv), which is not used); the result says how the array those premises name sits in the continuum. It neither meets nor
    fails refutation condition (a) of the window reading (no ordering of the fibre's energy is derived) nor the
    kill condition of pred.boundary-mode-density (no residue is derived). Units: the fibre phase is written in
    the field unit I_4, numbers in span{1, I_4}; the array's own flow uses the boundary modes' unit J = e_2 e_3,
    as in the stored half-offset theorem. Transport-absent.
---

## formal
Units $\hbar = c = 1$; numbers are read in $\mathrm{span}\{1, I_4\}$. Consider one chiral complex component of a light ray: the continuum mode space over the half-generator beyond the edge, whose one-particle boost generator $h$ has simple Lebesgue spectrum on $\R$ (in the Mellin representation $h$ acts as $-\kappa w$ on $u^{-1/2 + I_4w}$, Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(ii)), in the continuum I-state at $\beta = 2\pi/\kappa$, the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$ (Theorem \claimref{hawking.i-state-continuum}). Write the one-particle space as $L^{2}(\R, d\varpi)$ with $h$ the multiplication by the Killing frequency $\varpi$. Fix $r > 0$ and the window length $L = r\beta$. For a \emph{twist} $\delta \in [0, 1)$ let $\mathcal{A}(\delta, r)$ be the fermion array with weights $\tfrac{\kappa}{r}(k + \delta)$, $k \in \Z$, in its Gibbs product state at $\beta$, so $x_{k} = 2\pi(k + \delta)/r$; let $S_{\delta}(r)$ be its entropy (a mode of weight zero carrying $\ln 2$), $e_{\delta}(r)$ its energy above the filled sea times $\beta$, $v_{\delta}(r) = \beta^{2}\operatorname{Var}(E)$, and $\tfrac{\pi}{r}B_{2}(\delta)$, $B_{2}(a) = a^{2} - a + \tfrac16$, $0 < \delta < 1$, its zeta-regularised symmetric sea energy times $\beta$ (Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii)). $\mathcal{A}(\tfrac12, 1)$ is the array of version 3 of Premise (Q), $\mathcal{A}(0, 1)$ that of version 2. Then:
\begin{enumerate}
\item[(i)] \emph{(Fibres; proved.)} The map $(U\varphi)(\delta)_{k} = \sqrt{\kappa/r}\;\varphi\bigl(\tfrac{\kappa}{r}(k + \delta)\bigr)$ is a unitary from $L^{2}(\R, d\varpi)$ onto $L^{2}([0, 1), d\delta;\,\ell^{2}(\Z))$. It carries $h$ to the family $h_{\delta} = \operatorname{diag}\bigl(\tfrac{\kappa}{r}(k + \delta)\bigr)$, the one-particle generator of $\mathcal{A}(\delta, r)$; the I-state's symbol to the family of Gibbs symbols $\operatorname{diag}\bigl(1/(e^{x_{k}} + 1)\bigr)$ of the arrays; and the one-window Killing flow $e^{I_4Lh}$ to the multiplication by the phase $e^{2\pi I_4\delta}$ (its reverse for the opposite orientation of the flow). So, fibre by fibre in the twist, the continuum in the I-state is the array $\mathcal{A}(\delta, r)$ in its Gibbs state, for every $\delta$ and every $r$; the fibre on which the one-window flow is $-1$ is $\delta = \tfrac12$ and the fibre on which it is $+1$ is $\delta = 0$. The one-window flow has no eigenvector in $L^{2}(\R, d\varpi)$, so no nonzero one-particle vector of the continuum lies in a single fibre, and no closed subspace invariant under $h$ has point spectrum: an array is a fibre of the continuum and not a Killing-invariant subsystem of it. Subalgebras that are not invariant under the Killing flow can carry the same occupations, for any twist, and select none: for unit vectors $\phi_{k}$ supported in disjoint intervals around the frequencies $\tfrac{\kappa}{r}(k + \delta)$ and tuned so that $\int|\phi_{k}|^{2}(1 + e^{\beta\varpi})^{-1}d\varpi = 1/(e^{x_{k}} + 1)$, the restriction of the I-state to $\CAR(\overline{\mathrm{span}}\{\phi_{k}\})$ is the Gibbs product state of $\mathcal{A}(\delta, r)$, for every $\delta$ and $r$; such a subalgebra is neither invariant under the flow nor localised in a window, and its frequencies are chosen by hand.
\item[(ii)] \emph{(Boundary conditions on one window; classical, the boundary form computed.)} On $L^{2}(0, L)$, functions of the Killing time along one window, the self-adjoint realisations of the Killing generator $I_4\,d/d\tau$ are exactly those with the twisted condition $\varphi(L) = e^{-2\pi I_4\delta}\varphi(0)$, $\delta \in [0, 1)$ (eigenfunctions $e^{-I_4\varpi\tau}$), and their spectra are $\tfrac{\kappa}{r}(k + \delta)$: compressing the generator to one window gives an array for each twist and selects none. The Gibbs state of every $\mathcal{A}(\delta, r)$ is quasi-free and KMS at $\beta$ for its own flow, so neither property selects a twist. Particle-hole symmetry leaves $\delta \in \{0, \tfrac12\}$, with the flow at the recurrence time the identity and the parity automorphism respectively (stored: Theorem \claimref{synthesis.q-splits-maximum-entropy-affine-weights}(iv)); the antiperiodic twist is then the weight clause of Premise (Q) version 3, which the stored theorems say (N$_{+}$) does not give (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iii)).
\item[(iii)] \emph{(Finite form; proved.)} For every integer $M \ge 1$ and every twist $\delta$, the weights of $\mathcal{A}(\delta, Mr)$ are the disjoint union of the weights of $\mathcal{A}\bigl(\tfrac{j + \delta}{M}, r\bigr)$, $j = 0, \dots, M - 1$, so with their Gibbs states $\mathcal{A}(\delta, Mr)$ is the product of these $M$ arrays, and $S$, $e$ and $v$ add. For $\delta = \tfrac12$ the twists are $\delta_{j} = \tfrac{2j + 1}{2M}$, the solutions of $e^{2\pi I_4\delta M} = -1$, and the sea energies add too, as for every twist: $\sum_{j}B_{2}\bigl(\tfrac{j + \delta}{M}\bigr) = B_{2}(\delta)/M$. In particular $\mathcal{A}(\tfrac12, 2) = \mathcal{A}(\tfrac14, 1)\otimes\mathcal{A}(\tfrac34, 1)$, and the array of (Q) version 3 itself is $\mathcal{A}(\tfrac12, 1) = \mathcal{A}(\tfrac14, \tfrac12)\otimes\mathcal{A}(\tfrac34, \tfrac12)$, two arrays of spacing $2\kappa$ exchanged by the particle-hole relabelling, each carrying $\tfrac14\ln 2$, energy $\pi/24$ above its sea and sea energy $-\pi/24$ in units of $1/\beta$.
\item[(iv)] \emph{(Twist averages are the continuum's boost-ordered window values; the identity proved, the values those of Theorem \claimref{synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r}, which holds given the imported theta identities.)} For $g \ge 0$ integrable on $\R$, $\int_{0}^{1}\sum_{k \in \Z}g\bigl(2\pi(k + \delta)/r\bigr)\,d\delta = \tfrac{r}{2\pi}\int_{\R}g(x)\,dx$. Hence, for every $r$,
\[
\int_{0}^{1}S_{\delta}(r)\,d\delta = \frac{\pi r}{6}, \qquad \int_{0}^{1}e_{\delta}(r)\,d\delta = \frac{\pi r}{12}, \qquad \int_{0}^{1}v_{\delta}(r)\,d\delta = \frac{\pi r}{6}, \qquad \int_{0}^{1}\frac{\pi}{r}B_{2}(\delta)\,d\delta = 0 :
\]
the continuum's entropy rate times the window, its boost-ordered energy over the window (Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(i)) and its variance are the uniform averages over the twist of the arrays' values, and the twist average of the symmetric sea energy is $0$, the zero of the boost ordering, while the fibre $\delta = \tfrac12$ has $-\pi/(12r)$. On orderings: the continuum's boost ground state carries $-\pi r/12$ over the window in the null ordering, and the window reading is a statement in the null ordering; the twist average reproduces the continuum's values in the boost ordering and does not reproduce the null-ordered sea value, which the fibre $\delta = \tfrac12$ matches only at $r = 1$. The averages run over arrays that fail the stored energy equalities (at $r = 1$ all but $\delta = \tfrac12$; at $r = \tfrac12$ all but the two fibres $\tfrac14$, $\tfrac34$ of (iii); in each case a null set of the average), so $\pi r/6$ as a twist average is not the entropy of an array that passes them. By (iii) the average over the $M$ twists $\delta_{j}$ of $S_{\delta}(r)$ is $S_{1/2}(Mr)/M$; at $r = 1$ it differs from $\pi/6$ by $\Delta(M)/M$, with $\Delta$ the entropy difference of Theorem \claimref{synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r}(iii): amounts in $(-0.17703, -0.17702)$, $(-0.009847, -0.009846)$, $(-2.017, -2.016) \times 10^{-5}$, $(-7.4, -7.3) \times 10^{-11}$ for $M = 1, 2, 4, 8$.
\item[(v)] \emph{(The entropy across the twist circle at $r = 1$; certified bounds.)} $S_{\delta}(1) = S_{1 - \delta}(1)$, and
\[
S_{1/2} = \tfrac12\ln 2 \;<\; S_{1/4} \in (0.51375, 0.51376) \;<\; \tfrac{\pi}{6} \;<\; S_{6/25} \;<\; S_{0} \in (0.72039, 0.72040),
\]
with $S_{1/6} \in (0.6114, 0.6115)$. The two particle-hole symmetric twists lie on opposite sides of the continuum value, $0.177$ below and $0.197$ above; $S_{\delta}(1) = \pi/6$ at a twist in $(\tfrac{6}{25}, \tfrac14)$ and at its mirror image, which are not particle-hole symmetric.
\end{enumerate}
\emph{Remark (restriction; argued).} The restriction of the I-state to the algebra of one window of Killing time is not a state of an array: in the antiperiodic window modes at $r = 1$ its occupations are $n_{k} = \tfrac{2}{\pi}\int_{\R}\cos^{2}(x/2)\,(x - x_{k})^{-2}(e^{x} + 1)^{-1}dx$, numerically $0.165, 0.0359, 0.0207$ for $k = 0, 1, 2$ against the Gibbs values $0.0414$, $8.1 \times 10^{-5}$, $1.5 \times 10^{-7}$, with $n_{k}x_{k} \to 1/\pi$, so $\sum_{k \ge 0}n_{k}$ diverges and the restricted state is not given by a density matrix in the array's Fock space; its entropy is infinite, and the finite vacuum-subtracted interval entropy known from the literature, $\tfrac16\ln(\sinh(\pi r)/(\pi r))$, about $0.217$ at $r = 1$, is neither $\tfrac12\ln 2$ nor $\pi/6$.

So, for Killing-invariant constructions from the continuum over one window: the entropy is $\tfrac12\ln 2$ only when the fibre $\delta = \tfrac12$ and its Gibbs state are selected by hand; for other twists $S_{\delta}(1)$ takes every value between $\tfrac12\ln 2$ and $S_{0} \approx 0.7204$ (continuity and the certified end values; that these two are the extremes over the whole circle is not proved); the uniform average over twists is $\pi/6$, in the boost ordering; and the restriction to a window has no finite value (argued, the Remark). Non-invariant subalgebras as in (i) realise any $S_{\delta}(r)$ and select none. The twist average is an average over arrays that, at $r = 1$, fail the stored energy equalities except at $\delta = \tfrac12$, so $\pi/6$ is not the entropy of an array that passes them.

## technical
The window reading identifies an array with one chiral component of a light ray's continuum on a window, and names as its cost that the array's spectrum is a twisted identification of Killing time which the continuum does not supply. This result says exactly how the array sits in the continuum. Splitting each Killing frequency into an integer and a fractional part, in units of the array's spacing, writes the continuum's one-particle space as a continuous family of ladders labelled by the fractional part, the twist. On each ladder the continuum's thermal state is the Gibbs state of the array with that twist, and the Killing flow over one window is the constant phase given by the twist. The array of Premise (Q) version 3 is the ladder on which that phase is $-1$. No normalisable mode of the continuum lies on a single ladder, so the array is not a Killing-invariant subsystem; it is a fibre, a quotient of Killing time by the window with a sign, not a restriction to a window. Subalgebras that are not invariant under the Killing flow can carry the same occupations, for any twist, and select none.

Three consequences follow. Compressing the Killing generator to one window needs a boundary condition, and the admissible ones are exactly the twists, none preferred; thermality and quasi-freeness hold on every ladder, so the antiperiodic condition is an input, the weight clause of (Q), not a consequence of the null ground state premise. A long antiperiodic window is exactly a product of short windows with all the twists that are roots of $-1$; the array of (Q) is itself two particle-hole conjugate arrays of twice the spacing with twists one quarter and three quarters. And, given the stored base comparison (which rests on the imported theta identities) for the values, the continuum's window values $\pi r/6$ for entropy and variance and $\pi r/12$ for energy are the uniform averages over the twist of the arrays' values, in the boost ordering; the null-ordered sea value is not a twist average, and at one thermal period every averaged array except the antiperiodic one fails the stored energy equalities. At one thermal period the entropy is $\tfrac12\ln 2$ at the antiperiodic twist and about $0.72$ at the periodic one, takes every value between, and equals $\pi/6$ at a twist near $0.24$ that has no particle-hole symmetry. Restricting the continuum's state to a window gives no array state at all (argued, from a numerical quadrature and literature cited from memory).

## lay
The series counts a black hole's entropy with ladders of quantum modes on the horizon, and assumes that a ladder stands for one stretch of a light ray on the horizon. The light ray carries a continuous range of frequencies, the ladder only evenly spaced ones. This result shows how the two are related: the light ray's frequencies can be sorted into a continuous family of ladders, each shifted by a different amount, and the light ray is all of them together. The ladder the series counts is one member of the family, the one shifted by exactly half a step. Nothing about the light ray alone picks that member out; the choice comes from a separate assumption of the series. Given the series' stored comparison of the ladder with the light ray (which rests on classical identities of special functions), the light ray's entropy per unit time, multiplied by the length of the stretch, is the average over all the shifted ladders, which is why it differs from the entropy of the one ladder that is counted; the average is taken with one particular zero of energy, and almost all the ladders in it fail the energy conditions the series imposes on the counted one. Cutting a stretch out of the light ray does not, as far as an argued estimate shows, produce a ladder at all. One can pick out modes of the light ray that imitate any of the ladders, but such a choice is not preserved in time and favours no ladder.

## one-liner
The continuum of one chiral component in the I-state is, fibre by fibre in the twist $\delta$, the Gibbs array of weights $\tfrac{\kappa}{r}(k + \delta)$; the array of (Q) version 3 is the fibre $\delta = \tfrac12$ where the one-window flow is $-1$, not a Killing-invariant subsystem (non-invariant subalgebras can carry the same occupations for any twist and select none), and its boundary condition is an input; an antiperiodic array on $Mr$ periods is the product of $M$ twisted arrays on $r$ periods; and, given the stored base comparison (hence the imported theta identities), the continuum's boost-ordered window values $\pi r/6$, $\pi r/12$ are the twist averages (the null-ordered sea value is not; at $r = 1$ every averaged array but $\delta = \tfrac12$ fails the stored energy equalities), with $S_{1/2}(1) = \tfrac12\ln 2$, $S_{0}(1) = 0.7204$ and every value between taken.
