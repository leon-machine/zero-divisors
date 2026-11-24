---
id: synthesis.imported-zeta-of-a-real-quadratic-field-at-minus-one-as-a-divisor-sum
kind: claim
version: 1
title: 'Imported: L(-1, chi_D) for D > 0 as a divisor sum (Siegel; Cohen; Zagier)'
status: imported
region: synthesis
subject: thermality
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-24-number-theory
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-number-theory
review: draft
imported_from:
- citation: 'C. L. Siegel, Berechnung von Zetafunktionen an ganzzahligen Stellen, Nachr. Akad. Wiss. G\"ottingen Math.-Phys. Kl. II, Nr. 10 (1969), 87--102.'
  key: Siegel1969
  locator: 'the values of the zeta function of a totally real field at negative integers; cited from memory, not read'
- citation: 'H. Cohen, Sums involving the values at negative integers of L-functions of quadratic characters, Math. Ann. 217 (1975), 271--285.'
  key: Cohen1975
  locator: 'the divisor-sum formulas; cited from memory, not read'
- citation: 'D. Zagier, On the values at negative integers of the zeta-function of a real quadratic field, Enseign. Math. (2) 22 (1976), 55--95.'
  key: Zagier1976
  locator: 'the formula at $s = -1$ in elementary form; cited from memory, not read'
extraction:
  note: >-
    Imported by Leon's decision of 24 November 2026, as hypothesis (H3) of
    synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values. NOT checked against the
    sources: the statement and the bibliographic data are cited from memory, and which of the three sources
    states the formula in exactly this form is not verified. Support that is not a check of the sources: for
    $D = 5, 8, 12, 13$ the right side gives $L(-1, \chi_{D}) = -\tfrac25, -1, -2, -2$, equal to the values
    computed from the Bernoulli polynomials (the imported Hurwitz Fact) in the check of the using result. Not
    part of this Fact: other negative integers, non-fundamental discriminants, anything about zeros.
outside_ga:
  kind: imported
  why: 'A classical formula of number theory for a special value of a Dirichlet L-function; scalars only, stated in its source''s language.'
---

## formal
Cited from memory and not checked against the sources. Let $D > 1$ be a fundamental discriminant ($D \equiv 1 \pmod 4$ squarefree, or $D = 4d$ with $d \equiv 2, 3 \pmod 4$ squarefree; $D = 1$, which some conventions count, is excluded, and the formula is false there), $\chi_{D}(m) = \bigl(\tfrac{D}{m}\bigr)$ the Kronecker symbol, a real character of period $D$ with $\chi_{D}(-1) = 1$, and $\sigma(n)$ the sum of the positive divisors of $n$. With $\zeta(-1) = -\tfrac1{12}$ (\claimref{synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums}(ii) at $a = 1$),
\[
\zeta(-1)\,L(-1, \chi_{D}) = \frac{1}{60}\sum_{\substack{b \in \Z,\ b^{2} < D \\ b \equiv D \ (\mathrm{mod}\ 2)}}\sigma\Bigl(\frac{D - b^{2}}{4}\Bigr), \qquad\text{that is}\qquad L(-1, \chi_{D}) = -\frac15\sum_{b}\sigma\Bigl(\frac{D - b^{2}}{4}\Bigr).
\]
The left side is the value at $-1$ of the zeta function of the real quadratic field of discriminant $D$, which is the product $\zeta(s)L(s, \chi_{D})$.

## technical
The zeta function of a real quadratic field takes rational values at negative integers, and at $-1$ the value has an elementary closed form: one sixtieth of a sum of divisor sums over the integers $b$ of the parity of $D$ with $b^{2} < D$. Since the zeta function of the field factors as the Riemann zeta function times the L-function of the field's character, this is a formula for $L(-1, \chi_{D})$. For $D = 5$ the sum has the two terms $b = \pm 1$, each $\sigma(1) = 1$, and $L(-1, \chi_{5}) = -\tfrac25$. The result goes back to Siegel, with elementary treatments by Cohen and by Zagier; cited from memory.

## lay
For certain number systems built from a square root, a classical infinite sum can be assigned a value at $-1$, and that value turns out to be a small exact fraction given by adding up divisors of a few whole numbers. The store takes this formula from the literature.

## one-liner
Imported (Siegel 1969; Cohen 1975; Zagier 1976; from memory): for a fundamental discriminant $D > 1$ with Kronecker character $\chi_{D}$, $L(-1, \chi_{D}) = -\tfrac15\sum\sigma((D - b^{2})/4)$ over the integers $b \equiv D$ modulo $2$ with $b^{2} < D$; equivalently the zeta function of the real quadratic field takes the value $\tfrac1{60}$ of that sum at $-1$.
