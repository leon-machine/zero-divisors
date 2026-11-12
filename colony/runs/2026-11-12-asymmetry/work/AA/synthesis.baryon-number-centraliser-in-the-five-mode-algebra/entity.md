---
id: synthesis.baryon-number-centraliser-in-the-five-mode-algebra
kind: claim
version: 1
title: 'Baryon number in the five-mode algebra: its centraliser and the stored terms outside it'
status: proved
region: synthesis
subject: standard-model
tags: [matter-asymmetry, seesaw-and-majorana, hypercharge-and-anomalies, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-12-asymmetry
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-12-asymmetry
review: draft
derivations:
- name: main
  uses:
  - standard-model.hyp-s-slot-statistics@10
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.proton-decay-only-through-slot-pair@5
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - standard-model.majorana-element@7
  - standard-model.bidoublet-complex@11
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_baryon_and_lepton_number_as_elements
- kind: check
  ref: check.py::check_centraliser_is_the_shifts_by_multiples_of_three
- kind: check
  ref: check.py::check_table_of_the_forty_five
- kind: check
  ref: check.py::check_majorana_element_and_rung_vectors
- kind: check
  ref: check.py::check_exchange_reverses_the_charges
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.proton-decay-only-through-slot-pair
  - synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac
  - dark-matter.stored-asymmetry-charge-not-number
extraction:
  open_problem: op.matter-asymmetry-origin
  note: >-
    Written for the open problem on the origin of the matter asymmetry, on its third attack item (a
    proof over a class that no stored dynamics after the descent changes the charge). The kill
    condition registered before computing was: the target "the stored charge is conserved by every
    stored term" dies for a charge if one stored generator or term fails to commute with it. It was
    triggered for both candidate charges, as expected: B - L fails on the Majorana element (stored)
    and baryon number fails on the 24 slot-pair generators (stored). So the unconditional theorem is
    false and this result is the true statement in its place: the exact class of elements that
    conserve baryon number, with every bivector of the ten, the Majorana element and the rung
    vectors placed inside or outside it. What is new against the stored proton-decay result: the
    two charges as elements on all thirty-two states, not only on the sixteen; the centraliser as
    an if-and-only-if; the Majorana element inside it; the compensation identity for the six
    leptoquark generators and its failure for the 24; the grade-six part of baryon number. The
    physics is known (prior art, cited from memory: baryon and lepton number in the Pati-Salam and
    SO(10) models, J. C. Pati and A. Salam, Phys. Rev. D 10 (1974); B - L as a gauge charge broken
    by two units by the Majorana mass, R. N. Mohapatra and R. E. Marshak, Phys. Rev. Lett. 44
    (1980)); what is the store's is the statement in the mode algebra with its exact membership
    table. Not covered, and the reason the open problem stays open: anomalous electroweak processes
    are not elements of the mode algebra and nothing stored treats them as a dynamics (cited from
    memory: G. 't Hooft, Phys. Rev. Lett. 37 (1976); V. A. Kuzmin, V. A. Rubakov and M. E.
    Shaposhnikov, Phys. Lett. B 155 (1985)); thermal rates of the terms outside the class; the
    family index (one generation only); the identification of the descent's stored charge with one
    of the operators named here, which is a decision the store has not made. Ledger:
    transport-absent (algebra of the five modes under Hypothesis (S); no rule of transport is
    used); not evidence for the transport postulate.
---

## formal
Assume Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}): the three pair modes $a = 1, 2, 3$ and the two slot modes $s = 4, 5$ are one Clifford system. Work in $\Cl(5,5)$ over $\Q$ with generators $e_{i}, f_{i}$, $Q(e_{i}) = 1$, $Q(f_{i}) = -1$, set $v_{i} = \tfrac12(e_{i} + f_{i})$ (the creation operator), clear $w_{i} = \tfrac12(e_{i} - f_{i})$, $n_{i} = v_{i}w_{i}$, and the adjoint $x \mapsto x^{\dagger}$, reversion composed with $f_{i} \mapsto -f_{i}$, which exchanges $v_{i}$ and $w_{i}$. Let $k = n_{1} + n_{2} + n_{3}$ be the pair number, $B - L = 1 - \tfrac23 k$ (Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(3)), $P = \prod_{a}(1 - 2n_{a})$ the pair parity, $\Gamma = \prod_{i}(1 - 2n_{i})$ the parity of the total mode number, $\chi = -(1 - 2n_{4})(1 - 2n_{5})$ the rung parity, $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ the Majorana element (Proposition \claimref{standard-model.majorana-element}), and $\mathcal{A}_{d}$ the space of elements $x$ with $[k, x] = d\,x$. Define
\[
n_{B} = \tfrac14\bigl((B - L) - P\bigr), \qquad n_{L} = -\tfrac14\bigl(P + 3\,(B - L)\bigr).
\]
\begin{enumerate}
\item[(i)] \emph{(The two charges on all thirty-two states.)} $n_{B}$ and $n_{L}$ are functions of $k$ alone, with values $n_{B} = 0, \tfrac13, -\tfrac13, 0$ and $n_{L} = -1, 0, 0, 1$ at $k = 0, 1, 2, 3$. $\chi\Gamma = -P$, so on the sixteen ($\Gamma = 1$) they are the $n_{B} = \tfrac14((B - L) + \chi)$ and $n_{L} = \tfrac14(\chi - 3(B - L))$ of Proposition \claimref{standard-model.proton-decay-only-through-slot-pair}, and on the odd half they take on the complement of each state the opposite values. As elements, $B - L = \tfrac13\sum_{a}e_{a}f_{a} = -\tfrac23(k - \tfrac32)$ is a bivector, a multiple of the grading element of the three pairs ($[k, v_{a}] = v_{a}$, $[k, w_{a}] = -w_{a}$), while
\[
n_{B} = \tfrac1{12}\sum_{a}e_{a}f_{a} + \tfrac14\,e_{1}e_{2}e_{3}f_{1}f_{2}f_{3}
\]
has a part of grade six, and $[n_{B}, e_{a}]$ has a part of grade five: the commutator with $n_{B}$ does not map the ten vectors to vectors, so $n_{B}$ is the generator of no rotation of the ten.
\item[(ii)] \emph{(The centraliser.)} An element of $\Cl(5,5)$ commutes with $n_{B}$ if and only if it lies in $\mathcal{A}_{-3} \oplus \mathcal{A}_{0} \oplus \mathcal{A}_{3}$: its terms shift the pair number by $0$ or $\pm 3$. This space has dimension $22 \cdot 16 = 352$ of $1024$. An element commutes with $B - L$ if and only if it lies in $\mathcal{A}_{0}$, of dimension $320$.
\item[(iii)] \emph{(The forty-five bivectors.)} The bivectors commuting with $n_{B}$ are exactly the fifteen of shift $0$: the nine pair-number-preserving pair bivectors $v_{a}w_{b}$ ($a \ne b$), $n_{a} - \tfrac12$, and the six slot bivectors, that is $\uu(3) \oplus \su(2)_{L} \oplus \su(2)_{R}$ in the notation of Proposition \claimref{standard-model.automorphisms-preserve-slot-pair-split-are}. The six pair bivectors $v_{a}v_{b}$, $w_{a}w_{b}$ (shift $\pm 2$) commute with $P$ and with $\chi$ and satisfy
\[
[n_{B}, x] = \tfrac14\,[B - L, x] = \mp\tfrac13\,x :
\]
the change of $n_{B}$ they make is a fixed weight of the generator, one quarter of its $B - L$ weight. The twenty-four slot-pair bivectors (shift $\pm 1$) anticommute with $P$ and with $\chi$, and for each of them $[n_{B}, x]$ is not a multiple of $x$: no weight assigned to the generator accounts for the change of $n_{B}$.
\item[(iv)] \emph{(The Majorana element and the rung vectors.)} $[n_{B}, T] = [n_{B}, T^{\dagger}] = 0$, while $[B - L, T] = -2T$ and $[n_{L}, T] = 2T$. Every rung vector $a\,v_{s} + b\,w_{s}$ of a slot plane ($s = 4, 5$; Proposition \claimref{standard-model.bidoublet-complex}) commutes with $n_{B}$, $n_{L}$ and $B - L$. A vector of a pair plane commutes with none of them.
\item[(v)] \emph{(The exchange.)} The automorphism $X$ with $X(e_{i}) = e_{i}$, $X(f_{i}) = -f_{i}$ exchanges $v_{i}$ and $w_{i}$ for all five modes and is conjugation by $e_{1}e_{2}e_{3}e_{4}e_{5}$. It sends $n_{B}$, $n_{L}$, $B - L$, $P$ and $\Gamma$ to their negatives, fixes $\chi$, sends $T$ to $T^{\dagger}$, and maps each of the four families of (iii) (the nine, the six slot bivectors, the six, the twenty-four) and $\su(2)_{L}$ onto itself.
\item[(vi)] \emph{(Consequence.)} Let $\mathcal{D}$ be the subalgebra generated by the fifteen bivectors of shift $0$, the rung vectors of both slots, $T$ and $T^{\dagger}$, over $\Q$ or after any extension of the scalars. Every element of $\mathcal{D}$ commutes with $n_{B}$, so $u\,n_{B}\,u^{-1} = n_{B}$ for every invertible $u \in \mathcal{D}$. $\mathcal{D}$ conserves neither $B - L$ nor $n_{L}$ (it contains $T$). A subalgebra that contains one of the twenty-four, or a vector of a pair plane, does not conserve $n_{B}$.
\end{enumerate}
\emph{Reading (argued, not proved).} The stored terms of the one-generation chain are of four kinds: the gauge generators (the forty-five), the electroweak mass terms (rung vectors), the Majorana term ($T$) and their products. To the question whether one stored charge is conserved by all of them the answer is no, for each candidate: $B - L$, the charge whose sign the exchange of the flag's two halves reverses as a generator of the pair grading, is broken by $T$; $n_{B}$, the charge the measured baryon density reads, is conserved by $T$ and by everything stored except the twenty-four, whose gauge fields are massive at the unification scale (Proposition \claimref{standard-model.proton-decay-only-through-slot-pair}). So inheritance of the baryon charge is a theorem on the class $\mathcal{D}$ and conditional outside it, on a bound for the twenty-four that is not computed here. Anomalous electroweak processes are not elements of the mode algebra and are not covered: by the standard result (cited from memory in the extraction note) they change $n_{B}$ and $n_{L}$ together and conserve $B - L$, and where they act it is $B - L$ that must be protected, which among the stored terms only $T$ breaks. The statement concerns the charge; nothing is said about entropy.

