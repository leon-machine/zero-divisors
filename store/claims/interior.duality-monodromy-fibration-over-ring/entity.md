---
id: interior.duality-monodromy-fibration-over-ring
kind: claim
version: 6
title: Duality-monodromy fibration over the ring
status: conjectured
region: interior
subject: interior
tags: [kerr]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
- name: Claude Fable 5.2
  role: 'dated note at the formal, technical and lay levels: on a reading computed in a working file, the winding three is the degree of the field strength in the square root of the ring''s normal coordinate and only its parity is a class of a degenerating form; the conjecture is not reworded'
  version: 6
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 6
  kind: restatement
  defect: 'the statement names the winding number three as an invariant of the fibration with no note that, on the eigenbundle reading of the forced cover, three is a degree of homogeneity of the field strength and only its parity is a class, and that the Kerr-Schild cometric does not degenerate at the ring'
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
lineage:
  motivated_by:
  - sheaf.exceptional-algebra-deformation-normal-cone
  - interior.complex-factorisation-location-ring
  - interior.complex-scale-inverse-cube-killing-spinor
locators:
  paper: T06
  number: Conj 6.6
  label: conj:monodromy
  line: 827
extraction:
  maintainer_pass_2026_11_18_leads:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 5 -> 6. Dated note (18 November 2026), not a rewording; status and the conjecture''s wording unchanged; the one-liner is unchanged. Content from the working notes of 18 November 2026 on the Kerr ring: the forced cover is the orientation cover of the positive eigenline of the plane family of clause (5) of the strict-completions theorem in the normal coordinate w, with H = M Re(z)/|z|^2 linear in the unit eigenvector (computed exactly in the working file colony/runs/2026-11-18-leads/work/W/kerr_ring.py at rational points of both sheets); the winding three is the degree of -M z^-3 in z and only its parity is a class (argued); the Kerr-Schild cometric keeps the determinant and signature of eta^-1 where H is finite, so no stored completion statement applies (computed at sample points). Labelled in the text as computed and not refereed; there is no stored result behind it.'
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 4 -> 5. Note added at the formal and technical levels recording synthesis.kerr-ring-connection-limit-null-rotation-winding-three: the transport holonomy of small linking loops tends to the identity, so the sheet connection is carried by the limiting data (the deck map acts by -1 on the limit section, the adjoint action of the transverse rotor), with fibre the null-rotation plane on tangential directions. The conjecture itself is unchanged.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  typing:
    by: ai-typing-pass
    added: [interior.complex-factorisation-location-ring]
    note: 'Added the complex-factorisation proposition to lineage.motivated_by, since the conjecture is prompted by the duality winding of its scale around the ring (the winding remark has no store entity).'
  env: conjecture
  context_refs:
  - sheaf.exceptional-algebra-deformation-normal-cone
  unresolved_refs:
  - rem:winding
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: 'Open conjecture; added to motivated_by the Killing-spinor proposition, whose winding number three the statement names as an invariant of the fibration.'
  flags:
  - 'beyond one flat chart: the sheets of the Kerr maximal extension connected through the ring'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement (FLAG): the Kerr ring is named as the ring of the flat background where the Kerr-Schild gauge field hb fails; the holonomy connecting the sheets of the maximal extension is kept and flagged beyond one flat chart (DICTIONARY.md section 14, item 3). The conjecture is unchanged. Fix (referee GR1, 2026-10-23): the ring is where the Kerr-Schild hb is undefined (H diverges), not where it is non-invertible; hb is unimodular wherever defined (DICTIONARY C8).'
---

