---
id: synthesis.rung-field-on-the-lift-locus
kind: claim
version: 3
title: 'The rung field on the null-lift locus'
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, frozen-point, gauge-fields, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
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
  - standard-model.imported-tower-commuting-copies-fock-module@5
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - standard-model.transported-frozen-point@5
  - synthesis.rung-unit-is-frame-boost@3
  - synthesis.rung-unit-transverse-to-norm@3
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_setting
- kind: check
  ref: check.py::check_charge_preserving_locus
- kind: check
  ref: check.py::check_two_readings_of_gauge_masses
- kind: check
  ref: check.py::check_rung_unit_is_the_neutral_mode
- kind: check
  ref: check.py::check_rung_unit_is_imaginary_hypercharge
- kind: check
  ref: check.py::check_product_law_and_mirror
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.what-derived-what-not
  - synthesis.rung-unit-second-free-number
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the complexified rung summand and of its coefficients (the u(2) generators T_j = (I_4/2) sigma_j, Y = (I_4/2) 1, K = -2 I_4 Y, the stabiliser generator diag(0, I_4) and the gauge directions in the proof) is written as I_4, which commutes with the rung vectors; C is read as span{1, I_4} and R_C = R + I_4 R; nothing stays.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)). Nothing else is changed.'
  open_problem: op.rung-unit
  note: Bears on the Lagrangian half of the open problem without fixing the number. It writes the rung component as a field on the complexified rung summand, constrained to the locus L on which the frozen point's lift is null, and finds its field content and the readings of its scale; no potential is derived and v/H is not fixed. Clauses (1) and (5) are transport-essential (L is the null-lift condition of transport); clauses (2) to (4) are the Higgs-mechanism algebra of a doublet and its conjugate transposed to the tower's U(2), conjugation and tractor form, so transport-convenient. Clauses (1) to (4) use only the tower's structures and the lift; clause (5)'s tree-mass reading uses the one-vev corollary, which holds under Hypothesis (S). Imported from memory, not as store entities, and used only in the reading of the proof - the name of the Kempf-Ness theorem (G. Kempf and L. Ness, Lecture Notes in Math. 732, 1979; the convexity used is proved directly), the identification of the quadratic form of a kinetic term in the gauge fields as the gauge-boson mass matrix (S. Weinberg, The Quantum Theory of Fields II, 1996, section 21.1), and record values of the top and bottom masses and of the Hubble rate. Suggested decision for Leon (not a store change) - the product law of clause (5), read through c, puts the stored tree Yukawa reading and the reading of v/H as a frame of the frozen point's null lift in tension (see the proof's reading); clause (5) states what holds when the up-type entries are read through c* instead, where the law does not apply. Which kinetic term is physical in clause (2) depends on the Hermitian structure, which is open; the clause states both readings.
---