## technical
In the five-mode algebra of the derived generation, baryon and lepton number are functions of the number of occupied pairs alone. $B - L$ is a bivector, proportional to the element that grades the three pairs, the same element whose sign the exchange of the two halves of the flag reverses; baryon number is that bivector plus a grade-six term, the pair parity, and generates no rotation. An element conserves baryon number exactly when it shifts the pair number by a multiple of three. That places the Standard-Model generators, the right-handed $\su(2)$, the electroweak mass terms and the Majorana element inside the conserving class, and the 24 slot-pair generators outside it with no possible compensation by a charge of their gauge fields; the six leptoquark generators of $\su(4)$ are outside as operators on the fermions but change baryon number by a quarter of their own $B - L$ weight, which the gauge field carries. The Majorana element conserves baryon number and breaks $B - L$ and lepton number by two. So no single stored charge is conserved by all stored terms.

## lay
The series holds that the excess of matter over antimatter was laid down once, at the beginning, and not manufactured later. For that to be more than a stance one must show that nothing the theory contains can change the excess afterwards. This result checks the theory's own list of interactions for one family of particles. It finds that the count of baryons (protons and neutrons, less their antiparticles) is left exactly alone by all but one group of interactions: the known forces, the terms that give particles mass, and the term that gives the heavy neutrino its mass all preserve it. The exception is a set of 24 very heavy force carriers, the ones that would make the proton decay. A second count, baryons minus leptons, is changed by the heavy-neutrino mass term. So the claim that the excess is inherited is proved for a stated class of interactions and remains conditional for the rest.

## one-liner
In the five-mode algebra, $n_{B} = \tfrac14((B - L) - P)$ depends on the pair number alone and commutes exactly with the elements shifting it by $0$ or $\pm 3$: the fifteen bivectors of $\uu(3) \oplus \su(2)_{L} \oplus \su(2)_{R}$, the rung vectors and the Majorana element $T$ (which breaks $B - L$ by $2$), and not the twenty-four slot-pair generators.
