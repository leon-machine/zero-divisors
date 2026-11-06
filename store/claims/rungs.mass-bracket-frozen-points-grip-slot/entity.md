---
id: rungs.mass-bracket-frozen-points-grip-slot
kind: claim
version: 3
title: 'Mass bracket at $\Lambda = 0$: the frozen point''s grip on the slot bivector'
status: proved
region: rungs
subject: mass
tags: [frozen-point, conformal-spinors, mass-generation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - rungs.imported-mass-symplectic-area@4
  - rungs.imported-spinor-identification-witt-data-line@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:lem:bracket
- kind: check
  ref: check.py::check_volume_identities_and_mass
- kind: check
  ref: check.py::check_slot_trace_and_symmetric_square_component
- kind: check
  ref: check.py::check_mass_zero_iff_orthogonal_to_frozen_point
locators:
  paper: T12-rungs
  number: Lem 2.3
  label: lem:bracket
  line: 253
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the volume identities by 4x4 determinants, m^2 = 2|eps(n_inf ^ Z1 ^ Z2)|^2, the slot trace and the Lambda^2 C^2 (x) Lambda^2 CS component, and masslessness iff orthogonal to n_inf. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Both uses are cited in the proof as premises and are kept.'
  source_title: 'The mass bracket is the frozen point''s grip on the slot-antisymmetric bivector, at $\Lambda = 0$'
  source_formal: |-
    In the chart $\T = \Som \oplus \Spi$ with bases $e_{1}, e_{2}$ of $\Som$ and $\pi_{1}, \pi_{2}$ of $\Spi$, normalise $\varepsilon(e_{1} \wedge e_{2} \wedge \pi_{1} \wedge \pi_{2}) = 1$ and let $n_{\infty} = e_{1} \wedge e_{2} \in \Lambda^{2}\Som \subset \Lambda^{2}\T \cong V_{\C}$, the bivector of the line at infinity. For twistors $Z^{i} = (\omega^{i}, \pi^{i})$,
    \[
    \varepsilon\bigl(n_{\infty} \wedge Z^{1} \wedge Z^{2}\bigr) \;=\; \br{\pi^{1}\pi^{2}},
    \qquad\text{so}\qquad
    m^{2} \;=\; 2\,\bigl|\varepsilon(n_{\infty} \wedge Z^{1} \wedge Z^{2})\bigr|^{2}
    \]
    by Fact \claimref{rungs.imported-mass-symplectic-area}; and $\varepsilon(n_{0} \wedge Z^{1} \wedge Z^{2}) = \br{\omega^{1}\omega^{2}}$ for $n_{0} = \pi_{1} \wedge \pi_{2}$, so that the frozen point at general $\Lambda$ pairs to $\varepsilon(I_{\Lambda} \wedge Z^{1} \wedge Z^{2}) = \br{\pi^{1}\pi^{2}} + (\Lambda/6)\br{\omega^{1}\omega^{2}}$, the $\Lambda = 0$ term being the mass bracket. In the language of the $n$-tuple $\Psi = \sum_{i} e_{i}' \otimes Z^{i} \in \C^{2} \otimes \T$ (with $e_{i}'$ the slot basis), the total momentum is the slot trace of $\Psi \otimes \bar\Psi$ restricted to the $\pi$-parts, and $Z^{1} \wedge Z^{2}$ is the $\Lambda^{2}\C^{2} \otimes \Lambda^{2}\T$ component of $\Psi \odot \Psi$: at $\Lambda = 0$ the mass is the frozen point's pairing with the slot-antisymmetric bivector, and vanishes exactly when that bivector is orthogonal to the frozen point.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Twistor space \T is now the conformal spinor space \CS, with its chart halves named as the E-eigenspaces, V_C read as V + I6 V and the slot space taken over I6; the volume-form computation is unchanged.'
---

