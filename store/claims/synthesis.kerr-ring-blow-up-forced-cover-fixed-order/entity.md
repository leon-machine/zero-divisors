---
id: synthesis.kerr-ring-blow-up-forced-cover-fixed-order
kind: claim
version: 3
title: At the level of the cometric, among diagonal rescalings of a null frame, the Kerr ring's blow-up needs the double cover and has fixed order on it
status: proved
region: synthesis
subject: interior
tags: [kerr, null-directions, limits, curvature-and-field-equations]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
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
  - interior.unipotency-across-kerr-family@5
  - interior.imported-kerr-schild-form-kerr-gauge@1
  - synthesis.kerr-ring-double-cover-data@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_boost_identity
- kind: check
  ref: check.py::check_forced_weights
- kind: check
  ref: check.py::check_downstairs_sign
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.duality-monodromy-fibration-over-ring
  - sheaf.weights-are-forced-are-kasner-exponents
  - note.sheaf.setting-scope-successor-problems
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  open_problem: op.kerr-ring
  note: >-
    Carries out the first attack of the problem at the level of the cometric: the blow-up of the ring in the
    diagonal class of rescalings of a null coframe adapted to the Kerr-Schild vector. T04's preliminary
    reading (fixed-power weights fail; variable-order weights with a focal double cover appear forced) is
    sharpened: downstairs no choice of exponents, fixed or direction-dependent, keeps the singular term in a
    continuous limit, while on the double cover the single fixed weight vector (1/2, -1/2, 0, 0) does, and is
    forced; the variable order of T04 is the vanishing of the angular factor cos(psi) on the two disc faces,
    not a varying exponent. The weights are the boost weights of the Schwarzschild exceptional regime without
    its angular weight. Not covered: the weighted limit of the connection (Hubble-type normalisation of the
    Levi-Civita and tractor connections at the ring), which the fibration conjecture also needs; the
    exceptional algebra over the ring is therefore not yet identified, and the conjecture stays open beyond
    its data and cometric levels.
  flags:
  - 'beyond one flat chart: the double cover branched along the Kerr ring'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement (FLAG): the Kerr metric in Kerr-Schild form is the derived metric of the Kerr gauge field hb(b) = b + H (b.k) k on flat spacetime, its inverse the derived cometric hb^T(u).hb^T(v); eta is the flat product; the curvature scale is the field-strength scale; the double cover branched along the ring is kept and flagged beyond one flat chart (DICTIONARY.md section 14, item 3). Clauses (1)-(4) unchanged; check unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (referee GR1, 2026-10-23): the vector argument of hb renamed b (a is the Kerr spin): hb(b) = b + H (b.k) k.'
---

## formal
Let $a \neq 0$ and take the Kerr gauge field $\hb(b) = b + H\,(b \cdot k)\,k$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $k$ the null field of Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge} and $\eta$ the flat product, whose derived metric is the Kerr-Schild form $g = \eta - 2H\,k\otimes k$ of Proposition \claimref{interior.unipotency-across-kerr-family} and whose derived cometric is $g^{-1} = \eta^{-1} + 2H\,k\otimes k$ exactly. On the double cover of a neighbourhood of the ring (Theorem \claimref{synthesis.kerr-ring-double-cover-data}) use $z = r - Ia\cos\theta$, $\rho := |z|$, $\psi := \arg z$, so that $H = M\cos\psi/\rho$. Then:
\begin{enumerate}
\item \emph{(Smooth frame.)} The covector $k$ is a smooth function of the coordinates of the cover up to and including the ring, where it equals the time direction plus a unit tangent of the ring; so there is a smooth $\eta$-null frame $(k, \ell, e_1, e_2)$ with $\eta(k,\ell) = 1$ and $e_1, e_2$ orthonormal and orthogonal to both, near the ring on the cover.
\item \emph{(Forced fixed weights, cometric level.)} Within the class of diagonal rescalings of a smooth $\eta$-null frame (frame boosts and dilations depending on $\rho$; the connection is not considered), rescale this frame diagonally by $(\rho^{a_k}, \rho^{a_\ell}, \rho^{a_1}, \rho^{a_2})$. The rescaled cometric has the entries of $\eta^{-1}$ multiplied by $\rho^{a_k + a_\ell}$ (on $k\ell$) and $\rho^{2a_i}$ (on $e_ie_i$), plus $2M\cos\psi\,\rho^{2a_k - 1}\,k\otimes k$. It has a nondegenerate limit at $\rho = 0$ that keeps the Kerr term if and only if $(a_k, a_\ell, a_1, a_2) = (\tfrac12, -\tfrac12, 0, 0)$. For these weights the rescaled cometric equals $\eta^{-1} + 2M\cos\psi\,k\otimes k$ for every $\rho > 0$, its limit on the exceptional set $\{\rho = 0\}$ (the ring times the circle of $\psi$, times time) is $\eta^{-1} + 2M\cos\psi\,k_0\otimes k_0$, and its determinant is that of $\eta^{-1}$, so the limit is Lorentzian on the whole exceptional set. These are the boost weights $\pm\tfrac12$ of the exceptional regime of Theorem \claimref{sheaf.weights-are-forced-are-kasner-exponents}(2), without its angular weight.
\item \emph{(The cover is forced.)} Downstairs, rescale the same frame by powers of $|w|$, with weights $(b_k, -b_k, 0, 0)$ (so $b_k = a_k/2$, since $\rho = |w|^{1/2}$); with $\psi = \tfrac12\arg w$ the Kerr coefficient is $2M\cos(\tfrac12\arg w)\,|w|^{2b_k - 1/2}$, and it has a finite nonzero limit only for $b_k = \tfrac14$; and $\cos(\tfrac12\arg w)$ returns to its negative after one loop round the ring (the deck transformation of Theorem \claimref{synthesis.kerr-ring-double-cover-data}(1) reverses the sign of $H$). For any exponent $b_k$ that depends on the direction $\arg w$ in an arbitrary way, the limit on the downstairs exceptional circle is continuous only if the Kerr term's limit is zero in every direction. So a continuous blow-up that sees the Kerr pulse exists on the double cover, at a fixed order, and not downstairs at any order, fixed or variable.
\item \emph{(The data on the exceptional torus.)} On the exceptional set of the cover the pulse coefficient $2M\cos\psi$ vanishes exactly on the two disc faces $\psi = \pm\pi/2$ and is odd under the deck transformation $\psi \mapsto \psi + \pi$, and the normalised field-strength scale $\rho^3\mathfrak M = -M e^{-3I\psi}$ of Theorem \claimref{synthesis.kerr-ring-double-cover-data}(4) winds $-3$ round the circle of $\psi$: the winding three of the conjecture is an integer winding on the oblate exceptional circle of the cover, and the downstairs holonomy $-1$ is the deck transformation, which reverses both the pulse and the field-strength scale.
\end{enumerate}
\emph{Beyond one flat chart.} The double cover branched along the ring, on which the blow-up and its exceptional torus live, is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region (the exact derived cometric, the null frame, and the rescaled cometric and its values at every $\rho > 0$ along paths in the Kerr-Schild chart) are in Gauge Theory Gravity, and the cover is read on the manifold assembled from the derived metric's charts.