## formal
Let $\mathcal{R}_{\C} = (H_{4} \oplus H_{5}) \otimes \C$, with $\C = \mathrm{span}\{1, I_{4}\}$ (the unit is the field theory's unit $I_{4}$, which commutes with the rung vectors, so $\mathcal{R}_{\C} = \mathcal{R} \oplus I_{4}\mathcal{R}$), be the complexified rung summand of Theorem \claimref{synthesis.rung-unit-is-frame-boost}, with mode vectors $v_{a}, w_{a}$ ($a = 4, 5$) of Fact \claimref{standard-model.imported-tower-commuting-copies-fock-module}, and write $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$ with $\alpha, \beta \in \C^{2}$. The complex-bilinear extension of the quadratic form is $Q(c) = \alpha^{\mathsf T}\beta$, and the Hermitian norm of the tower's conjugation is $N(c) = c^{*}\cdot c = \tfrac12(|\alpha|^{2} + |\beta|^{2})$. Let $X \in U(2)$, the slot mixing of Proposition \claimref{standard-model.ten-transported-ambient-space-doublets-are}, act by $\alpha \mapsto X\alpha$, $\beta \mapsto \bar{X}\beta$, with generators $T_{j} = \tfrac{I_{4}}{2}\sigma_{j}$ and hypercharge $Y = \tfrac{I_{4}}{2}\mathbf{1}$; let $K = -2I_{4}Y$, so $Kv_{a} = v_{a}$ and $Kw_{a} = -w_{a}$, and let $m(c) = \operatorname{Re}(c^{*}\cdot Kc) = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, the hypercharge moment map. Let $\Lambda > 0$, $H^{2} = \Lambda/3$, let $L = \{c \in \mathcal{R}_{\C} : Q(c) = -\Lambda/3\}$, the rung components $c$ for which $I + c$ is null with $I$ the frozen point, and let $c_{\lambda} = -\lambda w_{4} + \tfrac{\Lambda}{3\lambda}v_{4}$, $\lambda > 0$, be the rung component of the lift of $I$ in the frame $\lambda$ (Theorem \claimref{synthesis.rung-unit-transverse-to-norm}, Proposition \claimref{standard-model.transported-frozen-point}(i) at $\lambda = 1$); write $\eta = \log(\lambda/H)$.
\begin{enumerate}
\item \emph{(The charge-preserving locus is the lift family.)} The stabiliser in $U(2)$ of $c \in L$ is trivial unless $\beta \in \C\bar{\alpha}$, and is then a circle. The points of $L$ with a circle stabiliser are exactly the $U(2)$-images of the $c_{\lambda}$, $\lambda > 0$; on them $|\beta| = \lambda$ and $|\alpha| = H^{2}/\lambda$, so $\lambda$ is a $U(2)$-invariant and $|\alpha||\beta| = \Lambda/3$. At $c_{\lambda}$ the unbroken generator is $Y - T_{3}$.
\item \emph{(Two readings of the gauge-boson masses.)} For gauge fields $(W^{j}, B)$ acting through $gT_{j}$ and $g'Y$, the quadratic forms in the gauge fields at $c_{\lambda}$ of the Hermitian kinetic term $\operatorname{Re}((Dc)^{*}\cdot Dc)$ and of the bilinear kinetic term $Q(Dc, Dc)$ are $\tfrac14 N(c_{\lambda})P$ and $\tfrac14 Q(c_{\lambda})P$, with $P = \operatorname{diag}(g^{2}, g^{2}) \oplus \bigl(\begin{smallmatrix} g^{2} & gg' \\ gg' & g'^{2}\end{smallmatrix}\bigr)$, of eigenvalues $g^{2}, g^{2}, g^{2} + g'^{2}, 0$. The Hermitian reading has the electroweak pattern (one massless combination, $M_{Z}^{2}/M_{W}^{2} = (g^{2} + g'^{2})/g^{2}$) with scale $N(c_{\lambda}) = H^{2}\cosh 2\eta$; the bilinear reading has the same pattern with scale $-\Lambda/3$ in every frame.
\item \emph{(The rung unit is the neutral physical mode.)} The tangent space of $L$ at $c_{\lambda}$, of real dimension $6$, is the sum of the tangent space of the gauge orbit, of dimension $3$, and its orthogonal complement in it for $\operatorname{Re}(x^{*}\cdot y)$, of dimension $3$, on which the unbroken generator acts with charges $0, +1, -1$: the neutral line is spanned by $dc_{\lambda}/d\lambda$, and the charged plane is its orthogonal complement. Along the family $Q(dc_{\lambda}/d\eta) = \Lambda/3$ and $N(dc_{\lambda}/d\eta) = N(c_{\lambda})$.
\item \emph{(The rung unit is the imaginary hypercharge, fixed by the moment map.)} $e^{tK}c_{\lambda} = c_{\lambda e^{-t}}$, so the rung-unit boost $B_{s}$ on the plane $H_{4}$ is $e^{(\log s)K}$, the complexified hypercharge. Along every orbit $N(e^{tK}c) = \tfrac12(e^{2t}|\alpha|^{2} + e^{-2t}|\beta|^{2})$, whose $t$-derivative is $2m(e^{tK}c)$; for $\alpha, \beta \ne 0$ it is strictly convex in $t$ and minimal exactly where $m = 0$. On the family $m(c_{\lambda}) = -H^{2}\sinh 2\eta$ and $N(c_{\lambda}) = H^{2}\cosh 2\eta$, so the frame is fixed by the value of $m$, and the balanced frame $\lambda = H$ is the zero of the hypercharge moment map.
\item \emph{(Product law, and the conjugation as mirror.)} For every $c$ with $\beta \in \C\bar{\alpha}$, $|Q(c)| = |\alpha||\beta|$ and $N(c)^{2} = |Q(c)|^{2} + m(c)^{2}$; for every other $c$, $N(c)^{2} > |Q(c)|^{2} + m(c)^{2}$. \emph{Reading through $c$:} by Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern}, the tree Dirac entries of the mass form of $c_{\lambda}$ itself are $H^{2}/\lambda$ on the up-type and neutrino pairs and $\lambda$ on the down-type and charged-lepton pairs: their product is $\Lambda/3$ in every frame and their ratio is $e^{2\eta}$. \emph{Reading through $c^{*}$:} if the up-type and neutrino entries are read from the mass form of $c_{\lambda}^{*} = \bar{\beta}\cdot v + \bar{\alpha}\cdot w$ and the down-type and charged-lepton entries from that of $c_{\lambda}$, the product law does not apply: both entries equal $\lambda$, their ratio is one in every frame, and their product is $\lambda^{2} = |\beta|^{2} = N(c_{\lambda}) - m(c_{\lambda}) = H^{2}e^{2\eta}$, a Hermitian quantity that the tractor norm does not fix. The conjugation $c \mapsto c^{*}$ preserves $L$, $N$ and $Q$, reverses $m$, and sends $c_{\lambda}$ to $-c_{H^{2}/\lambda}$, so it acts on the charge-preserving orbits as $\eta \mapsto -\eta$.
\end{enumerate}

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). The order $10^{-42}$ GeV of $H$ quoted in the proof holds for either.

