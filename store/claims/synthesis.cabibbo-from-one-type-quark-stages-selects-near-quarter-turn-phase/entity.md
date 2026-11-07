---
id: synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase
kind: claim
version: 3
title: 'Cabibbo angle from one-type quark stages selects a near quarter-turn phase'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
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
derivations:
- name: main
  uses:
  - neutrino.breaking-relation@3
  - synthesis.solar-angle-light-plane-sum-rule@1
  - synthesis.series-family-structures-give-no-lopsided-second-stage@2
  - synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns@1
  - families.faces-ordered-what-identification-requires-first@3
  - synthesis.imported-fritzsch-texture-cabibbo-formula@1
  - synthesis.imported-flag-2024-light-quark-mass-ratios@1
  proof: proof-main.tex
quantities:
- quantity.ckm-vus-magnitude@1
- quantity.down-quark-mass-mz@1
- quantity.strange-quark-mass-mz@1
- quantity.up-quark-mass-mz@1
- quantity.charm-quark-mass-mz@1
checked_by:
- kind: check
  ref: check.py::check_light_angle_is_the_gst_relation
- kind: check
  ref: check.py::check_overlap_formula
- kind: check
  ref: check.py::check_real_and_third_turn_phases_miss_vus
- kind: check
  ref: check.py::check_quarter_turn_band_contains_vus
- kind: check
  ref: check.py::check_phase_window
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.faces-ordered-what-identification-requires-first
  - synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit in the Gaussian-rational test value 1 + 2i and in the rephasings diag(e^{i beta_1}, e^{i beta_2}) and e^{i(beta_1 - beta_2)} became I_4, mass-matrix entries and phases read in span{1, I_4}; no bare i remains. The formal''s ''quark Dirac matrices'' (the mass matrices M_q) now reads ''quark Dirac mass matrices'', so that it is not read as the Dirac gamma matrices.'
  open_problem: op.second-order-breaking
  note: 'Outside idea tested in the series structures: the Gatto-Sartori-Tonin relation and Fritzsch textures. The stored light-plane block [[k, x], [y, 0]] with |x| = |y| is the heavy-quark-limit Fritzsch texture, so the stored sum rule for leptons and the families paper''s Cabibbo pass are one relation read in two sectors. The heavy-quark-limit formula sin theta_C = |R_u - R_d e^{-i psi}| and the fitted psi near 90 degrees are Fritzsch and Xing (hep-ph/9904286, the light quark sector, CP violation and the unitarity triangle; imported as the Fact synthesis.imported-fritzsch-texture-cabibbo-formula). The ratio windows cover the FLAG 2024 lattice averages (arXiv:2411.04268, Table 1, imported as the Fact synthesis.imported-flag-2024-light-quark-mass-ratios: m_s/m_ud = 27.227(81), m_u/m_d = 0.465(24), m_c/m_s = 11.766(30), so m_s/m_d = 19.94 and m_c/m_u = 505) by more than three standard deviations; they are hypotheses of the clauses, since the stored M_Z running masses (whose central ratios 18.97 and 487 lie inside) are too uncertain individually to fix them. Numerology guard: the formula and the five candidate phases (cos phi in {1, 1/2, 0, -1/2, -1}, those of finite symmetries with rational cosine) were fixed before comparing; one of five fits, and with candidate values about 0.02 apart against a tolerance of about 0.003 the chance that one fits is about 0.3 (estimate), so the phase is selected by the data, not predicted; the Nf = 2+1 lattice averages put the quarter-turn value just below the measured window, so the quarter turn fits only within the lattice spread and the firm content is |cos phi| < 1/2. Free numbers at this order: one phase for one observable. Whether the quark sectors carry one-type stages at all is open (the lepton sector needs a lopsided one under Premise (H)). Transport-absent.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the Fritzsch-Xing formula (with Gatto-Sartori-Tonin and Fritzsch 1978) and the FLAG 2024 ratios now cite imported Facts (uses edges added, claimrefs in the formal statement and the proof); the pin to synthesis.series-family-structures-give-no-lopsided-second-stage moved to its version 2 (a pointer note added there). No clause changed.'
---

