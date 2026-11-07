---
id: synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
kind: claim
version: 6
title: 'The rung field''s D-term action and tree masses on the lift locus'
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, frozen-point, gauge-fields, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
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
- name: Claude Opus 5.5
  role: 'GA rewrite (the weak generators as slot bilinears)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'notation: the Hermitian norm renamed sans-serif N'
  version: 6
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-on-the-lift-locus@4
  - synthesis.rung-unit-is-frame-boost@3
  assumes:
  - synthesis.rung-unit-second-free-number@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_invariants_moment_maps_and_orbit_space
- kind: check
  ref: check.py::check_d_term_vacuum_and_tree_masses
- kind: check
  ref: check.py::check_added_invariant_shifts_masses
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-on-the-lift-locus
  - synthesis.rung-unit-second-free-number
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R04 item 4): the rung-field results wrote N for the Hermitian norm of the rung component, N(c) = (|alpha|^2 + |beta|^2)/2, while N = M_P/H is the hierarchy number in the same subject, and this entity names it in its units remark (the H of N = M_P/H), which keeps N. The norm is now \mathsf{N} (its values \mathsf{N}^*, \mathsf{N}_0, its derivative \partial_{\mathsf{N}}, and W(\mathsf{N})) in formal, proof and the other levels, in every rung-field entity that writes it (14 entities, one batch), so the family stays uniform. The letter was chosen free in the entity and in its subject (standard-model and quantum-fields): R04''s example \mathcal{N} is the store macro \Ncone (the null cone) and the number operator of synthesis.floor-regulator-... in quantum-fields. No content change.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. The weak generators, written as Pauli matrices on the coefficient doublet (T_j = (I_4/2) sigma_j, Y = (I_4/2) 1), are now Clifford elements in the slot generators E_ab = v_a w_b: T_1 = (I_4/2)(E_45 + E_54), T_2 = (1/2)(E_45 - E_54), T_3 = (I_4/2)(E_44 - E_55), Y = (I_4/2)(E_44 + E_55), as reader R04 proposed; the matrices on alpha stay as a labelled reading. Verified exactly with lib/GA.py in Cl(2,2) (v_a w_b + w_b v_a = delta_ab, [E_ab, v_c] = delta_bc v_a, [E_ab, w_c] = -delta_ac w_b) and by the matrix identities (I_4/2) sigma_j = the stated combinations of matrix units. The proof''s moment maps and Fierz identity stay in the coefficient reading.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit on the complexified rung summand is written as I_4, which commutes with the rung vectors (C read as span{1, I_4}): the generators T_j and Y, the moment maps G(c, -I_4 T_a c) and G(c, -I_4 Y c), K = -2 I_4 Y and the components of T_1 c_lambda in the proof; nothing stays.'
  maintainer_pass_qft:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, by Leon''s decision of 2026-11-01: a marked note at the end of the formal level recording the rung field as the elementary palatial linear field with two hypercharge-1/2 doublets, the null-lift constraint read as the limit k_10 -> infinity of that field (synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum). The statement and the tree masses on the locus are unchanged; no edge added (that result uses this one).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 (Leon''s register decision of 2026-11-01): the reading in clause (2), the lay text and the one-liner no longer say that the premise registers the frame as v/H, a law; a marked note says that under the promotion the level xi G, and so v/M_P, is the law and v/H initial data (synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion), as synthesis.rung-unit-second-free-number version 3 now states, and the assumes edge is repinned to that version. The proof''s Fayet-Iliopoulos mention now cites the imported Fact. a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)). The clauses are unchanged.'
  open_problem: op.rung-unit
  note: >-
    The problem's first line of attack: an action for the rung field whose hypercharge D-term fixes
    the moment-map level, and whether that level can be anything but an input. On the null-lift locus
    the U(2)-invariants are the Hermitian norm N and the hypercharge moment map m (the bilinear norm is
    fixed there), the orbit space is the region N^2 - m^2 >= H^4 and its boundary is the stored lift
    family, so an invariant potential conserves electromagnetism exactly when its minimum lies on the
    boundary. The D-term action (the stored Hermitian kinetic term plus one half the sum of the squared
    gauge-coupled moment maps, the hypercharge one shifted by a constant) has its minimum on the
    boundary automatically, at the level m* = g'^2 xi/(g^2 + g'^2): the frame is fixed by xi and by
    nothing in the stored structure, which is the registered premise in dynamical form (xi is odd under
    the conjugation c -> c*, so a conjugation-even D-term puts the vacuum at the balanced frame). Its
    tree masses are exact: the neutral mode has m_h = M_Z and the charged pair M_W, in every frame, the
    mechanism of the tree-level bound of the supersymmetric two-doublet sector; here the constraint to
    the locus leaves one neutral mode, so no mixing angle appears. Measured against m_h = 125.2 GeV and
    M_Z = 91.19 GeV (PDG, from memory) the pure D-term potential is excluded at tree level, so the
    series' rung potential needs a further invariant, which on the locus can only be a function W(N),
    or quantum corrections of the kind that lift the supersymmetric bound. With W: along the family the
    neutral mass is M_Z^2 + 2 W'' m*^2/N* + 2 W' H^4/N*^2 (for v >> H, M_Z^2 + v^2 W'' up to 10^-176, so
    the measured masses need W'' about 0.12), the charged pair M_W^2 + 2 W'(N*), which is twice the
    outward N-derivative of the potential at the boundary: the vacuum is stable against charge breaking
    exactly when the charged mass squared is positive. Transport-convenient: the locus, the family and
    the frame are the series' (the lift of the frozen point); the D-term and the Hessians are standard
    gauge theory. Literature from memory: the first fundamental theorem for U(n) invariants, the
    Fayet-Iliopoulos term, the tree-level Higgs mass bound of the two-doublet supersymmetric model, and
    the PDG values. Numerical work (the value of W'') is in the proof text only.
