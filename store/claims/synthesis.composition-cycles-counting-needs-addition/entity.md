---
id: synthesis.composition-cycles-counting-needs-addition
kind: claim
version: 1
title: 'Composition only cycles; counting needs addition'
status: proved
region: synthesis
subject: clifford-structure
tags: [forcing-and-uniqueness, grading-and-parity]
proposed_by:
  kind: ai
  session: 2026-11-08-ga-deck
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal, proof and drafting
  source: run 2026-11-08-ga-deck
review: draft
founded_on:
- synthesis.premise-superposition-over-the-integers@2
lineage:
  motivated_by:
  - synthesis.division-gives-the-rationals
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_the_bit_counts_modulo_two
- kind: check
  ref: check.py::check_every_signed_configuration_has_order_dividing_four
- kind: check
  ref: check.py::check_powers_of_a_direction_cycle
- kind: check
  ref: check.py::check_sums_of_the_unit_are_an_injective_copy_of_the_integers
- kind: check
  ref: check.py::check_no_product_of_signed_configurations_counts
- kind: proof
  derivation: main
extraction:
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026, suggestion of
    8 November 2026 under Step 3, "Counting needs addition"), filed for the Zero Divisors site's
    "Why geometric algebra" deck, whose ladder slide cites it. It answers a tempting reading in which
    a number is a count of repeated directional acts (five copies of a direction read as the number
    five): composing a direction with itself only cycles, so the integers cannot come from
    composition and enter with the addition of Premise (F3). Clauses (i) and (ii) use only Premises
    (F1) and (F2); clause (iii) uses the freeness of the integer algebra, clause (v) of
    synthesis.signed-directions-and-the-integer-clifford-algebra. The extraspecial and exponent-4
    structure of such groups is classical (Salingaros's vee groups; extraspecial 2-groups), cited
    from memory; the proof here is self-contained. Ledger: transport-absent.
---

## formal
Grant Premises (F1) to (F3): the bit $\mathbb{F}_{2}$, a group $G$ of signed directions $e_{1}, \dots, e_{n}$ with central bit $c$ (Premise (F2)), and $A = \Z[G]/(c + 1)$ (Premise (F3)).
\begin{enumerate}
\item[(i)] \emph{(The bit does not count.)} In $\mathbb{F}_{2}$, $k \cdot 1 = 1$ for $k$ odd and $0$ for $k$ even: repeated comparison distinguishes only odd from even.
\item[(ii)] \emph{(Composition cycles.)} Every $g \in G$ has $g^{2} \in \{1, c\}$, so $g^{4} = 1$ and the powers of $g$ form a cyclic group of order $1$, $2$ or $4$. In particular, for a direction $e_{i}$ the power $e_{i}^{k}$ depends only on $k \bmod 4$, and only on $k \bmod 2$ when $e_{i}^{2} = 1$; five copies of a direction give the direction again, $e_{i}^{5} = e_{i}$.
\item[(iii)] \emph{(Addition counts.)} The map $\Z \to A$, $k \mapsto k \cdot 1 = 1 + \dots + 1$, is an injective ring homomorphism onto the grade-$0$ part $\Z\,1$ of $A$.
\item[(iv)] \emph{(Only addition counts.)} The image of $G$ in $A$ is the set $\{\pm e_{S}\}$ of signed blades, which is closed under multiplication, and $k \cdot 1 \in \{\pm e_{S}\}$ only for $k = \pm 1$. So no product of signed configurations equals $k \cdot 1$ with $|k| \ge 2$: the integers beyond $\pm 1$ are sums, not products.
\end{enumerate}

## technical
Neither of the first two ingredients of the foundation can count. The bit adds by comparison, $1 + 1 = 0$, so it sees only parity. The group of signed directions composes by the geometric product, and every element squares to $1$ or to the sign bit $c$, so every element has order $1$, $2$ or $4$: composing a direction with itself five times returns the direction, not the number five. Counting appears with superposition: in the integer algebra $\Z[G]/(c + 1)$ the sums $1 + 1 + \dots + 1$ are all distinct, because the algebra is free on its blades, and they fill the grade-$0$ part. They are the only way to reach an integer of size two or more, since every product of signed configurations is again a signed blade. Number in the sense of quantity therefore comes after geometry, but it needs addition as an ingredient of its own.

## lay
One way to try to build numbers from directions is to count repetitions: take a step five times and call it five. In this algebra that does not work. Taking a direction twice gives plus or minus one, so taking it five times just gives the direction back. The basic on-off distinction is no better, since doing it twice undoes it. Counting only becomes possible when combinations can be added together: then one plus one plus one is genuinely three, never the same as two or one. The whole numbers come from adding, not from repeating.

## one-liner
In the group of signed directions every element has order dividing $4$ ($g^{2} \in \{1, c\}$, so $e^{5} = e$) and in $\mathbb{F}_{2}$ only parity survives, while in $\Z[G]/(c + 1)$ the sums $k \cdot 1$ are an injective copy of $\Z$ that no product of signed configurations reaches for $|k| \ge 2$: counting needs addition.
