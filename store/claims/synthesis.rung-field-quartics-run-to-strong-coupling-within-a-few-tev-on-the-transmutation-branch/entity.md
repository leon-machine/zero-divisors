---
id: synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch
kind: claim
version: 3
title: 'On the transmutation branch the rung quartics turn strong within a few TeV'
status: proved
region: synthesis
subject: quantum-fields
tags: [symmetry-breaking, running-and-unification, mass-generation, confronted-with-data, needs-continuum]
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
- citation: 'M. E. Machacek and M. T. Vaughn, Two-loop renormalization group equations in a general quantum field theory (III). Scalar quartic couplings, Nucl. Phys. B 249 (1985), 70--92.'
  key: MachacekVaughn1985
  doi: 10.1016/0550-3213(85)90040-9
- citation: 'M. Luo, H. Wang and Y. Xiao, Two-loop renormalization group equations in general gauge field theories, Phys. Rev. D 67 (2003), 065019; arXiv:hep-ph/0211440.'
  key: LuoWangXiao2003
  doi: 10.1103/PhysRevD.67.065019
- citation: 'H. E. Haber and R. Hempfling, The renormalization-group improved Higgs sector of the minimal supersymmetric model, Phys. Rev. D 48 (1993), 4280--4309.'
  key: HaberHempfling1993
  doi: 10.1103/PhysRevD.48.4280
- citation: 'G. C. Branco, P. M. Ferreira, L. Lavoura, M. N. Rebelo, M. Sher and J. P. Silva, Theory and phenomenology of two-Higgs-doublet models, Phys. Rept. 516 (2012), 1--102; arXiv:1106.0034.'
  key: Branco2012
  doi: 10.1016/j.physrep.2012.02.002
- citation: 'H. Kleinert and V. Schulte-Frohlinde, Critical Properties of phi^4-Theories, World Scientific, Singapore, 2001.'
  key: KleinertSchulteFrohlinde2001
derivations:
- name: main
  uses:
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@3
  - synthesis.rung-field-on-the-lift-locus@2
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@2
  - synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass@1
  - synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count@1
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces@2
  - synthesis.imported-general-quartic-running-and-two-doublet-renormalisation-group-equations@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_rung_field_generators_and_form_from_the_clifford_algebra
- kind: check
  ref: check.py::check_method_reproduces_one_doublet_and_on_coefficients
- kind: check
  ref: check.py::check_one_loop_running_of_the_ten_rung_quartics
- kind: check
  ref: check.py::check_two_loop_pure_quartic_running_on_the_z2_branch
- kind: check
  ref: check.py::check_flat_direction_running_is_the_scalon_sum
- kind: check
  ref: check.py::check_dictionary_to_the_standard_two_doublet_equations
- kind: check
  ref: check.py::check_scalon_trilinear_is_five_thirds
