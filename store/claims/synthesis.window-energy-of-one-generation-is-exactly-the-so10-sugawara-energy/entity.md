---
id: synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy
kind: claim
version: 1
title: "On every window one generation's channel energy is so(10) Sugawara plus the number term"
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, representation-theory, gauge-fields, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-08-current-algebra
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-08-current-algebra
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves@1
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators@1
  - synthesis.spin10-clause-content-is-the-neutral-singlet-choice@2
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_window_quadratic_form_lemma
- kind: check
  ref: check.py::check_window_energy_is_the_u_n_sugawara_form
- kind: check
  ref: check.py::check_so10_casimir_tensor_identity
- kind: check
  ref: check.py::check_window_energy_equals_so10_sugawara_plus_number
- kind: proof
  derivation: main
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Attack on the item "the current algebra along generators" of op.qft-non-abelian-gauge-fields, its question on the
    Sugawara decomposition of the energy along a generator and whether it is exact on finite windows. Stored and used:
    the one-channel window Sugawara identity, whose antisymmetrisation argument is generalised here
    (synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (i)), the pair currents
    of the channels (synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (iv)), the tower modes
    (field-theory.imported-tower-limit), the sixteen channels of a light ray and generation
    (synthesis.slot-module-light-ray-arrays-are-weyl-components (ii)) as the even half of the slot module
    (synthesis.cpt-closure-forces-slot-module-and-chirality), and the so(10) of all bilinears of its five modes
    (synthesis.spin10-clause-content-is-the-neutral-singlet-choice). Prior art, not premises: the Sugawara
    construction (H. Sugawara, Phys. Rev. 170 (1968) 1659, cited from memory), free-fermion current algebras (P. Goddard
    and D. Olive, Int. J. Mod. Phys. A 1 (1986) 303, cited from memory) and conformal embeddings, among them so(10) at
    level 4 in su(16) at level 1 through the spinor (A. N. Schellekens and N. P. Warner, Phys. Rev. D 34 (1986) 3092;
    F. A. Bais and P. G. Bouwknegt, Nucl. Phys. B 279 (1987) 561; cited from memory), which in conformal field theory
    is an equality of stress tensors on every integrable representation; the operator form of the equality, the
    free-fermion Sugawara energy equal to that of a subalgebra because the quartic term cancels, is the symmetric-space
    criterion of P. Goddard, W. Nahm and D. Olive, Symmetric spaces, Sugawara's energy momentum tensor in two dimensions
    and free fermions, Phys. Lett. B 160 (1985) 111 (title and journal checked by the referee, volume and page from
    memory), whose condition is in substance A_C proportional to delta delta - delta delta (here the symmetric space
    E6/(SO(10) x U(1)), from memory). None of these is used. New here: the window quadratic-form lemma (i), exact on
    every finite window with no edge term, with its u(n) case (ii), which generalises the stored one-channel identity;
    and the exact finite-window form of the so(10) equality (iii), on every vector of every window, not only on
    edge-clean vectors or in the limit. The tensor identity A_so = -3 A_N is the classical symmetric-space condition,
    computed exactly here. Ledger: (i), (ii) transport-absent (finite CAR algebra of tower planes); (iii), (iv)
    transport-convenient (the sixteen channels are the series' slot module on the light rays of a horizon). What is
    not claimed: that the so(10) currents are gauge currents (only the gauge algebra inside them is), any statement
    distinguishing the halvings (the identity is a property of the spinor embedding of so(10) in gl(16), and the swap
    of the neutral singlets carries it to the vacuum-swapped half), the transverse dynamics, or the four-dimensional
    gauge field.
---

## formal
On a window of $L$ levels $k = 0, \dots, L - 1$ with $n$ channels, let the modes $c_{x,k}$ be tower modes (Fact \claimref{field-theory.imported-tower-limit}), $j^{xy}_{m} = \sum_{k}c^{*}_{x,k}c_{y,k+m}$ the pair currents (Theorem \claimref{synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators}(iv)), $N_{m} = \sum_{x}j^{xx}_{m}$ and $H = \sum_{x,k}(k + \tfrac12)n_{x,k}$. For a tensor $C_{xy,zu}$ with entries in $\mathrm{span}\{1, J\}$ ($J$ the kernel unit of the tower level) and $C_{xy,zu} = C_{zu,xy}$ put
\[
\Phi(C) = \sum_{x,y,z,u}C_{xy,zu}\Bigl(2\sum_{q \ge 1}j^{xy}_{-q}j^{zu}_{q} + j^{xy}_{0}j^{zu}_{0}\Bigr), \quad (K_{C})_{xu} = \sum_{y}C_{xy,yu}, \quad A_{C}(a, b, c, d) = C_{ac,bd} - C_{ad,bc},
\]
and $Q(A) = \sum A(x_{\alpha}, x_{\beta}, x_{\gamma}, x_{\delta})\,c^{*}_{\alpha}c^{*}_{\beta}c_{\gamma}c_{\delta}$, summed over the quadruples of modes $\alpha = (x_{\alpha}, k_{\alpha})$, \dots\ of the window with $k_{\alpha} + k_{\beta} = k_{\gamma} + k_{\delta}$. For a family of matrices $M_{A}$ with trace-dual family $M^{A}$, $C = \sum_{A}M^{A}\otimes M_{A}$ gives $\Phi(C) = 2\sum_{q \ge 1}J(M^{A})_{-q}J(M_{A})_{q} + J(M^{A})_{0}J(M_{A})_{0}$, $J(M)_{m} = \sum M_{xy}j^{xy}_{m}$, and the Sugawara energy of the family is $H_{\mathfrak{f}} = \Phi(C)/(2 + \lambda_{\mathfrak{f}})$ with $\sum_{A}[M^{A}, [M_{A}, X]] = \lambda_{\mathfrak{f}}X$.
\begin{enumerate}
\item[(i)] \emph{(Window quadratic forms.)} On every window, exactly in the algebra,
\[
\Phi(C) = \sum_{x,u}(K_{C})_{xu}\sum_{l}(2l + 1)\,c^{*}_{x,l}c_{u,l} - \tfrac12 Q(A_{C}) .
\]
\item[(ii)] \emph{(The level-one $\uu(n)$ form.)} For $C = \sum_{x,y}E_{xy}\otimes E_{yx} + 1\otimes 1$, $K_{C} = (n + 1)1$ and $A_{C} = 0$, so on every window
\[
(n + 1)H = \sum_{q \ge 1}\Bigl(\sum_{x,y}j^{yx}_{-q}j^{xy}_{q} + N_{-q}N_{q}\Bigr) + \tfrac12\Bigl(\sum_{x,y}j^{xy}_{0}j^{yx}_{0} + N_{0}^{2}\Bigr),
\]
with no edge correction; for $n = 1$ this is Theorem \claimref{synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves}(i), and in general $H = H_{\su(n)} + H_{N}$ ($\lambda_{\su(n)} = 2n$, $H_{N} = \Phi(\tfrac1n 1\otimes 1)/2$).
\item[(iii)] \emph{(The $\so(10)$ form for one generation.)} Take for the $n = 16$ channels of a light ray of one generation the even-degree states of the slot module $\Lambda^{\bullet}\C^{5}$ (Theorems \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}(ii), \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}) and for the family the $45$ bilinears $a^{*}_{a}a_{b} - \tfrac12\delta_{ab}$, $a^{*}_{a}a^{*}_{b}$, $a_{a}a_{b}$ of the five modes, which preserve this half (Theorem \claimref{synthesis.spin10-clause-content-is-the-neutral-singlet-choice}). Then $K_{C} = \tfrac{45}{16}1$, $A_{C} = -\tfrac{3}{16}(\delta_{ac}\delta_{bd} - \delta_{ad}\delta_{bc})$ and $\lambda_{\so(10)} = 4$ ($\so(10)$ at level $4$: $\lambda = 2h/k$ with $h = 8$; $c = 15$), so on every window and every vector
\[
H = H_{\so(10)} + H_{N}, \qquad H_{\so(10)} = \tfrac16\Phi(C_{\so(10)}), \quad H_{N} = \tfrac{1}{32}\Phi(1\otimes 1);
\]
equivalently $H_{\su(16)} = H_{\so(10)}$. The two sides have central values $2\cdot 45/6 = 15 = 2\cdot 255/34$.
\item[(iv)] \emph{(What it needs.)} The number-conserving part $\uu(5)$ alone does not give this (its $A_{C}$ is not a multiple of $\delta_{ac}\delta_{bd} - \delta_{ad}\delta_{bc}$): the pair bilinears are needed. For any subfamily $\mathfrak{f}_{1}, \dots, \mathfrak{f}_{r}$ of commuting, trace-orthogonal subalgebras of this $\so(10)$, among them the gauge algebra $\su(3) \oplus \su(2) \oplus \uu(1)$ acting through $\sum X_{ab}a^{*}_{a}a_{b}$, $H - H_{N} - \sum_{i}H_{\mathfrak{f}_{i}} = H_{\so(10)} - \sum_{i}H_{\mathfrak{f}_{i}}$ exactly: the part of the channels' energy not carried by the gauge factors and the number current is a function of the $\so(10)$ currents alone, on every window.
\end{enumerate}
\emph{Reading.} The energy of one generation's sixteen channels along a light ray is, on every finite window and with no edge term, the Sugawara energy of the $\so(10)$ of the five internal modes plus that of the fermion number: the $\so(10)$ currents carry all of the energy that the full set of $\uu(16)$ pair currents carries apart from the number current, a finite exact form of a conformal embedding.

