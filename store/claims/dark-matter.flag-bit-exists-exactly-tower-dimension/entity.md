---
id: dark-matter.flag-bit-exists-exactly-tower-dimension
kind: claim
version: 3
title: The flag bit exists exactly at tower dimension $0 \bmod 4$
status: proved
region: dark-matter
subject: dark-matter
tags: [witt-index, towers-by-residue, chirality, matter-asymmetry]
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
- obj.dark-matter.witt-flag
derivations:
- name: main
  uses:
  - dark-matter.two-families-are-two-chiralities@7
  assumes:
  - dark-matter.p3-nearest-dimension-representatives@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:thm:paritybit
- kind: check
  ref: check.py::check_bit_iff_tower_dimension_zero_mod_four
- kind: check
  ref: check.py::check_odd_ambient_no_bit
- kind: check
  ref: check.py::check_even_residues_at_p3_and_other_windows
locators:
  paper: T14
  number: Thm 3.10
  label: thm:paritybit
  line: 269
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Fock-model chirality of the pure spinors of W and W'' opposite iff m odd (m = 1..4), partner-negating isometry det (-1)^m, odd ambient: central omega, det +1 exchange and grade mixing; P3 even representatives carry the bit, (1,1) and (1,5) do not. Version 2 -> 3.'
  env: theorem
  context_refs:
  - dark-matter.towers-are-residues-single-clock-filter
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.chirality-two-halves-spinor-module-conjugation
    note: 'Removed the chirality proposition of the Standard-Model paper: the proof cites it only to say
      that its listing choice is this flag choice, a remark rather than a premise; the residue proposition
      is used only to name the alternative windows, whose representatives are listed explicitly, so it
      is not edged. Levels pass: the lay level and one-liner now name Premise P3 for the even residues
      carrying the bit.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.p3-nearest-dimension-representatives
---

## formal
Let a tower have dimension $n$ and conformal completion with ambient $V$ of dimension $n + 2$, and let $W, W' \subset V_{\C}$ be a Witt pair, the two halves of Definition \claimref{obj.dark-matter.witt-flag} taken coherently across the pairs, with pure spinors the null blade $f$ and the top state (Definition \claimref{obj.dark-matter.null-blades-fock-ideal-chirality}). Then the choice between $W$ and $W'$ is a discrete invariant of the connected conformal spin group, a \emph{bit}, if and only if $n \equiv 0 \pmod 4$ (ambient dimension $2m$ with $m$ odd), and the bit is the chirality of the pure spinor, that is, the parity of the Fock grade of the complementary half's pure spinor ($0$ for $f$, $m$ for the top state). (i) The odd residues are odd-dimensional for every signature in the class, so the ambient is odd-dimensional, the pseudoscalar central, an even versor carries $W$ to $W'$, and the spin algebra mixes the Fock grades: no bit, on any window. (ii) The even residues carry the bit exactly at tower dimension $0 \bmod 4$: under Premise \claimref{dark-matter.p3-nearest-dimension-representatives} all four are at dimension four and carry it; the causal representatives of the alternative windows of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}(iii), $(1,1)$ of $r = 0$ and $(1,5)$ of $r = 4$, do not. So the towers that can be oriented are the even residues $\{0, 2, 4, 6\}$ given P3, and the odd residues cannot be, given nothing.

## technical
Take a tower of dimension $n$ with conformal ambient $V$ of dimension $n + 2$, and a Witt pair $W, W' \subset V_{\C}$ with pure spinors the null blade $f$ and the top state. The choice between $W$ and $W'$ is a discrete invariant of the connected conformal spin group, a bit, exactly when $n \equiv 0 \pmod 4$, that is ambient dimension $2m$ with $m$ odd, and the bit is the chirality of the pure spinor: Fock grade $0$ for $f$ against $m$ for the top state. Odd residues are odd-dimensional in every signature of the class, so the ambient is odd-dimensional, the pseudoscalar is central and an even versor carries $W$ to $W'$: no bit on any window.

Among even residues, under the nearest-dimension premise all four representatives are four-dimensional and carry the bit, while the alternative causal representatives $(1,1)$ and $(1,5)$ do not. So given that premise the towers that can be oriented are the even residues, and the odd residues cannot be oriented on any premise.

## lay
At the descent a choice is made between two complementary halves of a geometric structure. This result shows that the choice is a genuine two-way switch, one the world's continuous symmetries cannot undo, only when the world's dimension is a multiple of four. Four-dimensional worlds like ours and the mirror have the switch, and if the other even hidden worlds take their nearest-dimension forms (Premise P3) they are four-dimensional and have it too; odd-dimensional hidden worlds never do, whatever is assumed.

## one-liner
The choice between the two halves of a Witt pair is a bit of the connected conformal spin group exactly when the tower dimension is $0 \bmod 4$, so, under Premise P3 (nearest-dimension representatives), the even residues can be oriented, and the odd residues never can.
