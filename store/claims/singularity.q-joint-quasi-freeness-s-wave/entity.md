---
id: singularity.q-joint-quasi-freeness-s-wave
kind: claim
version: 3
title: '(Q): joint quasi-freeness, with the s-wave weights at the half-integer offset'
status: postulate
region: singularity
subject: thermality
tags: [thermal-premises, car-algebra]
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
review: typed
about:
- obj.singularity.geometric-modular-condition-g
lineage:
  motivated_by:
  - synthesis.q-splits-maximum-entropy-affine-weights
  - synthesis.half-integer-weight-array-carries-half-ln2
  - synthesis.positive-null-energy-gives-r-premises
locators:
  paper: T05
  number: Premise 8.1
  label: prem:quasifree
  line: 2008
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: >-
      Version 3 (Leon's decision of 23 October on the array offset): the weight clause's offset becomes
      kappa(k + 1/2), the sea level midway between two sites, adopted as a consequence of reading the array's
      modes as the discretised modes of the field theory's spinor fields on the horizon's light rays (boost
      weight 1/2) in the state that (N+) (synthesis.n-plus-null-ground-state) selects, not as a bare premise; the reading is a decision, not a
      derivation (the stored premises leave the offset free, synthesis.q-splits-maximum-entropy-affine-weights
      (iv)). The paragraph on the zero-weight mode k = 0 is replaced (the array has none), the statement
      records that the joint KMS part's continuum form follows from (N+)
      (synthesis.positive-null-energy-gives-r-premises (ii), (iii)), and the consequences of the offset are
      stated at the strength of the stored results. The source's Premise 8.1 (weights kappa k) is kept as
      source_formal and is version 2; results computed under kappa k (the residue value 0.3470, the
      zero-mode charge doublet, the one-channel-per-mode count) refer to version 2 and carry notes saying so.
  maintainer_pass_2026_11_07:
    by: ai-maintainer-pass
    note: >-
      Leon's decision of 7 November (a note, the premise unchanged): the half-integer offset kappa(k + 1/2) of the
      weight clause appears exactly as the band centre when the null momentum of a horizon generator is compressed
      to band modes of width Delta, whose weights are Delta(k + 1/2)
      (synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (iii)). The
      compression is not invariant under the null translations, so this is a second reading of the offset beside
      the boost-weight reading of version 3, not a derivation of it.
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'Folded-state-selection (R) fix: the formal level''s (R) now carries a claimref to T05''s premise singularity.r-regularity-fixed-locus, so it is not read as the folded note''s regularity premise.'
  source_formal: "In the stationary idealisation of the boundary modes, and for this step alone, the joint state of the mode array is taken to be the gauge-invariant quasi-free state with the marginal data that (P) and (R) fix unconditionally (Theorem \\claimref{singularity.rate-discharge-hypothesis-iii}, Corollary \\claimref{singularity.chains-state-class-stability}): writing $\\psi_k$ for the fermion modes of the array of Theorem \\claimref{singularity.bosonisation-bridge-s-wave-sector} below, its two-point function is $\\langle \\psi^\\dagger_k \\psi_l \\rangle = \\delta_{kl}\\,n_k$, and every higher correlation function factorises by Wick's theorem, so that all connected correlators vanish and the joint state is KMS at $\\beta = 2\\pi/\\kappa$ for the joint modular flow. The mode weights are assigned linearly, $\\omega_k = \\kappa k$, with the array's sea level at $k = 0$: the weights $\\omega_k$ of Definition \\claimref{obj.singularity.geometric-modular-condition-g} are fixed nowhere in the framework, and the linear assignment is the s-wave reduction's convention, adopted here as part of the premise. The $k = 0$ mode carries $\\omega_0 = 0$ and is the one mode at which (R) carries no temperature: the gluing equation of Theorem \\claimref{singularity.rate-discharge-hypothesis-iii} becomes $n_0 = 1 - n_0$ independently of the period, so it fixes $n_0 = \\tfrac12$ but says nothing about $\\beta$; (Q)'s sea-level convention agrees with that value and additionally fixes the weight. At this one mode three results of Section \\ref{subsec:selection} need, and carry, their own local scopes: Theorem \\claimref{singularity.descended-form-state-independent}'s Gibbs form loses uniqueness there always, and existence unless $p_0 = \\tfrac12$, the value the degenerate gluing forces for the chain's state but not for an arbitrary one; Corollary \\claimref{singularity.universality-temperature-under-g}'s nonzero-weight clause excludes the mode outright; and Theorem \\claimref{singularity.rate-discharge-hypothesis-iii}'s boundary-case clause is scoped to $\\omega \\neq 0$, the tracial marginal being at $\\omega_0 = 0$ exactly the one the gluing fixes."
  env: premise
  context_refs:
  - singularity.bosonisation-bridge-s-wave-sector
  - singularity.chains-state-class-stability
  - singularity.descended-form-state-independent
  - singularity.rate-discharge-hypothesis-iii
  - singularity.universality-temperature-under-g
  typing:
    by: ai-typing-pass
    note: "Postulate with no derivation; its context references (the rate theorem, state-class corollary, bosonisation bridge and others) are scope remarks, not premises, so no edges were added."
---

## formal
In the stationary idealisation of the boundary modes, and for this step alone, the joint state of the mode array is taken to be the gauge-invariant quasi-free state with the marginal data that (P) and (R) (Premise \claimref{singularity.r-regularity-fixed-locus}) fix unconditionally (Theorem \claimref{singularity.rate-discharge-hypothesis-iii}, Corollary \claimref{singularity.chains-state-class-stability}): writing $\psi_k$ for the fermion modes of the array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, its two-point function is $\langle \psi^\dagger_k \psi_l \rangle = \delta_{kl}\,n_k$, and every higher correlation function factorises by Wick's theorem, so that all connected correlators vanish and the joint state is KMS at $\beta = 2\pi/\kappa$ for the joint modular flow. The mode weights are evenly spaced with the array's sea level midway between two sites,
\[
\omega_k = \kappa\bigl(k + \tfrac12\bigr), \qquad k \in \Z ,
\]
so that no mode has zero weight, the weights are symmetric under the particle-hole relabelling $k \mapsto -1-k$, and the Killing flow at one modular period $2\pi/\kappa$ is the parity automorphism $\psi \mapsto -\psi$.

\emph{Why this offset.} The weights $\omega_k$ of Definition \claimref{obj.singularity.geometric-modular-condition-g} are fixed nowhere else in the framework: given (P), (R) and the quasi-free clause, an affine law $\omega_k = ck + d$ is what the currents' being normal modes of the boost flow requires, particle-hole symmetry leaves exactly two offset classes, $d = 0$ and $d = c/2$, and the slope is the value $\beta c = 2\pi$ (Theorem \claimref{synthesis.q-splits-maximum-entropy-affine-weights}(ii), (iv)). The class $d = c/2$ is adopted as a consequence of one reading, not as a bare premise: the array's modes are read as the discretised modes of the field theory's spinor fields on the horizon's light rays, $\psi(u) \mapsto e^{\kappa t/2}\psi(e^{\kappa t}u)$, of boost weight $\tfrac12$ (the weight at which the boost preserves the anticommutator), in the state that Premise \claimref{synthesis.n-plus-null-ground-state} (N$_{+}$) selects, a ground state for the affine null translations of the generators (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}). A field of boost weight $\tfrac12$ changes sign under a full turn of the regular Euclidean section, and $\kappa(k + \tfrac12)$ is the offset at which the array's Killing flow at one modular period carries that sign (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}). The reading is a decision, not a derivation: the Euclidean-period sign $R_{2\pi} = -1$ (Proposition \claimref{state-selection.where-fermi-dirac-comes}) holds in a KMS state of the array at either offset, so identifying the array's real-time recurrence at one period with it is part of the reading.

