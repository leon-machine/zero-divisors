---
id: synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix
kind: claim
version: 3
title: 'The covariant completion of the conjugate reading: a second family matrix'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, mass-generation, two-readings, symmetry-breaking]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-on-the-lift-locus@3
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@4
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.yukawa-pattern-two-rung-module@5
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.hyp-s-slot-statistics@9
  - synthesis.rung-field-level-needed-off-balance-and-not-right-invariant@3
  - synthesis.imported-left-right-bidoublet-two-yukawa-couplings@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mass_entries_of_c_and_its_conjugate_on_the_module
- kind: check
  ref: check.py::check_conjugate_transforms_like_the_field
- kind: check
  ref: check.py::check_sum_rules_in_the_rung_invariants
- kind: check
  ref: check.py::check_lift_family_balanced_frame_and_the_c_share
- kind: check
  ref: check.py::check_coupling_is_su2r_covariant_and_per_sector_reading_is_not
- kind: check
  ref: check.py::check_charged_pair_couples_at_yukawa_strength_under_the_covariant_coupling
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-on-the-lift-locus
  - synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit on the rung field is written as I_4, which commutes with the rung vectors (C read as span{1, I_4}): R_2 = I_4 [b_2, .] in the formal level and R_2, the hypercharge (I_4/2, -I_4/2) and the compensating factor in the proof; nothing stays.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: uses edges to synthesis.rung-field-level-needed-off-balance-and-not-right-invariant@2 (the right-handed su(2) as the commutant of the weak su(2), and the level that sets m*) and to the imported left-right bidoublet Fact @1; clause (i) and the proof now cite both, and the note''s from-memory citation of the bidoublet structure now names the Fact. Content unchanged.'
  open_problem: op.rung-unit
  note: >-
    The problem's fourth line of attack asks for the second family matrix under the c* reading and for a
    check that the top mass does not come from the rung 10 read through c. The stored lift-locus result
    gives the two per-sector readings of one coupling: through c the up-type entry is H^2/lambda and the
    down-type entry lambda, through c* both are lambda; the per-sector reading takes down entries from c and
    up entries from c*, so it sees only the beta half of the rung field. Here the conjugate is treated as a
    field in its own right: its coefficients transform under the slot U(2) as those of c, and under the
    su(2) generated on the rung summand by the bivectors (v_4 v_5 +- w_4 w_5)/2, which commutes with the
    weak su(2), leaves the pairing anti-invariant, commutes with the conjugation and has the hypercharge
    as the commutator of its two generators (the right-handed su(2) of the result synthesis.rung-field-level-needed-off-balance-and-not-right-invariant). So the coupling Y on c plus Yt
    on c*, as wholes, is su(2)_L + su(2)_R covariant, while the per-sector reading is covariant for no
    action on the fermions: it vanishes on the alpha half, which the right-handed generators carry into the
    beta half where it is injective. This two-coupling structure is the standard one of a complex bidoublet
    in left-right models (imported: synthesis.imported-left-right-bidoublet-two-yukawa-couplings; transport-absent); the sum rules below are that structure
    written in the rung field's invariants. For a 10 only the symmetric part of a family matrix couples
    (Yukawa pattern, stored), so physically Y and Yt are complex symmetric; the identities hold for any
    matrices. The mass matrices are M_d = beta Y + conj(alpha) Yt and M_u = alpha Y + conj(beta) Yt. The
    difference of their summed squares is 2 m (|Y|^2 - |Yt|^2) with m the hypercharge moment map, the sum
    2 N (|Y|^2 + |Yt|^2) + 4 Re(Q tr(Y Yt^dag)) with N the Hermitian norm and Q the bilinear form
    (-Lambda/3 on the lift locus). Yt = Y (coupling to the real part c + c*, a real 10) gives m_u = m_d and
    V = 1 exactly in every frame, and agrees with the stored per-sector reading up to relative e^{-2 eta};
    so the second family matrix the stored no-go asks for is the coupling Yt to c*, and with it M_d and M_u
    are -lambda Y and -lambda Yt up to relative corrections e^{-2 eta}. At the balanced frame lambda = H
    (m = 0) M_u = -M_d for every Y, Yt. On the D-term action the vacuum's moment map is m* = g'^2 xi/(g^2 + g'^2),
    set by the level xi (stored; the level's role is synthesis.rung-field-level-needed-off-balance-and-not-right-invariant), so the
    up-down split carries the same c*-odd constant through which the weak scale enters: a vacuum at the
    mirror frame would give m_t = m_b as well as v of order H. The rung 10 read through c cannot carry the
    top: given M_u and M_d at frame eta, the part of M_u from the coupling to c is exactly
    -(r M_d + r^2 M_u)/(1 - r^2), r = e^{-2 eta}, and that coupling's down-type entries are 1/r times its
    up-type ones, so a top entry m_t through c would come with a down-type entry e^{2 eta} m_t (computed
    order of magnitude: e^{2 eta} about 10^{88} for ln(v/H) about 101.9, the registered value with H = H_0;
    using H_0 sqrt(Omega_Lambda) instead changes eta by a quantity of order 0.2; no value of v/H is derived
    or fitted here). The charged pair: at c_lambda the charged plane is alpha' = (0, a), beta' = (0, r conj a)
    (computed: tangent to the locus, orthogonal to the gauge orbit and the neutral line). Under the covariant
    coupling its normalised squared Yukawa weights relative to the vev's are |Yt + rY|^2/|Y - rYt|^2 (down
    type) and |Y + rYt|^2/|Yt - rY|^2 (up type), tending to |Yt|^2/|Y|^2 and |Y|^2/|Yt|^2: with Y about
    M_d/v and Yt about M_u/v the pair couples to the top and bottom with strength of order m_t/v, so searches
    in top decays apply; under the per-sector reading the same weights are r^2 (suppressed by e^{-4 eta}).
    Conventions: r = e^{-2 eta}, the two-doublet tan(beta) of the rung field is e^{2 eta} = 1/r.
---

## formal
Let $c = \alpha\cdot v + \beta\cdot w$ be the complexified rung field of Theorem \claimref{synthesis.rung-field-on-the-lift-locus}, with $N(c) = \tfrac12(|\alpha|^{2} + |\beta|^{2})$, $m(c) = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, $Q(c) = \alpha^{\mathsf T}\beta$, the slot $U(2)$ acting by $\alpha \mapsto X\alpha$, $\beta \mapsto \bar{X}\beta$, and $c^{*} = \bar{\beta}\cdot v + \bar{\alpha}\cdot w$; on a charge-preserving point take the frame in which $\alpha$ and $\beta$ lie along rung $4$ (every such point is a $U(2)$-image of the lift family, loc. cit. (i)) and write $\alpha$, $\beta$ for those components. By Theorem \claimref{standard-model.yukawa-pattern-two-rung-module}, on the sixteen of Proposition \claimref{standard-model.hyp-s-slot-statistics} with the pairing $B$ of Lemma \claimref{standard-model.invariant-pairing-five-modes}, the $w_{4}$ coefficient of a rung vector gives the down-type and charged-lepton entries and the $v_{4}$ coefficient the up-type and Dirac-neutrino entries. For family matrices $Y$, $\tilde{Y}$ (complex symmetric for a $10$; (ii) to (iv) hold for any complex matrices) let the Yukawa coupling be $Y$ on $c$ plus $\tilde{Y}$ on $c^{*}$, as wholes, so that
\[
M_{d} = \beta Y + \bar{\alpha}\tilde{Y}, \qquad M_{u} = \alpha Y + \bar{\beta}\tilde{Y},
\]
and write $H_{q} = M_{q}M_{q}^{\dagger}$, $\|Y\|^{2} = \tr(YY^{\dagger})$, $r = e^{-2\eta}$.
\begin{enumerate}
\item[(i)] \emph{(Covariance.)} The coefficients $(\bar{\beta}, \bar{\alpha})$ of $c^{*}$ transform under $U(2)$ as $(\alpha, \beta)$ do. The bivectors $b_{1} = \tfrac12(v_{4}v_{5} + w_{4}w_{5})$ and $b_{2} = \tfrac12(v_{4}v_{5} - w_{4}w_{5})$ act on rung vectors by commutator; $R_{1} = [b_{1}, \cdot]$ and $R_{2} = I_{4}[b_{2}, \cdot]$ (the unit on the rung field is the field theory's unit $I_{4}$, which commutes with the rung vectors; $\C = \mathrm{span}\{1, I_{4}\}$) commute with the weak $\su(2)$ and with $c \mapsto c^{*}$, $[R_{1}, R_{2}]$ is the hypercharge action, and $B$ is anti-invariant under $b_{1}$, $b_{2}$, so $x \mapsto B(\cdot, x\,\cdot)$ is equivariant. Hence the coupling $Yc + \tilde{Y}c^{*}$ is covariant under the weak $\su(2)$ and this right-handed $\su(2)$ (the commutant of the weak $\su(2)$ of \claimref{synthesis.rung-field-level-needed-off-balance-and-not-right-invariant}(2)), the two-coupling structure of a complex bidoublet in left-right models (Fact \claimref{synthesis.imported-left-right-bidoublet-two-yukawa-couplings}): it is the $\su(2)_{R}$-covariant completion of the per-sector conjugate reading of Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern} (down entries from $c$, up entries from $c^{*}$, one matrix), which vanishes on the $\alpha$ half and so is covariant for no action of $\su(2)_{R}$ on the fermions.
\item[(ii)] \emph{(Sum rules.)} For all $\alpha$, $\beta$, $Y$, $\tilde{Y}$:
$\tr H_{u} - \tr H_{d} = 2m(c)(\|Y\|^{2} - \|\tilde{Y}\|^{2})$ and $\tr H_{u} + \tr H_{d} = 2N(c)(\|Y\|^{2} + \|\tilde{Y}\|^{2}) + 4\operatorname{Re}(Q(c)\tr(Y\tilde{Y}^{\dagger}))$.
\item[(iii)] \emph{(One matrix.)} If $\tilde{Y} = Y$ (the coupling to the real part $c + c^{*}$), then $\bar{z}M_{d} = zM_{u}$ with $z = \beta + \bar{\alpha}$: $m_{u_{i}} = m_{d_{i}}$ and $V = 1$ exactly, in every frame; on the lift family this agrees with the per-sector conjugate reading up to relative corrections $e^{-2\eta}$.
\item[(iv)] \emph{(The lift family.)} On $c_{\lambda}$, $\eta = \log(\lambda/H)$: $M_{d} = -\lambda Y + (H^{2}/\lambda)\tilde{Y}$ and $M_{u} = (H^{2}/\lambda)Y - \lambda\tilde{Y}$. At the balanced frame $\lambda = H$, where $m = 0$, $M_{u} = -M_{d}$ for every $Y$, $\tilde{Y}$. For $\eta \ne 0$ the part of $M_{u}$ carried by the coupling to $c$ is $(H^{2}/\lambda)Y = -(rM_{d} + r^{2}M_{u})/(1 - r^{2})$, and the same coupling's down-type part $-\lambda Y$ is $r^{-1}$ times it.
\item[(v)] \emph{(The charged pair.)} At $c_{\lambda}$ the charged plane is $\alpha' = (0, a)$, $\beta' = (0, r\bar{a})$, $a \in \C$. Under the covariant coupling (one family, scalar couplings $Y$, $\tilde{Y}$) its squared Yukawa weights per unit $N$, relative to those of the vev, are $|\tilde{Y} + rY|^{2}/|Y - r\tilde{Y}|^{2}$ on the down-type pairs and $|Y + r\tilde{Y}|^{2}/|\tilde{Y} - rY|^{2}$ on the up-type pairs, of order one (tending to $|\tilde{Y}|^{2}/|Y|^{2}$ and $|Y|^{2}/|\tilde{Y}|^{2}$); under the per-sector reading both are $r^{2}$.
\end{enumerate}
So the second family matrix that the conjugate reading needs is the coupling $\tilde{Y}$ to $c^{*}$ in its $\su(2)_{R}$-covariant completion: for $\eta \gg 1$, $M_{d} \approx -\lambda Y$ and $M_{u} \approx -\lambda\tilde{Y}$; the up-down split of the summed squares is $2m(c)$ times the difference of the two norms, which at the vacuum of the D-term action of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus} is $2m^{*}$ times it, $m^{*} = g'^{2}\xi/(g^{2} + g'^{2})$ set by the level $\xi$, and it vanishes at the mirror frame for every coupling; the charged pair couples at Yukawa strength; and the rung $10$ read through $c$ does not carry the top mass, since a top entry through $c$ comes with a down-type entry $e^{2\eta}$ times larger.

