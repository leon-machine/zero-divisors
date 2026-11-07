---
id: singularity.modular-theory-matrix-factor-proved-outright
kind: claim
version: 6
title: Modular theory of a matrix factor, proved outright
status: proved
region: singularity
subject: descent
tags: [modular-theory, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.1
- kind: check
  ref: check.py::check_cyclic_and_separating_iff_weights_positive
- kind: check
  ref: check.py::check_tomita_polar_decomposition
- kind: check
  ref: check.py::check_modular_flow_and_kms
locators:
  paper: T05
  number: Lem 7.1
  label: lem:tomita
  line: 1701
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Tomita-Takesaki theory on the abstract complex Hilbert space C^n (x) C^n of a full matrix factor: by U1 its scalars are span{1, I_4}, the default scalar field of an abstract complex Hilbert space and matrix algebra, so rho^{it}, Delta^{it} become rho^{I_4 t}, Delta^{I_4 t}, with a sentence fixing the scalars and naming J as the modular conjugation; the basis indices i, j are renamed k, l (index letters only) so that no letter i is read as a unit. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): Tomita-Takesaki theory on the Hilbert space C^n (x) C^n of a full complex matrix factor (rho^{it}, Delta^{it}); the space is not one of the series'' geometric-algebra mode spaces with unit I_4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: cyclic and separating iff all weights positive, the Tomita operator computed from its definition with J = swap and Delta = rho (x) conj(rho)^{-1}, the modular flow and the KMS identity. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'no edges remain, everything being a finite-dimensional computation within the lemma; removed
      the mechanical repair edge to the transport algorithm: the section frames its results as a step
      of that algorithm, but the proof is a self-contained computation and does not use it as a premise;
      the lemma is standard Tomita-Takesaki theory in finite dimensions but the source proves it outright
      and no imported Tomita-Takesaki claim is in the store, so no standard route was added'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$\rho^{it}$, $\Delta^{it}$: Tomita-Takesaki modular flow on the matrix factor''s Hilbert space (imported
      Hilbert-space theory); indices $i, j$ (index)'
---

## formal
Let $H = \C^n \otimes \C^n$, let $M = \Mat_n(\C) \otimes 1$ act on the first factor (here the complex numbers are $\C = \mathrm{span}\{1, I_4\}$, the default scalar field of an abstract complex Hilbert space and matrix algebra, and $J$ is the modular conjugation), and let $\Omega = \sum_k \lambda_k\, |kk\rangle$ with all $\lambda_k > 0$ and $\sum \lambda_k^2 = 1$ (any cyclic separating vector of $M$ has this form in its Schmidt basis). Define the Tomita operator as the closure of $S : a\Omega \mapsto a^*\Omega$ ($a \in M$). Then its polar decomposition $S = J\Delta^{1/2}$ has
\[
\Delta = \rho \otimes \bar\rho^{\,-1}, \qquad \rho = \sum_k \lambda_k^2\,|k\rangle\langle k| , \qquad J\,|kl\rangle = |lk\rangle \ \text{(antilinearly)},
\]
and the modular flow on $M$ is $\sigma_t(a) = \rho^{I_4t} a\, \rho^{-I_4t}$. Moreover the state $\omega = \langle\Omega, \cdot\,\Omega\rangle$ satisfies the KMS identity $\omega(ab) = \omega(b\,\rho\,a\,\rho^{-1})$ for all $a, b \in M$.

## technical
Take $H = \C^n \otimes \C^n$ over $\C = \mathrm{span}\{1, I_4\}$, $M = \Mat_n(\C) \otimes 1$ and a cyclic separating vector in Schmidt form $\Omega = \sum_k \lambda_k |kk\rangle$ with all $\lambda_k > 0$ and $\sum_k \lambda_k^2 = 1$. The Tomita operator $S : a\Omega \mapsto a^*\Omega$ acts on basis vectors as $|kl\rangle \mapsto (\lambda_k/\lambda_l)|lk\rangle$, and its polar decomposition $S = J\Delta^{1/2}$ is explicit: $\Delta = \rho \otimes \bar\rho^{\,-1}$ with $\rho = \sum_k \lambda_k^2 |k\rangle\langle k|$, and $J$ the antilinear swap $|kl\rangle \mapsto |lk\rangle$.

Consequently the modular flow on $M$ is $\sigma_t(a) = \rho^{I_4t} a \rho^{-I_4t}$, and the vector state $\omega = \langle\Omega, \cdot\,\Omega\rangle$ satisfies the KMS identity $\omega(ab) = \omega(b\,\rho a \rho^{-1})$ for all $a, b \in M$. Because everything is finite-dimensional, all of this follows by direct computation.

## lay
Tomita-Takesaki theory attaches to a quantum state a natural time evolution, called the modular flow. For two finite quantum systems in an entangled state, this lemma works out every ingredient of that theory by hand. The modular flow turns out to be the evolution generated by the reduced density matrix of one side, and the state satisfies the equilibrium (KMS) condition with respect to it.

## one-liner
For a full matrix algebra with a cyclic separating vector, the modular operator, modular conjugation and modular flow are computed explicitly, and the state is KMS for that flow.
