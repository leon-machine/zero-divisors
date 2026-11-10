---
id: synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element
kind: claim
version: 1
title: 'Order-four elements with square the grading: Klein twist, pseudoscalar, Majorana element'
status: proved
region: synthesis
subject: standard-model
tags: [no-go]
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
  - synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics@5
  - standard-model.majorana-element@7
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_klein_twist_is_a_polynomial_in_the_grading
- kind: check
  ref: check.py::check_pseudoscalar_of_the_ten_generators
- kind: check
  ref: check.py::check_pseudoscalar_is_the_unit_times_the_chirality
- kind: check
  ref: check.py::check_majorana_element_is_odd_under_the_pseudoscalar
- kind: check
  ref: check.py::check_signed_dimension_sums_for_fifteen_and_sixteen
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.majorana-element
  - synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5
extraction:
  open_problem: op.order-four-anomaly-and-sixteen
  note: >-
    Attack items 1 and 2 of op.order-four-anomaly-and-sixteen, answered mostly in the negative. The open problem
    names the Klein twist as the store's order-four element whose square is the grading; clause (1) shows that it
    is a polynomial in the grading, exists for every content and assigns no charge, so it cannot bear on fifteen
    against sixteen components. The element that does act with one odd charge on all sixteen is the pseudoscalar of
    the ten Majorana generators, clause (2); it lies in the group of every stage of the chain down to Pati-Salam,
    and the element T along which the stored chain breaks Pati-Salam to the Standard Model algebra, the Majorana
    term of the neutral singlet, is odd under it, clause (3). So in the store's chain there is no stage at which it
    is both a symmetry and not a gauge transformation, unless the Majorana term is absent. Clause (4) is arithmetic
    only: it records what the modulo-16 statement of the literature (the anomaly of an order-four symmetry whose
    square is fermion parity, cited from memory in the open problem: Garcia-Etxebarria and Montero; Hsieh; Tachikawa
    and Yonekura) would say about the content if it were imported. That statement is not imported, not derived and
    not used as a premise here. Not claimed: any anomaly statement; that walls with projective cross-section
    constrain the content. Transport-absent: Clifford algebra of the stored five-mode system.
---

## formal
Under Hypothesis (S), with the ten Majorana generators $\gamma_{1}, \dots, \gamma_{10}$ of the five modes ($\gamma_{p}^{2} = 1$), the creation operators $v_{j} = \tfrac12(\gamma_{2j-1} + I\gamma_{2j})$, the mode numbers $n_{j} = v_{j}^{*}v_{j}$, the chirality $\Gamma = \prod_{j}(1 - 2n_{j})$ (the parity of the total mode number), the sixteen components of one generation the even part $V_{+}$ of $V = \Lambda^{\bullet}\C^{5}$, and the Majorana element $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ of \claimref{standard-model.majorana-element}; $I$ is the commuting unit of the module (the field theory's unit in the store's reading).
\begin{enumerate}
\item \emph{(The Klein twist carries no charge.)} For an even involution $k$ commuting with $I$, the twist $V_{k} = (1 + Ik)(1 + I)^{-1}$ of \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}(iv) is $p_{+} - Ip_{-}$ with $p_{\pm} = \tfrac12(1 \pm k)$: a polynomial in $k$. So it exists on every graded module, whatever the number of components; it commutes with everything that commutes with $k$, in particular with every even element; every map that preserves the grading preserves it; and on an odd element $a$, $V_{k}aV_{k}^{-1} = -Iak$, which for two or more modes is not a multiple of $a$ nor in the span of the generators over $\mathrm{span}\{1, I\}$. It is an order-four element with $V_{k}^{2} = k$, but it assigns no charge to the generators and no condition on the content can come from it.
\item \emph{(The pseudoscalar of the ten.)} $\omega = \gamma_{1}\gamma_{2}\cdots\gamma_{10}$ satisfies $\omega^{2} = -1$, anticommutes with every $\gamma_{p}$ and commutes with all $45$ bivectors $\gamma_{p}\gamma_{q}$, hence with the gauge algebra of every stage of the chain; and $\omega = I\,\Gamma$. So $\omega$ acts on all sixteen components of $V_{+}$ by the same unit $I$ (and by $-I$ on $V_{-}$): it is an order-four element whose square $-1$ is the grading of the field algebra, with one odd charge on every component, on fifteen components as on sixteen. It is the product of the five mode rotors, $\omega = \prod_{j}\exp(\tfrac{\pi}{2}\gamma_{2j-1}\gamma_{2j})$, each generated by a bivector that preserves the split into slot and pair generators, so $\omega$ lies in the group generated by the Pati-Salam algebra (and by $\uu(5)$ and $\so(10)$).
\item \emph{(The Majorana element is odd under it.)} $T$ has grade five and $\omega T\omega^{-1} = -T$; on $V_{+}$ the bilinear form $B(\psi, T\varphi)$ of the cited claim changes sign under $\psi, \varphi \mapsto \omega\psi, \omega\varphi$. Hence $\omega$ is not in the group generated by the subalgebra that fixes $T$, the Standard Model algebra $\su(3) \oplus \su(2)_{L} \oplus \uu(1)_{Y}$ of clause (2) of the cited claim, and a vev along $T$ breaks $\omega$ to $\omega^{2} = -1$. So in the stored chain $\omega$ is a gauge transformation at the Pati-Salam stage and above, and below it is broken to the grading by the same element that gives the neutral singlet its Majorana mass; it is an unbroken symmetry that is not a gauge transformation only if the Majorana term is absent.
\item \emph{(Arithmetic of signed counts; no anomaly statement is made.)} An order-four element with square $-1$ that commutes with the Standard Model algebra acts on each of the six multiplets of $V_{+}$, of dimensions $6, 3, 3, 2, 1, 1$, by $\pm I$. The difference between the numbers of components with $+I$ and with $-I$ is $16$ for $\omega$, and takes the values $\pm 16$ and $0$ among others; on fifteen components (the neutral singlet removed) it is odd for every choice, so for an odd number of fifteen-component generations it is never divisible by $2$, and with the same uniform choice in each generation it is $15n_{g}$, divisible by $16$ only when $16$ divides $n_{g}$.
\end{enumerate}
Clause (4) is what a statement of the form "the difference must vanish modulo $16$" would give; that statement is literature cited from memory in the open problem and is neither imported nor derived here.

