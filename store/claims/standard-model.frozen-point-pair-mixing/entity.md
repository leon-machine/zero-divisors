---
id: standard-model.frozen-point-pair-mixing
kind: claim
version: 4
title: The frozen point and the pair mixing
status: proved
region: standard-model
subject: mass
tags: [frozen-point, representation-theory]
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
  - standard-model.module-factorises-even-ground-elements-act@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_ambient_weights_are_nonzero
- kind: check
  ref: check.py::check_generic_stabiliser_is_u2
- kind: check
  ref: check.py::check_vectors_commute_with_rung_mixing
locators:
  paper: T12
  number: Prop 9.14
  label: prop:mixing
  line: 1625
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the weights +-e_i of V_C under the pair numbers with no invariant vector, the u(2) stabiliser of a vector of C^3, and commutation with the rung mixing. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: proposition
  context_refs:
  - standard-model.module-factorises-even-ground-elements-act
  typing:
    by: ai-typing-pass
    added:
    - standard-model.module-factorises-even-ground-elements-act
    note: 'Added the module-factorisation proposition, which the statement cites for the commutation of
      every ambient vector with the rung mixing and rung number; the stabiliser fact is called standard
      but no imported claim for it is in the store. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.module-factorises-even-ground-elements-act
---

## formal
Under the pair mixing $U(3)$ of $W$, the ambient space $V_{\C} = W \oplus \overline{W}$ is $3 \oplus \bar{3}$: its weights are $\pm e_{i}$, none zero, so no nonzero vector of $V_{\C}$, in particular no frozen point at any $\Lambda$, is $U(3)$-invariant, and the stabiliser in $U(3)$ of a generic vector is a $U(2)$. By contrast every vector of $V_{\C}$ commutes with the rung mixing $U(2)$ and the rung number (Proposition \claimref{standard-model.module-factorises-even-ground-elements-act}(3)). The frozen point is exactly insensitive to the slots and exactly sensitive to the pairs.

## technical
The complexified ambient space splits as $V_{\C} = W \oplus \overline{W}$, and under the pair mixing $U(3)$ acting on $W$ it is the representation $3 \oplus \bar{3}$, with weights $\pm e_{i}$. No weight is zero, so no nonzero vector of $V_{\C}$ is fixed by $U(3)$: in particular the frozen point is not, at any value of $\Lambda$, and a generic vector has stabiliser $U(2)$ in $U(3)$.

By contrast every vector of $V_{\C}$ commutes with the rung mixing $U(2)$ and with the rung number, because the ground and rung orthogonal algebras commute elementwise on the two-rung module. The frozen point is therefore exactly insensitive to the slots and exactly sensitive to the pairs.

## lay
The frozen point is the fixed reference vector against which the framework measures mass. This result asks which internal symmetries leave it unchanged. Mixing the three pair directions always moves it, while mixing the two slot (rung) directions never does. So the frozen point is blind to the slots and sensitive to the pairs.

## one-liner
No nonzero ambient vector, the frozen point included, is invariant under the pair mixing $U(3)$, while every one commutes with the rung mixing $U(2)$ and the rung number.