## technical
Write the rung component as a field with values in the complexified rung summand, a doublet $\alpha$ of hypercharge $+\tfrac12$ (the creation coefficients) and a conjugate doublet $\beta$ of hypercharge $-\tfrac12$ (the annihilation coefficients), and keep the one condition transport imposes: the frozen point's lift is null, so the field lies on $L$, where the complex bilinear invariant $\alpha^{\mathsf T}\beta$ is fixed at $-\Lambda/3$. On $L$ electromagnetism survives exactly on the frozen point's lift family and its gauge images; there the two doublet lengths are $H^{2}/\lambda$ and $\lambda$, with product $\Lambda/3$ whatever the frame. Of the field's six real directions along $L$ three are gauge, one is neutral and two form a charged pair: the neutral one is the rung unit, so the radial Higgs mode of this field is the frame boost, not the tractor norm, which is frozen. The gauge-boson masses read the Hermitian norm $H^{2}\cosh 2\eta$ in the electroweak pattern, while a bilinear kinetic term would give the same pattern at the scale $\Lambda/3$ in every frame. The frame boost is the hypercharge rotation at imaginary angle; the Hermitian norm is convex along it, and its slope is the hypercharge moment map, which vanishes exactly at the balanced frame. On charge-preserving vectors the Hermitian norm, the tractor norm and the moment map satisfy $N^{2} = |Q|^{2} + m^{2}$, and through the stored tree mass relations read through $c$ the up-type and down-type entries of the lift multiply to $\Lambda/3$ in every frame; if the up-type entries are read through the conjugate $c^{*}$ instead, as the Standard Model reads the conjugate doublet, the two entries are equal and their product is the Hermitian quantity $H^{2}e^{2\eta}$. The conjugation exchanges the frames $\lambda$ and $H^{2}/\lambda$.

## lay
In the series the Higgs field sits in the extra directions that transport adds, and transport fixes one combination of its two halves, through the cosmological constant. Treating it as a field under that condition, the only direction in which it can change physically without breaking electromagnetism is the scale the earlier work called the rung unit, so the Higgs boson of this field is a ripple of that scale. The masses of the W and Z bosons come out in the right pattern if they are read with the quantum-mechanical (Hermitian) norm, which sees the scale; the geometric norm would give them a cosmologically small mass whatever the scale. Changing the scale is the hypercharge symmetry turned through an imaginary angle, and the scale is measured by a quantity that vanishes only at the frame matched to the cosmological scale. One consequence is sharp: if the quark masses come from this field through the series' single coupling and the up-type masses are read from the field itself rather than its conjugate, the up-type and down-type masses at tree level multiply to the coupling squared times the cosmological scale squared, whatever the scale chosen, which the observed top and bottom masses rule out; so one of those two readings has to go. Read through the conjugate, the up-type and down-type masses are equal and both grow with the scale.

## one-liner
On the locus where the frozen point's lift is null, the rung field preserves electromagnetism exactly on the lift family, whose neutral mode is the rung unit; the gauge masses read, in the Hermitian reading, $H^{2}\cosh 2\eta$ (the bilinear form gives $-\Lambda/3$), the rung unit is the imaginary hypercharge fixed by the moment map $-H^{2}\sinh 2\eta$, and the two doublet lengths multiply to $\Lambda/3$ in every frame, so tree masses read through $c$ alone have up-down product $\Lambda/3$ times the coupling squared, while through $c^{*}$ for the up type the product is $H^{2}e^{2\eta}$.