## technical
The problem asks for the oblate blow-up of the Kerr ring and whether the winding three appears as an integer winding on its exceptional circle; T04's preliminary computation suggested that fixed-power weights fail and that variable-order weights on a focal double cover are forced. The statement is at the level of the cometric and within the class of diagonal rescalings of a smooth null frame; the rescaling found is a $\rho$-dependent Lorentz boost of the frame, so ``forced'' is relative to that class. Because the derived cometric of the Kerr gauge field $\hb(b) = b + H(b \cdot k)k$ on flat spacetime is exactly $\eta^{-1} + 2H\,k\otimes k$ with $k$ null, and because on the branched double cover of the ring $H = M\cos\psi/\rho$ with $k$ smooth up to the ring, the blow-up is algebra. Rescaling an $\eta$-null frame adapted to $k$ by a boost of weight $\rho^{1/2}$ leaves $\eta^{-1}$ unchanged and multiplies the Kerr term by $\rho$, so the rescaled cometric is $\eta^{-1} + 2M\cos\psi\,k\otimes k$ exactly, with a Lorentzian limit on the exceptional torus. In the diagonal class of such rescalings these weights are the only ones that give a nondegenerate limit keeping the Kerr term: the boost weights $\pm\tfrac12$ of the Schwarzschild exceptional regime, without the angular weight since the ring does not shrink. Downstairs the angular factor is $\cos(\tfrac12\arg w)$, which changes sign round the ring, so no exponent, fixed or direction-dependent, gives a continuous limit that keeps the pulse. So the double cover is forced and the order on it is fixed; what looked like variable order is the vanishing of $\cos\psi$ on the two faces of the disc. On the exceptional circle of the cover the normalised field-strength scale winds $-3$, as already recorded in the stored double-cover data, and the deck transformation reverses both the pulse and the field strength. The weighted limit of the connection at the ring, which the fibration conjecture also needs, is not computed here. The exact checks verify, at rational Kerr-Schild points, the null frame, the boost identity, the determinant, the forced weight vector, and the sign reversal under the deck map. Its double cover is global: no single gravitational field on flat spacetime carries it, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The singularity of a rotating black hole is a ring, not a point. To study it the series "blows it up": it zooms in on the ring with a magnification that depends on the distance to it, choosing the magnification so that the gravitational field has a sensible limit. This result shows that there is exactly one way to do this with fixed powers of the distance, but only after passing to a double cover of the region around the ring, the natural setting in which going once around the ring brings you to the other sheet of the spacetime. Without the double cover, no magnification works, because the field's profile around the ring flips sign after one loop. This concerns how the field measures lengths, not yet how it carries directions around. On the double cover the limit carries the expected number three: the phase of the field strength turns three times around the circle that replaces the ring.

## one-liner
At the level of the derived cometric and among diagonal rescalings of a smooth null frame: with the exact Kerr-Schild cometric $\eta^{-1} + 2H\,k\otimes k$ and $H = M\cos\psi/|z|$ on the double cover, the null-frame rescaling with forced weights $(\tfrac12, -\tfrac12, 0, 0)$ gives the exact Lorentzian cometric $\eta^{-1} + 2M\cos\psi\,k\otimes k$ up to the ring, while downstairs no fixed or direction-dependent order keeps the pulse continuously; the connection's weighted limit is not computed.
