---
id: synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum
kind: claim
version: 4
title: 'The linear rung field adds a neutral normal pair to the scalon sum'
status: proved
region: synthesis
subject: quantum-fields
tags: [symmetry-breaking, gauge-fields, pseudoscalar-and-centre, mass-generation, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - synthesis.rung-field-on-the-lift-locus@2
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@3
  - synthesis.scale-free-rung-potentials-need-the-flat-physical-branch@2
  - synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev@4
  - synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass@1
  - field-theory.boost-modes@3
  - synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count@1
  proof: proof-main.tex
quantities:
- quantity.higgs-boson-mass@1
- quantity.w-boson-mass@1
- quantity.z-boson-mass@2
- quantity.top-quark-mass@1
- quantity.top-quark-mass-mz@1
- quantity.bottom-quark-mass@1
- quantity.charm-quark-mass@1
- quantity.tau-mass@1
- quantity.fermi-scale@1
checked_by:
- kind: check
  ref: check.py::check_i4_is_the_rung_fields_imaginary_unit_and_hypercharge_is_the_imaginary_rapidity_boost
- kind: check
  ref: check.py::check_linear_field_spectrum_at_the_family_point
- kind: check
  ref: check.py::check_null_lift_level_of_the_linear_vacuum
- kind: check
  ref: check.py::check_scale_free_linear_field_on_the_flat_ray
- kind: check
  ref: check.py::check_scalon_sum_with_the_normal_pair
- kind: check
  ref: check.py::check_diphoton_below_090_for_every_charged_mass
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev
  - field-theory.composite-scalars-mean-field-level
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The statements ''the field theory''s unit i = I_4'' now name the unit I_4 directly, and the hypercharge generator is Y = (1/2) I_4 1; no bare i remains (the name R_C of the complexified rung summand is kept as stored; clause (1) shows it is span{1, I_4} tensor (H_4 + H_5)).'
  maintainer_pass_qft_full:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 2 -> 3, by Leon''s decision of 2 November 2026 on the weak scale: a dated note at every level records the scale-free (transmutation) branch of clauses (3) to (5) as excluded under the decided coupling reading (covariant completion, complex symmetric family matrices), collecting the three strikes with numbers and sources (PDG 2026 diphoton average 1.10 +- 0.06, read from pdglive node S126SGG on 2 November 2026, against the bound 0.900, 3.3 standard deviations; tree-level B mixing more than 50 times measured for every splitting; quartics at 4 pi by 0.8 to 4 TeV at one loop) and naming the branch with a level as the working branch; the extraction note''s ''not computed'' items (running, Landau pole, limits on the normal pair) are now the subject of those results. The pin of synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev moves to @4 (its dated note, content unchanged). Clauses (1) to (5), their mathematics, status and check unchanged.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-01: a uses edge to the imported Fact synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count@1 (the two-doublet Gildener-Weinberg sum rule, Lee-Pilaftsis and Lane-Shepherd, and the light-neutrino count from the Z resonance), which replaces the in-text citation and the Z width cited from memory; the pins of synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev and synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus move to @3 (marked notes added there recording this result''s reading, their content unchanged). Statement and check unchanged.'
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    The problem asks for the rung field quantised in the palatial (polynomial) storey with i = I4 and its one-loop
    effective potential. A field restricted to the quadric L = {Q = -H^2} (or the cone Q = 0) is a nonlinear field;
    a renormalisable elementary field with a polynomial potential, which is what the polynomial CCR representation
    and the imported Gildener-Weinberg Fact presuppose, is the linear field on all eight real components. Clause (1)
    fixes the unit: I4 commutes with the rung vectors (the stored single-algebra field already says I4 commutes with
    every mode), so the complexification is internal to the algebra, c^2 = Q(c) is I4-bilinear, and on the rung
    summand the hypercharge rotation is the rung boost at I4-imaginary rapidity, the stored reading of
    field-theory.boost-modes on the rung planes; the continued rotor moves every spacetime vector, so this holds on
    rung values, not on spacetime points. Clause (2) gives the spectrum of the linear field at the stored
    family point: the stored tangent masses survive and two neutral states are added, the alpha_1 directions, whose
    mass is set by the Q-dependent invariants; the constrained field is their infinite-mass limit (the vacuum's
    null-lift level is H^2(1 - 2W'/m_H^2)). Clauses (3) to (5) are the one-loop (Gildener-Weinberg) potential of the
    scale-free linear field: the stored transmutation result counted the six directions tangent to the cone, which is
    the linear field's sum with a massless normal pair; counted in full, the stored bracket 450-456 GeV becomes an
    upper bound and the normal pair is bounded by 542 GeV, so the constraint cannot be imposed by a large coupling in
    the transmutation scenario. The diphoton deficit does not depend on the charged mass: mu_gamgam < 0.900 for every
    charged mass below 456 GeV, lower for lighter pairs (computed: 0.899 at 456, 0.873 at 100 GeV). Standard pieces:
    the two-doublet spectrum and the scalon formula (Gildener-Weinberg, imported); the sum rule of clause (4) is the
    standard one of the scale-invariant two-doublet model (J. S. Lee and A. Pilaftsis, Phys. Rev. D 86 (2012) 035004,
    arXiv:1201.4891; K. Lane and W. Shepherd, arXiv:1808.07927, Eq. (10), (sum M^4)^(1/4) = 540 GeV; imported,
    synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count), and the new content is that the series' rung field quantised linearly is that model and
    that the stored 450-456 GeV bracket is its massless-normal-pair edge; the loop functions are cited from
    memory as in the stored transmutation result. Transport-convenient: the field, the locus and the unit are the
    series'; the computation is standard. Not computed: running couplings, the Landau pole of the large quartics,
    collider limits on the normal pair (LEP's Z width excludes a massless pair, argued in the proof from the imported light-neutrino count,
    synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count).
---

## formal
In the setting of \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}: the complexified rung summand $\mathcal{R}_{\C}$ with $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$, $Q(c) = \alpha^{\mathsf T}\beta$, $N = \tfrac12(|\alpha|^{2} + |\beta|^{2})$, $m = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, the slot mixing $U(2)$ with generators $T_{j}$ and $Y$, the rung boost $e^{tK}$, the D-term potential $V_{D}$ at level $\xi = 2\zeta$, the null-lift locus $L = \{Q = -H^{2}\}$, its cone $L_{0} = \{Q = 0\}$ (the limit $H \to 0$) and the physical family point $\alpha = 0$, $\beta = (-\lambda, 0)$ of $L_{0}$, with $N^{*} = \tfrac12\lambda^{2}$, $M_{W}^{2} = \tfrac12 g^{2}N^{*}$, $M_{Z}^{2} = \tfrac12(g^{2} + g'^{2})N^{*}$, $v^{2} = 2N^{*}$. Take the field theory's unit to be $I_{4}$ (\claimref{obj.field-theory.single-algebra-field}). The \emph{linear rung field} is the field with values in all of $\mathcal{R}_{\C}$, eight real components, with a real $U(2)$-invariant polynomial potential; the \emph{constrained field} is its restriction to $L$ or $L_{0}$. Masses are eigenvalues of the Hessian divided by the kinetic coefficient of the stored Hermitian term. Write $r = \sqrt{k_{8}^{2} + k_{9}^{2}}$.
\begin{enumerate}
\item \emph{(The unit.)} In $\Cl(3,5)$, spacetime with the two rung planes, $I_{4}^{2} = -1$ and $I_{4}$ commutes with every $v_{a}$, $w_{a}$; so $\mathcal{R}_{\C} = \mathrm{span}\{1, I_{4}\}\otimes(H_{4} \oplus H_{5})$ inside the algebra, $c^{2} = Q(c)$ is $I_{4}$-bilinear, and the field has four $I_{4}$-complex modes per momentum. With $b = \sum_{a}v_{a}\wedge w_{a}$, $\mathrm{Ad}(e^{tb})$ is the rung boost $e^{tK}$, and $\mathrm{Ad}(e^{\phi I_{4}b})$ multiplies each $v_{a}$ by $e^{\phi I_{4}}$ and each $w_{a}$ by $e^{-\phi I_{4}}$, which is $e^{2\phi Y}$: on the rung summand the hypercharge rotation is the rung boost at $I_{4}$-imaginary rapidity, the reading \claimref{field-theory.boost-modes} gives on the modes. Since $I_{4}b$ anticommutes with every spacetime vector, $\mathrm{Ad}(e^{\phi I_{4}b})$ does not fix the spacetime vectors (it moves $\gamma_{0}$ for $\cos\phi = -\tfrac{7}{25}$), so the identification holds on rung values, not on spacetime points.
\item \emph{(Spectrum of the linear field.)} Let $V = V_{D} + W(N) + k_{8}\operatorname{Re}Q^{2} + k_{9}\operatorname{Im}Q^{2} + k_{10}|Q|^{2}$, with the level fixed by the stored vacuum condition so that the family point is critical. Its eight masses there are $0$ three times (the gauge orbit), $m_{h}^{2} = M_{Z}^{2} + 2N^{*}W''$ and $m_{\pm}^{2} = M_{W}^{2} + 2W'$ twice, as on $L$, and the \emph{normal pair}, spanned by the two directions of $\alpha_{1}$, the only directions that change $Q$ at first order, with
\[
m_{H}^{2},\ m_{A}^{2} = 2W'(N^{*}) + 4N^{*}(k_{10} \pm r) = m_{\pm}^{2} - M_{W}^{2} + 4N^{*}(k_{10} \pm r),
\]
not mixed with the other modes. For the pure D-term the normal pair is massless. With $k_{8} = k_{9} = 0$ and the term $k_{10}|Q + H^{2}|^{2}$, the vacuum lies at $Q = -H^{2}(1 - 2W'/m_{H}^{2})$ to first order in $H^{2}$: the constrained field is the limit $k_{10} \to \infty$ of the linear one, at fixed $m_{h}$ and $m_{\pm}$.
\item \emph{(Scale-free linear field.)} Let $V$ be a quartic over the ten stored invariants on all of $\mathcal{R}_{\C}$, $V = k_{1}|\alpha|^{4} + k_{2}|\beta|^{4} + k_{3}|\alpha|^{2}|\beta|^{2} + |\alpha|^{2}(k_{4}\operatorname{Re}Q + k_{5}\operatorname{Im}Q) + |\beta|^{2}(k_{6}\operatorname{Re}Q + k_{7}\operatorname{Im}Q) + k_{8}\operatorname{Re}Q^{2} + k_{9}\operatorname{Im}Q^{2} + k_{10}|Q|^{2}$, with the flat condition $a + b - e = 0$ and the admissibility $e \ge 0$, $2a \ge e$ of \claimref{synthesis.scale-free-rung-potentials-need-the-flat-physical-branch}(3). The physical ray $\alpha = 0$ is a critical point exactly when $k_{6} = k_{7} = 0$. There the masses are $0$ four times (three gauge directions and the scalon), $m_{\pm}^{2} = 2(2a - e)N$ twice, and $m_{H}^{2}, m_{A}^{2} = 2(2a - e)N + 4N(k_{10} \pm r)$, all proportional to $N$. If $k_{4} = k_{5} = 0$ and $k_{10} \ge r$, then $V \ge 0$ on $\mathcal{R}_{\C}$ and $m_{H}, m_{A} \ge m_{\pm}$; if $k_{10} + r < -(2a - e)/2$ the normal pair is tachyonic.
\item \emph{(The scalon sum.)} Under the hypotheses (GW) and (D) of \claimref{synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev}, applied to the scale-free linear field of (3) (real scalars with a quartic polynomial potential, the setting of Fact \claimref{synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass}), the real scalars other than the scalon and the gauge directions are the charged pair and the normal pair, and
\[
8\pi^{2}v^{2}m_{h}^{2} = 6M_{W}^{4} + 3M_{Z}^{4} + 2m_{\pm}^{4} + m_{H}^{4} + m_{A}^{4} - 12m_{t}^{4} - \ell, \qquad \ell = 12m_{b}^{4} + 12m_{c}^{4} + 4m_{\tau}^{4}.
\]
With the stored input box of that result ($m_{h} \in [125, 125.4]$, $v \in [246, 247]$, $m_{t} \in [162, 173]$ GeV, the stored $M_{W}$, $M_{Z}$, $m_{b}$, $m_{c}$, $m_{\tau}$), $2 \cdot 450^{4} < 2m_{\pm}^{4} + m_{H}^{4} + m_{A}^{4} < 2 \cdot 456^{4}$ GeV$^{4}$. Hence $m_{\pm} < 456$ GeV and $m_{H}, m_{A} < 542$ GeV; when $m_{H}, m_{A} \ge m_{\pm}$ (as under $k_{4} = k_{5} = 0$, $k_{10} \ge r$), $m_{\pm} < 383$ GeV. The stored bracket $450 < m_{\pm} < 456$ GeV is the case $m_{H} = m_{A} = 0$. The displayed relation is the standard Gildener-Weinberg sum rule of the scale-invariant two-doublet model; what is new is that the linear rung field is that model.
\item \emph{(Diphoton rate.)} Under the same hypotheses, with the loop functions of the stored result, the normal pair is neutral and does not enter $h \to \gamma\gamma$ at one loop, the charged pair enters with unit weight, and its loop function $A_{0}(\tau) = \tfrac12\sum_{n \ge 2}4^{n}\tau^{n - 2}/(n^{2}\binom{2n}{n})$, $\tau = m_{h}^{2}/4m_{\pm}^{2}$, increases as $m_{\pm}$ decreases; so $\mu_{\gamma\gamma}$ decreases with $m_{\pm}$ and $\mu_{\gamma\gamma} < 0.900$ for every $m_{\pm} \in (m_{h}/2, 456]$ GeV.
\end{enumerate}

\emph{Note (the transmutation branch excluded, 2 November 2026).} Under the decided coupling reading, the $\su(2)_{R}$-covariant completion $Yc + \tilde{Y}c^{*}$ with complex symmetric family matrices (the rung $10$), the scale-free (transmutation) branch of clauses (3) to (5) is recorded as excluded, by three independent strikes: (a) $h \to \gamma\gamma$: the bound $\mu_{\gamma\gamma} < 0.900$ of (5) lies $3.3$ standard deviations below the Particle Data Group 2026 average $1.10 \pm 0.06$ (pdglive node S126SGG, read on 2 November 2026; inputs ATLAS 2023 $1.04^{+0.10}_{-0.09}$, CMS 2022 $1.13 \pm 0.09$, ATLAS and CMS Run 1 $1.14^{+0.19}_{-0.18}$); (b) $B$-meson mixing: with the normal pair below $542$ GeV, as (4) requires, its tree-level exchange exceeds the measured $B_{s}$ and $B_{d}$ mass differences more than $50$ times for every splitting of $m_{H}$ and $m_{A}$ (more than $52$ and $50$), with quark mixing from tree-level determinations and three-family unitarity (\claimref{synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch}); (c) strong coupling: on the surface of (4) the quartic couplings reach $4\pi$ between about $0.8$ and $4$ TeV at one loop (\claimref{synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch}). Clauses (1) to (5) and their mathematics are unchanged: (1) and (2) hold for the linear field on every branch, and (3) to (5) stand as statements about the scale-free linear field under (GW) and (D); what is excluded is that branch as the origin of the weak scale under that coupling reading. The branch with a level, on which the normal pair and the charged pair are heavy (about $2.5$ to $3.5$ TeV), is the working branch.
## technical
Take the field theory's unit to be $I_{4}$. In the algebra of spacetime and the two rung planes, $I_{4}$ commutes with the rung vectors, so the rung field's complex coefficients are $\mathrm{span}\{1, I_{4}\}$-valued inside the algebra, $c^{2} = Q(c)$ is bilinear over them, and the field carries four $I_{4}$-complex modes per momentum; on the rung summand the hypercharge rotation is the rung boost $\mathrm{Ad}(e^{tb})$, $b = \sum_{a}v_{a}\wedge w_{a}$, taken at imaginary rapidity $t = \phi I_{4}$. The continued rotor moves the spacetime vectors ($I_{4}b$ anticommutes with them), so this holds on rung values, not on spacetime points.

A polynomial (elementary) quantum field is linear: it takes values in all eight real components, not on the quadric $Q = -H^{2}$. For $V = V_{D} + W(N) + k_{8}\operatorname{Re}Q^{2} + k_{9}\operatorname{Im}Q^{2} + k_{10}|Q|^{2}$ at the stored family point on the cone, the stored masses $m_{h}^{2} = M_{Z}^{2} + 2N^{*}W''$ and $m_{\pm}^{2} = M_{W}^{2} + 2W'$ survive, and a neutral normal pair appears, the two directions that change $Q$, with $m_{H,A}^{2} = 2W' + 4N^{*}(k_{10} \pm r)$, $r = \sqrt{k_{8}^{2} + k_{9}^{2}}$; it is massless for the pure D-term, and the constrained field is the limit $k_{10} \to \infty$ (the linear vacuum sits at $Q = -H^{2}(1 - 2W'/m_{H}^{2})$ to first order in $H^{2}$).

For the scale-free linear field with the flat physical ray ($k_{6} = k_{7} = 0$ is needed for the ray to be critical), the masses are $0$, $m_{\pm}^{2} = 2(2a - e)N$ and $m_{H,A}^{2} = m_{\pm}^{2} + 4N(k_{10} \pm r)$, all proportional to $N$, so under the Gildener-Weinberg formula and decoupling the normal pair enters the scalon sum, the standard sum rule of the scale-invariant two-doublet model: $2m_{\pm}^{4} + m_{H}^{4} + m_{A}^{4}$ lies between $2 \cdot 450^{4}$ and $2 \cdot 456^{4}$ GeV$^{4}$ over the stored inputs. The charged pair lies below $456$ GeV (below $383$ GeV when the normal pair is the heavier, as for $k_{4} = k_{5} = 0$, $k_{10} \ge r$), the normal pair below $542$ GeV; the stored $450$ to $456$ GeV is the edge with a massless normal pair. That edge is itself excluded (argued): the normal pair is the neutral part of a doublet, so a massless pair would add about half a neutrino species to the invisible width of the $Z$, which the measured width rules out. The normal pair is neutral, and the charged pair's loop function grows as it gets lighter, so $h \to \gamma\gamma$ stays below $0.900$ of the Standard Model rate for every charged mass between $m_{h}/2$ and $456$ GeV. (Note, 2 November 2026: under the series' coupling reading with symmetric family matrices the transmutation branch is excluded, by the diphoton rate, whose Particle Data Group 2026 average $1.10 \pm 0.06$ lies $3.3$ standard deviations above the bound $0.900$, by tree-level $B$-meson mixing from the light normal pair more than fifty times the measured rate, and by quartic couplings that reach $4\pi$ between about $0.8$ and $4$ TeV; the spectrum of the linear field stands on every branch, and the branch with a level, with the second doublet at a few TeV, is the working branch.)
## lay
To treat the series' Higgs candidate, the rung field, as a quantum field one has to say what its quantum values are. The series' own imaginary unit, the spacetime volume element, works for it, and with that unit the hypercharge symmetry turns out to be the series' frame boost taken at imaginary speed. A quantum field of the ordinary, well-behaved kind cannot be confined to the curved surface on which the rung field was defined; it has to range over all its directions, and two extra neutral particles appear, the directions off the surface. If the weak scale arises from quantum corrections alone, as an earlier result explored, these two particles must be counted: the charged scalar that result predicted near 450 GeV is then lighter, the new neutral pair lies below about 540 GeV, and the predicted shortfall in the Higgs boson's decays to two photons, about ten per cent, remains for every allowed charged mass. (Since 2 November 2026 that quantum-corrections route is recorded as ruled out under the series' reading of how the Higgs field couples to quarks: the measured two-photon rate lies well above the predicted shortfall, the new neutral pair would make bottom mesons turn into their antiparticles far faster than is observed, and the forces among these particles would grow too strong within a few TeV. The working alternative has the second set of particles at a few TeV.)
## one-liner
With $i = I_{4}$ the elementary rung field is linear on eight components (on the rung summand, hypercharge is the rung boost at $I_{4}$-imaginary rapidity) and adds a neutral normal pair at $2W' + 4N(k_{10} \pm r)$ to the stored spectrum, the constraint being $k_{10} \to \infty$; under Gildener-Weinberg and decoupling $2m_{\pm}^{4} + m_{H}^{4} + m_{A}^{4} \in (2 \cdot 450^{4}, 2 \cdot 456^{4})$ GeV$^{4}$, so $m_{\pm} < 456$ GeV, $m_{H,A} < 542$ GeV, and $\mu_{\gamma\gamma} < 0.900$ for every charged mass in $(m_{h}/2, 456]$ GeV. (Excluded on 2 November 2026 under the symmetric coupling reading: Particle Data Group 2026 $\mu_{\gamma\gamma} = 1.10 \pm 0.06$, $B$ mixing over $50$ times the measured rate, quartics at $4\pi$ by $0.8$ to $4$ TeV; the level branch is the working branch.)
