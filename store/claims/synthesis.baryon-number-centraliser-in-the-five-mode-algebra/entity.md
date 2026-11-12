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
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Wording, version kept: the Reading said that the charge is inherited on the class D; by Leon''s decision of 12 November 2026 the inherited charge is B - L (dark-matter.stored-asymmetry-charge-not-number, version 11), so the sentence now says that baryon number is unchanged on that class.'
  open_problem: op.matter-asymmetry-origin
  note: >-
    Written for the open problem on the origin of the matter asymmetry, on its third attack item (a
    proof over a class that no stored dynamics after the descent changes the charge). The kill
    condition registered before computing was: the target "the stored charge is conserved by every
    stored term" dies for a charge if one stored generator or term fails to commute with it. It was
    triggered for both candidate charges, as expected: B - L fails on the Majorana element (stored)
    and baryon number fails on the 24 slot-pair generators (stored). So the unconditional theorem is
    false and this result is the true statement in its place: the exact class of elements that
    commute with baryon number, with every bivector of the ten, the Majorana element and the slot
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
    of the operators named here, which is a decision the store has not made. Clause (v) is the five-mode instance of the result on the exchange of set and clear for any
    number of switches (synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state,
    proposed with this one), kept here only for what it does to the charges; clause (iv) and the
    statement on the twenty-four overlap with the classification of the abelian charges of the
    sixteen (synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them, proposed
    with this one), which treats all charges commuting with the gauge algebra, the mixed
    coefficients and the question which operator the stored charge is; this result keeps the
    centraliser on the whole algebra, the grade-six part, the six leptoquark bivectors and the
    class D. Ledger:
    transport-absent (algebra of the five modes under Hypothesis (S); no rule of transport is
    used); not evidence for the transport postulate.
---

