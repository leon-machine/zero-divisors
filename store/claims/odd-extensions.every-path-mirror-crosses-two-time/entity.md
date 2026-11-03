---
id: odd-extensions.every-path-mirror-crosses-two-time
kind: claim
version: 4
title: Every path to the mirror crosses the two-time fork
status: proved
region: odd-extensions
subject: tower
tags: [mirror-sector, towers-by-residue]
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
- obj.tower.tower
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_sign_change_moves_residue_by_two
- kind: check
  ref: check.py::check_every_path_crosses_two_two
- kind: check
  ref: check.py::check_euclidean_dead_end
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Prop 5.2
  label: prop:path
  line: 553
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the sign-change graph at dimension four, every walk from (1,3) to (3,1) through (2,2), and the Euclidean dead end. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: Self-contained combinatorial proof with no premises; no edges needed.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about:
    - obj.tower.tower
    verdict: standalone
    note: A self-contained walk on the five signatures at dimension four; the residue is the tower's transport
      charge (about), the sterile name is vocabulary from Fact 1.2, and only the remark on no mechanism
      draws on it.
---

## formal
At fixed dimension four, a change of the sign of one generator moves the signature $(p, 4-p)$ to $(p \pm 1, 4 - p \mp 1)$ and the residue by $\pm 2$. Every sequence of such changes from $(1,3)$ to $(3,1)$ passes through $(2,2)$, residue $0$, the two-time sterile fork; the other neighbour of $(1,3)$, the Euclidean $(0,4)$ at residue $4$, is a dead end from which the only continuation returns to $(1,3)$.

## technical
At fixed dimension four the signatures are $(p, 4-p)$ with $p = 0, \ldots, 4$, and changing the sign of one generator moves $p$ by one and the residue $p - q \bmod 8$ by $\pm 2$.

Every sequence of such changes from this world's $(1,3)$ to the mirror's $(3,1)$ passes through $(2,2)$, the residue-$0$ two-time sterile fork. The other neighbour of $(1,3)$, the Euclidean $(0,4)$ at residue $4$, is a dead end whose only continuation returns to $(1,3)$.

## lay
Flipping the sign of one direction at a time, there is no way to get from our spacetime's signature to its mirror image without passing through a signature with two time directions. The only other move from our signature leads to the purely spatial one, and from there the only way out is straight back. So every such route to the mirror goes through the two-time case.

## one-liner
In dimension four, every sequence of single sign changes from $(1,3)$ to $(3,1)$ passes through the two-time fork $(2,2)$, the other neighbour $(0,4)$ being a dead end.