## formal
Suppose the quark Dirac mass matrices carry the textures of Lemma \claimref{neutrino.breaking-relation} at the $S_{3} \to S_{2}$ direction with one-type second stages, $M_{q} = c_{q}\bigl(\J + \delta_{q}(E + X_{q})\bigr)$, $q = u, d$, each $X_{q}$ odd under $P_{12}$ and symmetric, antisymmetric or Hermitian with any complex coefficient, as Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule} takes for the leptons. Work at that order, where each sector's light states are the left singular vectors of $B_{q} = \bigl[\begin{smallmatrix} 2/3 & x_{q} \\ y_{q} & 0 \end{smallmatrix}\bigr]$ and $|x_{q}| = |y_{q}|$ (ibid.\ (i); Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}(iii)). Let $x = m_{d}/m_{s}$, $y = m_{u}/m_{c}$, and let $\phi$ be the relative phase of the off-diagonal entries of $B_{u}B_{u}^{\dagger}$ and $B_{d}B_{d}^{\dagger}$, which no rephasing of the families or of either sector's right-handed fields changes.
\begin{enumerate}
\item[(i)] \emph{(The Gatto-Sartori-Tonin relation and the Cabibbo element.)} In each sector $\tan^{2}\theta_{q} = m_{1q}/m_{2q}$: this is the stored relation $\sigma_{2}/\sigma_{1} = \tan^{2}\theta$ for $|x| = |y|$ (Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}(ii), and Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}(iv) for complex stages), read in the quark sectors, where it is the relation of Gatto, Sartori and Tonin \cite{GST1968} for the nearest-neighbour texture of Fritzsch \cite{Fritzsch1978} (Fact \claimref{synthesis.imported-fritzsch-texture-cabibbo-formula}). With it
\[
|V_{us}|^{2} = \frac{x + y - 2\cos\phi\,\sqrt{xy}}{(1 + x)(1 + y)} ,
\]
the heavy-quark-limit formula of the Fritzsch texture (Fritzsch and Xing, 1999, who also find $\phi$ near $90^{\circ}$; Fact \claimref{synthesis.imported-fritzsch-texture-cabibbo-formula}); the formula and that phase are standard and transport-absent, and what is new here is that the store's one-type light-plane block is that texture. Real stages, in particular every real texture of the form the store uses for the leptons, have $\cos\phi = \pm1$. A lopsided block, $|y_{q}| \ne |x_{q}|$, does not obey the first relation.
\item[(ii)] \emph{(Excluded phases.)} If $m_{s}/m_{d} \in [18, 22]$ and $m_{c}/m_{u} \in [440, 580]$, then $\cos\phi = 1, \tfrac12, -\tfrac12, -1$ give $|V_{us}| < 0.196$, $< 0.2163$, $> 0.2301$, $> 0.247$, all outside $W = (0.22176, 0.22705)$, the join of three standard deviations of the stored global-fit and direct values.
\item[(iii)] \emph{(The selected phase.)} Every point of the windows with $|V_{us}| \in W$ has $\cos\phi \in (-0.42, 0.36)$, so $|\cos\phi| < \tfrac12$: the up-down phase is within $30^{\circ}$ of a quarter turn. The quarter turn lies inside that range: under the same windows $\cos\phi = 0$ gives $|V_{us}| \in (0.2111, 0.2350) \supset W$; at the central ratios of the $N_{f} = 2+1+1$ lattice averages (Fact \claimref{synthesis.imported-flag-2024-light-quark-mass-ratios}), $m_{s}/m_{d} = 19.94$, $m_{c}/m_{u} = 505$, it gives $|V_{us}| \in (0.22256, 0.22257)$, inside $W$, and at those of the $N_{f} = 2+1$ averages, $20.36$ and $496.2$, it gives $(0.22054, 0.22055)$, just below $W$.
\end{enumerate}
So, under this hypothesis, the families paper's Cabibbo pass (Proposition \claimref{families.faces-ordered-what-identification-requires-first}(2), $\tan\theta_{d} = \sqrt{m_{d}/m_{s}}$) is realised at the breaking lemma's order only with a non-real up-down relative phase within $30^{\circ}$ of a quarter turn: the up-sector angle enters in quadrature and the down-sector angle alone gives $\sin\theta_{d} \approx 0.2185$ at the central ratios. Among the five phases with rational cosine that a finite symmetry supplies, only the quarter turn is compatible, and only within the spread of the lattice averages; $\phi$ is one free number selected by one observable and $|V_{us}|$ is not predicted. The phase comes from couplings independent of each other in the two sectors' second stages (for the $\su(2)_{R}$-covariant completion, the frame coefficients and the two family matrices $Y$, $\tilde{Y}$ of Theorem \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}), and nothing stored fixes it. The one-type hypothesis is what family-symmetric couplings supply: second stages built from the $10$s, among them that completion's $Y$ and $\tilde{Y}$, have $y_{s} = x_{s}$ in every sector (\claimref{synthesis.complex-neutrino-stages-keep-the-solar-sum-rule}, clause (v), where the same stages fail the solar angle under Premise (H)). Real one-type quark stages give no Cabibbo angle, which with Proposition \claimref{synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns} leaves the quark second stage two requirements: $S_{2}$-odd entries, and a relative phase between up and down within $30^{\circ}$ of a quarter turn.

