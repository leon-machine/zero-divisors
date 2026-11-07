---
id: synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev
kind: claim
version: 5
title: 'Rung-field transmutation needs a charged pair near 450 GeV, now excluded'
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, undetermined-input, gauge-fields, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-weak-scale
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'consistency pass, Lie-algebra name written with its macro'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-on-the-lift-locus@4
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@5
  - synthesis.scale-free-rung-potentials-need-the-flat-physical-branch@2
  - synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass@1
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
- quantity.weak-mixing-angle-mz@1
- quantity.inverse-fine-structure-mz@1
- quantity.fermi-scale@1
checked_by:
- kind: check
  ref: check.py::check_weights_from_the_rung_content
- kind: check
  ref: check.py::check_charged_mass_scales_with_the_norm_on_the_flat_ray
- kind: check
  ref: check.py::check_standard_model_content_alone_gives_negative_mass
- kind: check
  ref: check.py::check_positivity_threshold
- kind: check
  ref: check.py::check_measured_higgs_mass_brackets_the_charged_pair
- kind: check
  ref: check.py::check_diphoton_rate_with_the_charged_pair
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
  - synthesis.rung-field-charged-scalar-sum-rule
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'su(2)_R, written as text with a math subscript, is written with the stored macro, $\su(2)_{R}$, in the formal level and the proof; no mathematics changed.'
  maintainer_pass_qft_full:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 3 -> 4, by Leon''s decision of 2 November 2026 on the weak scale: a dated note at every level records the transmutation branch as excluded under the decided coupling reading (covariant completion, complex symmetric family matrices), collecting the three strikes with numbers and sources (PDG 2026 diphoton average 1.10 +- 0.06 against the bound 0.900, 3.3 standard deviations; tree-level B mixing more than 50 times measured for every splitting; quartics at 4 pi by 0.8 to 4 TeV at one loop) and naming the branch with a level as the working branch. Clauses (i) to (v), their mathematics, status and edges unchanged.'
  maintainer_pass_qft:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, by Leon''s decision of 2026-11-01 recording the rung field as the elementary palatial linear field with two hypercharge-1/2 doublets: a marked note at the end of the formal and technical levels that the Gildener-Weinberg count here was that of the constrained field (the linear field with a massless neutral normal pair), so for the elementary linear field the bracket becomes the upper bound m_pm < 456 GeV and h -> gamma gamma stays below 0.900 for every charged mass in (m_h/2, 456] GeV (synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum). Clauses (i) to (v), as statements about the constrained field, unchanged; no edge added (that result uses this one); the pin of synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus moves to @3 (its marked note, content unchanged).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: uses edges to synthesis.scale-free-rung-potentials-need-the-flat-physical-branch@1 (its clauses (3) and (4), already cited for the flat ray and the charged mass) and to the imported Coleman-Weinberg and Gildener-Weinberg Fact @1, and quantity.fermi-scale@1 under quantities; the formula (GW) and v = 246.22 GeV, earlier cited from memory, now cite the Fact and the quantity. Content unchanged: (GW) and (D) remain the stated hypotheses.'
  open_problem: op.rung-unit
  note: >-
    The one-loop half of the dimensional-transmutation route to the weak scale, under two hypotheses stated
    at every level: the Gildener-Weinberg scalon formula (imported: synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass), and decoupling, namely that the
    only states whose masses depend on the rung field are the Standard Model's and the rung field's charged
    pair. On a Gildener-Weinberg flat direction the tree potential vanishes and the scalon (the rung unit, the
    neutral mode) gets its mass at one loop from the fourth powers of the masses on the flat direction; with
    the Standard Model content the top makes it negative, the known failure of the Coleman-Weinberg Higgs.
    The tree half is synthesis.scale-free-rung-potentials-need-the-flat-physical-branch:
    its clause (3) gives the flat ray on the cone Q = 0 and the charged mass squared (2a - e) v^2, its clause
    (4) excludes the norm-quartic potential. Every mass on the ray scales with N; the fermion masses do so in
    the per-sector reading and in its su(2)_R-covariant completion alike, since on alpha = 0 both c and c*
    have size |beta|. Exact arithmetic with rational brackets: bosons alone 9.7 to 9.9 GeV (the classic
    value); with the top about -(46 GeV)^2; positivity above a threshold in (249, 268) GeV (m_t from 162 to
    173 GeV); the measured Higgs mass needs 450 < m_pm < 456 GeV (454 to 455 at central inputs), and the
    charged quartic 2a - e is between 3.2 and 3.5, about 1.7 in the Standard Model normalisation m_h^2 =
    2 lambda v^2, large, its running not computed here. The pair is closed to top decays and the W = kappa N^2
    point near 117 GeV is not reached. Confrontation with data: the pair does not decouple from h -> gamma
    gamma (coupling 2 m_pm^2/v) and gives 0.898 < mu_gamma_gamma < 0.900 (exact interval arithmetic, one-loop
    amplitudes cited from memory), against the Particle Data Group average signal strength 1.10 +- 0.06 (ATLAS and CMS):
    about three standard deviations low (about 1.5 below the ATLAS full Run 2 value 1.04 +0.10 -0.09). Decoupling is a real restriction on
    the series' content: under the c* reading the neutrino Dirac entries have the up-type size, and with the
    stored v_R = 4.15 x 10^10 GeV heavy Majorana neutrinos with order-one Dirac couplings give a one-loop rung
    mass term of order y^2 M_R^2/(4 pi^2), far above v^2, which lifts the flat direction (the Vissani-type
    bound, F. Vissani, Phys. Rev. D 57 (1998) 7027, from memory: M_R below about 10^7 GeV for order-one
    Dirac couplings); the right-handed gauge bosons at the Pati-Salam scale, which couple to the rung
    bidoublet, do the same at one loop. The weak scale is not derived: the transmutation scale is an input,
    of v/M_P type under the Henneaux-Teitelboim promotion (synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion). Transport-convenient:
    the content (one charged pair, the readings) is the series'; the formulas are standard. Imported:
    E. Gildener and S. Weinberg, Phys. Rev. D 13 (1976) 3333, and S. Coleman and E. Weinberg, Phys. Rev. D 7
    (1973) 1888 (synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass); v = 246.22 GeV from the Fermi
    constant (quantity.fermi-scale). Literature cited from memory: the h -> gamma gamma loop functions (as in
    A. Djouadi, Phys. Rept. 457 (2008) 1); the MS-bar top mass near 162.5 GeV.
