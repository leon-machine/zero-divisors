---
id: synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue
kind: claim
version: 2
title: In the homogeneous diagonal Kasner class an aligned Maxwell field and a perfect fluid at rest are potentials on the logarithmic scales; the Maxwell field is a wall on the hyperplane of the curvature wall of its axis and reflects the weights by the BKL law, a fluid with w < 1 is subleading, and among these sources only stiff matter moves the residue off the unit boosts
status: proved
region: synthesis
subject: interior
tags: [kasner, curvature-and-field-equations, no-go]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@1
  - synthesis.kasner-curvature-wall-is-negative-weight-helicity@1
  - synthesis.bkl-bounces-no-framewise-invariant@2
  - synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall@1
  - synthesis.unit-boost-residue-needs-nonpositive-exponent@3
  - synthesis.imported-maxwell-stress-spacetime-algebra@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_aligned_maxwell_stress
- kind: check
  ref: check.py::check_bianchi_i_ricci
- kind: check
  ref: check.py::check_matter_is_potential
- kind: check
  ref: check.py::check_single_wall_bounce
- kind: check
  ref: check.py::check_activity_and_residue
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall
  - synthesis.kasner-curvature-wall-is-negative-weight-helicity
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'uses edge added to the new Fact synthesis.imported-maxwell-stress-spacetime-algebra@1, which pins the Maxwell stress T(a) = -(1/2) F a F of clause (i), previously cited from memory; the proof now cites it. Version 1 -> 2.'
  open_problem: op.forcing-half-beyond-diagonal
  note: >-
    Answers the matter item of the problem (whether a Maxwell field or a stiff fluid has its wall residue
    completed to a unit boost in a larger Clifford algebra, as the massless scalar's is, or needs wall data with a
    non-unit residue) in the homogeneous diagonal class, by importing the minisuperspace picture of cosmological
    billiards. With the harmonic time (lapse equal to the volume) the field equations of the sources considered (an aligned Maxwell field, a perfect fluid at rest)
    become one Hamiltonian system on the logarithmic scales, with the DeWitt form as kinetic term and the source
    as a potential V. A potential that is a single exponential of a spacelike linear form reflects the velocity in
    the kernel of that form, so the bounce depends only on the wall's hyperplane: the aligned Maxwell field
    (form alpha_1) and the curvature wall of the stored helicity result (form 2 alpha_1) give the same in and out
    epochs, the BKL law, and are active on the same axis (the negative weight). A fluid with p = w rho, w < 1,
    has a timelike form (the volume) and decays relative to the Hubble scale like tau^(1 - w) on the whole
    circle; stiff matter is a constant potential, which moves the velocity off the null cone onto the scalar
    disk with exactly the massless scalar's residue. So the answer is neither alternative for Maxwell: it needs
    no completion and no non-unit wall data, since it is either subleading or a wall of the curvature kind; the
    stiff fluid is the scalar case (its completion is algebraic only: the constant rho_0 has no dynamical slot).
    Not new in substance: the minisuperspace form and the electric and magnetic walls of p-form fields are those
    of Misner and of Damour, Henneaux and Nicolai (2003), the magnetic Bianchi I solutions go back to Jacobs
    (1968), the stress of the Maxwell field in the spacetime algebra, T(a) = -(1/2) F a F, is Hestenes' and
    Doran and Lasenby's, and the subcritical behaviour of fluids with w < 1 is classical (all cited from memory;
    every computation is re-derived and checked here). What the entity adds to the store: the matter item in the
    store's residue language, and the observation that a wall's in/out law depends only on its hyperplane, which
    explains why the Maxwell wall and the helicity wall of the same axis give the same BKL law. Misaligned Maxwell
    fields carry a Poynting component and leave the diagonal class (non-diagonal, not treated). The KK vector of
    the stored five-dimensional reduction is a Maxwell field with a dilaton coupling, whose wall form is shifted
    by the scalar's rate; that case and inhomogeneous matter walls remain open. Transport-absent: a statement
    about the field equations, bearing on the connection's residue.
---