- kind: check
  ref: check.py::check_one_loop_quartics_reach_four_pi_within_a_few_tev
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum
  - synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the coefficient generators (I_4/2) sigma_j and +-(I_4/2), of the real matrix (I_4/2) sigma_2 and of the complex coupling lambda_5 = 4(k_8 - I_4 k_9) is now the field theory''s unit I_4 (numbers read in span{1, I_4}), and the statements i = I_4 name the unit directly; no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2 November 2026: an assumes edge to the Krein premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, which clause (ii) states as the hypothesis of its gauge terms (internal gauge lines in Landau gauge), following the stored running coefficients; a uses edge to the new imported Fact synthesis.imported-general-quartic-running-and-two-doublet-renormalisation-group-equations@1 (Machacek-Vaughn and Luo-Wang-Xiao general formulas; the type-II two-doublet equations), which replaces the citations from memory in the formal level and the proof and is touched by the checks of the two-loop terms and of the dictionary; the B-mixing result is cited by claimref (technical, proof) and by id (note), with no edge. Pin of synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum moved to @3 (dated note recording the transmutation branch as excluded under the coupling reading, with this result as one of its three strikes). Statement unchanged; the branch it studies is now recorded as excluded on that reading.'
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    Answers the attack line on the running of the linear rung field's quartic couplings, their Landau pole and the
    one-loop effective potential beyond the flat direction. Method: the one-loop running is read off the
    renormalisation-group invariance of the one-loop effective potential in Landau gauge (Coleman-Weinberg),
    16 pi^2 beta_V = (1/2)[Tr V''^2 + 3 Tr M_V^4 - 2 Tr (M_F M_F^dag)^2] + phi.gamma.grad V with the scalar
    anomalous dimension gamma = Y2(S) + 3 sum_A g_A^2 t_A t_A; the two-loop pure-quartic part is the general
    formula of Machacek and Vaughn in the form -(1/2) V''_ef V'''_egh V'''_fgh + (1/12)(lam lam)_ab phi_a d_b V
    (general formulas cited from memory; the check tests them against the standard one-doublet beta function and
    the O(N) coefficients (N + 8)/3 and -(3N + 14)/3, also from memory, standard). Applied to the eight real
    components of the rung field with the potential of the stored ten invariants, the stored U(2) action (here
    built as commutators with rung bivectors in Cl(3,5), I4 the unit) and the covariant coupling of the third
    family. Standard: the one-loop two-doublet equations (Haber and Hempfling 1993; Branco et al. 2012, from
    memory) are reproduced term by term under the dictionary lambda1 = 8k1, lambda2 = 8k2, lambda3 = 4k3,
    lambda4 = 4k10, lambda5 = 4(k8 - i k9) (the factors from |beta|^2 = v^2 for canonical real components);
    the relation between the flat-direction running and the scalon mass is Gildener-Weinberg. New: the
    equations for the series' field in its own invariants, with the series' coupling reading, which gives both
    doublets the top coupling (y1 = y2 at the vacuum, so the two doublets run alike from k1 = k2 = 0); the
    two-loop pure-quartic terms in those invariants; the explicit check that the flat-direction running with
    the normal pair is the stored sum; and the strong-coupling scale of the transmutation branch. The gauge coefficients (7, -3, -7) are the stored two-doublet coefficients (21/5, -3, -7) of
    synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces with g' in the non-GUT
    normalisation. See also synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch,
    which excludes the same branch under the same coupling reading by B mixing. The range of
    clause (v) is from a floating-point scan in the proof text (fourth-order Runge-Kutta in floating point, labelled computed); the
    initial gauge and top couplings at m_t are from memory. Transport-convenient: the field, the generators as
    rung bivectors and the coupling reading are the series'; the running is standard field theory.
  flags:
  - 'clause (v) is computed, not proved: the check brackets the one-loop crossing at the two endpoint spectra by an exact-rational Runge-Kutta flow; the full range comes from a floating-point scan in the proof text. The two-loop pure-quartic terms are already 30 to 70 percent of the one-loop terms at the crossing, so the two-loop shift (to 1 to 15 TeV) is not a controlled estimate; it marks strong coupling. The two-loop gauge and Yukawa terms are omitted'
  - 'the general one-loop (effective-potential) and two-loop pure-quartic formulas are cited from memory; the check tests them on the standard one-doublet and O(N) cases'
  - 'the gauge terms (internal gauge lines, Landau gauge) hold under the Krein premise (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields), as the stored one-loop running coefficients do'
  - 'the bottom, charm and lighter couplings are neglected (Y_33 = m_b/v small); with them, couplings odd under alpha -> -alpha (k4 to k7) are generated at order y_t^3 y_b'
  - 'the dictionary to the standard lambda_i assumes the hypercharge-one-half doublet reading of the stored U(2) action, which the generator check confirms'
---

