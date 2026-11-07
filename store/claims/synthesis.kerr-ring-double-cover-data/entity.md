---
id: synthesis.kerr-ring-double-cover-data
kind: claim
version: 3
title: The Kerr data on the double cover of the ring
status: proved
region: synthesis
subject: interior
tags: [kerr, null-directions, curvature-and-field-equations]
proposed_by:
  kind: ai
  session: colony-2026-10-22
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
  - interior.complex-factorisation-location-ring@6
  - interior.complex-scale-inverse-cube-killing-spinor@6
  - interior.imported-kerr-curvature@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_double_cover_identities
- kind: check
  ref: check.py::check_windings
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.duality-monodromy-fibration-over-ring
  - note.interior.duality-winding-around-ring
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  open_problem: op.kerr-ring
  note: >-
    The identities z = sqrt(x^2 + y^2 + (Z - i a)^2) = r - i a cos theta and H = M Re(1/z) are the
    classical complex point-source (Appell / Newman-Janis) representation of the Kerr solution (Appell,
    Math. Ann. 30 (1887); Newman and Janis, J. Math. Phys. 6 (1965) 915; Israel, Phys. Rev. D 2 (1970)
    641; Newman, J. Math. Phys. 14 (1973) 102; cited from memory, to be confirmed), and the inverse-cube
    scale is the classical Psi_2, already imported in the store. They are restated here for use; what is
    added is the reading of the store's winding remark on the branched double cover: the integer winding
    three on the exceptional circle of the cover, the holonomy -1 downstairs, and its identification with
    the deck action. It also gives T04's preliminary computation (rank-one null pulse along the ring
    generator, normal-circle cosine, vanishing on the two disc directions) in closed form, with the cosine
    read on the double cover; there the pulse is a simple pole of fixed order in |z| (of order -1/2 in the
    ordinary distance to the ring). It does not construct the completion's exceptional structure over the
    ring, so Conjecture interior.duality-monodromy-fibration-over-ring stays open; the classical fact that
    the r < 0 region is isometric to the r > 0 region of the Kerr solution with mass -M (Carter 1968,
    cited from memory) is consistent with clause (3) but not used, and oddness of H alone does not show it,
    since k also changes between the branches.
  flags:
  - 'beyond one flat chart: the double cover branched along the Kerr ring and the r < 0 sheet of the maximal extension'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement (FLAG): the Kerr-Schild metric is the derived metric of the Kerr gauge field hb(b) = b + H (b.k) k on flat spacetime, the coordinates are background labels, the curvature scale is the field-strength scale; the double cover branched along the ring and the passage to the r < 0 sheet are kept and flagged beyond one flat chart (DICTIONARY.md section 14, item 3). Clauses (1)-(4) unchanged; check unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (referee GR1, 2026-10-23): the vector argument of hb renamed b (a is the Kerr spin): hb(b) = b + H (b.k) k.'
---

