---
id: synthesis.spin-product-state-of-the-massless-dirac-field-is-odd-under-chirality-and-never-hadamard
kind: claim
version: 2
title: 'The massless Dirac spin-product state is never Hadamard'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, no-go, pairing-and-bogoliubov, undetermined-input, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
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
imported_from:
- citation: 'C. J. Fewster and B. Lang, Pure quasifree states of the Dirac field from the fermionic projector, Class. Quantum Grav. 32 (2015), 095001; arXiv:1408.1645.'
  key: FewsterLang2015
  locator: 'Sec. 3 (the state from the positive spectral projection of the weighted spacetime spin product; the mode functions, Xi and cos 2 theta = f^(0) m/(lambda Xi)); Thm. 3.4 (the unsoftened state on an ultrastatic slab is not Hadamard for almost every lifetime); Thm. 3.5 (softened states, f smooth, compactly supported, nonnegative and nonzero, are Hadamard); the paper treats ultrastatic slabs with compact spatial sections and assumes m > 0'
  doi: 10.1088/0264-9381/32/9/095001
- citation: 'L. Hormander, The Analysis of Linear Partial Differential Operators I, Springer, Berlin, 1983.'
  key: Hormander1983
  locator: 'Thm. 8.2.4 (pullback of distributions); cited from memory'
derivations:
- name: main
  uses:
  - synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field@2
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard@2
  - synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite@2
  - synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness@1
  - synthesis.attachment-conformal-energy-is-generated-by-z@1
  - synthesis.imported-fewster-lang-spin-product-states-of-the-dirac-field@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_spin_product_is_odd_and_current_even_under_chirality
- kind: check
  ref: check.py::check_block_density_and_block_chirality
- kind: check
  ref: check.py::check_massless_spin_product_state_is_perpendicular_to_the_conformal_vacuum
- kind: check
  ref: check.py::check_massive_block_reproduces_the_fewster_lang_angle
- kind: check
  ref: check.py::check_sharp_collar_does_not_decay_and_the_softened_bound
- kind: check
  ref: check.py::check_conformal_weight_of_the_spin_product
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-deposit-premise
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields
  - synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s list of routine imports of 2 November 2026: a uses edge to the new imported Fact synthesis.imported-fewster-lang-spin-product-states-of-the-dirac-field@1 (the Fewster-Lang construction and its Hadamard theorems on ultrastatic slabs with compact spatial sections), cited by claimref in the formal level and the proof and touched by the check of the massive block. The entity''s bibliography entry is kept for the section and theorem locators. Statement unchanged.'
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Tests a candidate for deriving (HD), synthesis.hadamard-deposit-premise: a selection of the deposit's state
    from the Dirac field's own indefinite form. The descent's conditional expectation is the identity on its
    range and the wall selects nothing, so a selection must come from elsewhere; the one built from the field
    alone is the spectral split of the spacetime spin product against the conserved current on a collar (the
    Fewster-Lang weighted spin-product state, the finite-time form of the fermionic projector state of Finster
    and Reintjes, and the Dirac analogue of the Sorkin-Johnston state; the Finster-Reintjes construction on a
    whole spacetime uses a family of masses and does not exist at m = 0, the weighted collar form does). Fewster
    and Lang treat m > 0 on ultrastatic slabs with compact spatial sections (unsoftened state not Hadamard,
    softened states Hadamard); their paper was read via the arXiv text (definition, mode functions, Thms 3.4 and
    3.5) on 2 November 2026. New here: the chirality identity and the massless no-go on every collar of every
    gravitational field, the block computation on the radiation-type (Weyl-flat) collar, and the comparison with
    the twistor form, whose positive part selects the conformal vacuum. Bears on the Krein-form theme
    (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields): an indefinite form on Dirac
    spinors used as a state selector fails for massless fields where the conformal (twistor) one succeeds.
    Transport-absent.
---