---

## formal
In the setting of Theorem \claimref{synthesis.rung-field-on-the-lift-locus}: the complexified rung summand $\mathcal{R}_{\C}$ with $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$, $Q(c) = \alpha^{\mathsf T}\beta$, $\mathsf{N}(c) = \tfrac12(|\alpha|^{2} + |\beta|^{2})$, $G(c, d) = \operatorname{Re}(c^{*}\cdot d)$, the slot mixing $U(2)$ acting by $\alpha \mapsto X\alpha$, $\beta \mapsto \bar{X}\beta$ with generators $T_{1} = \tfrac{I_{4}}{2}(E_{45} + E_{54})$, $T_{2} = \tfrac12(E_{45} - E_{54})$, $T_{3} = \tfrac{I_{4}}{2}(E_{44} - E_{55})$ and $Y = \tfrac{I_{4}}{2}(E_{44} + E_{55})$, in the slot generators $E_{ab} = v_{a}w_{b}$ of Theorem \claimref{synthesis.rung-unit-is-frame-boost}, which act by commutator as the matrix unit on the $\alpha$-coefficients and as minus its transpose on the $\beta$-coefficients (on $\alpha$, the matrices $\tfrac{I_{4}}{2}\sigma_{j}$ and $\tfrac{I_{4}}{2}\mathbf{1}$, a labelled reading in which the proof computes the moment maps; the unit on $\mathcal{R}_{\C}$ and its coefficients is the field theory's unit $I_{4}$, which commutes with the rung vectors; $\C = \mathrm{span}\{1, I_{4}\}$), the hypercharge moment map $m(c) = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, $H^{2} = \Lambda/3$, the null-lift locus $L = \{Q(c) = -H^{2}\}$ and the lift family $c_{\lambda}$ with $\eta = \log(\lambda/H)$. Let $\mu_{a}(c) = G(c, -I_{4}T_{a}c)$ for $a = 1, 2, 3$ and $\mu_{Y}(c) = G(c, -I_{4}Yc)$ be the moment maps of the gauge generators for the Hermitian form, and let $g$, $g'$ be the couplings of Theorem \claimref{synthesis.rung-field-on-the-lift-locus}(2). The \emph{D-term action} of the rung field on $L$ is $S = \int \operatorname{Re}((Dc)^{*}\cdot Dc) - V_{D}(c)$ with $V_{D} = \tfrac12\bigl(g^{2}\sum_{j}\mu_{j}^{2} + g'^{2}(\mu_{Y} - \zeta)^{2}\bigr)$, $\xi := 2\zeta$ the level.
\begin{enumerate}
\item \emph{(Invariants and orbit space.)} The $U(2)$-invariant polynomials on $\mathcal{R}_{\C}$ are generated by $|\alpha|^{2}$, $|\beta|^{2}$, $Q$ and $\bar{Q}$; $\mu_{Y} = \tfrac12 m$ and $\sum_{j}\mu_{j}^{2} = \tfrac14(\mathsf{N}^{2} - |Q|^{2})$. On $L$ every invariant function is a function of $(\mathsf{N}, m)$, the orbit space is $\{\mathsf{N}^{2} - m^{2} \ge H^{4}\}$, and its boundary $\mathsf{N}^{2} - m^{2} = H^{4}$ is exactly the set of charge-preserving orbits, the $U(2)$-images of the lift family, on which $\mu_{1} = \mu_{2} = 0$ and $\mu_{3} = \mu_{Y} = \tfrac12 m$. Hence an invariant potential on $L$ conserves electromagnetism if and only if its minimum over the orbit space lies on the boundary, and a potential depending on $\mathsf{N}$ alone leaves the frame undetermined (its minimum set is a curve $\mathsf{N} = \mathsf{N}_{0}$ through charge-breaking points when $\mathsf{N}_{0} > H^{2}$): the frame is fixed only through $m$. The conjugation $c \mapsto c^{*}$ keeps $\mathsf{N}$ and $|Q|$ and reverses $m$, so it sends the level $\xi$ to $-\xi$.
\item \emph{(The D-term vacuum.)} On $L$, $V_{D} = \tfrac12\bigl(\tfrac{g^{2}}{4}(\mathsf{N}^{2} - H^{4}) + g'^{2}(\tfrac{m}{2} - \zeta)^{2}\bigr)$, increasing in $\mathsf{N}$ at fixed $m$, so its minimum over the orbit space lies on the boundary, at $m^{*} = g'^{2}\xi/(g^{2} + g'^{2})$, and is one charge-preserving orbit: the vacuum frame is $\sinh 2\eta^{*} = -m^{*}/H^{2}$ with $\mathsf{N}^{*} = \sqrt{m^{*2} + H^{4}}$, so for $|\xi| \gg H^{2}$ the weak scale $\mathsf{N}^{*} \approx g'^{2}|\xi|/(g^{2} + g'^{2})$ and $v/H$ are set by the level $\xi$, a constant of the action that nothing in the stored structure fixes (reading: this is the premise \claimref{synthesis.rung-unit-second-free-number} in dynamical form, the level being the constant of the laws it registers; \emph{note (register, 2026-11-01)}: under the Henneaux-Teitelboim promotion, with $\xi$ a constant of the action, the laws fix $\xi G$, and so $v/M_{P}$ up to relative order $(H/v)^{4}$, while $v/H$ is initial data (\claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}); this reading earlier said that the premise registers the frame as $v/H$, a law, which the action read under the promotion does not support). A D-term even under $c \mapsto c^{*}$ has $\xi = 0$ and its vacuum at the balanced frame $\mathsf{N}^{*} = H^{2}$.
\item \emph{(Tree masses of the D-term action.)} With the stored kinetic term the gauge masses are $M_{W}^{2} = \tfrac12 g^{2}\mathsf{N}^{*}$ and $M_{Z}^{2} = \tfrac12(g^{2} + g'^{2})\mathsf{N}^{*}$. The Hessian of $V_{D}$ restricted to $L$ at the vacuum, divided by the kinetic coefficient of the stored Hermitian term, gives the neutral mode (the rung unit $dc_{\lambda}/d\lambda$) the mass $m_{h}^{2} = M_{Z}^{2}$ and each of the two charged modes the mass $M_{W}^{2}$, in every frame: the rung field is not a one-doublet Higgs field (six real directions on $L$, three eaten), and it predicts a physical charged scalar pair, degenerate with the $W$ in the pure D-term theory. Against the measured $m_{h}$ and $M_{Z}$ the pure D-term potential is excluded at tree level, so the rung potential needs a further invariant, on $L$ a function $W(\mathsf{N})$, or quantum corrections.
\item \emph{(An added invariant.)} For $V = V_{D} + W(\mathsf{N})$ the vacuum on the family satisfies $\tfrac{g^{2}}{4}m + \tfrac{g'^{2}}{4}(m - \xi) + W'(\mathsf{N})\tfrac{m}{\mathsf{N}} = 0$, and there
\[
m_{h}^{2} = M_{Z}^{2} + 2W''(\mathsf{N}^{*})\frac{m^{*2}}{\mathsf{N}^{*}} + 2W'(\mathsf{N}^{*})\frac{H^{4}}{\mathsf{N}^{*2}}, \qquad m_{\pm}^{2} = M_{W}^{2} + 2W'(\mathsf{N}^{*}) = 2\Bigl(\frac{g^{2}}{4}\mathsf{N}^{*} + W'(\mathsf{N}^{*})\Bigr),
\]
the charged mass squared being twice the outward $\mathsf{N}$-derivative of $V$ at the boundary: the family point is a local minimum of $V$ on $L$, locally stable against charge breaking, exactly when $m_{\pm}^{2} > 0$ (and $m_{h}^{2} > 0$); whether it is the global minimum depends on $W$ away from the boundary and is not decided here. The charged pair's mass measures $W'(\mathsf{N}^{*})$, which charged-scalar searches constrain. For $v \gg H$, $m_{h}^{2} = M_{Z}^{2} + 2\mathsf{N}^{*}W''(\mathsf{N}^{*})$ up to a relative $H^{4}/\mathsf{N}^{*2}$.
\end{enumerate}

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). The order $10^{-176}$ of $H^{4}/\mathsf{N}^{*2}$ at the weak scale holds for either.

\emph{Note (the elementary rung field, 2026-11-01).} The rung field is recorded as the elementary palatial linear field: an elementary quantum field with a polynomial potential takes values in all eight real components of the complexified rung summand, two complex doublets of hypercharge $\tfrac12$, not on the locus (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}). The null-lift constraint used here, $Q = -H^{2}$ or the cone $Q = 0$, is read as a limit of that field: with the term $k_{10}|Q + H^{2}|^{2}$ the constrained field is the limit $k_{10} \to \infty$, at fixed $m_{h}$ and $m_{\pm}$. The tree masses above survive in the linear field, which adds a neutral normal pair, the two directions that change $Q$, of mass squared $2W' + 4\mathsf{N}^{*}(k_{10} \pm r)$ in the notation there.

## technical
The rung field lives on the null-lift locus, a six-dimensional real surface in the complexified rung plane, three of whose directions are gauge. Its gauge-invariant functions there depend only on two numbers, the Hermitian norm and the hypercharge moment map, which range over a region whose boundary is the family of charge-preserving vacua found earlier. A potential conserves electric charge exactly when its minimum sits on that boundary. The simplest gauge-covariant potential, the D-term built from the gauge moment maps with a constant shift in the hypercharge one, sits there automatically and puts the vacuum at a frame fixed by the shift, so the weak scale is that shift: an input, as the registered premise says, and odd under the rung conjugation. Its tree spectrum is rigid: the neutral rung mode weighs exactly the Z boson and the charged modes exactly the W, in every frame, which the measured Higgs mass rules out. Any further invariant is a function of the norm alone; it raises the neutral mass by the norm times its second derivative and the charged mass by twice its first derivative, and that charged mass squared is also the slope of the potential out of the charge-preserving boundary, so a positive charged mass is the same thing as a vacuum that is locally stable against charge breaking. The field has a physical charged scalar pair besides the neutral mode: it is not a one-doublet Higgs field.

## lay
The series' candidate for the Higgs field is a component of the frozen point's lift, constrained to a surface where the lift stays null. This result writes down the simplest field theory for it: the standard kinetic term and the D-term potential, whose strength is fixed by the gauge couplings as in supersymmetric theories, with one free constant. That theory automatically keeps electric charge unbroken and sets the weak scale by the free constant, so the weak scale is an input here, matching the series' premise that registers that constant as a free number (with the cosmological constant read as a fact about the universe's history, as the series does, it is the weak scale against the Planck mass that the constant fixes). But the theory also predicts that the Higgs particle weighs exactly as much as the Z boson, which is false by about a third, so a second term in the potential is needed; the result says what such a term can be and how it moves the Higgs mass. The field is not the single Higgs doublet of the Standard Model: it also carries a pair of charged scalars, as heavy as the W boson in the simplest theory, which searches for charged scalars constrain (the bound, from memory, is near that mass).

## one-liner
On the null-lift locus the rung field's invariant potentials are functions of $(\mathsf{N}, m)$ on $\mathsf{N}^{2} - m^{2} \ge H^{4}$ with the lift family as boundary; the hypercharge D-term action has a charge-preserving vacuum at the level $m^{*} = g'^{2}\xi/(g^{2} + g'^{2})$, so $v/H$ is set by the input $\xi$ (the premise registering the level as the free number; under the promotion $\xi G$, and so $v/M_{P}$, is the law and $v/H$ initial data), with $m_{h} = M_{Z}$ and $m_{\pm} = M_{W}$ at tree level in every frame; an added $W(\mathsf{N})$ gives $m_{h}^{2} = M_{Z}^{2} + 2W''m^{*2}/\mathsf{N}^{*} + 2W'H^{4}/\mathsf{N}^{*2}$ and $m_{\pm}^{2} = M_{W}^{2} + 2W'$, twice the outward derivative, so local stability against charge breaking is the positivity of the charged mass, and the field carries a physical charged pair.