## formal
Let $a \neq 0$, let $(x, y, Z)$ be the Kerr-Schild coordinates of Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge}, labels of the flat background on which the Kerr gauge field $\hb(b) = b + H\,(b \cdot k)\,k$ lives (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), related to the oblate coordinates by $x^2 + y^2 = (r^2 + a^2)\sin^2\theta$, $Z = r\cos\theta$, identify $\R \oplus \R I$ with $\C$ as in Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor}, and put
\[
w \;:=\; x^2 + y^2 + (Z - Ia)^2, \qquad z \;:=\; r - Ia\cos\theta .
\]
\begin{enumerate}
\item \emph{(The double cover.)} $z^2 = w$ identically (the classical complex-source representation; see the proof for provenance). The function $w$ vanishes exactly on the ring $\{x^2 + y^2 = a^2, Z = 0\}$, with $dw = 2a\,d\varrho - 2Ia\,dZ \neq 0$ there ($\varrho^2 = x^2 + y^2$), so $w$ is a complex normal coordinate of the ring and $z = \sqrt w$ is the coordinate of the double cover of a tubular neighbourhood branched along it; the involution $(r, \theta) \mapsto (-r, \pi - \theta)$ fixes $(x^2 + y^2, Z)$ and acts as the deck transformation $z \mapsto -z$, exchanging the parameter regions $r > 0$ and $r < 0$.
\item \emph{(The pulse.)} The Kerr-Schild potential $H$ of the gauge field, whose derived metric is $g = \eta - 2H\,k\otimes k$ (Proposition \claimref{interior.unipotency-across-kerr-family}) is
\[
H \;=\; \frac{Mr^3}{r^4 + a^2Z^2} \;=\; M\,\operatorname{Re}\frac{1}{z} \;=\; \frac{M\cos(\arg z)}{|z|} :
\]
on the double cover a simple pole with the cosine of the normal angle as its angular factor, vanishing exactly on the two directions $\arg z = \pm\pi/2$, which are the two faces of the disc $\{r = 0\}$; downstairs $H = M|w|^{-1/2}\cos(\tfrac12\arg w)$, of order $-\tfrac12$ with a two-valued angular factor. At the ring the null vector $k$ is the time direction plus a unit tangent of the ring (the orientation of the tangent depends on the sign convention for the $a$-terms of $k$).
\item \emph{(Parity under the deck transformation.)} $H$ and the field-strength scale $\mathfrak M = -Mz^{-3}$ of Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor} are odd under $z \mapsto -z$.
\item \emph{(Windings.)} Around the ring once on the double cover ($\arg z$ increasing by $2\pi$) the duality phase of $\mathfrak M$ turns by $-6\pi$: an integer winding $-3$ on the exceptional circle of the blow-up of $\{z = 0\}$. Around the ring once downstairs ($\arg w$ increasing by $2\pi$; a loop closed in Kerr-Schild coordinate space, but an open path from one sheet to the other in the maximal extension, whose closed loop around the ring is the double-cover loop counted once in Remark \claimref{note.interior.duality-winding-around-ring}) it turns by $-3\pi$, so the duality holonomy is $e^{-3\pi I} = -1$, and it coincides with the action of the deck transformation in (3).
\end{enumerate}
\emph{Beyond one flat chart.} The double cover branched along the ring, and the $r < 0$ sheet of the maximal extension onto which the downstairs loop continues, are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region (the identity $z^2 = w$, the form of $H$, and the values and phases of $\mathfrak M$ along paths in the Kerr-Schild chart) are in Gauge Theory Gravity, and the cover and the second sheet are read on the manifold assembled from the derived metric's charts.

## technical
Near the Kerr ring the natural complex coordinate is $w = x^2 + y^2 + (Z - Ia)^2$, which vanishes simply on the ring, and the oblate combination $z = r - Ia\cos\theta$ is its square root: the parameter ranges $r > 0$ and $r < 0$ are the two branches of the double cover branched along the ring, exchanged by $z \mapsto -z$. On that cover the Kerr data are simple: the Kerr-Schild potential is $H = M\operatorname{Re}(1/z)$, a simple pole whose angular factor is the cosine of the normal angle and which vanishes on the two faces of the disc, and the field-strength scale is $-Mz^{-3}$, whose phase winds three times around the ring. Downstairs both are two-valued, the field-strength scale picking up a factor $-1$ per loop, which is exactly the effect of passing to the other branch. So the integer winding three conjectured for the ring lives on the double cover, and the holonomy that connects the sheets is the sign $-1$ in the duality circle. The exact checks verify the identities at fixed rational points and count the windings by crossings on rational polygons. Its double cover and the second sheet are global: no single gravitational field on flat spacetime carries them, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The singularity of a rotating black hole is a ring rather than a point. Near the ring, the gravitational field is naturally described on a doubled copy in which going once around the ring in ordinary space takes one half way around in the doubled copy, from one sheet of the solution to the other. On the doubled copy everything is simple: the potential of the gravitational field is one over the doubled copy's distance coordinate (in ordinary distance it grows like one over the square root of the distance to the ring), and the twist of the field strength goes three full times around. In ordinary space only half of that is visible, and the leftover half turn shows up as a sign flip: going once around the ring lands you on the other sheet, where the field strength has the opposite sign. These formulas for the field near the ring are classical; what is new is reading the twist and the sign flip this way.

## one-liner
With $w = x^2 + y^2 + (Z - Ia)^2$ and $z = r - Ia\cos\theta = \sqrt w$, the Kerr-Schild potential is $H = M\operatorname{Re}(1/z)$ and the field-strength scale $-Mz^{-3}$: on the double cover branched along the ring the duality winding is the integer $-3$, and downstairs the holonomy is $-1$, the deck transformation exchanging $r > 0$ and $r < 0$.