---

## formal
Assume (GW) the Gildener-Weinberg one-loop formula (Fact \claimref{synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass}): on a flat direction of a scale-free tree potential, along which every field-dependent mass squared is proportional to $\varphi^{2}$ with $\langle\varphi\rangle = v$, the scalon has
\[
8\pi^{2}v^{2}m_{S}^{2} = 3\sum_{\text{vectors}}M^{4} + \sum_{\text{real scalars}}M^{4} - 4N_{c}\sum_{\text{Dirac fermions}}M^{4};
\]
and assume (D) decoupling: the only states whose masses depend on the rung field are the Standard Model's and the rung field's charged pair (the Majorana and Pati-Salam sectors carry no coupling to the rung field that gives a rung mass term; (D) fails for order-one neutrino Dirac couplings with the stored $v_{R}$, see the proof). Apply (GW) to the rung field on its flat physical branch on the cone $Q = 0$ (the ray $m = -N$ of a scale-free potential with $a + b = e$, $e \ge 0$, $2a \ge e$; \claimref{synthesis.scale-free-rung-potentials-need-the-flat-physical-branch}, clause (3)), with the Hermitian gauge masses of \claimref{synthesis.rung-field-on-the-lift-locus}(2), the charged plane of (3), the fermion entries of (5) (on the physical ray of size $|\beta|$ in the per-sector reading and in its $\su(2)_{R}$-covariant completion alike), and $v^{2} = 2N$.
\begin{enumerate}
\item[(i)] \emph{(Content.)} The gauge mass form has eigenvalues $g^{2}$ twice, $g^{2} + g'^{2}$ once and $0$ once, so the vectors contribute $6M_{W}^{4} + 3M_{Z}^{4}$; the physical scalars are the scalon and the charged pair (two real directions), whose tree mass squared $2(2a - e)N$ is proportional to $N$, as are the gauge and fermion masses; the top contributes $-12m_{t}^{4}$. Hence $8\pi^{2}v^{2}m_{h}^{2} = 6M_{W}^{4} + 3M_{Z}^{4} + 2m_{\pm}^{4} - 12m_{t}^{4} - \ell$, with $\ell = 12m_{b}^{4} + 12m_{c}^{4} + 4m_{\tau}^{4}$.
\item[(ii)] \emph{(Standard Model content.)} Without the charged pair the right side is negative for every $m_{t} \in [162, 173]$ GeV, the range containing the stored pole and $M_{Z}$-scale top masses; at the stored pole mass $m_{h}^{2}$ lies between $-(47\ \mathrm{GeV})^{2}$ and $-(45\ \mathrm{GeV})^{2}$; the vector bosons alone would give $9.7 < m_{h} < 9.9$ GeV.
\item[(iii)] \emph{(Threshold.)} $m_{h}^{2} > 0$ exactly when $2m_{\pm}^{4} > 12m_{t}^{4} + \ell - 6M_{W}^{4} - 3M_{Z}^{4}$; the threshold lies in $(249, 250)$ GeV at $m_{t} = 162$ GeV and in $(267, 268)$ GeV at $m_{t} = 173$ GeV, above $m_{t} - m_{b}$: the charged pair is not produced in top decays.
\item[(iv)] \emph{(The measured Higgs mass.)} With $m_{h} \in [125, 125.4]$ GeV, $v \in [246, 247]$ GeV (containing the tree value from the stored $M_{W}$, $\sin^{2}\theta_{W}(M_{Z})$ and $\alpha(M_{Z})$, and $246.22$ GeV), $m_{t} \in [162, 173]$ GeV and the stored $M_{W}$, $M_{Z}$, $m_{b}$, $m_{c}$, $m_{\tau}$: $450 < m_{\pm} < 456$ GeV, with $454 < m_{\pm} < 455$ GeV at $v = 246.22$ GeV, the stored $m_{h}$ and the stored pole $m_{t}$; the charged quartic is $3.2 < 2a - e = m_{\pm}^{2}/v^{2} < 3.5$.
\item[(v)] \emph{(Diphoton rate.)} On the flat ray the charged pair couples to the scalon with $\partial m_{\pm}^{2}/\partial v = 2m_{\pm}^{2}/v$, so, with the standard one-loop amplitudes (cited from memory), $\mu_{\gamma\gamma} = \bigl((A_{1}(\tau_{W}) + \tfrac43 A_{1/2}(\tau_{t}) + A_{0}(\tau_{\pm}))/(A_{1}(\tau_{W}) + \tfrac43 A_{1/2}(\tau_{t}))\bigr)^{2}$, $\tau_{i} = m_{h}^{2}/4m_{i}^{2}$; with the stored $m_{h}$, $M_{W}$, pole $m_{t}$ and $m_{\pm} \in [450, 456]$ GeV, $0.898 < \mu_{\gamma\gamma} < 0.900$, below the measured signal strength (Particle Data Group average $1.10 \pm 0.06$; ATLAS full Run 2 alone $1.04^{+0.10}_{-0.09}$).
\end{enumerate}