## formal
Let a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) have the derived metric $g = N^{2}dT^{2} - \sum_{l}a_{l}(T)^{2}(dx^{l})^{2}$ with the harmonic lapse $N = a_{1}a_{2}a_{3}$, physical orthonormal frame $e_{0}, e_{1}, e_{2}, e_{3}$ ($e_{0}^{2} = 1$, $e_{l}^{2} = -1$), $B_{l} = e_{0}e_{l}$, logarithmic scales $\alpha_{l} = \log a_{l}$, $S = \sum_{l}\alpha_{l}'$ and $C = \alpha_{1}'\alpha_{2}' + \alpha_{2}'\alpha_{3}' + \alpha_{3}'\alpha_{1}'$. Write $G(x, y) = \sum_{l}x_{l}y_{l} - (\sum_{l}x_{l})(\sum_{l}y_{l})$ for the DeWitt form on velocities, so $C = -\tfrac12 G(\alpha', \alpha')$, and $G^{-1}(\xi, \eta) = \sum_{l}\xi_{l}\eta_{l} - \tfrac12(\sum_{l}\xi_{l})(\sum_{l}\eta_{l})$ for its inverse on linear forms. Matter: (M) a Maxwell field aligned with axis $1$, the bivector $F = (E + IB)\,e_{1}e_{0}$ with $E, B$ functions of $T$ and stress $T(a) = -\tfrac12 FaF$; (P) a perfect fluid at rest in the frame, density $\rho$ and pressure $w\rho$ with $0 \le w \le 1$. The field equations are Einstein's, $\Ric = -8\pi G\,(T - \tfrac12(\operatorname{tr}T)\,g)$ in the store's sign, with Maxwell's equations for (M) and the conservation law for (P).
\begin{enumerate}
\item[(i)] \emph{(These sources are potentials.)} For (M), Maxwell's equations hold exactly when $E\,a_{2}a_{3} = Q_{e}$ and $B\,a_{2}a_{3} = Q_{m}$ are constant; then $T(e_{a})\cdot e_{b} = \mathrm{diag}(\rho, -\rho, \rho, \rho)$ with $\rho = \tfrac12(E^{2} + B^{2})$, trace-free. For (P), conservation is $\rho = \rho_{0}N^{-(1 + w)}$. In both cases, and for the vacuum Bianchi II field of \claimref{synthesis.kasner-curvature-wall-is-negative-weight-helicity}(iv), the field equations are equivalent to
\[
\alpha_{l}'' = -\sum_{m}G^{-1}_{lm}\,\frac{\partial V}{\partial\alpha_{m}}, \qquad C = V,
\]
with $V = 4\pi G\,(Q_{e}^{2} + Q_{m}^{2})\,e^{2\alpha_{1}}$ for (M), $V = 8\pi G\rho_{0}\,e^{(1 - w)(\alpha_{1} + \alpha_{2} + \alpha_{3})}$ for (P), and $V = \tfrac14 e^{4\alpha_{1}}$ for the Bianchi II curvature; the constraint $C = V$ is propagated by the evolution, and for (P) exactly with the exponent $1 + w$.
\item[(ii)] \emph{(A single wall reflects in its hyperplane.)} Let $V = c\,e^{2\omega(\alpha)}$ with $c > 0$ and $\omega$ a linear form with $G^{-1}(\omega, \omega) > 0$. Then every solution tends at $T \to \pm\infty$ to velocities $v_{\pm}$ with $C = 0$, and $v_{-} = R_{\omega}v_{+}$, where $R_{\omega}v = v - 2\,\omega(v)\,\omega^{\sharp}/G^{-1}(\omega, \omega)$ is the $G$-reflection in $\ker\omega$ ($\omega^{\sharp} = G^{-1}(\omega, \cdot)$); $R_{\omega}$ depends on $\omega$ only through $\ker\omega$. For the Maxwell form $\omega = \alpha_{1}$ ($G^{-1}(\omega, \omega) = \tfrac12$) and the curvature form $\omega = 2\alpha_{1}$ the reflections coincide, and with the singularity at $T \to -\infty$ the normalised weights $p = v_{+}/S_{+}$ (with $p_{1} < 0$) and $p' = v_{-}/S_{-}$ are related by the BKL law
\[
p' = \frac{(-p_{1},\ p_{2} + 2p_{1},\ p_{3} + 2p_{1})}{1 + 2p_{1}},
\]
that is $u \mapsto u - 1$, or $u \mapsto 1/(u - 1)$ at the end of an era, as in \claimref{synthesis.bkl-bounces-no-framewise-invariant}.
\item[(iii)] \emph{(Which sources act at a Kasner wall.)} Along an epoch with weights $p$ on the Kasner circle ($\sum p_{l} = \sum p_{l}^{2} = 1$), the source's term in the Hamiltonian constraint relative to the Hubble term is of order $\tau^{2\omega(p)}$ in the proper time $\tau$. The Maxwell field aligned with axis $l$ is of order $\tau^{2p_{l}}$, so on the open Kasner arc it is subleading exactly when $p_{l} > 0$ and active exactly on the axis of the negative weight, where the curvature wall $\tau^{4p_{l}}$ of \claimref{synthesis.kasner-curvature-wall-is-negative-weight-helicity}(ii) is active; after its bounce $p_{1}' > 0$ and the field is subleading for all earlier times. A fluid with $w < 1$ is of order $\tau^{1 - w}$ on the whole circle, and its form (the volume) is $G$-timelike, $G^{-1}(\omega, \omega) = -\tfrac38(1 - w)^{2} < 0$ for $\omega = \tfrac12(1 - w)(\alpha_{1} + \alpha_{2} + \alpha_{3})$, so it never reflects. Stiff matter ($w = 1$) is a constant potential: $C = V$ puts the weights on the disk, $\sum_{l}p_{l}^{2} = 1 - 2V/S^{2}$, and the residue $B_{w} = \sum_{l}p_{l}B_{l}$ has $B_{w}^{2} = 1 - 2V/S^{2} < 1$, the massless scalar's value $1 - 8\pi Gq^{2}$ of \claimref{synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall} under $\rho_{0} = \tfrac12\phi'^{2}$.
\end{enumerate}
So in this class, among these sources, only stiff matter changes the residue of a Kasner wall, and it does so exactly as the massless scalar does. An aligned Maxwell field needs neither a larger Clifford algebra nor non-unit wall data: it is either subleading, leaving the vacuum residue (a unit boost), or a wall on the hyperplane of the curvature wall of the same axis, which reflects the weights by the BKL law instead of supplying a residue.

