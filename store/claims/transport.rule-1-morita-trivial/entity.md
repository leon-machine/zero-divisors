---
id: transport.rule-1-morita-trivial
kind: claim
version: 5
title: Rule 1 is Morita-trivial
status: proved
region: transport
subject: completion
tags: [transport-algorithm, ladder-pairs, idempotents, clifford-classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.matrix-units-peirce-isomorphism@3
  - std-algebra.involution-properties@1
  - std-algebra.morita-amplification@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:7.1
- kind: check
  ref: check.py::check_ladder_pair_matrix_units_and_corner
- kind: check
  ref: check.py::check_twisted_diagonal_and_mat2
- kind: check
  ref: check.py::check_morita_invariants_preserved
locators:
  paper: T01
  number: Thm 7.1
  label: thm:morita
  line: 1437
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.involution-properties, std-algebra.morita-amplification where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the ladder pair as matrix units with corner A ff*, Cl(p+1,q+1) = Mat_2(Cl(p,q)) with the twisted diagonal embedding, and the Morita invariants for all n <= 4. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  context_refs:
  - transport.no-transport-terminates
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'Kept the Peirce isomorphism; the no-termination proposition is cited only to contrast what
      is not preserved, so not added. The final step uses classical Morita equivalence of A and M_2(A),
      which the store holds only as a later-paper import, so no edge was added for it. Levels pass: conditions
      already kept.'
---

## formal
The elements
\[
E_{11} = ff^*, \qquad E_{22} = f^*f, \qquad E_{12} = f, \qquad E_{21} = f^*
\]
form a full $2 \times 2$ system of matrix units in $B$ ($E_{11} + E_{22} = 1$, $E_{ij}E_{kl} = \delta_{jk}E_{il}$); the corner is the base, $E_{11} B E_{11} = A\,ff^* \cong A$ via $a \mapsto a\,ff^*$; and therefore
\[
\Cl(p{+}1, q{+}1) \;\cong\; \Mat_2\bigl(\Cl(p,q)\bigr),
\]
under which the ascent embedding $A \hookrightarrow B$ becomes the twisted diagonal $a \mapsto \mathrm{diag}(a, \hat{a})$. In particular Rule 1 preserves the Morita class: the Wedderburn type, and with it the simplicity or splitness and the type-C diagnosis of Section \ref{sec:taxonomy}, are the same for $B$ as for $A$, and the clock residue $d = p - q \pmod 8$ is fixed. (The \emph{presence} of types N and P is not preserved and could not be: Proposition \claimref{transport.no-transport-terminates} below shows every completion carries fresh obstructions of its own.) The adjoined ladder pair is, in the matrix description, exactly the off-diagonal matrix units, and the descent projectors $f^*f,\, ff^*$ are the diagonal ones.

## technical
Let Rule 1 adjoin a hyperbolic pair $f, f^*$ to $A = \Cl(p,q)$, giving $B = \Cl(p+1, q+1)$. Then $E_{11} = ff^*$, $E_{22} = f^*f$, $E_{12} = f$, $E_{21} = f^*$ form a full system of $2 \times 2$ matrix units in $B$, whose corner is the base, $E_{11} B E_{11} = A\,ff^* \cong A$. Therefore $\Cl(p+1, q+1) \cong \Mat_2(\Cl(p,q))$, under which the ascent embedding becomes the twisted diagonal $a \mapsto \mathrm{diag}(a, \hat a)$.

So Rule 1 preserves the Morita class: the Wedderburn type, simplicity or splitness, the type-C diagnosis and the clock residue $d = p - q \pmod 8$ are unchanged, although the presence of obstructions of types N and P is not preserved. In the matrix picture the adjoined ladder pair is the off-diagonal matrix units and the descent projectors $f^*f$, $ff^*$ are the diagonal ones.

## lay
The basic transport step adds one new pair of null directions to an algebra. The enlarged algebra turns out to be the algebra of two-by-two matrices with entries in the original one, with the new null pair playing the role of the off-diagonal entries. So the step leaves the essential type of the algebra unchanged, although whether certain other kinds of obstruction are present can change.

## one-liner
Rule 1 gives $\Cl(p+1, q+1) \cong \Mat_2(\Cl(p,q))$ with the adjoined ladder pair as off-diagonal matrix units, so it preserves the Morita class, the Wedderburn type and the clock residue $p - q \pmod 8$.
