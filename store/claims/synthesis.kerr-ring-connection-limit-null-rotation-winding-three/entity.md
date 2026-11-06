---
id: synthesis.kerr-ring-connection-limit-null-rotation-winding-three
kind: claim
version: 1
title: At the Kerr ring the weighted limit of the rotation-gauge field is a null rotation about the principal null direction carrying half the normalised field-strength scale, so its values on tangential directions span the duality-complex null-rotation plane and wind three times
status: proved
region: synthesis
subject: interior
tags: [kerr, null-directions, limits, curvature-and-field-equations, needs-continuum]
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
  - interior.imported-kerr-schild-form-kerr-gauge@1
  - interior.unipotency-across-kerr-family@5
  - synthesis.imported-gtg-dictionary@1
  - synthesis.kerr-ring-double-cover-data@3
  - synthesis.kerr-ring-blow-up-forced-cover-fixed-order@3
  - interior.complex-scale-inverse-cube-killing-spinor@5
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - transport.group-null-rotations@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_connection_formula
- kind: check
  ref: check.py::check_frame_components
- kind: check
  ref: check.py::check_forced_normalisation_and_limit
- kind: check
  ref: check.py::check_deck_reverses_limit
- kind: check
  ref: check.py::check_linking_loop_generator
- kind: check
  ref: check.py::check_null_rotation_plane
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.duality-monodromy-fibration-over-ring
  - interior.weighted-limit-theorem
  - note.sheaf.setting-scope-successor-problems
extraction:
  open_problem: op.kerr-ring
  note: >-
    Carries out the first attack of the problem at the level of the connection: the weighted limit on the
    double cover with the forced weights of the stored cometric result. The rotation-gauge field of the Kerr
    gauge field is exactly linear in the potential, which makes the limit explicit. Values level, as in
    the stored weighted limit theorem, plus the transport round small linking loops, which tends to the
    identity; the bundle structure in the sense of T4 and the count are not addressed. The conjecture stays open beyond its data,
    cometric and connection-value levels.
  flags:
  - 'beyond one flat chart: the double cover branched along the Kerr ring'
---