## technical
The matter half of the forcing problem asks how sources other than a massless scalar sit at a Kasner wall. In the homogeneous diagonal class the question has a uniform answer once the field equations are written in the harmonic time, where the lapse equals the volume. Then the logarithms of the three scale factors move like a particle in a three-dimensional space with the indefinite DeWitt form, and each of the sources treated becomes a potential on that space: the aligned Maxwell field contributes an exponential of the first logarithm, a perfect fluid an exponential of the logarithm of the volume, and the curvature of the Bianchi II slices (the active helicity wall of the stored result) an exponential of twice the first logarithm. A single exponential wall reflects the velocity in its kernel, so the Maxwell wall and the curvature wall of the same axis, whose kernels coincide, produce the same in and out Kasner epochs: the BKL law. Both are active exactly where that axis carries the negative weight. A fluid softer than stiff matter is a decaying, timelike wall that never reflects. Stiff matter is a constant potential, which shifts the Hamiltonian constraint and moves the weights from the Kasner circle onto the disk, giving the same non-unit residue as the massless scalar (a kinetic term, a fifth slot of the DeWitt form, rather than a potential). So among these sources only stiff matter changes the wall residue, and it is the scalar case already completed in $\Cl(1,4)$; the Maxwell field either drops out or is a wall of the curvature kind. The minisuperspace and billiard picture is classical (Misner; Damour, Henneaux and Nicolai 2003, cited from memory); the content specific to the store is the residue reading. Fluids with $w > 1$, misaligned Maxwell fields, the dilaton-coupled vector of the five-dimensional reduction and inhomogeneous walls are not treated. The result concerns the field equations, not transport.

## lay
Near a singularity of the simplest kind, space stretches in some directions and squeezes in others at fixed rates, and these rates are the data the series attaches to the singularity. This result asks what happens when matter is present. In the simplest uniform setting each kind of matter acts like a wall in the space of rates: an electric or magnetic field along one direction is a wall that, when hit, swaps the rates by the same rule as the field strength of the slices, and ordinary fluids fade out before the singularity is reached. Only the stiffest possible matter, which behaves like a massless field, changes the rates themselves, and it does so in the way already described for that field.

## one-liner
In the homogeneous diagonal class, with the lapse equal to the volume, an aligned Maxwell field and a perfect fluid at rest are potentials on the logarithmic scales: an aligned Maxwell field is a wall on the hyperplane of the curvature wall of its axis and reflects the weights by the BKL law, a fluid with $w < 1$ fades out, and among these sources only stiff matter moves the residue onto the disk, exactly as the massless scalar does.