\emph{On the continuum.} The joint KMS part of this premise is not a separate assumption on the continuum mode space of a horizon's generators: there it follows from (N$_{+}$), whose null ground state restricts on either side of the edge to the continuum I-state at $\beta = 2\pi/\kappa$, jointly KMS and even (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(ii), (iii)). The stationary array statement here is its point-spectrum discretisation, on which (N$_{+}$) itself cannot be posed (part (iv) there). The quasi-free clause is a hypothesis of (N$_{+}$) as well, and (N$_{+}$) does not give the weight clause.

\emph{Consequences of the offset.} At these weights one array carries exactly $\tfrac12\ln 2$ at the Hawking temperature, given the classical theta-function identities, so under the entropy-matching hypothesis two arrays carry the capacity $\ln 2$ of one registered boundary mode with no zero-weight mode (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(i), (iii)); the current sector of one array is one oscillator tower, one helicity channel, at either offset (Theorem \claimref{synthesis.array-ln2-is-zero-mode-doublet-one-tower}(ii), (iv)), so one registered mode then corresponds to two arrays and two helicity channels. Since every mode has nonzero weight, the gluing equation of Theorem \claimref{singularity.rate-discharge-hypothesis-iii} fixes $\beta$ at every mode of the array, and the zero-weight scopes of Theorems \claimref{singularity.descended-form-state-independent}, \claimref{singularity.universality-temperature-under-g} and \claimref{singularity.rate-discharge-hypothesis-iii} do not arise on it.

