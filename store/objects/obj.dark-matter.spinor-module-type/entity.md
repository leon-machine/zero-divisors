---
id: obj.dark-matter.spinor-module-type
kind: object
version: 1
title: Spinor module and type
status: defined
region: dark-matter
subject: dark-matter
tags:
- spinor-modules
- clifford-classification
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
locators:
  paper: T14
  number: Def 3.3
  label: def:type
  line: 172
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: Definition only; no edges changed.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - dark-matter.type-residue-what-each-tower-can (about)
    - dark-matter.radiation-audit-what-theorem-closes-what (about)
    - dark-tower-matter.mirror-algebra (about)
    added_about: []
    verdict: connected
    note: Linked by about from the type-by-residue theorem, the radiation audit (intrinsic group Z2) and
      the T14c mirror-algebra theorem (quaternionic against real modules), whose statements use the defined
      type.
---

## formal
For a representative $\Cl(p,q)$ let $S$ be an irreducible real module (a real spinor space), and let $D = \End_{\Cl(p,q)}(S)$ be its commutant, a real division algebra by Schur's lemma. Its \emph{type} is $D \in \{\R, \C, \mathbb{H}\}$ together with the number of inequivalent irreducible modules (one or two). The \emph{intrinsic group} of $S$ is the group of $D$-unitary automorphisms of $S$ commuting with the Clifford action, $U(1, D) = \{d \in D : d\bar{d} = 1\}$: $\mathbb{Z}_{2}$, $U(1)$ or $Sp(1)$.

## technical
For a representative $\Cl(p,q)$ take an irreducible real module $S$, a real spinor space. By Schur's lemma its commutant $D = \End_{\Cl(p,q)}(S)$ is a real division algebra, so $D \in \{\R, \C, \HH\}$. The type of $S$ is $D$ together with the number, one or two, of inequivalent irreducible modules. The intrinsic group is the group of $D$-unitary automorphisms of $S$ commuting with the Clifford action, $U(1,D) = \{d \in D : d\bar{d} = 1\}$, which is $\Z_{2}$, $U(1)$ or $Sp(1)$.

## lay
A spinor space of a geometric algebra comes with symmetries that commute with everything the algebra does. Those symmetries form one of three number systems: the real numbers, the complex numbers or the quaternions. The type records which one it is and how many distinct spinor spaces there are, and the intrinsic group is the set of such symmetries of unit size.

## one-liner
The type of a representative's irreducible real spinor module is its commutant division algebra, $\R$, $\C$ or $\HH$, with the number of inequivalent modules, and its intrinsic group is the corresponding unit group $\Z_{2}$, $U(1)$ or $Sp(1)$.
