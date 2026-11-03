---
id: odd-extensions.two-towers-one-curved-universe
kind: claim
version: 6
title: The two towers on one gravitational field
status: proved
region: odd-extensions
subject: tower
tags: [cosmological-constant, mirror-sector, towers-by-residue]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - odd-extensions.doubling-or-complexification@5
  - odd-extensions.four-extensions-oriented-pair@5
  - odd-extensions.imported-copy-theorem-soldered-residue@5
  - odd-extensions.imported-frozen-point@6
  - odd-extensions.belongs-tower@5
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_intermediate_algebras_and_the_rule
- kind: check
  ref: check.py::check_even_subalgebras_coincide
- kind: check
  ref: check.py::check_fifth_generator_alone_differs
locators:
  paper: T14a
  number: Prop 9.3
  label: prop:twotowers
  line: 711
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: I^perp signatures for both towers and both signs of Lambda, omega^2 and the doubling rule; Cl^0(1,4) = Cl^0(4,1) by an explicit multiplicative basis map; the fifth generator in both cases. Version 5 -> 6.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Tractor wording completed by the lead: the tractor bundle is the Cl(2,4) vectors with the tractor gauge field of the one gravitational field; the mirror reads the reversed derived metric, so its tractors are Cl(4,2). Content unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - dark-energy.point-infinity-has-no-physical-fluctuation
  - odd-extensions.belongs-tower
  unresolved_refs:
  - rem:pseudo
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.belongs-tower
    - dark-energy.point-infinity-has-no-physical-fluctuation
    note: 'Added the belongs-tower proposition and the pure-gauge fact, both named in the statement as
      the grounds of its concluding clause; the four existing uses are cited in the proof and kept; Remark
      rem:pseudo, used for (iii), is not a store entity. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.point-infinity-has-no-physical-fluctuation
    - odd-extensions.belongs-tower
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: title and opening restated on the flat background: both towers are soldered to the one gravitational field (hb, Omega) on flat spacetime, the mirror reading its derived metric with the sign reversed (-g). Clauses (i)-(iii) and the consequence unchanged; tractor wording left to the lead. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Both oriented towers are soldered to the one gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the mirror reading its derived metric with the sign reversed, $-g$, so the mirror's tractor bundle has signature $(4,2)$ (this world's tractors being the vectors of $\Cl(2,4)$ carried by the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, the mirror's those of $\Cl(4,2)$) and its frozen point has norm $-Q(I)$. Then:
\begin{enumerate}
\item[(i)] in a de Sitter universe the intermediate algebra of this world's ascent is the doubled $\Cl(1,4)$ and the mirror's is the complexified $\Cl(4,1)$; in an anti-de Sitter universe they are the complexified $\Cl(2,3)$ and the doubled $\Cl(3,2)$. The rule is: doubled if and only if (de Sitter and this world) or (anti-de Sitter and mirror);
\item[(ii)] the even subalgebras $\Cl^{0}(1,4)$ and $\Cl^{0}(4,1)$ have the same presentation, the bivectors $e_{\mu}e_{5}$ anticommuting with squares $(+,-,-,-)$, so the two towers' conformal-to-de-Sitter spin groups, spinor modules and MacDowell-Mansouri bivector algebras coincide; the derived content of the dark-matter paper's copy theorem, which runs through the spin group, does not see the doubling;
\item[(iii)] what differs is the bare fifth generator alone: $e_{5}^{2} = -1$ with $e_{5} = \pm\omega'$ on the two summands in the doubled case, against $e_{5}^{2} = +1$ with $e_{5} = \omega'^{-1}\omega$, a central complex unit times the pseudoscalar, in the complexified case.
\end{enumerate}
Consequently the sign of $\Lambda$ does not select the visible tower: it distinguishes the two towers' intermediate algebras, but through an element no derived quantity of the series uses, and that element is the unit vector along $V$, which Proposition \claimref{odd-extensions.belongs-tower} places outside the soldered space and Fact \claimref{dark-energy.point-infinity-has-no-physical-fluctuation} places in the pure-gauge sector.

## technical
Both oriented towers are soldered to the one gravitational field on flat spacetime, the mirror reading its derived metric with the sign reversed, so the mirror's tractor bundle has signature $(4,2)$ and its frozen point has norm $-Q(I)$. In de Sitter the intermediate algebras are the doubled $\Cl(1,4)$ for this world and the complexified $\Cl(4,1)$ for the mirror; in anti-de Sitter they are the complexified $\Cl(2,3)$ and the doubled $\Cl(3,2)$. The even subalgebras $\Cl^{0}(1,4)$ and $\Cl^{0}(4,1)$ share one presentation, so the two towers' spin groups, spinor modules and MacDowell-Mansouri bivector algebras coincide, and the derived content of the copy theorem does not see the doubling.

What differs is the bare fifth generator alone: $Q(e_5) = -1$ with $e_5 = \pm\omega'$ on the two summands when doubled, against $Q(e_5) = +1$ with $e_5 = \omega'^{-1}\omega$ when complexified. That generator is the unit vector along $V$, outside the soldered space and in the pure-gauge sector, so the sign of $\Lambda$ distinguishes the towers' intermediate algebras without selecting which tower is visible.

## lay
Our world and its mirror share one gravitational field on a flat background, the mirror with the sign of every squared distance reversed. The sign of the cosmological constant decides which of the two gets the doubled form of the halfway algebra and which gets the complex form. But everything the series derives from these algebras is the same for both, and the one element that differs points along a direction that is not part of spacetime and carries no physical fluctuation, so the sign of the constant does not pick out which world is the visible one.

## one-liner
On one gravitational field the sign of $\Lambda$ decides which oriented tower's intermediate algebra is doubled and which complexified, but the difference sits only in the unsoldered, pure-gauge fifth generator, so it does not select the visible tower.