\emph{Version 2.} The source states the weight clause as $\omega_k = \kappa k$ with the sea level at $k = 0$, one mode of zero weight at which the gluing equation fixes $n_0 = \tfrac12$ but not $\beta$. Results computed under that offset refer to version 2.

## technical
In the stationary idealisation of the boundary modes, and for this step alone, the joint state of the mode array is taken to be the gauge-invariant quasi-free state with the marginal data already fixed by (P) and (R): $\langle \psi_k^\dagger \psi_l \rangle = \delta_{kl}\, n_k$, with every higher correlation function factorising by Wick's theorem, so that all connected correlators vanish and the joint state is KMS at $\beta = 2\pi/\kappa$ for the joint modular flow. The mode weights are $\omega_k = \kappa(k + \tfrac12)$: evenly spaced, with the sea level midway between two sites, so no mode has zero weight and the Killing flow at one modular period is minus the identity on the fermions. These are the fermionic Matsubara frequencies at the Hawking temperature.

The framework leaves the weights free up to an affine law with two choices, the offset and the slope. The offset is fixed by reading the array's modes as the discretised modes of the field theory's spinor fields on the horizon's light rays, which carry boost weight one half, in the state singled out by the null ground-state premise (N$_{+}$): such fields change sign under a full Euclidean turn, and the half-integer offset is the one whose Killing flow at one period carries that sign. This is a reading adopted by decision, not a derivation. On the continuum of modes along the generators, the joint thermal part of this premise follows from (N$_{+}$); the array is its discretisation. The quasi-free clause and the weights remain assumptions.

With these weights one array carries exactly half of $\ln 2$ at the Hawking temperature, so two arrays carry one registered boundary mode's $\ln 2$, with no zero-weight mode, and since one array is one helicity channel, one registered mode then carries two. The source paper's weights $\kappa k$, with one zero-weight mode, are the premise's version 2.

## lay
This is an assumption, not a derived result. It says that, in an idealised steady state, the boundary modes are uncorrelated beyond what their individual thermal occupations already require. It also fixes how much energy each mode carries: equally spaced energies, set half a step away from zero so that no mode has zero energy. That half step is chosen because the modes are read as the matter fields that live on light rays at the horizon, which turn into their negatives after a full rotation; the framework itself does not determine these energies. With this choice two such arrays of modes hold exactly one bit of information between them.

## one-liner
Premise: in the stationary idealisation the joint state of the boundary modes is the quasi-free state with the marginals fixed by (P) and (R), and the mode weights are $\omega_k = \kappa(k + \tfrac12)$, the half-integer offset read from the modes being spinor fields of boost weight $\tfrac12$ under (N$_{+}$); its joint thermal part follows from (N$_{+}$) on the continuum.