## technical
For any symmetric tensor $C$ of pair-current coefficients, the window operator $\Phi(C) = \sum C(2\sum_{q\ge1}j_{-q}j_{q} + j_{0}j_{0})$ equals a one-body term with weights $2l + 1$ and coefficient matrix $K_{C} = \sum_{y}C_{xy,yu}$, minus half a level-conserving quartic whose coefficients are the antisymmetrised tensor $A_{C}(a,b,c,d) = C_{ac,bd} - C_{ad,bc}$; this holds exactly on every finite window, by the antisymmetrisation argument of the stored one-channel identity. For the $\uu(n)$ Casimir plus the number term, $A = 0$ and $K = (n + 1)1$: the energy with half-integer weights is the level-one $\uu(n)$ Sugawara form on every window. For one generation's sixteen channels and the $\so(10)$ of all bilinears of the five internal modes, $K = \tfrac{45}{16}$ and $A_{\so(10)} = -3A_{N}$, so the $\so(10)$ Sugawara energy (coefficient $\tfrac16$, adjoint Casimir $4$) plus the number term equals the channels' energy exactly: the $\su(16)$ Sugawara energy equals the $\so(10)$ one on every window. The number-conserving $\uu(5)$ alone fails. Hence the remainder of the energy after the gauge factors and the number current is built from the $\so(10)$ currents alone.

## lay
On a light ray at a horizon, one generation of matter supplies sixteen fermion channels. Their energy along the ray can be written as a sum of squares of currents built from pairs of fermions. The result is that, on any finite stretch of the ray and exactly, a much smaller set of currents suffices: those of the forty-five-dimensional symmetry of the five internal modes that build a generation, together with the total fermion number. This symmetry contains the Standard Model forces; here it is a symmetry of the currents along the light ray, not a unified gauge symmetry. Whatever energy the forces do not account for is still expressed through it.

## one-liner
On every finite window, $\Phi(C) = \sum(2l + 1)K_{C}c^{*}c - \tfrac12Q(A_{C})$ for any symmetric current tensor; hence the energy is the level-one $\uu(n)$ Sugawara form, and for one generation's sixteen channels $A_{\so(10)} = -3A_{N}$, $K = \tfrac{45}{16}$ give $H = H_{\so(10)} + H_{N}$ exactly, with no edge term.