## formal
Let the rung field $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$ of \claimref{synthesis.rung-field-on-the-lift-locus} take values in the complexified rung summand inside $\Cl(3,5)$ (spacetime and the two rung planes), with coefficients in $\mathrm{span}\{1, I_{4}\}$ (the field theory's unit $I_{4}$, numbers read in $\mathrm{span}\{1, I_{4}\}$, \claimref{obj.field-theory.single-algebra-field}), eight real components each with kinetic coefficient one, and the scale-free quartic of \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}(3), $V = k_{1}A^{2} + k_{2}B^{2} + k_{3}AB + A(k_{4}\operatorname{Re}Q + k_{5}\operatorname{Im}Q) + B(k_{6}\operatorname{Re}Q + k_{7}\operatorname{Im}Q) + k_{8}\operatorname{Re}Q^{2} + k_{9}\operatorname{Im}Q^{2} + k_{10}|Q|^{2}$, $A = |\alpha|^{2}$, $B = |\beta|^{2}$, $Q = c^{2} = \alpha^{\mathsf T}\beta$. Gauge couplings $g$, $g'$; third family coupled as in \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix} with $\tilde{Y}_{33} = y$ and $Y_{33}$ neglected. Write $w = 9g^{2} + 3g'^{2}$, $G = \tfrac{9}{32}g^{4} + \tfrac{3}{16}g^{2}g'^{2} + \tfrac{3}{32}g'^{4}$, $s = k_{8}^{2} + k_{9}^{2}$, $t = \ln\mu$.
\begin{enumerate}
\item[(i)] \emph{(The field's symmetries and coupling from the algebra; proved.)} With $b_{a} = v_{a}\wedge w_{a}$, the maps $\tfrac12[I_{4}(v_{4}w_{5} + v_{5}w_{4}), \cdot]$, $\tfrac12[v_{4}w_{5} - v_{5}w_{4}, \cdot]$, $\tfrac12[I_{4}(b_{4} - b_{5}), \cdot]$ and $\tfrac12[I_{4}(b_{4} + b_{5}), \cdot]$ on rung values are the stored $T_{1}$, $T_{2}$, $T_{3}$ and $Y$ (on the coefficients, $\alpha \mapsto \tfrac{I_{4}}{2}\sigma_{j}\alpha$, $\beta \mapsto \overline{\tfrac{I_{4}}{2}\sigma_{j}}\beta$, and $\pm\tfrac{I_{4}}{2}$), and $V$ is invariant. At the third family the covariant coupling is $y\,\epsilon(q, \bar{\beta})u^{c} - y\,(q\cdot\bar{\alpha})d^{c}$ in Weyl fields, invariant under $SU(2) \times U(1)$ with hypercharges $\tfrac16$, $-\tfrac23$, $\tfrac13$: the doublet $\beta$ carries the top mass and the doublet $\alpha$ couples to $(q, d^{c})$ with the same strength. Below, $y_{2}$ is its coefficient on $\bar\beta$ and $y_{1}$ on $\bar\alpha$; the covariant coupling has $y_{1} = y_{2} = m_{t}/v$ at the vacuum.
\item[(ii)] \emph{(One loop; proved, computed exactly; the terms in $g$, $g'$ come from internal gauge lines in Landau gauge and hold under the Krein premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}, as for the stored one-loop running.)} On the branch $k_{4} = k_{5} = k_{6} = k_{7} = 0$, which the running preserves at one and at two loops,
\begin{align*}
16\pi^{2}\dot k_{1} &= 96k_{1}^{2} + 8k_{3}^{2} + 8k_{3}k_{10} + 4k_{10}^{2} + 4s + G - wk_{1} + 24k_{1}y_{1}^{2} - 6y_{1}^{4},\\
16\pi^{2}\dot k_{2} &= 96k_{2}^{2} + 8k_{3}^{2} + 8k_{3}k_{10} + 4k_{10}^{2} + 4s + G - wk_{2} + 24k_{2}y_{2}^{2} - 6y_{2}^{4},\\
16\pi^{2}\dot k_{3} &= 48(k_{1} + k_{2})k_{3} + 16(k_{1} + k_{2})k_{10} + 16k_{3}^{2} + 8k_{10}^{2} + 8s + \tfrac{9}{16}g^{4} - \tfrac38g^{2}g'^{2} + \tfrac{3}{16}g'^{4} - wk_{3} + 12k_{3}(y_{1}^{2} + y_{2}^{2}) - 12y_{1}^{2}y_{2}^{2},\\
16\pi^{2}\dot k_{10} &= 16(k_{1} + k_{2})k_{10} + 32k_{3}k_{10} + 16k_{10}^{2} + 32s + \tfrac34g^{2}g'^{2} - wk_{10} + 12k_{10}(y_{1}^{2} + y_{2}^{2}) + 12y_{1}^{2}y_{2}^{2},\\
16\pi^{2}\dot k_{8,9} &= k_{8,9}\bigl(16(k_{1} + k_{2}) + 32k_{3} + 48k_{10} - w + 12(y_{1}^{2} + y_{2}^{2})\bigr);
\end{align*}
the forms with $k_{4}, \ldots, k_{7}$ are in Step 2. Under $\lambda_{1} = 8k_{1}$, $\lambda_{2} = 8k_{2}$, $\lambda_{3} = 4k_{3}$, $\lambda_{4} = 4k_{10}$, $\lambda_{5} = 4(k_{8} - I_{4}k_{9})$, $y_{b} = \sqrt2y_{1}$, $y_{t} = \sqrt2y_{2}$ these are the standard one-loop equations of the two-doublet model with a discrete symmetry and type-II couplings (Fact \claimref{synthesis.imported-general-quartic-running-and-two-doublet-renormalisation-group-equations}(ii)); under the covariant completion the down-type doublet's coupling is the top's.
\item[(iii)] \emph{(Two loops, pure-quartic part; proved, computed exactly.)} On the same branch,
\begin{align*}
(16\pi^{2})^{2}\dot k_{1}^{(2)} &= -4992k_{1}^{3} - 320k_{1}k_{3}^{2} - 320k_{1}k_{3}k_{10} - 192k_{1}k_{10}^{2} - 224k_{1}s - 128k_{3}^{3} - 192k_{3}^{2}k_{10} - 256k_{3}k_{10}^{2} - 96k_{10}^{3} - 320k_{3}s - 352k_{10}s,\\
(16\pi^{2})^{2}\dot k_{3}^{(2)} &= -(k_{1}^{2} + k_{2}^{2})(960k_{3} + 256k_{10}) - (k_{1} + k_{2})(1152k_{3}^{2} + 512k_{3}k_{10} + 448k_{10}^{2} + 576s) - 192k_{3}^{3} - 64k_{3}^{2}k_{10} - 256k_{3}k_{10}^{2} - 192k_{10}^{3} - 288k_{3}s - 704k_{10}s,\\
(16\pi^{2})^{2}\dot k_{10}^{(2)} &= -448(k_{1}^{2} + k_{2}^{2})k_{10} - 1280(k_{1} + k_{2})k_{3}k_{10} - 640(k_{1} + k_{2})k_{10}^{2} - 768(k_{1} + k_{2})s - 448k_{3}^{2}k_{10} - 448k_{3}k_{10}^{2} - 768k_{3}s - 416k_{10}s,\\
(16\pi^{2})^{2}\dot k_{8,9}^{(2)} &= k_{8,9}\bigl(-448(k_{1}^{2} + k_{2}^{2}) - 1280(k_{1} + k_{2})k_{3} - 1408(k_{1} + k_{2})k_{10} - 448k_{3}^{2} - 1216k_{3}k_{10} - 512k_{10}^{2} + 96s\bigr),
\end{align*}
and $\dot k_{2}^{(2)}$ is $\dot k_{1}^{(2)}$ with $k_{1} \to k_{2}$. The two-loop gauge and Yukawa terms are not computed.
\item[(iv)] \emph{(The flat direction; proved.)} On the stored flat ray ($k_{2} = k_{6} = k_{7} = 0$, vacuum $\alpha = 0$, $|\beta| = v$), with the stored tree masses $M_{W}^{2} = \tfrac14g^{2}v^{2}$, $M_{Z}^{2} = \tfrac14(g^{2} + g'^{2})v^{2}$, $m_{\pm}^{2} = 2k_{3}v^{2}$, $m_{H,A}^{2} = 2v^{2}(k_{3} + k_{10} \pm \sqrt{s})$, $m_{t} = y_{2}v$,
\[
2v^{4}\cdot16\pi^{2}\dot k_{2} = 6M_{W}^{4} + 3M_{Z}^{4} + 2m_{\pm}^{4} + m_{H}^{4} + m_{A}^{4} - 12m_{t}^{4},
\]
so the Gildener-Weinberg scalon mass of \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}(4) is $m_{h}^{2} = 4v^{2}\dot k_{2}$: the scalon sum is the one-loop running of the flat-direction quartic (standard, Fact \claimref{synthesis.imported-coleman-weinberg-gildener-weinberg-scalon-mass}). Along the ray the one-loop potential $B\rho^{4}(\ln(\rho^{2}/v^{2}) - \tfrac12)$ gives $V''(v) = 8Bv^{2} = m_{h}^{2}$ and $V'''(v) = 40Bv = \tfrac53\cdot3m_{h}^{2}/v$ (standard for Gildener-Weinberg potentials).
\item[(v)] \emph{(Strong coupling; computed.)} If the Gildener-Weinberg formula holds and the Majorana and Pati-Salam sectors decouple (the hypotheses of \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}(4)), then starting at $\mu_{0} = m_{t}$ on the scalon-sum surface $2m_{\pm}^{4} + m_{H}^{4} + m_{A}^{4} \in (2\cdot450^{4}, 2\cdot456^{4})$ GeV$^{4}$ with $k_{1}(\mu_{0}) = k_{2}(\mu_{0}) = 0$, the gauge couplings running with the stored two-doublet coefficients of \claimref{synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces}, the largest of $|\lambda_{1}|, \ldots, |\lambda_{5}|$ reaches $4\pi$ between about $0.8$ and $4$ TeV with the one-loop equations, and the one-loop couplings diverge between about $2$ and $11$ TeV; a larger $k_{1}(\mu_{0}) \ge 0$ lowers these scales. At the crossing the two-loop pure-quartic terms of (iii) are already $30$ to $70$ percent of the one-loop terms; adding them moves the crossing to between about $1$ and $15$ TeV, a shift that marks strong coupling rather than a controlled estimate.
\end{enumerate}

## technical
Quantised as an elementary field, the series' rung field is a two-doublet scalar field, and on its scale-free branch the measured Higgs mass fixes the fourth powers of the other scalar masses through the scalon sum, which forces large quartic couplings. This result gives the running of those couplings in the series' own variables. The gauge generators are commutators with bivectors of the two rung planes (with $I_{4}$ as the unit), the quartic is the stored ten-invariant potential, and the top coupling is the series' covariant reading, under which the doublet without a vacuum value couples to the top with full strength, like the other doublet.

The one-loop equations follow from the renormalisation-group invariance of the one-loop effective potential and coincide with the standard two-doublet equations under an explicit dictionary; the two-loop pure-quartic terms follow from the general formula. Both are checked in exact arithmetic against the field's own fourth-derivative tensor. On the flat direction the running of the vanishing quartic reproduces the stored scalon sum with the neutral normal pair, so the stored Higgs mass relation is a statement about running. Integrating the one-loop equations from the top mass on the scalon-sum surface, some quartic reaches $4\pi$ between about $0.8$ and $4$ TeV, where the two-loop terms are already a large fraction of the one-loop ones: the transmutation branch of the elementary rung field is a strongly coupled theory not far above the weak scale. The gauge contributions come from internal gauge lines and hold under the Krein premise, as the stored running coefficients do. With the same coupling reading the branch is also excluded by $B$-meson mixing (\claimref{synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch}).

## lay
The series' Higgs field, read as an elementary quantum field, has eight components and, on the branch where all masses come from quantum effects, must have its extra particles near 400 to 500 GeV. That needs strong self-interactions. This result computes how those interactions change with energy, using the series' own description of the field, and finds that, under the approximations assumed for that branch, they grow too strong for ordinary calculation within a few TeV.

## one-liner
For the scale-free linear rung field (generators as rung bivectors with the unit $I_{4}$, covariant top coupling giving both doublets top strength) the one-loop running of all ten quartics (gauge terms under the Krein premise) is the standard two-doublet system under $\lambda_{1,2} = 8k_{1,2}$, $\lambda_{3} = 4k_{3}$, $\lambda_{4} = 4k_{10}$, $\lambda_{5} = 4(k_{8} - I_{4}k_{9})$, the two-loop pure-quartic part is given exactly, $m_{h}^{2} = 4v^{2}\beta_{k_{2}}$ is the stored scalon sum and the scalon self-coupling is $\tfrac53$ of tree; under Gildener-Weinberg and decoupling the quartics reach $4\pi$ at $0.8$ to $4$ TeV at one loop (computed); the two-loop quartic terms are already 30 to 70 percent of the one-loop terms there, so perturbation theory has failed at that scale.
