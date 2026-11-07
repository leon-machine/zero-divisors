---
id: synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity
kind: claim
version: 3
title: '$e^{+}e^{-} \to \mu^{+}\mu^{-}$ in the spacetime algebra: tree and one loop'
status: proved
region: synthesis
subject: quantum-fields
tags: [recovers-known-physics, scattering-amplitudes, gauge-fields]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.field-theory.single-algebra-field
imported_from:
- citation: 'H. Lehmann, K. Symanzik and W. Zimmermann, Zur Formulierung quantisierter Feldtheorien, Nuovo Cimento 1 (1955), 205--225.'
  key: LSZ1955
  locator: 'the reduction formula: S-matrix elements are the residues of the amputated Green functions at the one-particle poles, with one factor Z^(1/2) per external leg; imported in Fact synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient (i)'
  doi: 10.1007/BF02731765
- citation: 'M. E. Peskin and D. V. Schroeder, An Introduction to Quantum Field Theory, Addison-Wesley (1995), chapters 5 and 7.'
  key: PeskinSchroeder1995
  locator: 'sec. 5.1 (e+e- -> mu+mu-: the spin sums, the angular distribution 1 + cos^2 theta, sigma = 4 pi alpha^2/(3 s) and the threshold factor), sec. 7.3 (the optical theorem) and sec. 7.5, eqs. (7.90) to (7.92) (the on-shell polarisation function, its large-s form and its imaginary part); cited from memory, equation numbers not checked'
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@5
  - field-theory.coupled-system-tree-level@3
  - synthesis.one-loop-qed-in-the-spacetime-algebra@4
  - synthesis.imported-one-loop-integrals-and-pauli-villars-regulators@2
  - synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_lsz_residues_are_spin_projectors
- kind: check
  ref: check.py::check_tree_spin_sum_from_clifford_traces
- kind: check
  ref: check.py::check_massless_angular_distribution_and_cross_section
- kind: check
  ref: check.py::check_massive_cross_section_threshold_factor
- kind: check
  ref: check.py::check_one_loop_absorptive_part_equals_tree_rate
- kind: check
  ref: check.py::check_one_loop_large_s_constant_and_longitudinal_part
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.coupled-system-tree-level
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the photon two-point function''s Feynman rule, the i0 boundary values, the branch ln(m^2/(A - I_4 0)) = ln(m^2/|A|) + I_4 pi and the absorptive part Im Pi(s + I_4 0) (Im the coefficient of I_4) now use the field theory''s unit I_4, numbers read in span{1, I_4}, one unit for the entity by Leon''s ruling R4; no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decision of 2026-11-02 (an assumes edge from every accepted result that states the Krein-form premise as the hypothesis of a clause): an assumes edge to synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, since clause (3) states it as the hypothesis of its charge-renormalisation sentence (the edge covers that sentence only; the tree amplitude, the absorptive part and the large-s form do not use it); a uses edge to the new Fact synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient@1 (the reduction formula, Ward''s identity), which replaces the citation from memory; the regulator-free vacuum polarisation accepted with it is cited by claimref (no uses edge: a supporting remark, not a premise); the lay level states the condition. Statement unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    The problem statement lists the missing LSZ reduction and S-matrix. Standard results (Lehmann, Symanzik and
    Zimmermann 1955; Peskin and Schroeder sec. 5.1 and ch. 7), recomputed in the series' formalism, not copied:
    on-shell external states are the minimal left ideals cut out by the propagator residues $p \pm m$ (twice the
    mass times idempotents of trace two, the two spin states), the spin sums are these multivectors, the trace is
    four times the scalar part, and the units stand outside the product. The cross sections are exact rationals
    times $\pi\alpha^{2}/s$ at rational kinematics; logarithms and $\pi$ symbolic. What is not done: the one-loop
    vertex and box corrections and real soft-photon emission (infrared), so no complete one-loop cross section is
    claimed; the one-loop content is the polarisation insertion, its absorptive part and the charge renormalisation. The
    relation of the absorptive part to the tree rate is the s-channel optical-theorem relation for the photon self-energy; full unitarity of the S-matrix
    at order e^4 also involves e+e- -> gamma gamma, the t-channel and box cuts, which are not computed.
    Transport-absent: no transport structure enters; the spacetime algebra is convenient (the spin sums are real
    multivectors). The polarisation loop has no internal photon, and the subtracted function does not depend on the regulator;
    a regulator-free construction with no Krein form is
    synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants.
    Only the charge-renormalisation sentence (Z1 = Z2, from vertex and self-energy loops with an internal photon)
    rests on the Krein-form premise, through the stored one-loop result; the assumes edge to the premise (2 November
    2026) covers that sentence only.