## technical
The open problem asks whether the store has an order-four symmetry whose square is the grading, and whether it could force sixteen components per generation. Two candidates are in the store and they behave differently. The Klein twist, which enters the geometric modular conjugations, is $p_{+} - Ip_{-}$: the identity on the even part and the unit on the odd part. It is built from the grading alone, so every theory with a grading has it, with one component or with sixteen, and conjugation by it sends a generator $a$ to $-Iak$, a product with the full parity operator. It is not a transformation of the generators by a phase, and nothing about the content can be read from it.

The element that acts by one phase on all sixteen components is the pseudoscalar of the ten Majorana generators. Its square is $-1$, it commutes with every bivector, so with every gauge algebra of the chain, and it equals the unit times the chirality. It is the centre of the rotor group of the ten, a product of five quarter-period mode rotors, each inside the Pati-Salam algebra: at the Pati-Salam stage and above it is a gauge transformation, and the sixteenth component is already forced there by the multiplet structure. Below that stage the chain is broken by the element $T$, the product of the five creation operators, which is the Majorana term of the neutral singlet. $T$ has odd grade, so the pseudoscalar anticommutes with it: the same element that gives the singlet its mass breaks the order-four element to its square. The only reading in which the order-four element is an unbroken symmetry that is not a gauge transformation is one without the Majorana term, against the stored premise that the term is realised. The last clause records the counting that the literature's modulo-16 statement would use, as arithmetic: fifteen components always give an odd signed count.

## lay
Some consistency arguments in particle physics use a symmetry that returns to the starting point only after four steps, and whose second step is the sign flip of all fermions; such a symmetry can require the fermions of one generation to come in sixteens. The store was thought to contain a symmetry of this kind in a twist used for its vacuum states. This result shows that the twist is built from the sign flip alone and so says nothing about how many fermions there are. A second four-step element does treat all sixteen fermions alike, but in the series' chain of symmetry breaking it is either part of the gauge symmetry, or it is broken by the very term that makes the sixteenth fermion, the heavy neutrino partner, massive. So within the stored chain it cannot be used to argue for sixteen rather than fifteen, unless that mass term is absent.

## one-liner
Under Hypothesis (S), the Klein twist is $p_{+} - Ip_{-}$, a polynomial in the grading that assigns no charge to generators; the pseudoscalar $\omega$ of the ten Majoranas has $\omega^{2} = -1$, equals $I\Gamma$ (one odd charge on all sixteen), lies in the Pati-Salam group, and the Majorana element satisfies $\omega T\omega^{-1} = -T$, so a vev along $T$ breaks it to the grading.
