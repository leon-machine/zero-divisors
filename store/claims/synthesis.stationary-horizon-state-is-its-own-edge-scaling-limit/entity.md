---
id: synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit
kind: claim
version: 5
title: 'A stationary horizon state is its own edge scaling limit'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, modular-theory, car-algebra, forcing-and-uniqueness, no-go, needs-continuum]
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
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: the carrier content of (i) to (iii) split out into synthesis.stationary-generator-states-and-the-edge-scaling, which the proof now cites
  version: 4
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: 'maintainer pass, restated clauses marked with their premise-free home at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.stationary-generator-states-and-the-edge-scaling@1
  - hawking.i-state-continuum@5
  - hawking.imported-quasi-free-kms-reduces-two@2
  - synthesis.positive-null-energy-gives-r-premises@8
  - singularity.why-calibration-cannot-be-internal@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_boost_is_the_car_scaling_about_the_edge
- kind: check
  ref: check.py::check_kernels_homogeneous_and_differ_only_at_the_edge_scale
- kind: check
  ref: check.py::check_off_the_edge_every_member_is_locally_the_vacuum
- kind: check
  ref: check.py::check_null_energy_of_the_family
- kind: check
  ref: check.py::check_cross_edge_block
- kind: check
  ref: check.py::check_zero_null_energy_does_not_select_the_vacuum
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.positive-null-energy-gives-r-premises
  - singularity.why-calibration-cannot-be-internal
  - angle.imported-theorems-deliver-their-hypotheses
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item E11 (routine; no retirement): clauses (i) to (iii) restate synthesis.stationary-generator-states-and-the-edge-scaling (i) to (iii) after the 7 November split; a marked Restatement sentence in the formal names the premise-free home so counts take each once (the uses edge already exists). The store has no clause-level restates link, so the build''s restatement count is unchanged; the marking is in the text.'
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4, at Leon''s decision of 7 November 2026 (third cut, option (b)): the carrier content of (i) to (iii) (the weight-1/2 boost is the scaling about the edge; a stationary state is its own scaling limit there, so locally the null vacuum at the edge means the null vacuum; the half-thermal products are locally the vacuum off the edge and not at it), which uses no premise, is now the separate result synthesis.stationary-generator-states-and-the-edge-scaling, its (i) to (iii); the proofs of (i) to (iii) cite it, and this result keeps the identification of each horizon''s flow with the boost (through synthesis.positive-null-energy-gives-r-premises, pin moved from 4 to 6, statement unchanged there) and the reading of (ii) as (N+). Statement unchanged; no assumes edge added or removed; the four checks of (i) to (iii) are kept and also record the new premise. Units already I_4 throughout (rulings R2, R4); nothing to change.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the continuum mode space is written as the field unit I_4: the two-point kernels (prefactor and boundary value I_4 0), the Mellin modes, the complex shifts y -> y - 2 pi I_4 c and zeros 2 pi I_4 c k of the kernels in span{1, I_4}, and the null energy density T_uu = (I_4/2)(...); nothing stays.'
  open_problem: op.r-premises-external
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Citation fix: the dilation u -> e^{kappa t} u is the boost beta_t of the setup of synthesis.positive-null-energy-gives-r-premises, not its item (iii) (the KMS restatements); the formal setup and proof (i) now cite the setup. Content unchanged. Version 1 -> 2.'
  note: >-
    The second alternative of the open problem, "show what form any such principle must take", answered
    within the stationary quasi-free class. On every horizon in the scope of (N+) the boost acts on a
    generator as the dilation u -> e^{kappa t} u about the edge with the weight 1/2 that preserves the
    anticommutator, which is the scaling map of a chiral field of scaling dimension 1/2. So a stationary state
    is its own scaling limit at the edge, and the local form of (N+) imposed at the edge alone (the scaling
    limit there is the null vacuum) is equivalent to (N+) on the whole generator. Conversely the edge cannot be
    avoided: the stationary product states thermal on each half at any rapidity period 2 pi c (c in (0, infinity],
    c = infinity the boost ground state), and at c = 1 the product of the two half I-states, are locally the null
    vacuum at every point off the edge, and their kernels differ from the vacuum's by a function homogeneous of
    degree -1 that is analytic off the edge and unbounded at it. Vanishing renormalised null energy does not
    rescue an off-edge principle: a stationary mixture of symbols has zero null energy everywhere and is not the
    vacuum. This is the null-line form of the Kay-Wald uniqueness argument and of the Fredenhagen-Haag
    scaling-limit condition (both cited from memory; Kay-Wald is in the store's imported Fact), proved here on
    the series' continuum carrier. It is transport-absent, and it sharpens the stored remark that (N+) relocates
    the import to regularity across the bifurcation surface: within the stationary class that regularity is the
    whole of it, and on the eternal hole the bifurcation surface lies beyond the Painleve-Gullstrand chart.
    Literature from memory: B. S. Kay and R. M. Wald, Phys. Rep. 207 (1991) 49; K. Fredenhagen and R. Haag,
    Commun. Math. Phys. 127 (1990) 273; the thermal two-point function of a chiral fermion and the
    Boulware-type negative energy -kappa^2/(48 pi) of one complex chiral fermion.
  flags:
  - 'beyond one flat chart: the bifurcation surface of the eternal hole and of de Sitter space, where the equivalence of (ii) is posed, is not carried by the Painleve-Gullstrand or static chart; the half-generators off it are'
---

## formal
Units $\hbar = c = 1$. Let $\mathcal{H}$ be a horizon in the scope of Premise \claimref{synthesis.n-plus-null-ground-state}, with the affine parameter $u \in \R$ on each generator, $u = 0$ on the edge (bifurcation) surface, and the continuum mode space $\CAR(L^{2}(\R, du)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, $\{\psi(u), \psi^{*}(v)\} = \delta(u - v)\otimes\id_{K}$. The boost acts as $\beta_{t}(\psi(u)) = e^{\kappa t/2}\psi(e^{\kappa t}u)$ (the boost $\beta_{t}$ of the setup of Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}, for the Killing flows of the eternal hole and of de Sitter space and the local boost of Minkowski space). Write $W_{\omega}(u, v) = \omega(\psi^{*}(v)\psi(u))$, and $\omega_{0}$ for the gauge-invariant quasi-free state with $W_{0}(u, v) = \tfrac{I_{4}}{2\pi}(u - v + I_{4}0)^{-1}\otimes\id_{K}$ (numbers are read in $\mathrm{span}\{1, I_{4}\}$, $I_{4}$ the unit of the mode space), the state that (N$_{+}$) selects (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i)). For a point $u_{0}$ of a generator and $\lambda > 0$ let $\sigma^{u_{0}}_{\lambda}(\psi(u_{0} + x)) = \lambda^{1/2}\psi(u_{0} + \lambda x)$; the \emph{scaling limit} of $\omega$ at $u_{0}$ is the gauge-invariant quasi-free state with two-point function $\lim_{\lambda \to 0^{+}}\lambda\,W_{\omega}(u_{0} + \lambda x, u_{0} + \lambda y)$ (as distributions), when the limit exists. Read the local form of (N$_{+}$) at $u_{0}$ as: the scaling limit at $u_{0}$ exists and is $\omega_{0}$ (\emph{locally the null vacuum at $u_{0}$}). Call $\omega$ stationary if $\omega\circ\beta_{t} = \omega$ for all $t$.
\begin{enumerate}
\item[(i)] \emph{(The boost is the scaling about the edge.)} (Theorem \claimref{synthesis.stationary-generator-states-and-the-edge-scaling}(i).) $\beta_{t} = \sigma^{0}_{e^{\kappa t}}$. Among the weights $\lambda^{p}$, only $p = \tfrac12$ makes $\sigma_{\lambda}$ preserve the anticommutator. In $\Cl(1,3)$ (store signature) the rotor $B = \cosh\tfrac{\lambda}{2} + \sinh\tfrac{\lambda}{2}\,e_{1}e_{0}$ sends $\ell = e_{0} + e_{1}$ to $e^{\lambda}\ell$, $n = e_{0} - e_{1}$ to $e^{-\lambda}n$ and fixes $e_{2}, e_{3}$: on the null plane $\{u\ell + y\}$ it dilates every generator about its own edge point. (The same weight-$\tfrac12$ dilation, with its Mellin and rotor factorisations, is the subject of the result filed alongside, synthesis.boost-evolution-on-generators-is-one-unitary-group, in fuller form; here only the identification with the scaling map is used.)
\item[(ii)] \emph{(Stationarity plus the edge is (N$_{+}$).)} (Theorem \claimref{synthesis.stationary-generator-states-and-the-edge-scaling}(ii).) A stationary gauge-invariant quasi-free $\omega$ is its own scaling limit at the edge. Hence $\omega$ is locally the null vacuum at the edge if and only if $\omega = \omega_{0}$, that is, if and only if $\omega$ satisfies (N$_{+}$). The same holds with the weaker condition that $W_{\omega} - W_{0}$ be a bounded function on some neighbourhood of $(0, 0)$ (in each $K$-component): a function homogeneous of degree $-1$ and bounded near the origin vanishes.
\item[(iii)] \emph{(Off the edge every stationary thermal state is locally the vacuum.)} (Theorem \claimref{synthesis.stationary-generator-states-and-the-edge-scaling}(iii).) For $c \in (0, \infty]$ let $\omega_{c}^{\times}$ be the product, over the two halves $u > 0$ and $u < 0$, of the quasi-free states KMS at rapidity period $2\pi c$ for the boost future-directed on each half ($c = \infty$: the ground state of that boost). Each is stationary, even and gauge-invariant quasi-free. On $u, v > 0$, with $y = \ln(u/v)$,
\[
W_{c}(u, v) = \frac{I_{4}}{2\pi}\,\frac{(uv)^{-1/2}}{2c\,\sinh\!\big((y + I_{4}0)/2c\big)}, \qquad \text{Mellin symbol } (1 + e^{-2\pi c w})^{-1} \text{ on } u^{-1/2 + I_{4}w},
\]
the I-state of Theorem \claimref{hawking.i-state-continuum} at period $2\pi c$ (the mirror image on $u, v < 0$), $W_{1} = W_{0}$ there. The difference $D_{c} = W_{c} - W_{0}$ is $\tfrac{I_{4}}{2\pi}(uv)^{-1/2}g_{c}(y)$ with $g_{c}$ analytic for $|\mathrm{Im}\,y| < 2\pi\min(c, 1)$, $g_{c}(y) = -\tfrac{1}{24}(c^{-2} - 1)\,y + O(y^{3})$. So every $\omega_{c}^{\times}$ is locally the null vacuum at every point $u_{0} \neq 0$ of every generator. The scaling limit at $u_{0} \neq 0$ involves only the block of the two-point function on the half containing $u_{0}$, so the same holds for every stationary gauge-invariant quasi-free state whose restrictions to the two halves are those of $\omega_{c}^{\times}$, whatever its cross-edge block; for $c \neq 1$ none of these is $\omega_{0}$, since its half restrictions differ from those of $\omega_{0}$. The cross-edge block of $\omega_{c}^{\times}$ vanishes while that of $\omega_{0}$ is $\tfrac{I_{4}}{2\pi}(u - v)^{-1}$; so $\omega_{c}^{\times} \neq \omega_{0}$ for every $c$, including $c = 1$, where both halves are the I-state at $2\pi$. For $c \neq 1$ the difference on each half, and for every $c$ the cross-edge difference, is homogeneous of degree $-1$, nonzero and unbounded on every neighbourhood of the edge.
\item[(iv)] \emph{(The null energy.)} The point-split renormalised null energy of $\omega_{c}^{\times}$ is $\langle T_{uu}\rangle = (c^{-2} - 1)/(48\pi u^{2})$ per component, so the Killing-frame density $\kappa^{2}u^{2}\langle T_{uu}\rangle = \kappa^{2}(c^{-2} - 1)/(48\pi)$ is constant along the generator ($-\kappa^{2}/(48\pi)$ for the boost ground state), while the affine-frame density diverges at the edge for $c \neq 1$. Zero null energy does not select $\omega_{0}$ among stationary states: the quasi-free state with symbol $\tfrac14 m_{1/2} + \tfrac34 m_{\infty}$ on each half ($m_{c}$ the symbol above) is stationary, locally the null vacuum off the edge, has $\langle T_{uu}\rangle = 0$ everywhere, and differs from $\omega_{0}$ (its $y^{3}$ coefficient of $g$ is $\tfrac{21}{5760}$).
\item[(v)] \emph{(What form a principle must take.)} By (ii) and (iii), within the stationary gauge-invariant quasi-free class, (N$_{+}$) is equivalent to one temperature-free local condition at the edge, and no condition on the scaling limits at points off the edge, with stationarity, implies it, nor implies (R) on a half-generator (the family $\omega_{c}^{\times}$ restricted to $u > 0$ meets every such condition at every period); by (iv) neither does the further condition of vanishing null energy. On the eternal hole the half-generators $u > 0$ are on the Painlev\'e-Gullstrand chart of the store and the edge is not, so a principle stated at the points of that chart, with stationarity, through the scaling limits or the null energy, cannot supply (N$_{+}$) or (R): it must be posed at the bifurcation surface (on the manifold assembled from several charts), or fix the whole Mellin symbol on the chart, which is (R) itself. On a local Rindler horizon of Minkowski space the edge is an ordinary point of the flat chart, and for a boost-invariant state (N$_{+}$) is the local form of (N$_{+}$) at that one point.
\end{enumerate}
\emph{Beyond one flat chart.} The bifurcation surface of the eternal hole (case (a)) and of de Sitter space (case (b)), where (ii) is posed, is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the half-generators of (iii) to (v) are.

