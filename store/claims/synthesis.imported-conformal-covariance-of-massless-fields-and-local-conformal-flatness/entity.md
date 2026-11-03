---
id: synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness
kind: claim
version: 1
title: 'Imported: a four-dimensional gravitational field with vanishing Weyl curvature is locally a conformal rescaling of the flat field (Weyl, Schouten), and in four dimensions the conformally coupled massless scalar (weight 1), the massless Dirac field (weight 3/2) and the Maxwell and Yang-Mills fields (weight 0) are conformally covariant'
status: imported
region: synthesis
subject: quantum-fields
tags: [gauge-fields, curvature-and-field-equations, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
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
imported_from:
- citation: 'J. A. Schouten, Ueber die konforme Abbildung n-dimensionaler Mannigfaltigkeiten mit quadratischer Massbestimmung auf eine Mannigfaltigkeit mit euklidischer Massbestimmung, Math. Z. 11 (1921), 58--88.'
  key: Schouten1921
- citation: 'H. Weyl, Reine Infinitesimalgeometrie, Math. Z. 2 (1918), 384--411.'
  key: Weyl1918
- citation: R. M. Wald, General Relativity, University of Chicago Press (1984).
  key: Wald1984
  locator: 'Appendix D'
- citation: 'R. Penrose and W. Rindler, Spinors and Space-Time, Vol. 1, Cambridge University Press (1984).'
  key: PenroseRindler1984
  locator: 'Sec. 5.7'
extraction:
  note: >-
    Imported so that the deposit-state results can cite as Facts the conformal covariance of the massless
    fields and the local conformal flatness of Weyl-flat fields, which they cited from memory; the proofs of
    the conformal transfer of the Hadamard condition (null geodesics and their covectors, wave-front sets)
    remain in the result on Weyl-flat fields. Checked on 2026-11-01: the conformal-flatness theorem (a
    pseudo-Riemannian manifold of dimension at least four is conformally flat if and only if its Weyl tensor
    vanishes, attributed to Schouten, Math. Z. 11 (1921)) against the course notes of A. Derdzinski (Ohio
    State University, Math 7711, "cf.pdf"); the rescaling psi = Omega^(-3/2) psi-tilde of the massless Dirac
    field under g = Omega^2 g-tilde, with the massless Dirac equation holding in one metric exactly when it
    holds in the other, against arXiv:1009.2064 (Sec. III, eqs. (8) to (10)), which cites two earlier papers
    of Gibbons and collaborators for it; the four-dimensional conformal invariance of the massless
    Dirac-Maxwell equations against the introduction of arXiv:1407.1177. Cited from memory, not checked: the
    bibliographic data of Schouten 1921 and Weyl 1918; Wald 1984 Appendix D (the
    conformally coupled scalar and the Maxwell field); Penrose and Rindler 1984 Sec. 5.7 (massless free-field
    equations); the conformal invariance of the Yang-Mills equations in four dimensions; and the
    preservation of the conserved Dirac current and of the Klein-Gordon symplectic form under the rescaling.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decisions of 2026-11-01 (routine import for the deposit-state results: conformal covariance of the massless Dirac, Maxwell and Yang-Mills fields and local conformal flatness of Weyl-flat four-dimensional fields; the conformally coupled scalar added for the band result), partly checked as recorded in the note.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with smooth derived metric $g$ on an open region $U$, and read the Weyl curvature as the Weyl part of the field strength (Fact \claimref{synthesis.imported-gtg-dictionary}).
\begin{enumerate}
\item[(a)] \emph{(Local conformal flatness; Weyl, Schouten.)} If the Weyl curvature vanishes on $U$, every point of $U$ has a neighbourhood and a gauge in which $\hb(b) = b/\varphi(x)$ with $\varphi$ smooth and positive, so that the derived metric there is $\varphi^{2}$ times the flat one; conversely such a field has vanishing Weyl curvature. (In dimension at least four, a metric is locally conformally flat exactly when its Weyl tensor vanishes.)
\item[(b)] \emph{(Conformal covariance.)} Let $\tilde g = \varphi^{2}g$ with $\varphi$ smooth and positive on $U$, and use the rescaled frame for spinors. Then $\phi$ solves the conformally coupled massless equation (the wave equation with the coupling to the scalar curvature at one sixth, in the sign that makes it conformally covariant) exactly when $\tilde\phi = \varphi^{-1}\phi$ solves it for $\tilde g$; $\psi$ solves the massless Dirac equation for $g$ exactly when $\tilde\psi = \varphi^{-3/2}\psi$ solves it for $\tilde g$; and the source-free Maxwell and Yang-Mills equations for a gauge potential $A$ are the same for $g$ and $\tilde g$, with $A$ unchanged. These are bijections of the solution spaces; the Klein-Gordon symplectic form and the conserved Dirac current are preserved, so they identify the CCR and CAR algebras of the two fields.
\end{enumerate}
\emph{Provenance:} \cite{Weyl1918}, \cite{Schouten1921} (clause (a)); \cite[Appendix~D]{Wald1984} (the scalar and the Maxwell field), \cite[Sec.~5.7]{PenroseRindler1984} (massless free fields, the Dirac rescaling among them). Massive fields, and the minimally coupled massless scalar off fields with $R = 0$, are not conformally covariant and are not part of this Fact.

## technical
Two classical facts of conformal geometry. First, a four-dimensional gravitational field whose Weyl curvature vanishes is, near each point, a rescaling of the flat field by a smooth positive factor (Weyl and Schouten; in four or more dimensions the Weyl tensor is the complete local obstruction to conformal flatness). Second, the massless fields of the standard model are conformally covariant in four dimensions: under a rescaling of the metric by $\varphi^{2}$ a solution of the massless Dirac equation is carried to a solution by the factor $\varphi^{-3/2}$, a conformally coupled massless scalar by $\varphi^{-1}$, and the Maxwell and Yang-Mills equations are unchanged. The maps preserve the conserved current or symplectic form, so the quantum field algebras are identified. Together they let the conformal vacuum of a Weyl-flat field be the flat vacuum, rescaled.

## lay
Some gravitational fields are, up to a change of scale from place to place, the same as empty flat space: exactly those in which gravity stretches but does not distort shapes. Massless particles, such as light and massless electrons, cannot tell a change of scale apart, so on such fields their physics is that of flat space, rescaled. These are classical results, taken from the literature.

## one-liner
A four-dimensional gravitational field with vanishing Weyl curvature is locally $\hb(b) = b/\varphi$, the flat field rescaled (Weyl, Schouten); under $g \mapsto \varphi^{2}g$ the conformally coupled massless scalar rescales by $\varphi^{-1}$, the massless Dirac field by $\varphi^{-3/2}$, and the Maxwell and Yang-Mills equations are unchanged, with the field algebras identified.
