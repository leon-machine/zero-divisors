---
id: synthesis.imported-class-number-formula-at-zero-for-negative-discriminants
kind: claim
version: 1
title: 'Imported: the class number formula L(0, chi_D) = 2h(D)/w(D) for D < 0 (Dirichlet)'
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
- citation: 'P. G. Lejeune Dirichlet, Recherches sur diverses applications de l''analyse infinit\''esimale \`a la th\''eorie des nombres, J. Reine Angew. Math. 19 (1839), 324--369; 21 (1840), 1--12, 134--155.'
  key: Dirichlet1839
  locator: 'the class number formula; cited from memory, not read'
- citation: 'H. Davenport, Multiplicative Number Theory, 2nd ed., Graduate Texts in Mathematics 74, Springer, New York (1980).'
  key: Davenport1980
  locator: 'Ch.~6 (the class number formula at $s = 1$) and Ch.~9 (the functional equation, which carries it to $s = 0$); cited from memory, not read for this entry'
extraction:
  note: >-
    Imported by Leon's decision of 24 November 2026, as hypothesis (H2) of
    synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values. NOT checked against the
    sources: cited from memory. The form at $s = 0$ is the classical formula $L(1, \chi_{D}) = 2\pi h/(w\sqrt{|D|})$
    carried through the functional equation; that passage is part of this Fact and is not derived in the store.
    Support that is not a check of the sources: for $D = -3, -4, -7, -8, -11, -15, -20, -23$ the value of
    $L(0, \chi_{D})$ computed from the Bernoulli polynomials (the imported Hurwitz Fact) equals $2h/w$ with $h$
    counted directly as the number of reduced forms, in the check of the using result. Not part of this Fact:
    real quadratic fields, non-fundamental discriminants, anything about zeros.
outside_ga:
  kind: imported
  why: 'A classical theorem of number theory on binary quadratic forms and a Dirichlet series; scalars only, stated in its source''s language.'
---

## formal
Cited from memory and not checked against the sources. Let $D < 0$ be a fundamental discriminant ($D \equiv 1 \pmod 4$ and squarefree, or $D = 4d$ with $d \equiv 2, 3 \pmod 4$ squarefree), $\chi_{D}(m) = \bigl(\tfrac{D}{m}\bigr)$ the Kronecker symbol, a real character of period $|D|$ with $\chi_{D}(-1) = -1$, and $L(s, \chi_{D})$ its L-function, continued analytically (\claimref{synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums}(iii)). Let $h(D)$ be the number of reduced positive definite forms $ax^{2} + bxy + cy^{2}$ with integer coefficients and $b^{2} - 4ac = D$ (reduced: $|b| \le a \le c$, and $b \ge 0$ when $|b| = a$ or $a = c$), and $w(D)$ the number of integer solutions of $x^{2} + xy + \tfrac{1 - D}{4}y^{2} = 1$ for odd $D$, of $x^{2} - \tfrac{D}{4}y^{2} = 1$ for even $D$: $w(-3) = 6$, $w(-4) = 4$ and $w(D) = 2$ otherwise. Then
\[
L(0, \chi_{D}) = \frac{2h(D)}{w(D)} .
\]

## technical
Dirichlet's class number formula gives the number of classes of binary quadratic forms of a negative discriminant as a value of the L-function of the corresponding real character. At $s = 1$ it reads $L(1, \chi_{D}) = 2\pi h/(w\sqrt{|D|})$; the functional equation of the L-function turns it into the rational statement $L(0, \chi_{D}) = 2h/w$. The class number is the number of reduced forms, which can be counted directly. Cited from memory.

## lay
Whole-number expressions of the shape $ax^{2} + bxy + cy^{2}$ fall into finitely many essentially different kinds for each value of $b^{2} - 4ac$. A formula of Dirichlet from 1839 says that this count is, up to a simple factor, the value of a certain infinite sum attached to the same number. The store takes the formula from the literature.

## one-liner
Imported (Dirichlet 1839; Davenport, ch. 6 and 9; from memory): for a negative fundamental discriminant $D$ with Kronecker character $\chi_{D}$, $L(0, \chi_{D}) = 2h(D)/w(D)$, $h$ the number of reduced positive definite binary forms of discriminant $D$ and $w = 6, 4, 2$ for $D = -3$, $D = -4$, and otherwise.