## formal
Units $\hbar = c = 1$; $\Cl(1,3)$ with $e_{0}^{2} = 1$, $e_{i}^{2} = -1$, $I_{4} = e_{0}e_{1}e_{2}e_{3}$; spinors acted on by left multiplication, unit $i$ the right unit $\psi \mapsto \psi I_{4}$; matrix forms are parenthetical readings. Let $N$ be a globally hyperbolic region of a gravitational field $(\hb, \Omega)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with a time function $t$, $\mathcal{H}$ the solutions of the Dirac equation of mass $m \ge 0$ with the conserved current product $(\psi|\phi)$ (Fact \claimref{synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field}), and $F \ge 0$ a weight in $t$ for which $\langle\psi|\phi\rangle_{F} = \int_{N}F\,\bar\psi\phi\,\mathrm{dvol}$ is bounded on $\mathcal{H}$, with $\bar\psi\phi$ read as $\langle e_{0}\tilde\psi\phi\rangle_{0}$ plus its unit part. Let $A_{F}$ be the self-adjoint operator with $(\psi|A_{F}\phi) = \langle\psi|\phi\rangle_{F}$, $\Pi_{F}$ the projection onto its kernel, and $\omega_{F}$ the gauge-invariant quasi-free state with one-particle projection $Q_{F} = \chi_{(0,\infty)}(A_{F})$: the Fewster-Lang weighted spin-product state (Fact \claimref{synthesis.imported-fewster-lang-spin-product-states-of-the-dirac-field}), the finite-time form of the fermionic projector state. Let $\Gamma\psi = I_{4}\psi I_{4}$ (the matrix $\gamma_{5}$).
\begin{enumerate}
\item[(i)] \emph{(Chirality.)} $\Gamma$ is an involution commuting with the unit, minus the grade involution on the algebra, anticommuting with the left action of vectors and commuting with that of bivectors; the spin product is odd and the current even under it. Hence for $m = 0$, $\Gamma A_{F}\Gamma = -A_{F}$ and $Q_{F} + \Gamma Q_{F}\Gamma = 1 - \Pi_{F}$.
\item[(ii)] \emph{(Massless no-go.)} If $m = 0$ and $A_{F}$ is injective, $\omega_{F}$ is Hadamard on no open subset of $N$: Hadamard would give $C^{+} = C^{-}$ (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(b)).
\item[(iii)] \emph{(Homogeneous collars.)} On a flat slab, and for $m = 0$ on a spatially flat Robertson-Walker collar $\hb(b) = b/a(\eta)$ in conformal time (with the flat weight $Fa$), each momentum-helicity block is the two-level system $H = Ms_{3} + ks_{1}$ of Theorem \claimref{synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard}, the spin-product density is $\partial H/\partial M = s_{3}$, $A_{F}$ restricted to a block is the weighted mean $\int Fa\,\tilde Us_{3}U\,d\eta$ of the turned density ($U = e^{-IH\eta}$), and $\omega_{F}$ is the pure state with Bloch vector $\hat A$. For constant $M$, with $\hat F(\lambda) = \int Fe^{i\lambda t}dt$ and $\omega^{2} = k^{2} + M^{2}$: $A\cdot\hat h = (M/\omega)\hat F(0)$, $|A|^{2} = (M/\omega)^{2}\hat F(0)^{2} + (k/\omega)^{2}|\hat F(2\omega)|^{2}$ and $1 - 2|\beta_{k}|^{2} = M\hat F(0)/(\omega|A|)$ against the vacuum. For $m = 0$, $A \perp \hat h = s_{1}$ for every weight, so $|\beta_{k}|^{2} = \tfrac12$ over the conformal vacuum wherever $\widehat{Fa}(2k) \ne 0$; for every nonzero compactly supported weight this is every momentum off a null set, $A_{F}$ is injective and (ii) applies; the energy density over the conformal vacuum diverges.
\item[(iv)] \emph{(Massive slab.)} For the sharp slab of length $T$, along $\omega T = (n + \tfrac12)\pi$, $|\beta_{k}|^{2} \to \tfrac12(1 - MT(1 + M^{2}T^{2})^{-1/2})$ ($\tfrac15$ at $MT = \tfrac34$), so the state is not Hadamard; for smooth compactly supported weights $|\beta_{k}|^{2} \le k^{2}|\hat F(2\omega)|^{2}/(4M^{2}\hat F(0)^{2})$ at large $k$, rapidly decreasing, and these states are Hadamard (Fact \claimref{synthesis.imported-fewster-lang-spin-product-states-of-the-dirac-field}, \cite[Thms 3.4, 3.5]{FewsterLang2015}, proved there for ultrastatic slabs with compact spatial sections; carried to the flat slab mode by mode, argued).
\item[(v)] \emph{(The deposit.)} So the selection by the Dirac field's own spin product gives no Hadamard state for the massless Dirac field on any collar of the descent with injective $A_{F}$ (on the radiation-type collar, for every compactly supported weight), and for massive fields only with a smooth weight, which the form does not fix: it does not supply the occupation profile that the premise (HD) leaves free (Premise \claimref{synthesis.hadamard-deposit-premise}). The massless no-go holds with torsion as well: with $\Omega$ independent of $\hb$ (the definition's Einstein-Cartan choice) the connection term of the Dirac operator is a vector plus a trivector, both odd, so $\Gamma$ still anticommutes with it. The twistor form, by contrast, selects the attachment's vacuum (Theorem \claimref{synthesis.attachment-conformal-energy-is-generated-by-z}), the conformal vacuum on a Weyl-flat collar, which is Hadamard there.
\end{enumerate}
Status: (i) proved; (ii) proved given the Fact and the invariance of wave-front sets under bundle isomorphisms (cited from memory); (iii) proved and computed, the energy-density statement argued; (iv) computed, its Hadamard conclusions imported from Fewster and Lang; (v) argued. Standard: the mode form and the massive conclusions. Transport-absent.

