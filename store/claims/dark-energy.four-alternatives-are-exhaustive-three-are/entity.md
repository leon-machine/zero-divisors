---
id: dark-energy.four-alternatives-are-exhaustive-three-are
kind: claim
version: 2
title: The four alternatives are exhaustive; the three are not
status: proved
region: dark-energy
subject: dark-energy
tags: [classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_trichotomy_and_independence
- kind: proof
  derivation: main
locators:
  paper: T10
  number: Prop 5.7
  label: prop:exhaustive
  line: 1025
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Definition applied to all small finite theories: D, P, I partition every conserved q (counts 3, 6, 72), K holds with each, and not K, D, I implies P. Version 1 -> 2. Wording fix (check writer T10''s finding, Leon 2026-10-23): (K) is not independent of (D): (D) implies (K); (K) is excluded by none of the three, and (P) and (I) are compatible with (K) and with its negation (statement levels and proof).'
  typing:
    by: ai-typing-pass
    added: [obj.dark-energy.four-ways-number-enters-theory-shape]
    note: 'The proof is a case split on the definition alone, so the only edge added is the about link to the four-ways definition.'
  env: proposition
---

## formal
Every conserved $q$ is (D), (P) or (I), and exactly one of them; (K) can hold together with any of them and is excluded by none; (D) implies (K), while (P) and (I) are compatible with (K) and with its negation. A conserved $q$ that is neither (K), (D) nor (I) is (P). Hence the inference ``not kinematic, not dynamical, therefore initial data'' is valid only if (P) is excluded.

## technical
For a theory with kinematic structure $\mathcal{K}$ and actions $S_\mu$ with solution spaces $\mathcal{S}_\mu$, a conserved quantity $q$ is exactly one of: dynamically fixed (D), constant on $\bigcup_\mu\mathcal{S}_\mu$; a parameter of the laws (P), constant on each $\mathcal{S}_\mu$ but not on the union; or initial data (I), not constant on some $\mathcal{S}_\mu$. Being kinematic (K) can hold together with any of the three and is excluded by none; (D) implies (K), while (P) and (I) are compatible with (K) and with its negation.

Hence a conserved $q$ that is neither (K), (D) nor (I) is (P), and the inference "not kinematic, not dynamical, therefore initial data" is valid only once (P) has been excluded.

## lay
A number in a physical theory can be fixed by the dynamics, can be a setting of the laws themselves, or can vary from one solution to another as initial data. These three options exclude one another and cover every case, while being kinematic is a separate question. So ruling out kinematic and dynamical does not leave initial data as the only possibility: the number might be a parameter of the laws.

## one-liner
Every conserved quantity is exactly one of dynamically fixed, a parameter of the laws or initial data, with being kinematic excluded by none of these (implied by the first, compatible with the other two and with its negation), so excluding kinematic and dynamical leaves initial data only if parameters of the laws are excluded.