## formal
Assume Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}): the three pair modes $a = 1, 2, 3$ and the two slot modes $s = 4, 5$ are one Clifford system. Work in $\Cl(5,5)$ over $\Q$ with generators $e_{i}, f_{i}$, $Q(e_{i}) = 1$, $Q(f_{i}) = -1$, set $v_{i} = \tfrac12(e_{i} + f_{i})$ (the creation operator), clear $w_{i} = \tfrac12(e_{i} - f_{i})$, $n_{i} = v_{i}w_{i}$, and the adjoint $x \mapsto x^{\dagger}$, reversion composed with $f_{i} \mapsto -f_{i}$, which exchanges $v_{i}$ and $w_{i}$. Let $k = n_{1} + n_{2} + n_{3}$ be the pair number, $B - L = 1 - \tfrac23 k$ (Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(3)), $P = \prod_{a}(1 - 2n_{a})$ the pair parity, $\Gamma = \prod_{i}(1 - 2n_{i})$ the parity of the total mode number, $\chi = -(1 - 2n_{4})(1 - 2n_{5})$ the rung parity, $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ the Majorana element (Proposition \claimref{standard-model.majorana-element}), and $\mathcal{A}_{d}$ the space of elements $x$ with $[k, x] = d\,x$. Define
\[
n_{B} = \tfrac14\bigl((B - L) - P\bigr), \qquad n_{L} = -\tfrac14\bigl(P + 3\,(B - L)\bigr).
\]
\begin{enumerate}
\item[(i)] \emph{(The two charges on all thirty-two states.)} $n_{B}$ and $n_{L}$ are functions of $k$ alone, with values $n_{B} = 0, \tfrac13, -\tfrac13, 0$ and $n_{L} = -1, 0, 0, 1$ at $k = 0, 1, 2, 3$. \emph{The extension to the odd half is a choice}: the charges are taken as functions of the pair number, that is with $-P$ where the stored formulas have $\chi$. Since $\chi\Gamma = -P$, on the sixteen ($\Gamma = 1$) they are the $n_{B} = \tfrac14((B - L) + \chi)$ and $n_{L} = \tfrac14(\chi - 3(B - L))$ of Proposition \claimref{standard-model.proton-decay-only-through-slot-pair}, and on the odd half they take on the complement of each state the opposite values, as the antiparticles must; the stored form with $\chi$, extended verbatim to the odd half, equals $\tfrac14((B - L) + \chi) = n_{B} + \tfrac12\chi$ there and is wrong on all sixteen odd states. As elements, $B - L = \tfrac13\sum_{a}e_{a}f_{a} = -\tfrac23(k - \tfrac32)$ is a bivector, a multiple of the grading element of the three pairs ($[k, v_{a}] = v_{a}$, $[k, w_{a}] = -w_{a}$), while
\[
n_{B} = \tfrac1{12}\sum_{a}e_{a}f_{a} + \tfrac14\,e_{1}e_{2}e_{3}f_{1}f_{2}f_{3}
\]
has a part of grade six, and $[n_{B}, e_{a}]$ has a part of grade five: the commutator with $n_{B}$ does not map the ten vectors to vectors, so $n_{B}$ is the generator of no rotation of the ten.
\item[(ii)] \emph{(The centraliser.)} An element of $\Cl(5,5)$ commutes with $n_{B}$ if and only if it lies in $\mathcal{A}_{-3} \oplus \mathcal{A}_{0} \oplus \mathcal{A}_{3}$: its terms shift the pair number by $0$ or $\pm 3$. This space has dimension $22 \cdot 16 = 352$ of $1024$. An element commutes with $B - L$ if and only if it lies in $\mathcal{A}_{0}$, of dimension $320$. This is elementary, the commutant of a function of the pair number ($8^{2} + 12^{2} + 12^{2}$ and $4^{2} + 12^{2} + 12^{2} + 4^{2}$ by the multiplicities of the values on the thirty-two states); the content is the membership table of (iii) and (iv) that it yields.
\item[(iii)] \emph{(The forty-five bivectors.)} The bivectors commuting with $n_{B}$ are exactly the fifteen of shift $0$: the nine pair-number-preserving pair bivectors $v_{a}w_{b}$ ($a \ne b$), $n_{a} - \tfrac12$, and the six slot bivectors, that is $\uu(3) \oplus \su(2)_{L} \oplus \su(2)_{R}$ in the notation of Proposition \claimref{standard-model.automorphisms-preserve-slot-pair-split-are}. The six pair bivectors $v_{a}v_{b}$, $w_{a}w_{b}$ (shift $\pm 2$) commute with $P$ and with $\chi$ and satisfy
\[
[n_{B}, x] = \tfrac14\,[B - L, x] = \mp\tfrac13\,x :
\]
the change of $n_{B}$ they make is a fixed weight of the generator, one quarter of its $B - L$ weight. The twenty-four slot-pair bivectors (shift $\pm 1$) anticommute with $P$ and with $\chi$, and for each of them $[n_{B}, x]$ is not a multiple of $x$: no weight assigned to the generator accounts for the change of $n_{B}$.
\item[(iv)] \emph{(Corollary of (ii): the Majorana element and the slot vectors.)} $T \in \mathcal{A}_{3}$ and every slot vector $a\,v_{s} + b\,w_{s}$ ($s = 4, 5$) lies in $\mathcal{A}_{0}$; for $s = 4$ these are the rung vectors of Proposition \claimref{standard-model.bidoublet-complex}, and the vectors of the second slot plane are included here without a stored name. So $[n_{B}, T] = [n_{B}, T^{\dagger}] = 0$, while $[B - L, T] = -2T$ (as stored) and $[n_{L}, T] = 2T$; a slot vector commutes with $n_{B}$, $n_{L}$ and $B - L$; a vector of a pair plane commutes with none of them.
\item[(v)] \emph{(The exchange.)} The exchange of set and clear in all five modes, conjugation by $e_{1}e_{2}e_{3}e_{4}e_{5}$, sends $n_{B}$, $n_{L}$ and $B - L$ to their negatives and $T$ to $T^{\dagger}$, and maps each family of (iii) onto itself.
\item[(vi)] \emph{(The class.)} Let $\mathcal{D}$ be the subalgebra generated by the fifteen bivectors of shift $0$, the slot vectors of both slots, $T$ and $T^{\dagger}$, over $\Q$ or after any extension of the scalars. Every element of $\mathcal{D}$ commutes with $n_{B}$, so $u\,n_{B}\,u^{-1} = n_{B}$ for every invertible $u \in \mathcal{D}$. Not every element of $\mathcal{D}$ commutes with $B - L$ or with $n_{L}$ (it contains $T$). A subalgebra that contains one of the six, one of the twenty-four, or a vector of a pair plane has elements that do not commute with $n_{B}$.
\end{enumerate}
\emph{Reading (argued, not proved).} The stored terms of the one-generation chain are of four kinds: the gauge generators (the forty-five), the electroweak mass terms (slot vectors), the Majorana term ($T$) and their products. To the question whether one stored charge is conserved by all of them the answer is no, for each candidate: $B - L$, the charge whose sign the exchange of the flag's two halves reverses as a generator of the pair grading, is broken by $T$; $n_{B}$, the charge the measured baryon density reads, commutes with $T$ and with everything stored except the six, whose change of $n_{B}$ is a fixed weight that a charge of their gauge field can carry (argued, not proved here), and the twenty-four, whose gauge fields are massive at the unification scale (Proposition \claimref{standard-model.proton-decay-only-through-slot-pair}). What is proved is commutation with $n_{B}$ on the class $\mathcal{D}$; that an element of the mode algebra commuting with $n_{B}$ is a dynamics conserving baryon number, and so that baryon number is unchanged on that class, is the reading (argued; baryon number is not the inherited charge, which is named as the total $B - L$ in Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i) from its version 11), and outside the class it is conditional on a bound for the twenty-four that is not computed here. Anomalous electroweak processes are not elements of the mode algebra and are not covered: by the standard result (literature cited from memory, not a stored Fact: 't Hooft 1976; Kuzmin, Rubakov and Shaposhnikov 1985) they change $n_{B}$ and $n_{L}$ together and conserve $B - L$, and where they act it is $B - L$ that must be protected, which among the stored terms only $T$ breaks. The statement concerns the charge; nothing is said about entropy.