\emph{Note (the elementary rung field, 2026-11-01).} The rung field is recorded as the elementary palatial linear field, with values in all eight real components of the complexified rung summand, two doublets of hypercharge $\tfrac12$ (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}). The count in (i) is that of the field constrained to the cone, the six directions tangent to it; for the linear field it is the case of a massless neutral normal pair. Counted in full, with the normal pair in the scalon sum (the standard two-doublet sum rule), the bracket of (iv) becomes an upper bound, $m_{\pm} < 456$ GeV (below $383$ GeV when the normal pair is the heavier), the normal pair lies below $542$ GeV, and $h \to \gamma\gamma$ stays below $0.900$ of the Standard Model rate for every charged mass in $(m_{h}/2, 456]$ GeV, under the same hypotheses (GW) and (D) (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}). The edge $450 < m_{\pm} < 456$ GeV, a massless normal pair, is excluded by the measured invisible width of the $Z$ (argued there). Clauses (i) to (v) stand as statements about the constrained field.

\emph{Note (the transmutation branch excluded, 2 November 2026).} Under the decided coupling reading of the rung field, the $\su(2)_{R}$-covariant completion $Yc + \tilde{Y}c^{*}$ with complex symmetric family matrices (the rung $10$), the transmutation branch, for the constrained field here and for the elementary linear field (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}), is recorded as excluded, by three independent strikes: (1) $h \to \gamma\gamma$: the bound $\mu_{\gamma\gamma} < 0.900$ lies $3.3$ standard deviations below the Particle Data Group 2026 average $1.10 \pm 0.06$ (pdglive node S126SGG, read on 2 November 2026; inputs ATLAS 2023 $1.04^{+0.10}_{-0.09}$, CMS 2022 $1.13 \pm 0.09$, ATLAS and CMS Run 1 $1.14^{+0.19}_{-0.18}$); (2) $B$-meson mixing: tree-level exchange of the neutral normal pair, below $542$ GeV on this branch, exceeds the measured $B_{s}$ and $B_{d}$ mass differences more than $50$ times for every splitting of its two masses (more than $52$ and $50$), with quark mixing from tree-level determinations and three-family unitarity (\claimref{synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch}); (3) strong coupling: on the scalon-sum surface the quartic couplings reach $4\pi$ between about $0.8$ and $4$ TeV at one loop (\claimref{synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch}). Clauses (i) to (v) and their mathematics are unchanged and stand as statements under (GW) and (D); what is excluded is this branch as the origin of the weak scale under that coupling reading. The branch with a level, on which the second doublet is heavy (about $2.5$ to $3.5$ TeV), is the working branch.
## technical
If the weak scale arises by dimensional transmutation, the tree potential of the rung field is flat along the physical branch and the Higgs mass comes entirely from one loop, from the fourth powers of the masses the vacuum gives to every particle that feels the rung field. This result assumes that those are the Standard Model's particles and the rung field's charged pair only; the series' Majorana and Pati-Salam sectors would otherwise feed the rung field a mass term of their own scale and lift the flat direction. Bosons push the Higgs mass up and fermions down; with the Standard Model's particles the top wins and the mass squared is negative, about $-(46$ GeV$)^{2}$. The rung field's charged pair restores it once heavier than about $250$ to $268$ GeV, and the measured $125$ GeV fixes the pair between $450$ and $456$ GeV, above the top, with a large quartic coupling. The pair does not decouple from the Higgs decay to two photons and lowers that rate to $0.90$ of the Standard Model's, below the measured value. The scale itself is not derived: it is where the physical-branch coupling runs through zero, an input of the same kind as the weak scale against the Planck mass. (Note, 2026-11-01: the rung field is recorded as the elementary linear field with two doublets, for which this count is the edge with a massless neutral pair; counted in full, the charged pair lies below $456$ GeV rather than in the $450$ to $456$ GeV bracket, and the diphoton rate stays below $0.900$ of the Standard Model's for every charged mass between $m_{h}/2$ and $456$ GeV, \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}.) (Note, 2 November 2026: under the series' coupling reading with symmetric family matrices this branch is excluded, by the diphoton rate, whose Particle Data Group 2026 average $1.10 \pm 0.06$ lies $3.3$ standard deviations above the bound $0.900$, by tree-level $B$-meson mixing more than fifty times the measured rate, and by quartic couplings that reach $4\pi$ between about $0.8$ and $4$ TeV; the branch with a level, with the second doublet at a few TeV, is the working branch.)
## lay
One way to explain why the weak scale is so far below the gravitational one is the mechanism that makes the proton's mass: a scale generated by the slow running of a coupling, with no mass put in by hand. For the Higgs this works only if the particles that feel the Higgs field supply the Higgs mass through quantum effects, and in the Standard Model the top quark spoils it. The series' Higgs field carries an extra electrically charged scalar, which rescues the mechanism if it weighs between $450$ and $456$ GeV, provided the series' very heavy neutrino and unification sectors do not talk to the Higgs field, which on the series' present readings they do. The same charged scalar would make the Higgs decay to two photons about ten percent rarer than the Standard Model predicts, while the measurements, as recalled here, lean the other way. The route does not explain the size of the weak scale; it moves the question to where a coupling runs through zero. (Since 2 November 2026 this route is recorded as ruled out under the series' reading of how the Higgs field couples to quarks: the two-photon rate now measured lies well above what it predicts, the extra particles would make bottom mesons turn into their antiparticles far faster than is observed, and the forces among them would grow too strong within a few TeV.)
## one-liner
Under the Gildener-Weinberg formula and with the Majorana and Pati-Salam sectors decoupled from the rung field, its flat branch gives $8\pi^{2}v^{2}m_{h}^{2} = 6M_{W}^{4} + 3M_{Z}^{4} + 2m_{\pm}^{4} - 12m_{t}^{4} - \ell$: negative without the charged pair, positive for $m_{\pm}$ above $249$ to $268$ GeV; the measured $m_{h}$ needs $450 < m_{\pm} < 456$ GeV and gives $\mu_{\gamma\gamma} \approx 0.90$, below the measured rate. (Excluded on 2 November 2026 under the symmetric coupling reading: Particle Data Group 2026 $\mu_{\gamma\gamma} = 1.10 \pm 0.06$, $B$ mixing over $50$ times the measured rate, quartics at $4\pi$ by $0.8$ to $4$ TeV.)