## formal
The exceptional structure of the completion over the Kerr ring (the ring of the flat background where the Kerr-Schild gauge field $\hb$ of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, unimodular wherever it is defined, is singular: its potential $H$ diverges) is a duality-monodromy fibration: a bundle of exceptional algebras over the ring in the sense of \cite[Prop.~6.1]{ButlerT4}, refined by codimension two and carrying the monodromy of Remark \ref{rem:winding}, whose holonomy connects the sheets of the maximal extension. Equivalently: the codimension-two blow-up that replaces T4's hypersurface wall theory over rotating singularities has structure group containing the duality circle, and the winding number three of the Kerr scale is an invariant of the fibration. \emph{Note.} Theorem \claimref{synthesis.kerr-ring-connection-limit-null-rotation-winding-three} computes the limit of the rotation-gauge field at the ring on the forced cover. The transport holonomy of small loops linking the ring tends to the identity (its clause (6)), so a connection between the sheets is carried by the limiting data, not by transport round the ring: the deck transformation acts by $-1$ on the limit section, which is the adjoint action of the rotor $\hat\varpi\hat z$, the rotation by $\pi$ of the plane transverse to the principal null direction; and at the level of connection values the fibre is the plane $\mathfrak n$ of null rotations about the principal null direction on tangential directions ($\mathfrak n + \R\,F_K \wedge F_N$ with the normal direction), a complex line under the pseudoscalar on which the limit has degree $-3$. The bundle of exceptional algebras in the sense above and its structure group are not addressed there; the conjecture is unchanged. \emph{Note (18 November 2026; a reading, computed in a working file and not refereed, with no stored result behind it).} In the notation of that theorem let $w = z^{2}$ be the normal coordinate of the ring, $z = r - Ia\cos\theta$. The family of symmetric forms on the plane $\R \oplus \R I$ with matrix $\begin{psmallmatrix} \operatorname{Re}w & \operatorname{Im}w \\ \operatorname{Im}w & -\operatorname{Re}w\end{psmallmatrix}$, which is the family $\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$ of clause (5) of Theorem \claimref{synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump} in the coordinates $(\operatorname{Re}w, \operatorname{Im}w)$, has positive eigenline $\R z$ and negative eigenline $\R Iz$, with eigenvalues $\pm|w|$; and the Kerr-Schild potential is $H = M\operatorname{Re}(z)/|z|^{2}$, linear in the unit eigenvector $z/|z|$ and so odd under the deck map $z \mapsto -z$, with $H^{2} = M^{2}(1 + \operatorname{Re}w/|w|)/(2|w|)$ a function of $w$ (computed, exactly, at rational points of both sheets). So the forced double cover is the orientation cover of that positive eigenline, the class of degree one of that family pulled back by $w$. A punctured plane has only one nontrivial double cover, so this identification of classes is forced by parity alone; what the computation adds is that $H$ is a function of the eigenvector of that family. On this reading (argued, on stored statements) the winding number three is the degree of the field-strength scale $\mathfrak M = -Mz^{-3}$ in the eigenvector $z$. A class of degree one of a real line is a parity: the potential, of degree one, and the field strength, of degree three, are odd under the deck map and carry it, and a field of even degree would not. So on this reading three is not an invariant of the cover or of any completion; only its parity is a class of a degenerating form, and that parity is the holonomy $-1$ of clause (5) of Theorem \claimref{synthesis.kerr-ring-connection-limit-null-rotation-winding-three}. No stored completion statement applies at the ring: the cometric of the Kerr-Schild gauge field, $\eta^{-1}$ plus $2H$ times the square of the null field $k$, has the determinant and signature of $\eta^{-1}$ wherever $H$ is finite (computed at rational sample points on both sheets), so it diverges at the ring and does not degenerate there; the rescaled cometric on the blown-up cover was not treated. The bundle of exceptional algebras of the conjecture and its structure group are not addressed by this reading, and the conjecture's wording, which names the winding number three as an invariant of the fibration, is not changed. \emph{Beyond one flat chart.} The sheets of the Kerr maximal extension that the holonomy connects are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the ring, the Kerr scale and its winding around the ring are in Gauge Theory Gravity on the invertible region, and the sheets are read on the manifold assembled from the derived metric's charts.

## technical
Conjecture: over the Kerr ring, the ring of flat spacetime where the gauge field $\hb$, unimodular wherever it is defined, is singular (its potential $H$ diverges), the exceptional structure of the completion is a duality-monodromy fibration, a bundle of exceptional algebras over the ring refined to codimension two, carrying the duality-phase monodromy of the curvature scale and with holonomy connecting the sheets of the maximal extension. Equivalently, the codimension-two blow-up that replaces the hypersurface wall theory over rotating singularities has a structure group containing the duality circle, and the winding number three of the Kerr scale $\mathfrak M \propto (r - Ia\cos\theta)^{-3}$ is an invariant of the fibration. A computed limit of the rotation-gauge field at the ring (\claimref{synthesis.kerr-ring-connection-limit-null-rotation-winding-three}) bears on it: the transport holonomy of small loops linking the ring tends to the identity, so the connection between the sheets is carried by the limiting data (the deck map acts by $-1$ on the limit section, as the rotation by $\pi$ of the plane transverse to the principal null direction), and the fibre of connection values on tangential directions is the null-rotation plane, on which the limit winds three times. A reading of 18 November 2026, computed in a working file and not refereed (no stored result): the forced double cover is the orientation cover of the positive eigenline $\R z$ of the plane family $\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$ in the ring's normal coordinate $w = z^{2}$, the Kerr-Schild potential being linear in the unit eigenvector; the winding number three is then the degree of the field-strength scale $-Mz^{-3}$ in $z$, and only its parity, the stored holonomy $-1$, is a class of a degenerating form. The Kerr-Schild cometric does not degenerate at the ring (it diverges), so no stored completion statement applies there. The conjecture's wording is unchanged. Its sheets of the maximal extension are global: no single gravitational field on flat spacetime carries them, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
Going once around the ring singularity of a rotating black hole, the complex phase of the curvature turns three times. The conjecture is that this twisting is the visible trace of a larger geometric structure attached to the ring, a bundle whose twisting links the different sheets of the black hole's extended spacetime. It is posed as an open problem, not proved. A later reading, computed but not reviewed, suggests that the number three belongs to how strongly the field grows near the ring, and that the only part of it a twisting of this kind can remember is that it is odd; the conjecture's wording has not been changed.

## one-liner
Conjecture: the completion's exceptional structure over the Kerr ring is a duality-monodromy fibration whose structure group contains the duality circle, with the winding number three of the Kerr scale as an invariant.
