---
id: dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
kind: claim
version: 5
title: 'Imported: the weighted limit at the Schwarzschild singularity, and its matching'
status: proved
region: dark-energy
subject: interior
tags: [schwarzschild, kasner, limits]
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
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.boosts-generate-exactly-levi-factor@5
  - interior.exact-parallelism-convergence-rate@6
  - interior.interior-connection-exactly@8
  - interior.kasner-form-interior@7
  - interior.schwarzschild-de-sitter-weighted-limit@7
  - interior.schwarzschild-lines-exactly@5
  - interior.transport-level-convergence-along-tangential-curves@4
  - interior.weighted-limit-theorem@6
  - sheaf.matching-connection-level@8
  - sheaf.matching-fibre@5
  - sheaf.weights-are-forced-are-kasner-exponents@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_parallel_frame_and_leading_kasner_connection
- kind: check
  ref: check.py::check_schwarzschild_de_sitter_relative_correction
- kind: check
  ref: check.py::check_unit_boost_residue
- kind: check
  ref: check.py::check_weights_are_the_exponents
locators:
  paper: T10
  number: Fact 4.7
  label: fact:weightedlimit
  line: 867
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: interior gauge field: D-parallel frame, Kasner leading connection with O(tau^{2/3}) boost and O(tau^{1/3}) sphere rates by exact series; SdS relative O(Lambda tau^2); unit-boost B_w; weights equal exponents. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    added:
    - interior.exact-parallelism-convergence-rate
    - interior.interior-connection-exactly
    note: 'Fact restating series results: kept every restated source and added the parallel-frame and
      interior-connection lemmas, which its provenance names and whose content (frame parallelism, rotation-block
      rate) it restates. Levels pass: all three levels now say Kasner at leading order; lay and one-liner
      add the values-level scope and the fixed Hubble-normalised length restriction at transport level.'
  env: fact
  context_refs:
  - interior.boosts-generate-exactly-levi-factor
  - interior.kasner-form-interior
  - interior.schwarzschild-de-sitter-weighted-limit
  - interior.schwarzschild-lines-exactly
  - interior.transport-level-convergence-along-tangential-curves
  - interior.weighted-limit-theorem
  - sheaf.matching-connection-level
  - sheaf.matching-fibre
  - sheaf.weights-are-forced-are-kasner-exponents
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the interiors are named as gravitational fields (hb, Omega) on flat spacetime, metric functions as functions of the derived metric, the parallel frame as D-parallel along the free-fall worldlines, the connection omega as the rotation-gauge field on physical vectors (omega(A) = Omega(hb(A))), admissible metric as admissible gravitational field. Limits, rates and matching unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
For the Schwarzschild interior gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in synchronous time $\tau$ (with $\tau = 0$ the singularity), and equally for the Schwarzschild-de Sitter interior field, the functions of whose derived metric differ by relative $O(\Lambda\tau^2)$ and for which the same limit holds with the same exponents and rates \cite[Thm.~5.9]{ButlerT6}, the orthonormal physical frame adapted to the Killing and sphere directions is $D$-parallel along the free-fall worldlines of velocity $g_\tau$, and the connection is Kasner at leading order: the Hubble-normalised connection $\tau\,\omega$, with $\omega(A) = \Omega(\hb(A))$ the rotation-gauge field on physical vectors, tends to $-\sum_i p_i\, B_i \otimes \hat\theta^i$ with $B_i$ the boosts (the sign of the Definition, in which the Cartan forms $\omega^i{}_0 = \sigma_i\theta^i$ assemble to $-\sigma_i B_i$), $\hat\theta^i$ the normalised coframe, and exponents $(p_1, p_2, p_3) = (-\tfrac13, \tfrac23, \tfrac23)$, with explicit rates: $O(\tau^{2/3})$ in the boost block and $O(\tau^{1/3})$ in the rotation block, the latter being the sphere's own connection, which is outside the Kasner comparison; the limit is a values-level statement (the algebra generated by the limiting connection values); the transport-level statement, convergence of the transport to the Kasner model's transport, holds along every tangential curve of fixed Hubble-normalised length, for every admissible gravitational field of the geometry paper's class \cite[Def.~5.5]{ButlerT6}, whose exponents satisfy $\sum_i p_i^2 = 1$ \cite[Thm.~5.11]{ButlerT6}, and along the Schwarzschild $\varphi$-lines exactly, at rate $\tau^{1/3}$ \cite[Cor.~5.12]{ButlerT6}; what the geometry paper disclaims is the comparison over segments of fixed coordinate length, whose Hubble-normalised length diverges, and about which no claim is made here either. This coframe consists of sections of the sheaf paper's exceptional module, the weights of the sheaf paper's completion are forced to equal the exponents, and the total residue bivector $B_w = \sum_i p_i\, \hat e_0\wedge\hat e_i$ is a unit boost of the exceptional algebra. \emph{Provenance:} \cite[Lems.~5.1-5.4, Def.~5.5, Thm.~5.6, Thm.~5.9, Thm.~5.11, Cor.~5.12]{ButlerT6}; \cite[Thm.~8.16, Prop.~8.26, Thm.~8.27]{ButlerT4}.

## technical
For the Schwarzschild interior gravitational field on flat spacetime in synchronous time $\tau$, and equally the Schwarzschild-de Sitter one, the functions of whose derived metric differ by relative $O(\Lambda\tau^2)$, the orthonormal physical frame adapted to the Killing and sphere directions is $D$-parallel along the free-fall worldlines and the rotation-gauge field is Kasner at leading order: the Hubble-normalised connection $\tau\,\omega$ tends to $-\sum_i p_i B_i \otimes \hat\theta^i$ with exponents $(-\tfrac13, \tfrac23, \tfrac23)$. The rates are $O(\tau^{2/3})$ in the boost block and $O(\tau^{1/3})$ in the rotation block, the latter being the sphere's own connection. The limit is a values-level statement. At transport level, convergence to the Kasner model's transport holds along every tangential curve of fixed Hubble-normalised length, for every admissible gravitational field (whose exponents satisfy $\sum_i p_i^2 = 1$), and exactly along the Schwarzschild $\varphi$-lines at rate $\tau^{1/3}$; no claim is made for segments of fixed coordinate length.

On the sheaf side, this coframe consists of sections of the exceptional module, the weights of the completion are forced to equal the exponents, and the total residue bivector $B_w = \sum_i p_i\,\hat e_0 \wedge \hat e_i$ is a unit boost of the exceptional algebra. The statement collects results proved earlier in the series.

## lay
Close to the centre of a non-rotating black hole, space stretches in one direction and squeezes in the other two at fixed power-law rates. This collected result records that, at leading order and after a natural rescaling by time, the way directions twist into one another settles to a simple limiting pattern at known rates, and that the same holds with a cosmological constant. The limit is a statement about the field's values; for how directions are carried along paths it holds only over stretches of fixed rescaled length, and nothing is claimed for stretches of fixed coordinate length. It also records that this limiting pattern matches the structure found independently in the series' algebraic treatment of the singularity.

## one-liner
At the Schwarzschild and Schwarzschild-de Sitter singularities the Hubble-normalised connection tends, at leading order and at values level, to the Kasner boosts weighted by $(-\tfrac13, \tfrac23, \tfrac23)$ at stated rates (at transport level only along tangential curves of fixed Hubble-normalised length), and this limit matches the completion's exceptional module, forced weights and unit boost.