## technical
Under Hypothesis (S), with the stored identifications of the charges: in the five-mode algebra of the derived generation, baryon and lepton number are functions of the number of occupied pairs alone. $B - L$ is a bivector, proportional to the element that grades the three pairs, the same element whose sign the exchange of the two halves of the flag reverses; baryon number is that bivector plus a grade-six term, the pair parity, and generates no rotation. An element commutes with baryon number exactly when it shifts the pair number by a multiple of three (an elementary fact about the commutant of a function of the pair number; the membership table is the content). That places the Standard-Model generators, the right-handed $\su(2)$, the electroweak mass terms and the Majorana element inside that class, and the 24 slot-pair generators outside it with no possible compensation by a charge of their gauge fields; the six leptoquark generators of $\su(4)$ are outside as operators on the fermions but change baryon number by a quarter of their own $B - L$ weight, which the gauge field carries. The Majorana element commutes with baryon number and shifts $B - L$ and lepton number by two. So no single stored charge commutes with all stored terms.

## lay
The series holds that the excess of matter over antimatter was laid down once, at the beginning, and not manufactured later. For that to be more than a stance one must show that nothing the theory contains can change the excess afterwards. This result checks the algebra of the theory's interactions for one family of particles. It finds that the count of baryons (protons and neutrons, less their antiparticles) is left alone by the generators of the known forces, by the terms that give particles mass, and by the term that gives the heavy neutrino its mass. Two groups of very heavy force carriers do change it: six that turn quarks into leptons, where the carrier itself can be given the missing amount, and 24, the ones that would make the proton decay, where it cannot. A second count, baryons minus leptons, is changed by the heavy-neutrino mass term. This is a statement about the algebra of one family only: the anomalous weak process, which is not an element of that algebra, does change the baryon count, and it is not covered. So no count is protected from everything, and the claim that the excess is inherited remains conditional.

## one-liner
Under Hypothesis (S), in the five-mode algebra, $n_{B} = \tfrac14((B - L) - P)$ depends on the pair number alone and commutes exactly with the elements shifting it by $0$ or $\pm 3$: the fifteen bivectors of $\uu(3) \oplus \su(2)_{L} \oplus \su(2)_{R}$, the slot vectors and the Majorana element $T$ (which breaks $B - L$ by $2$); not the twenty-four slot-pair generators, nor the six leptoquark bivectors, which change it by the fixed weight $\mp\tfrac13$.