---

## formal
Signature $(+,-,-,-)$ in $\Cl(1,3)$, the Clifford product in place of the matrix product, traces $4\langle\cdot\rangle_{0}$, the units of the Feynman rules (the field theory's unit $I_{4}$) outside the product (\claimref{synthesis.one-loop-qed-in-the-spacetime-algebra}), the vertex of \claimref{field-theory.coupled-system-tree-level}, the free fields of \claimref{field-theory.second-quantisation}, and the on-shell external states of Fact \claimref{synthesis.imported-one-loop-integrals-and-pauli-villars-regulators}(v). Let $p_{1}, p_{2}$ be the incoming electron and positron, $p_{3}, p_{4}$ the outgoing muon and antimuon, $s = Q(p_{1} + p_{2})$, $\beta$ the muon speed in the centre-of-mass frame.
\begin{enumerate}
\item (LSZ; proved.) If $Q(p) = m^{2}$ then $(p + m)^{2} = 2m(p + m)$, $(p - m)^{2} = -2m(p - m)$, $(p + m)(p - m) = 0$, and $4\langle p \pm m\rangle_{0} = \pm 4m$: for $m \neq 0$, $(p + m)/(2m)$ is an idempotent of trace two. The propagator $S(p) = (p + m)/(Q(p) - m^{2})$ has residue $p + m$ at the pole, so after amputation and multiplication by $Z_{2}^{1/2}$ per leg (the reduction formula \cite{LSZ1955}, Fact \claimref{synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient}(i)) the sums over the two spin states of an outgoing particle and an incoming antiparticle are the multivectors $p + m$ and $p - m$.
\item (Tree; computed.) $\tfrac14\sum|M|^{2} = \tfrac{e^{4}}{4s^{2}}\,4\langle(p_{2} - m_{e})\gamma^{\mu}(p_{1} + m_{e})\gamma^{\nu}\rangle_{0}\,4\langle(p_{3} + m_{\mu})\gamma_{\mu}(p_{4} - m_{\mu})\gamma_{\nu}\rangle_{0} = \tfrac{8e^{4}}{s^{2}}[(p_{1}\cdot p_{3})(p_{2}\cdot p_{4}) + (p_{1}\cdot p_{4})(p_{2}\cdot p_{3}) + m_{\mu}^{2}\,p_{1}\cdot p_{2} + m_{e}^{2}\,p_{3}\cdot p_{4} + 2m_{e}^{2}m_{\mu}^{2}]$. For massless leptons $d\sigma/d\Omega = \tfrac{\alpha^{2}}{4s}(1 + \cos^{2}\theta)$ and $\sigma = \tfrac{4\pi\alpha^{2}}{3s}$; for $m_{e} = 0$, $\sigma = \tfrac{4\pi\alpha^{2}}{3s}\cdot\tfrac{\beta(3 - \beta^{2})}{2}$ \cite{PeskinSchroeder1995}.
\item (One loop; computed, the optical-theorem reading argued.) The longitudinal part $q_{\mu}q_{\nu}$ of the dressed photon vanishes between the on-shell currents ($q = p_{1} + p_{2}$), so the polarisation insertions resum to $M_{\mathrm{tree}}/(1 - \hat\Pi(s))$ with $\hat\Pi(s) = -\tfrac{2\alpha}{\pi}\int_{0}^{1}x(1-x)\ln\frac{m^{2}}{m^{2} - x(1-x)s - I_{4}0}\,dx$ (numbers read in $\mathrm{span}\{1, I_{4}\}$, $\mathrm{Im}$ the coefficient of $I_{4}$) for a loop fermion of mass $m$ (\claimref{synthesis.one-loop-qed-in-the-spacetime-algebra}(2), subtracted at $s = 0$; the subtracted function does not depend on the regulator, and the loop has no internal photon; with no regulator and no Krein form it is the extension of \claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants}(ii)). Its absorptive part is $\mathrm{Im}\,\hat\Pi(s + I_{4}0) = -2\alpha\int_{(1-\beta)/2}^{(1+\beta)/2}x(1-x)\,dx = -\tfrac{\alpha}{3}\cdot\tfrac{\beta(3 - \beta^{2})}{2}$, $\beta = (1 - 4m^{2}/s)^{1/2}$, and this equals $-s\,\sigma_{\mathrm{tree}}(e^{+}e^{-} \to f\bar f)/(4\pi\alpha)$ at $m_{e} = 0$: the cut of the photon self-energy is the tree rate (the s-channel optical-theorem relation for the photon self-energy; full unitarity at order $e^{4}$ also involves other channels, not computed). For $s \gg m^{2}$, $\mathrm{Re}\,\hat\Pi(s) = \tfrac{\alpha}{3\pi}(\ln(s/m^{2}) - \tfrac53) + O(m^{2}/s)$. Under the Krein-form premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields} (the vertex and self-energy loops carry an internal photon), $Z_{1} = Z_{2}$ (Ward's identity, Fact \claimref{synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient}(ii)) and the vertex counterterms cancel the leg factors $Z_{2}^{1/2}$, so the renormalised charge is $e = Z_{3}^{1/2}e_{0}$ and the insertion is the running $\alpha(s) = \alpha/(1 - \mathrm{Re}\,\hat\Pi(s))$ at this order (argued). All three clauses are standard \cite{LSZ1955, PeskinSchroeder1995}, recomputed in the spacetime algebra.
\end{enumerate}

## technical
With the conventions of one-loop electrodynamics in the spacetime algebra, the scattering of an electron and a positron into a muon pair is computed through the reduction formula. On shell, the propagator residue $p + m$ is twice the mass times an idempotent of trace two, so the spin sums of the external states are the real multivectors $p + m$ (particles) and $p - m$ (antiparticles); no imaginary unit enters.

At tree level the spin-averaged squared amplitude is the product of two Clifford traces, which reproduces the standard form exactly; for massless leptons it gives the $1 + \cos^{2}\theta$ distribution and $\sigma = 4\pi\alpha^{2}/(3s)$, and with the muon mass the threshold factor $\beta(3 - \beta^{2})/2$ (checked exactly at rational speeds, including threshold-free and massless limits).

At one loop the vacuum-polarisation insertion on the s-channel photon multiplies the tree amplitude by $1/(1 - \hat\Pi(s))$, the longitudinal part dropping between on-shell currents. Its absorptive part, the integral of $x(1-x)$ over the window where $x(1-x)s > m^{2}$, is $(\alpha/3)\beta(3 - \beta^{2})/2$ in size, which is exactly $s\sigma_{\mathrm{tree}}/(4\pi\alpha)$ for producing that fermion: the s-channel optical-theorem relation for the photon self-energy. The loop has no internal photon and the subtracted function does not depend on the regulator. At high energy the insertion is $(\alpha/(3\pi))(\ln(s/m^{2}) - 5/3)$, the running of the coupling, and under the Krein-form premise $Z_{1} = Z_{2}$ makes the charge renormalisation $Z_{3}^{1/2}$ alone. These are standard results, recomputed. Vertex and box corrections and soft-photon emission are not computed.

## lay
The series' algebra of spacetime now reproduces a standard textbook scattering prediction: an electron and a positron annihilate into a muon and an antimuon. The incoming and outgoing particles are fixed by algebraic projections built from their momenta, each picking out the particle's two spin states, and the rate comes out as the textbook formula, with the characteristic angular pattern and the suppression near the energy threshold for making the muons. At the next order the photon in the middle is dressed by virtual pairs; the part of this dressing that corresponds to real pairs being produced matches the rate computed at the first order exactly, one instance of the rule that probabilities add up to one, and the rest is the slow growth of the electric force with energy. Reading that growth as a change of the charge itself assumes the series' premise that the photon's states carry the standard indefinite measure.

## one-liner
Standard results recovered in the spacetime algebra: LSZ with spin sums $p \pm m$ (twice the mass times trace-two idempotents), the tree cross section $\sigma(e^{+}e^{-} \to \mu^{+}\mu^{-}) = \tfrac{4\pi\alpha^{2}}{3s}\beta(3 - \beta^{2})/2$ from two Clifford traces, and at one loop the polarisation insertion, whose cut $(\alpha/3)\beta(3-\beta^{2})/2$ equals $s\sigma_{\mathrm{tree}}/(4\pi\alpha)$ (the s-channel optical-theorem relation for the photon self-energy) and whose large-$s$ form is $(\alpha/(3\pi))(\ln(s/m^{2}) - 5/3)$; the charge renormalisation $e = Z_{3}^{1/2}e_{0}$ under the Krein-form premise.
