---
id: standard-model.invariant-pairing-five-modes
kind: claim
version: 5
title: The invariant pairing on five modes
status: proved
region: standard-model
subject: standard-model
tags: [spinor-modules, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.bivector-lie-algebra@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pairing_complement_nondegenerate
- kind: check
  ref: check.py::check_so10_invariance
locators:
  paper: T12
  number: Lem 9.23
  label: lem:pairing
  line: 1718
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-lie-algebra where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: nondegeneracy and complement pairing of B, its so(10) invariance under all 45 generators, and the reversal-sign control. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.imported-fock-model-twistor-space
    note: 'Removed the twistor Fock-model fact: the proof only compares the pairing with that fact''s
      three-mode version and verifies invariance directly. Levels pass: conditions already kept.'
---

## formal
On $\Lambda^{\bullet}(W \oplus R_{2})$ define, in the occupation basis $e_{S}$, $S \subseteq \{1, \ldots, 5\}$,
\[
B(\psi, \varphi) \;=\; \sum_{S} (-1)^{|S|(|S|-1)/2}\,\varepsilon(S, S^{c})\,\psi_{S}\,\varphi_{S^{c}},
\]
$\varepsilon(S, S^{c})$ the sign of $e_{S} \wedge e_{S^{c}} = \varepsilon\, e_{12345}$. Then $B$ is nondegenerate, pairs each state with its complement only (even degree with odd, the $16$ with the $\overline{16}$), and is invariant under $\so(10)$: $B(X\psi, \varphi) + B(\psi, X\varphi) = 0$ for every bivector $X$ of the ten. In particular $B(\psi, \varphi) = 0$ for $\psi, \varphi$ both in the $16$: two sixteens have no invariant pairing without a vector between them.

## technical
On the five-mode exterior algebra $\Lambda^{\bullet}(W \oplus R_{2})$, define $B(\psi, \varphi) = \sum_{S}(-1)^{|S|(|S|-1)/2}\,\varepsilon(S, S^{c})\,\psi_{S}\varphi_{S^{c}}$ in the occupation basis, with $\varepsilon(S, S^{c})$ the sign of $e_{S} \wedge e_{S^{c}}$ relative to $e_{12345}$.

Then $B$ is nondegenerate, pairs each basis state only with its complement, so even degree with odd and the $16$ with the $\overline{16}$, and is invariant under the forty-five bivectors spanning $\so(10)$. In particular two states of the $16$ always pair to zero: two sixteens have no invariant pairing without a vector between them.

## lay
The paper builds a natural way of pairing two states of a five-mode system: each pattern of occupied modes is matched with its complementary pattern, with a carefully chosen sign. This pairing respects the large $\mathrm{Spin}(10)$ symmetry. Because complementary patterns have opposite parity, it never pairs two states from the same sixteen-state half, so a mass term between two such states needs an extra ingredient in the middle.

## one-liner
The complement pairing on the five-mode Fock space is nondegenerate and $\so(10)$-invariant, pairs the $16$ only with the $\overline{16}$, and vanishes on two sixteens.