## technical
The rung field is a complex object, and its conjugate under the tower's conjugation transforms under the weak rotations, the hypercharge and the right-handed rotations of the rung summand exactly as the field does. A mass coupling of the matter sixteen can therefore use the field and its conjugate with two independent family matrices, as the two couplings of a complex bidoublet do in left-right models (standard structure, transport-absent). That pair of couplings is left-right covariant, while the series' reading sector by sector (down-type masses from the field, up-type masses from its conjugate, one matrix) is not: it ignores half of the field, which a right-handed rotation mixes into the other half. The covariant coupling reproduces the sector-by-sector masses up to corrections of relative size the inverse square of the frame boost, but not the couplings of the field's charged pair, which become as large as the quark Yukawa couplings. Reading off the masses, the difference between the summed squared up-type and down-type masses is twice the hypercharge moment map of the rung field times the difference of the two couplings' sizes, and the sum is fixed by the field's norm and its bilinear form. Equal couplings, which amount to coupling the real part of the rung field, give equal up and down masses in every frame. So the independent second family matrix that the up-down split needs is exactly the coupling to the conjugate. At the balanced, mirror-symmetric frame the split vanishes for every choice of couplings; on the D-term action the moment map's vacuum value is set by the D-term level, so the up-down split and the weak scale both depend on the one mirror-odd constant. Any part of the up-type masses carried by the coupling to the field itself is suppressed by the square of the frame boost, and that coupling's down-type entries are larger by the same factor, so the top quark cannot get its mass that way.

