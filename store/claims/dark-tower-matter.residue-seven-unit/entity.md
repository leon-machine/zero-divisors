---
id: dark-tower-matter.residue-seven-unit
kind: claim
version: 3
title: The central unit of the residue-seven tower
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [pseudoscalar-and-centre, mass-generation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - primer.sign@3
  - std-algebra.pseudoscalar-commutation@1
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:H1
  - id:H2
  - id:H3
  - id:H4
- kind: check
  ref: check.py::check_pseudoscalar_along_towers
- kind: check
  ref: check.py::check_omega_odd_at_r7
- kind: check
  ref: check.py::check_rotation_by_c_plus_s_omega
locators:
  paper: T14c
  number: Prop 7.1
  label: prop:omega7
  line: 628
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites primer.sign, std-algebra.pseudoscalar-commutation, std-algebra.involution-properties where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: pseudoscalar central with square -1 / +1 along both towers and the Q(omega) formula for p + q <= 9; omega odd at r = 7 with Cl hf = T + omega T; c + s omega rotation identity, complex structure and double angle. Version 1 -> 2.'
  env: proposition
  context_refs:
  - dark-tower-matter.gauge-algebras
  typing:
    by: ai-typing-pass
    note: 'No edges: the proof is a self-contained computation. The identification in (iii) with the slot
      rotation of the gauge-algebra theorem is a comparison that the paper lists at proof level, so the
      gauge algebras (context ref) were not added as a premise. Levels pass: levels written from scratch,
      keeping every condition and level qualifier of the formal statement.'
---

## formal
\begin{enumerate}
\item[(i)] Along the residue-seven tower ($\Cl(2,3)$, $\Cl(3,4)$, $\Cl(4,5)$, \ldots) the pseudoscalar is central and squares to $-1$ at every rung; along the residue-one tower ($\Cl(3,2)$, $\Cl(4,3)$, \ldots) it is central and squares to $+1$.
\item[(ii)] At $r = 7$ the pseudoscalar $\omega$ is odd: it carries the even ideal into the odd one, so it does not act on the constituent ideal, and the grade involution reverses it.
\item[(iii)] On the Clifford module $\Cl(\hatV)\hf = T \oplus \omega T$, left multiplication by $c + s\omega$ ($c^{2} + s^{2} = 1$) commutes with the whole Clifford action and carries $X + \omega Y$ to $(cX - sY) + \omega(sX + cY)$: on a pair of real constituents it is the slot rotation of Theorem \claimref{dark-tower-matter.gauge-algebras}(i), here supplied by the algebra itself. Every cell carries charge $\pm 1$ under it. If the tower's action is built from operations that commute with the Clifford action, as T12's are, a Majorana-type mass (charge $2$) is then forbidden in the $r = 7$ tower whether or not the rotation is gauged; this last clause is at assembly level.
\end{enumerate}

## technical
Along the residue-seven tower ($\Cl(2,3)$, $\Cl(3,4)$, $\Cl(4,5)$, and so on) the pseudoscalar $\omega$ is central with $Q(\omega) = -1$ at every rung, and along the residue-one tower it is central with $Q(\omega) = +1$. At $r = 7$, $\omega$ is odd: it carries the even ideal into the odd one, so it does not act on the constituent ideal, and the grade involution reverses it.

On the Clifford module $\Cl(\hatV)\hf = T \oplus \omega T$, left multiplication by $c + s\omega$ with $c^2 + s^2 = 1$ commutes with the whole Clifford action and sends $X + \omega Y$ to $(cX - sY) + \omega(sX + cY)$: on a pair of real constituents it is the slot rotation, supplied by the algebra itself, and every cell has charge $\pm 1$ under it. At assembly level, if the tower's action is built from operations commuting with the Clifford action, a Majorana-type mass (charge $2$) is forbidden at $r = 7$, gauged or not.

## lay
In the residue-seven tower the algebra itself contains a square root of minus one that commutes with everything, at every step of the tower. It cannot act on a single constituent, but it rotates a pair of real constituents into each other and gives them a conserved charge. If the tower's dynamics respects the algebra, an assumption at assembly level, this charge forbids the kind of mass that would turn a particle into its own antiparticle.

## one-liner
At $r = 7$ the central pseudoscalar, of square $-1$ at every rung, supplies the slot rotation of two real constituents, and at assembly level, if the action commutes with the Clifford action, it forbids Majorana-type masses.
