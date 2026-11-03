---
id: synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard
kind: claim
version: 2
title: 'Imported: for the Dirac field the Hadamard form is equivalent to the wave front set condition and propagates from a neighbourhood of one Cauchy surface to the whole field (Kratzert 2000; Hollands 2001; Sahlmann and Verch 2001), on Robertson-Walker fields the Dirac states adiabatic of infinite order are Hadamard (Hollands 2001), and quasi-free Hadamard states have as normal-coordinate scaling limit the flat massless Dirac two-point function (Sahlmann and Verch 2001, Prop. 5.6, posed for Majorana spinors)'
status: imported
region: synthesis
subject: quantum-fields
tags: [car-algebra, horizons, classical-theorem]
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
- citation: 'K. Kratzert, Singularity structure of the two point function of the free Dirac field on a globally hyperbolic spacetime, Ann. Phys. (Leipzig) 9 (2000), 475--498; arXiv:math-ph/0003015.'
  key: Kratzert2000
  doi: 10.1002/1521-3889(200006)9:6<475::AID-ANDP475>3.0.CO;2-S
- citation: 'S. Hollands, The Hadamard condition for Dirac fields and adiabatic states on Robertson-Walker spacetimes, Commun. Math. Phys. 216 (2001), 635--661; arXiv:gr-qc/9906076.'
  key: Hollands2001
  doi: 10.1007/s002200000350
- citation: 'H. Sahlmann and R. Verch, Microlocal spectrum condition and Hadamard form for vector-valued quantum fields in curved spacetime, Rev. Math. Phys. 13 (2001), 1203--1246; arXiv:math-ph/0008029.'
  key: SahlmannVerch2001
  locator: 'Sec. 5.2; Thm. 5.8; Def. 5.3; Prop. 5.6; Lemma 5.7'
  doi: 10.1142/S0129055X01001010
- citation: 'K. Sanders, The locally covariant Dirac field, Rev. Math. Phys. 22 (2010), 381--430; arXiv:0911.1304.'
  key: Sanders2010
  doi: 10.1142/S0129055X10003990
