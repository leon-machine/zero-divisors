---
id: obj.dark-matter.witt-flag
kind: object
version: 1
title: The Witt flag
status: defined
region: dark-matter
subject: dark-matter
tags:
- witt-index
- hyperbolic-plane
- matter-asymmetry
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
about:
- obj.dark-matter.null-blades-fock-ideal-chirality
locators:
  paper: T14
  number: Def 2.10
  label: def:flag
  line: 132
extraction:
  env: definition
  context_refs:
  - dark-matter.flag-bit-exists-exactly-tower-dimension
  - dark-matter.imported-derived-generation-flag
  - dark-matter.two-families-are-two-chiralities
  typing:
    by: ai-typing-pass
    note: Kept the about edge to the Fock-ideal definition; the flag-bit theorem, the derived-generation
      import and the two-families result are cited as consequences or context, not as parts of the definition.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - refuted.the-particle-antiparticle-orientation-is-determi (about)
    added_about: []
    verdict: connected
    note: Already well linked by about; added the refuted orientation conjecture, which concerns the flag's
      orientation.
---

## formal
On a rung's hyperbolic plane $H_k$ with null pair $(v_k, w_k)$, a \emph{flag} chooses one null line as the annihilated half; $v_k \leftrightarrow w_k$ exchanges the two. The \emph{descent's flag} chooses for every pair at once: a maximal isotropic $W$ of the complexified conformal ambient, the Fock vacuum's annihilator (Definition \claimref{obj.dark-matter.null-blades-fock-ideal-chirality}), on the three-pair structure of Fact \claimref{dark-matter.imported-derived-generation-flag}. Its conjugate exchanges all three halves, an odd number, which puts it in the other family (Proposition \claimref{dark-matter.two-families-are-two-chiralities}(iii)) and makes the flag a bit (Theorem \claimref{dark-matter.flag-bit-exists-exactly-tower-dimension}). A flag is an orientation datum, not a plane.

## technical
On a rung's hyperbolic plane $H_{k}$ with null pair $(v_{k}, w_{k})$, a flag chooses one null line as the annihilated half, and $v_{k} \leftrightarrow w_{k}$ exchanges the two. The descent's flag chooses for every pair at once: a maximal isotropic subspace $W$ of the complexified conformal ambient, the annihilator of the Fock vacuum, on the imported three-pair structure. Its conjugate exchanges all three halves, an odd number, which puts it in the other family and makes the flag a bit. A flag is an orientation datum, not a plane.

## lay
Each pair of null directions in the theory can be split in two ways, according to which member is taken to annihilate the vacuum. The Witt flag is the single choice made for all pairs at once by the descent that set up the present universe. Flipping it swaps three halves, an odd number, so the flipped choice is genuinely different, and the choice amounts to one bit of orientation.

## one-liner
The Witt flag is the descent's simultaneous choice of annihilated null half on every pair, a maximal isotropic subspace of the complexified conformal ambient, whose conjugate lies in the other family, so that the flag is a bit.