## technical
Under the hypothesis of a one-type $S_{2}$-odd second stage in each quark sector, at the $S_{3} \to S_{2}$ direction, the light-plane block has $|x| = |y|$, its light state makes the angle $\theta$ with $\tan^{2}\theta = m_{\mathrm{light}}/m_{\mathrm{heavy}}$ (the stored light-plane relation, which in the quark sectors is the Gatto-Sartori-Tonin relation for the Fritzsch texture), and the Cabibbo element is $|V_{us}|^{2} = (x + y - 2\cos\phi\sqrt{xy})/((1 + x)(1 + y))$ with $x = m_{d}/m_{s}$, $y = m_{u}/m_{c}$ and $\phi$ the physical relative phase of the two sectors' stages. With the lattice ratios ($m_{s}/m_{d} \in [18, 22]$, $m_{c}/m_{u} \in [440, 580]$) real stages give $|V_{us}| < 0.196$ or $> 0.247$, and $\cos\phi = \pm\tfrac12$ give $< 0.2163$ or $> 0.2301$, all outside the measured window $(0.22176, 0.22705)$; the data need $|\cos\phi| < \tfrac12$, an up-down phase within $30^{\circ}$ of a quarter turn; the quarter turn itself gives $(0.2111, 0.2350)$ over the windows, $0.22257$ at the $N_{f} = 2+1+1$ central ratios and $0.22055$, just below the window, at the $N_{f} = 2+1$ ones. The store's real textures therefore give no Cabibbo angle. The phase is one free number fixed by one observable, not a prediction, and nothing stored fixes it; the formula and a phase near $90^{\circ}$ are standard results of the Fritzsch-texture literature. Certified rational arithmetic and exact Gaussian-rational instances.

## lay
A well-known pattern from the 1960s and 1970s says that the angle describing how the down and strange quarks mix is roughly the square root of the ratio of their masses. In this framework, the same mathematical block that governs the lightest two families of leptons, if it also governs the quarks, reproduces that pattern exactly. But the up-type quarks contribute too, and how their contribution combines depends on a relative phase between the up and down sectors. Using current lattice values of the quark mass ratios, the measured mixing is reached only if that phase is within about thirty degrees of a quarter turn; with no phase, as in the real mass patterns the framework has written down so far, the result is clearly wrong. The phase is a free number that the measurement selects, so this is not a prediction; of five simple phases a symmetry could provide, only the quarter turn is compatible, and only within the spread between lattice calculations.

## one-liner
If the quark sectors carry one-type $S_{2}$-odd second stages at the $S_{3} \to S_{2}$ direction, each light plane obeys $\tan^{2}\theta = m_{1}/m_{2}$ and $|V_{us}|^{2} = (x + y - 2\cos\phi\sqrt{xy})/((1 + x)(1 + y))$; with $m_{s}/m_{d} \in [18, 22]$ and $m_{c}/m_{u} \in [440, 580]$ real stages ($\cos\phi = \pm1$) and $\cos\phi = \pm\tfrac12$ miss the measured $|V_{us}|$, the data need $|\cos\phi| < \tfrac12$ (the quarter turn inside it); the phase is selected from the data (one free number for one observable), not a prediction of $|V_{us}|$.