## formal
Let $a \neq 0$ and take the Kerr gauge field $\hb(b) = b + H\,(b \cdot k)\,k$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with $k$ the null field of Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge}, so that $k \cdot k = 0$ and $k \cdot \nabla k = 0$, and $H = M\operatorname{Re}(1/z)$ with $z = r - Ia\cos\theta$, $z^2 = w = x^2 + y^2 + (Z - Ia)^2$, $\rho = |z|$, $\psi = \arg z$ (Theorem \claimref{synthesis.kerr-ring-double-cover-data}); $\R \oplus \R I$ is identified with $\C$ as there. Write $k = e_0 + v$ with $v$ the spatial unit field, $\ell = \tfrac12(e_0 - v)$, and near the ring $e_2 = \hat z \times v / |\hat z \times v|$, $e_1 = v \times e_2$ (cross products of the spatial vectors at $e_0$), the smooth $\eta$-null frame of Theorem \claimref{synthesis.kerr-ring-blow-up-forced-cover-fixed-order}(1) with $e_1, e_2$ functions of $v$. For a frame $(F_A)$ write $\Gamma(A; B, C) = (D_{\hb(F_A)} F_B) \cdot F_C$. Then:
\begin{enumerate}
\item \emph{(Exact connection.)} On the invertible region $\Omega(b) = \dot\nabla \wedge \bigl(\dot H\,(b \cdot \dot k)\,\dot k\bigr)$, the vector $b$ held fixed: the rotation-gauge field is linear in the potential. This holds for every potential $H$ whenever $k$ is null and $k \cdot \nabla k = 0$.
\item \emph{(Frame components.)} $\Gamma(k; B, C) = 0$ for all $B, C$; $\Gamma(\ell; k, e_i) = 0$, $\Gamma(\ell; \ell, e_i) = e_i \cdot \nabla H$, $\Gamma(\ell; k, \ell) = -k \cdot \nabla H$ and $\Gamma(e_i; k, \ell) = 0$ exactly; and $\nabla H$ has Cartesian components $-M\operatorname{Re}\bigl((x, y, Z - Ia)\,z^{-3}\bigr)$, while $k \cdot \nabla z = 1$.
\item \emph{(Forced normalisation.)} In the forced-weight frame $(F_K, F_N, e_1, e_2) = (\rho^{-1/2}k, \rho^{1/2}\ell, e_1, e_2)$ of Theorem \claimref{synthesis.kerr-ring-blow-up-forced-cover-fixed-order}(2) (the weights $(\tfrac12, -\tfrac12)$ of that Theorem act on components, so on frame vectors as $\rho^{-1/2}$, $\rho^{1/2}$) every component, the derivative of the weights included, is $O(\rho^{-2})$ near the ring on the cover; the order $-2$ occurs only in $\Gamma(F_N; F_N, e_i)$, whose pair of leading coefficients never vanishes together, and in the boost components $\Gamma(e_i; F_K, F_N) = -\tfrac12\,e_i \cdot \nabla \log\rho$; every other component is $O(\rho^{-3/2})$. So among normalisations by powers of $\rho$, multiplying by the transverse distance $d := |w|/(2a) = \rho^2/(2a)$ is the only one that keeps every component bounded with a nonzero limit on a tangential direction.
\item \emph{(The limit.)} Let $\widehat\Omega := d\,\Omega$ in that frame, $\hat\varpi$ the outward radial and $\hat z$ the axial unit vector at the ring point, $\nu$ the unit vector of $\mathrm{span}(e_1, e_2)$ along the projection of $\nabla\rho$ and $\hat e_\psi$ the one orthogonal to it (the angular direction, tangent to the exceptional torus). Uniformly on the cover, with corrections $O(\rho^{1/2})$, $\widehat\Omega(F_K) \to 0$, $\widehat\Omega(\hat e_\psi) \to 0$, $\widehat\Omega(\nu) \to -\tfrac14 F_K \wedge F_N$ (the boost of the weights, along the normal direction), and
\[
\widehat\Omega(F_N) \;\to\; X(\psi) \;=\; F_K \wedge (L_\varpi\,\hat\varpi + L_Z\,\hat z), \qquad L_\varpi + I L_Z \;=\; -\tfrac{M}{2}\,e^{-3I\psi} \;=\; \tfrac12\,\rho^{3}\mathfrak M ,
\]
with $\mathfrak M = -Mz^{-3}$ the field-strength scale of Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor}. With the pseudoscalar $I = e_0\hat s\hat\varpi\hat z$, $\hat s$ the spatial part of $k$ at the ring, $F_K \wedge \hat z = -(F_K \wedge \hat\varpi)I$, so $X(\psi) = -\tfrac{M}{2}\,(F_K \wedge \hat\varpi)\,e^{3I\psi}$.
\item \emph{(Exceptional algebra, duality and winding.)} In frame components the limiting values on tangential directions span $\mathfrak n = \mathrm{span}(F_K \wedge \hat\varpi, F_K \wedge \hat z)$, the abelian algebra of null rotations about the principal null direction $k_0$ (the Lie algebra of the group of Proposition \claimref{transport.group-null-rotations}): it annihilates $k_0$, its elements are nilpotent of order three on vectors, it receives no boost or spatial rotation on tangential directions (contrast $\Lambda^2 W$ in the Schwarzschild limit); together with the boost of the weights on the normal direction, the limiting values on all directions span the solvable, not nilpotent, algebra $\mathfrak n + \R\,F_K \wedge F_N$, on which the boost acts on $\mathfrak n$ with weight one, and the pseudoscalar maps it to itself, so the duality rotations $e^{I\alpha}$ act on it as a circle. The limit $\psi \mapsto X(\psi)$ is a nowhere-vanishing section of this complex line of constant modulus $M/2$ whose phase turns three times round the circle of $\psi$: relative to any frame obtained from this one by a rotation of $(e_1, e_2)$ and a boost of $(k, \ell)$ continuous on the cover up to the ring, the degree of $L_\varpi + IL_Z$ is $-3$, the winding number of the Kerr scale recorded in Theorem \claimref{synthesis.kerr-ring-double-cover-data}(4), three in absolute value. Under the deck transformation $\psi \mapsto \psi + \pi$ it changes sign, so downstairs the limit is two-valued with holonomy $-1$. The tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} has the same limit: in vacuum its Schouten term vanishes, its soldering term $-\nInf \wedge \hb^{-1}(a)$ has constant frame components and is removed by the factor $d$, and $X$ commutes with $\nInf$ and $\nO$.
\item \emph{(Linking holonomy is trivial in the limit.)} Let $T = \partial_\psi$ be the tangent of the loop $z = \rho e^{I\psi}$, $0 \le \psi \le 2\pi$, at fixed time and fixed azimuth $\arg(x + Iy)$, closed on the cover and linking the ring. In the smooth frame $(k, \ell, e_1, e_2)$ the components $(D_T F_B) \cdot F_C$ are $A_0(\psi) + O(\rho)$ with
\[
A_0(\psi) \;=\; k_0 \wedge (G_\varpi\,\hat\varpi + G_Z\,\hat z), \qquad G_\varpi + IG_Z \;=\; I\,\tfrac{M}{a}\,e^{-2I\psi},
\]
the sum of $(e \cdot \nabla H)(T \cdot k)$ and $H\,T \cdot (e \cdot \nabla v)$. The values lie in the abelian plane $\mathfrak n$ and $\int_0^{2\pi} e^{-2I\psi}\,d\psi = \int_0^{\pi} e^{-2I\psi}\,d\psi = 0$, so the Levi-Civita transport round the linking loop, and along the half loop $0 \le \psi \le \pi$ that joins the two sheets, tends to the identity in that frame as $\rho \to 0$: the holonomy of small loops linking the ring, a frame-independent conjugacy class, tends to the identity. The sign by which the deck transformation acts on $X$ in (5) is therefore carried by the limiting data, not by transport round the ring.
\end{enumerate}
\emph{Beyond one flat chart.} The double cover branched along the ring, on which the weighted frame, the exceptional torus and the limit live, is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the identities (1) and (2) and the values of the normalised connection at every $\rho > 0$ along paths in the Kerr-Schild chart are in Gauge Theory Gravity, and the cover is read on the manifold assembled from the derived metric's charts.