extraction:
  note: >-
    Imported so that the Dirac step of the deposit chain (the propagation of a Hadamard deposit from a
    collar of the descent to every later field) and the massive-Dirac deposit result can cite Facts instead
    of citing from memory; the stored propagation Fact (Fulling, Sweeny and Wald) is for the scalar field
    only. Checked on 2026-11-01. Kratzert against the arXiv record and the text of math-ph/0003015 (ar5iv):
    the paper computes the polarisation set of a Hadamard two-point function of the free Dirac field on a
    globally hyperbolic spacetime, and its introduction states that the singularities of solutions of the
    Dirac equation propagate in a simple way, by Dencker's theorem on the propagation of polarisation sets
    (Thm. 6 there); the DOI is the one on the arXiv record; journal volume and pages from memory. Hollands
    against the arXiv abstract and text of gr-qc/9906076: the abstract states that "adiabatic states of
    infinite order are Hadamard" (homogeneous, isotropic, gauge-invariant quasi-free states of the Dirac
    field on Robertson-Walker spacetimes, the spatial sections flat or curved) and states no converse; the
    proof of its Thm. IV.1 uses a propagation of singularities theorem (Thm. VIII.1, appendix); a statement
    propagating the Hadamard form of a Dirac two-point function from one Cauchy surface was not found in
    the part of the text checked. Sahlmann and Verch against the arXiv abstract and introduction of
    math-ph/0008029: for fields obeying a Dirac equation quantised by the canonical anticommutation
    relations, on globally hyperbolic spacetimes of dimension at least three, Hadamard states are
    characterised by the wave front set condition (Thm. 5.8); Sec. 5.2 states and sketches the propagation of
    the Hadamard form for such fields, which the introduction says closes a gap in the published scalar
    argument also affecting the Dirac proofs of Koehler, Kratzert and Hollands; the DOI is on the arXiv
    record; journal volume and pages from memory. Not part of this Fact: the converse of clause (c).
    Version 2 (2 November 2026) adds clause (d), Sec. 5.3 of Sahlmann and Verch, checked against the arXiv
    text of math-ph/0008029: Def. 5.3 (CAR case: a state is Hadamard if near a Cauchy surface its two-point
    function is w(D f (x) f') with w of Hadamard form for the wave operator P = D D, Def. 5.1), Prop. 5.6
    (alpha_1 = m/2 + 1, alpha_2 = alpha_1 - 1/2, m the dimension; omega a quasifree Hadamard state of the CCR
    or the CAR; the dilations delta_lambda(q) = xi_p(lambda xi_p^{-1}(q)) of normal coordinates xi_p at p,
    lifted to the bundle; in the CAR case the limit of omega_2 on the dilated test sections with weight
    alpha_2 is G^(1)_eta((gamma^mu d_mu Theta R* f) R* f'), G^(1)_eta the distribution G^(1) of the flat
    metric, which has no mass term, R the identification of the fibres with C^r through the normal
    coordinates and a frame, Theta the matrix at p of vartheta o Gamma), Lemma 5.7 (the two limit
    distributions contain (p, xi; p, -xi) in their wave front sets for every (p, xi) in N-), Sec. 3.5 (the
    Dirac operators nabla-slash plus or minus i m with m >= 0 a constant or a bundle map) and Secs. 3.4, 5.1
    (the paper considers Majorana spinors only, on spacetimes of dimension 3, 4, 9, 10 mod 8, where Majorana
    algebras exist). So the paper's CAR results, clauses (a), (b) and (d) as far as they rest on it, are posed
    for Majorana spinors; for the Dirac field of four dimensions the class of Hadamard states is discussed by
    K. Sanders, The locally covariant Dirac field, Rev. Math. Phys. 22 (2010) 381-430, arXiv 0911.1304
    (abstract checked: it discusses the class of Hadamard states "filling some technical gaps in the
    literature"; its introduction read: Hadamard states are defined by a series expansion or by the
    microlocal condition, the arguments for their equivalence have not been fully convincing, and the paper
    aims to close the remaining gaps; its Sec. 4.2 not reached; volume, issue and pages checked against the
    Crossref record of the DOI), cited with Sahlmann and Verch for the Dirac form of clause (a). The
    statement of Thm. 5.8 itself was not read against the text: every text conversion of math-ph/0008029
    stops in Sec. 5.4, before the theorem, so clause (a) rests on the statement of it in the paper's abstract
    and introduction; their proof of Prop. 5.6 (Appendix A.5) was not read either.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decisions of 2026-11-01 (routine imports for the deposit-state results: Hadamard propagation for the Dirac field, and Hollands 2001 on adiabatic states, only the direction adiabatic of infinite order implies Hadamard), checked against the sources as recorded in the note; Sahlmann and Verch 2001 added as the source that states the Dirac propagation explicitly.'
  maintainer_pass_hs_scaling:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, at Leon''s decisions of 2 November 2026 (imports for the Hadamard scaling results): clause (d) adds Prop. 5.6 of Sahlmann and Verch (scaling limits of quasi-free Hadamard states, CAR case), checked against the text; the note and clause (a) record that the paper''s CAR results are posed for Majorana spinors, cite Sanders 2010 for the Dirac equivalence, and mark Thm. 5.8 as not read against the text. Clauses (a) to (c) assert what they asserted.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is smooth and globally hyperbolic, read on several charts where its global structure needs them, and let $\psi$ be the free Dirac field of mass $m \ge 0$ on it, quantised by the canonical anticommutation relations, with the two two-point functions $\mathcal{G}^{(\pm)}$ of a quasi-free state $\omega$ and the sets $C^{(\pm)}$ of Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(b).
\begin{enumerate}
\item[(a)] \emph{(Equivalence; Sahlmann and Verch, Thm.~5.8.)} $\omega$ satisfies the wave front set condition $\mathrm{WF}'(\mathcal{G}^{(\pm)}) = C^{(\pm)}$ exactly when its two-point functions have the Hadamard form, in the sense defined there through the squared Dirac operator (the Dirac operator applied to a Hadamard parametrix of its square, plus a smooth kernel). The source poses its CAR results for Majorana spinors; for the Dirac field of four dimensions the class of Hadamard states is treated by Sanders, who fills gaps in the earlier equivalence arguments. The statement of Thm.~5.8 is taken from the source's abstract and introduction, not read against its text.
\item[(b)] \emph{(Propagation; Kratzert, Hollands, Sahlmann and Verch, Sec.~5.2.)} If the two-point functions of $\omega$ have the Hadamard form on an open neighbourhood of one Cauchy surface, they have it on the whole field: Cauchy evolution preserves the Hadamard form of the Dirac field. The argument rests on the propagation of singularities (of polarisation sets) for the Dirac operator, the polarisation set of a Hadamard Dirac two-point function being computed by Kratzert.
\item[(c)] \emph{(Adiabatic states; Hollands.)} On a Robertson-Walker field (spatial sections flat or curved) with smooth scale factor, a homogeneous isotropic gauge-invariant quasi-free state of the massive Dirac field that is adiabatic of infinite order is Hadamard.
\item[(d)] \emph{(Scaling limits; Sahlmann and Verch, Prop.~5.6, Lemma~5.7, Def.~5.3; added in version 2.)} Posed for Majorana spinors on a globally hyperbolic spacetime of dimension $n = 3, 4, 9, 10 \bmod 8$, with Dirac operator $\slashed{\nabla} + im$, $m \ge 0$ (a constant, or a bundle map), and a state Hadamard when near a Cauchy surface its two-point function is $\omega_{2}(f\otimes f') = w(Df\otimes f')$ with $w$ of Hadamard form for the squared operator. Let $\omega$ be a quasi-free Hadamard state, $p$ a point, $\xi_{p}$ normal coordinates at $p$, $\delta_{\lambda}(q) = \xi_{p}(\lambda\,\xi_{p}^{-1}(q))$ the dilations, lifted to the bundle, and $\alpha = \tfrac{n}{2} + \tfrac12$ ($\tfrac52$ in four dimensions) the weight of the dilated test sections. Then, as $\lambda \to 0$, the two-point function of $\omega$ on the dilated test sections converges to $G^{(1)}_{\eta}((\gamma^{\mu}\partial_{\mu}\Theta R_{*}f)R_{*}f')$, where $G^{(1)}_{\eta}$ is the leading Hadamard distribution of the flat metric in the normal coordinates (with no mass term), $R$ identifies the fibres with $\mathbb{C}^{r}$ through the normal coordinates and a frame, and $\Theta$ is the matrix at $p$ of the Dirac conjugation composed with charge conjugation: the scaling limit of $\omega$ at $p$ is the two-point function of the massless Dirac field on Minkowski space, whatever the mass and the curvature. The limit distributions contain $(p, \xi; p, -\xi)$ in their wave front sets for every $(p, \xi)$ in the set $N^{-}$ of the source (Lemma~5.7).
\end{enumerate}
Not part of this Fact: the converse of (c) (that a homogeneous Hadamard state is adiabatic of infinite order); the transcription of (d) from Majorana to Dirac spinors and from normal-coordinate to other dilations, which the results that use (d) carry out themselves; the source's proof of (d) (its Appendix A.5). \emph{Provenance:} \cite{Kratzert2000}; \cite{Hollands2001}; \cite[Sec.~5.2, Thm.~5.8, Def.~5.3, Prop.~5.6, Lemma~5.7]{SahlmannVerch2001}; for the Dirac equivalence also \cite{Sanders2010}.

## technical
For the scalar field the store imports that a two-point function of Hadamard form near one instant has that form everywhere. This Fact supplies the same for the Dirac field. For quasi-free states of the free Dirac field on a globally hyperbolic gravitational field, the wave front set form of the Hadamard condition, imposed on both orderings of the two-point function, is equivalent to the Hadamard form defined through the squared Dirac operator (Sahlmann and Verch), and the Hadamard form propagates by Cauchy evolution from a neighbourhood of one Cauchy surface to the whole field; the propagation rests on the propagation of singularities for the Dirac operator, with the polarisation set of a Hadamard Dirac two-point function computed by Kratzert. On Robertson-Walker fields, Hollands showed that the homogeneous Dirac states adiabatic of infinite order, those that agree with the adiabatic expansion of the mode equation to every order in the inverse momentum, are Hadamard. Only that direction is imported; the converse is not. Sahlmann and Verch also determine the short-distance scaling limit of such states: scaled towards a point in normal coordinates, a quasi-free Hadamard state tends to the vacuum two-point function of the massless Dirac field on Minkowski space, whatever the mass and the curvature. Their results for the anticommutation relations are posed for Majorana spinors; Sanders treats the Hadamard states of the four-dimensional Dirac field and fills gaps in the earlier equivalence arguments.

## lay
Physicists require that a reasonable quantum state of a field, looked at closely enough, resembles empty space. For electrons and the other particles of spin one half, these results show that it is enough to check this at one moment: the equations of motion then keep it true at every other moment. They also show that in a uniformly expanding universe a standard recipe for building states, which follows the expansion smoothly to every order, gives states of this regular kind, and that close up such a state looks exactly like the empty state of massless particles in flat space. These are taken from the literature.

## one-liner
For the free Dirac field on a globally hyperbolic gravitational field, the Hadamard form is equivalent to the wave front set condition on both orderings and propagates from a neighbourhood of one Cauchy surface to the whole field (Kratzert 2000; Hollands 2001; Sahlmann and Verch 2001); on Robertson-Walker fields homogeneous Dirac states adiabatic of infinite order are Hadamard (Hollands 2001; the converse is not imported); quasi-free Hadamard states scale in normal coordinates to the flat massless Dirac two-point function (Sahlmann and Verch 2001, Prop. 5.6, posed for Majorana spinors; Sanders 2010 for the Dirac equivalence).