## formal
In the chart $\CS = \Som \oplus \Spi$ of the conformal spinor space (twistor space), the $E = -1$ and $E = +1$ eigenspaces, with bases $e_{1}, e_{2}$ of $\Som$ and $\pi_{1}, \pi_{2}$ of $\Spi$, normalise $\varepsilon(e_{1} \wedge e_{2} \wedge \pi_{1} \wedge \pi_{2}) = 1$ and let $n_{\infty} = e_{1} \wedge e_{2} \in \Lambda^{2}\Som \subset \Lambda^{2}\CS \cong V_{\C}$, the bivector of the line at infinity. For conformal spinors $Z^{i} = (\omega^{i}, \pi^{i})$,
\[
\varepsilon\bigl(n_{\infty} \wedge Z^{1} \wedge Z^{2}\bigr) \;=\; \br{\pi^{1}\pi^{2}},
\qquad\text{so}\qquad
m^{2} \;=\; 2\,\bigl|\varepsilon(n_{\infty} \wedge Z^{1} \wedge Z^{2})\bigr|^{2}
\]
by Fact \claimref{rungs.imported-mass-symplectic-area}; and $\varepsilon(n_{0} \wedge Z^{1} \wedge Z^{2}) = \br{\omega^{1}\omega^{2}}$ for $n_{0} = \pi_{1} \wedge \pi_{2}$, so that the frozen point at general $\Lambda$ pairs to $\varepsilon(I_{\Lambda} \wedge Z^{1} \wedge Z^{2}) = \br{\pi^{1}\pi^{2}} + (\Lambda/6)\br{\omega^{1}\omega^{2}}$, the $\Lambda = 0$ term being the mass bracket. In the language of the $n$-tuple $\Psi = \sum_{i} e_{i}' \otimes Z^{i} \in \C^{2} \otimes \CS$ (with $e_{i}'$ the slot basis, over the complex unit $I_{6}$), the total momentum is the slot trace of $\Psi \otimes \bar\Psi$ restricted to the $\pi$-parts, and $Z^{1} \wedge Z^{2}$ is the $\Lambda^{2}\C^{2} \otimes \Lambda^{2}\CS$ component of $\Psi \odot \Psi$: at $\Lambda = 0$ the mass is the frozen point's pairing with the slot-antisymmetric bivector, and vanishes exactly when that bivector is orthogonal to the frozen point.

## technical
In the chart $\CS = \Som \oplus \Spi$, with $\varepsilon(e_{1}\wedge e_{2}\wedge\pi_{1}\wedge\pi_{2}) = 1$ and $n_{\infty} = e_{1}\wedge e_{2}$, two conformal spinors satisfy $\varepsilon(n_{\infty}\wedge Z^{1}\wedge Z^{2}) = \br{\pi^{1}\pi^{2}}$, so $m^{2} = 2|\varepsilon(n_{\infty}\wedge Z^{1}\wedge Z^{2})|^{2}$. Likewise $\varepsilon(n_{0}\wedge Z^{1}\wedge Z^{2}) = \br{\omega^{1}\omega^{2}}$, so the frozen point at general $\Lambda$ pairs to $\br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}\br{\omega^{1}\omega^{2}}$.

For the tuple $\Psi = \sum_{i} e_{i}'\otimes Z^{i} \in \C^{2}\otimes\CS$, the total momentum is the slot trace of $\Psi\otimes\bar\Psi$ on the $\pi$-parts, and $Z^{1}\wedge Z^{2}$ is the $\Lambda^{2}\C^{2}\otimes\Lambda^{2}\CS$ component of $\Psi\odot\Psi$. So at $\Lambda = 0$ the mass is the frozen point's pairing with the slot-antisymmetric bivector, and it vanishes exactly when that bivector is orthogonal to the frozen point.

## lay
The mass of a particle made of two spinors of the conformal geometry can be read as a single pairing: the cosmological scale vector against the part of the pair that is antisymmetric in its two slots. With no cosmological constant this pairing is exactly the misalignment of the two light-like directions. The mass vanishes precisely when that antisymmetric part is blind to the scale vector.

## one-liner
At $\Lambda = 0$ the mass bracket is $\varepsilon(n_{\infty}\wedge Z^{1}\wedge Z^{2})$, the frozen point's pairing with the slot-antisymmetric part of the spinor pair.