## technical
The stored cometric result fixed how the Kerr ring must be blown up: on the double cover, with the null frame boosted by $\rho^{\pm 1/2}$. This result computes the connection in that frame. The rotation-gauge field of the Kerr gauge field is exactly $\Omega(b) = \nabla \wedge (H(b \cdot k)k)$, linear in the potential, because $k$ is null and geodesic in the flat sense. In the smooth null frame the connection along $k$ vanishes and the only component of top order is $\Gamma(\ell; \ell, e) = e \cdot \nabla H$, of order $\rho^{-3}$. After the boost by the forced weights every component is at most of order $\rho^{-2}$, so the normalisation by the transverse distance $d = \rho^2/(2a)$ is forced, and the normalised connection has a limit on the exceptional torus: zero along $k$ and along the angular direction, the weights' boost $-\tfrac14 F_K \wedge F_N$ along the normal, and along $F_N$ a null rotation about the principal null direction whose complex coefficient is $\tfrac12\rho^3\mathfrak M = -\tfrac{M}{2}e^{-3I\psi}$. The limiting values on tangential directions therefore span the abelian plane of null rotations about $k_0$, which the pseudoscalar makes a complex line carrying the duality circle, and the limit winds three times round it with constant modulus $M/2$ and is odd under the deck map. This gives the conjectured fibration its fibre at the level of connection values: the limiting values on tangential directions span the abelian nilpotent plane $\mathfrak n$; with the boost of the weights on the normal direction they span the solvable algebra $\mathfrak n + \R\,F_K \wedge F_N$; there is no Levi part, and the winding three is the degree of the connection's limit, an invariant under frame changes continuous across the ring. The checks verify the connection formula against an independent Koszul solution, the frame identities at rational points of both sheets, and the orders and limits along rational curves to the ring as exact rational functions of the curve parameter. At transport level the holonomy of small loops linking the ring tends to the identity: the generator along the loop is a null rotation of constant size $M/a$ whose direction turns twice and integrates to zero, so the sign by which the deck map acts on the limit is a property of the limiting data, not of transport round the ring. The bundle in the sense of T4 and the count are not addressed. The double cover is global: no single gravitational field on flat spacetime carries it, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
Near the ring singularity of a rotating black hole the series zooms in with a magnification already shown to be the only workable one for lengths. This result zooms in on how the gravitational field carries directions around. In the limit only one kind of motion survives: a null rotation, the kind of turning that leaves a light ray's direction fixed. Its strength is half the size of the field strength, and its direction turns three times as one goes once round the ring on the double cover, exactly as the phase of the field strength does. So the number three, previously seen only in the field strength, is also carried by the way the field transports directions, and it cannot be removed by any smooth change of reference frame. Carrying a direction once round a small loop about the ring, by contrast, brings it back unchanged in the limit.

## one-liner
For the Kerr gauge field $\Omega(b) = \nabla \wedge (H(b \cdot k)k)$ exactly; in the forced-weight frame on the double cover of the ring the connection normalised by the transverse distance $\rho^2/(2a)$ tends to a null rotation about the principal null direction with coefficient $\tfrac12\rho^3\mathfrak M = -\tfrac{M}{2}e^{-3I\psi}$, so the limiting values on tangential directions span the duality-complex null-rotation plane and wind three times, along the normal direction the limit is the boost $-\tfrac14 F_K \wedge F_N$ of the weights, while the holonomy of small loops linking the ring tends to the identity.