## technical
The premise (HD) leaves free which state the descent deposits; only its short-distance tail is fixed. One way the series might fix it without new input is through the Dirac field's own indefinite form, the spin product $\bar\psi\phi$ integrated over a collar of the descent. Split against the positive conserved current, this form singles out a state: the positive part of the operator it defines is the filled one-particle space. This is the weighted spin-product state of Fewster and Lang, the finite-time form of the fermionic projector state of Finster and Reintjes and the Dirac analogue of the Sorkin-Johnston state; Fewster and Lang showed, for massive fields on static slabs with compact spatial sections, that the sharp collar gives a state that is not Hadamard and that smoothing the collar's edges in time gives Hadamard states.

The result settles the massless case, which is the case of the radiation-type collar. The chirality, which in the spacetime algebra is left multiplication by $I_{4}$ composed with the unit (minus the grade involution), preserves the massless field equation and the current but reverses the spin product, because the spin product carries one factor $e_{0}$ and the current two. So the chirality exchanges the positive and negative parts of the spin-product operator: the selected state and its chirality image fill complementary spaces. A Hadamard state cannot do this, because the chirality is a smooth pointwise map and would carry the positive-frequency singularity onto the negative-frequency one. Mode by mode on a Weyl-flat Robertson-Walker collar this is visible directly: each momentum block is a two-level system, the spin-product density is $s_{3}$, the operator is the weighted average of $s_{3}$ turned about the energy axis, and for zero mass every turned copy is perpendicular to the energy axis, so the selected state is at right angles to the conformal vacuum in every block, an occupation of one half at every momentum, whatever the weight. For massive fields the same formula reproduces the Fewster-Lang mixing angle; the sharp collar leaves an occupation that does not fall off, smooth weights give a rapidly falling one.

So the Dirac field's own indefinite form does not supply the deposit that (HD) assumes: for massless fields it never gives a Hadamard state, and for massive fields it does so only after a smoothing that the form does not choose. The twistor form on the conformal spinors does better: its positive part is the attachment's vacuum, the conformal vacuum on a Weyl-flat collar, which is Hadamard. (HD) remains a premise.

## lay
Quantum fields need a well-behaved state, one that looks like empty space at very short distances. The series' account of the earliest universe leaves its fields in some state but does not say which, so it is assumed to be well behaved. One natural way to pick a state using only the electron field's own structure is to split its solutions with a mixed-sign quantity built from the field, the one that gives an electron its mass term, averaged over a slice of time. This result shows that for massless particles, which is how all particles behave at the universe's start, that split always picks a badly behaved state: the quantity changes sign under the swap of left- and right-handed particles, which forces the chosen state to be half filled at every energy. For massive particles it works only if the time slice is given soft edges, a choice the method does not make. A different mixed-sign quantity, from the series' twistor picture, does pick a well-behaved state.

## one-liner
The Dirac field's spin product, split against the conserved current over a collar (the Fewster-Lang weighted spin-product state, the finite-time form of the fermionic projector state), is odd under the chirality $\Gamma\psi = I_{4}\psi I_{4}$ for massless fields, so the selected state fills the chirality image of its complement and is Hadamard nowhere (occupation one half over the conformal vacuum on every spatially flat Robertson-Walker collar, for every weight); for massive fields it is Hadamard only with a smooth weight (Fewster-Lang, on ultrastatic slabs with compact spatial sections); so the spin product does not select the deposit (HD) assumes, while the twistor form selects the conformal vacuum.