## lay
In this framework the field that gives particles their masses comes with a mirror image, and both can talk to the quarks. The series has so far read the masses one sector at a time, which is not left-right symmetric; the left-right symmetric version lets the field and its mirror image each couple with its own strength. If they couple with the same strength, up-type and down-type quarks come out equally heavy, which is wrong; so the heavier up-type quarks (top above all) must come from the mirror image's own, different coupling. The imbalance between the two kinds of quark is then tied to the same quantity that sets the size of the weak scale, and it disappears exactly where that quantity would vanish. The other route, through the field itself, is far too weak to give the top its mass. In the symmetric version the field's electrically charged partner talks to quarks about as strongly as the quarks' own mass couplings, so it can be looked for in top-quark decays.

## one-liner
The $\su(2)_{R}$-covariant completion of the per-sector $c^{*}$ reading couples the sixteen to $c$ with $Y$ and to $c^{*}$ with $\tilde{Y}$ (complex symmetric for a $10$): $M_{d} = \beta Y + \bar{\alpha}\tilde{Y}$, $M_{u} = \alpha Y + \bar{\beta}\tilde{Y}$, matching the per-sector masses up to relative $e^{-2\eta}$; $\tr H_{u} - \tr H_{d} = 2m(c)(\|Y\|^{2} - \|\tilde{Y}\|^{2})$; $\tilde{Y} = Y$ gives $m_{u} = m_{d}$ exactly; the split vanishes at the balanced frame; the share of $M_{u}$ read through $c$ is $-(e^{-2\eta}M_{d} + e^{-4\eta}M_{u})/(1 - e^{-4\eta})$, so the top does not come from it; and the charged pair couples at Yukawa strength.