\emph{Restatement.} Clauses (i) to (iii) restate clauses (i) to (iii) of Theorem \claimref{synthesis.stationary-generator-states-and-the-edge-scaling}, which assumes no premise and is their home in the store; they are kept here in the scope of (N$_{+}$) and counted once, at the home.

## technical
The store's premise (N$_{+}$) says that the modes on a horizon's light rays are in the ground state for sliding along the rays, and records that this relocates the thermal input to regularity across the bifurcation surface. This result makes that relocation exact within the stationary class. On every horizon in the premise's scope the boost acts on a light ray as a rescaling of its affine parameter about the edge, with exactly the weight that preserves the anticommutator, so the boost is the scaling map that defines a state's short-distance limit at the edge. A state invariant under the boost is therefore its own short-distance limit there: if it looks like the null vacuum at short distances at the edge, it is the null vacuum everywhere, and (N$_{+}$) holds. Boundedness of the difference from the vacuum near the edge is already enough, because the difference is homogeneous of degree $-1$.

The converse shows that the edge cannot be avoided. The stationary states that are thermal on each half of the ray at any period, including zero temperature (the boost's ground state) and the correct period with no correlation across the edge, all look like the null vacuum at short distances at every point except the edge: their kernels differ from the vacuum's by a smooth function that blows up only there. Their renormalised null energy is $(c^{-2} - 1)/(48\pi u^{2})$, constant in the Killing frame. Requiring zero null energy does not help, since a mixture of two such states has zero null energy and is not the vacuum. So any principle with no temperature in it that delivers (N$_{+}$) must speak about the state at the bifurcation surface, or fix the whole spectral symbol, which is the thermal premise again. On the eternal hole the bifurcation surface lies off the Painlev\'e-Gullstrand chart that carries the store's gravitational field, while on local Rindler horizons of Minkowski space it is an ordinary point. This is the null-line form of the Kay-Wald uniqueness argument and of the Fredenhagen-Haag short-distance condition, proved on the series' continuum carrier; the transport principle plays no part.

## lay
The series assumes that the quantum modes along a horizon's light rays are in their lowest-energy state for sliding along the rays, and from that it gets the horizon's temperature. This result asks where that assumption really bites. A black hole in equilibrium does not change in time, and on the horizon's light rays "not changing in time" turns out to mean "looking the same at every magnification about the point where the two halves of the horizon meet". So if the state looks like empty space at very short distances at that one meeting point, it looks like empty space everywhere along the ray, and the assumption holds. At every other point of the ray, a state at the wrong temperature, or at zero temperature, also looks like empty space at short distances; only the meeting point tells them apart. So any deeper principle that would explain the black-hole temperature must say something about that meeting point, which lies outside the single map of spacetime the series uses for the black hole.

## one-liner
On every horizon in the scope of (N$_{+}$) the boost is the anticommutator-preserving scaling of a generator about its edge, so a stationary quasi-free state is its own short-distance limit there and satisfies (N$_{+}$) exactly when it is locally the null vacuum at the edge; the stationary states thermal on each half at any period (and at the right period with no cross-edge correlation) are locally the null vacuum at every other point, and zero null energy does not select the vacuum either, so within the stationary class the content of (N$_{+}$) is one temperature-free condition at the bifurcation surface, which on the eternal hole lies off the Painlev\'e-Gullstrand chart.
