---
id: synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise
kind: claim
version: 3
title: 'A parallel frozen point on matter regions is the field-space premise'
status: proved
region: synthesis
subject: einstein
tags: [tractors, frozen-point, forcing-and-uniqueness, curvature-and-field-equations]
proposed_by:
  kind: ai
  session: 2026-11-01-field-space
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: GA rewrite (dilation slot, dust field and matter term in GA)
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the sign of the dilation slot against its two siblings stated (wording)'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri@3
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@5
  - interior.scale-tractor-leaves-cone@8
  - interior.imported-tractor-connection@3
  - dark-energy.imported-frozen-point-geometry@7
  - odd-extensions.transport-constrains-frozen-point-only-through@3
  - synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_slot_rho_is_the_unique_parallel_extension
- kind: check
  ref: check.py::check_transport_differs_from_it_by_the_matter_term
- kind: check
  ref: check.py::check_transport_parallel_tractor_off_einstein_has_no_physical_scale
- kind: check
  ref: check.py::check_sections_exist_for_every_norm_and_are_gauge
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
  - pred.dark-energy-w-minus-one
extraction:
  maintainer_pass_pin_review_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second-round close-out): synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff 3 -> 4 repinned; its change is the setting maps and densities written in GA, the index forms kept as readings and proved equal (notation).'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part repinned 3 -> 4 after reviewing its restatement (formal setting restated (A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, l^2 = 3/|Lambda| dropped)); clauses (i) to (iv), the store sign and the frame equation, cited here, are unchanged, and the use here holds as cited. Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (DECISIONS H4, ga-issues-R03 item 4): this result writes the dilation slot beta(a) n0 ^ ninf, while synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff and synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen write beta(a) ninf ^ n0; the formal now says that their beta is minus the one here. No content change.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA: the dilation slot beta of the soldered connection is a scalar-valued linear function of background vectors, beta(a) = a . b (a one-form only in components); the dust field is the dilation field hb^{-1}(a) = tau^2 a with derived metric tau^4 (dtau^2 - dx^2) as its reading; the matter term T - (tau/3) g is written as the map T - (tau/3) id on physical vectors (g is the flat product there), on every level and in the proof. A notation change only; the slot equations of (iii) stay as the labelled component reading they already were. Statement unchanged. Notation (reader R03): the physical vector hb^{-1}(a) was also written A, the letter of the connection A(a), in one sentence; it is now u in the formal level and the proof.'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: the citations of the infinite-stiffness result are now claimrefs and a uses edge (the failure of the converse on the solution-only reading, stated in the title, rests on it; it does not depend on this result), with an untouched_premises record in coverage.yaml; the registration condition is repinned to version 8, whose clause (iii) now names the connection and the physical scale and assumes the field-space premise, and the Reading says so (the wording of the paper is what "read literally" refers to); the field-space premise synthesis.field-space-premise-parallel-frozen-point is named by claimref (text only, no assumes edge: this result is a reading of it); the curvature-only classification is repinned to version 3 (clause (iv), cited here, unchanged). The id is kept (see the maintainer report of 2026-11-01). Statement unchanged.'
  note: >-
    Route of the frozen point as a reduction of the Cl(2,4) gauge field. Everywhere the store makes the
    frozen point parallel it does so on the Einstein region, and the one stored request for a parallel
    frozen point off that region is the registration condition of the w = -1 prediction. In the gauge where
    the frozen point is n_inf + rho n_0 in the physical scale, a connection of the soldered tractor shape
    keeps it parallel exactly when its special-conformal slot is rho times the identity and its dilation slot
    vanishes: the field space of connections preserving I. So adopting the field space implies the
    registration condition. The converse holds only for the kinematic reading of the condition (the
    gravitational connection is that one for every configuration), where it restates the premise; read of
    solutions only, it is weaker. Read literally, the condition is met for every field. On the reduced space
    rho is constant, so Lambda is a constant parameter and w = -1 is the LambdaCDM equation of state, not
    evidence independent of LambdaCDM. Nothing here derives the field space. Transport-absent: the connection
    that keeps I parallel off the Einstein region is not the series' transport.
---

## formal
Work in $\Cl(2,4)$ in the stored chart, generators $e_{0}$ ($+1$), $e_{1}, e_{2}, e_{3}$ ($-1$), $e_{+}$ ($+1$), $e_{-}$ ($-1$), $\nO = \tfrac12(e_{+} + e_{-})$, $\nInf = e_{+} - e_{-}$, $\ip{\nO}{\nInf} = 1$, canonical tractor $X = \nO$, and for real $\rho$ put $I_{\rho} = \nInf + \rho\,\nO$, so $Q(I_{\rho}) = 2\rho$ and $\Lambda := 6\rho$ gives $Q(I_{\rho}) = \Lambda/3$ (Theorem \claimref{interior.scale-tractor-leaves-cone}). Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on its invertible region, torsion allowed, with derived metric $g$, and work in the scale $g$ (the physical scale), in which $\ip{X}{I_{\rho}} = 1$. A connection of the \emph{soldered tractor shape} is
\[
A(a) \;=\; \Omega(a) \;-\; \nInf \wedge \hb^{-1}(a) \;+\; \nO \wedge S\bigl(\hb^{-1}(a)\bigr) \;+\; \beta(a)\,\nO \wedge \nInf, \qquad D_{a}V = a \cdot \nabla V + A(a) \times V,
\]
(the sibling results \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff} and \claimref{synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen} write the dilation slot as $\beta(a)\,\nInf \wedge \nO$, so their $\beta$ is minus the one here) with $S$ a linear map of spacetime vectors (the special-conformal slot) and $\beta$ a scalar-valued linear function of background vectors, $\beta(a) = a\cdot b$ for a vector field $b$ (the dilation slot; in components a one-form). The series' transport, the normal tractor connection $D^{T}$, is $S = \Sch$, $\beta = 0$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}); the connection $A_{\rho}$ with $S = \rho\,\mathrm{id}$, $\beta = 0$ is the general connection preserving $I_{\rho}$ of Theorem \claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri}(iv), the field space of the frozen-point functional.
\emph{Gauge.} The statements are made in the gauge where the frozen point is $I_{\rho} = \nInf + \rho\,\nO$ in the physical scale, that is with the rotation gauge of the gravitational field and the scale $g$ fixed. A special-conformal rotor generated by $\nO \wedge y$ fixes $X$ but moves $I_{\rho}$ off this form and the slot off $\rho\,\mathrm{id}$, so under the parabolic group of the line of $X$ the invariant statement is about the pair $(A, I)$: $I$ is parallel for $A$ with $\ip{X}{I} = 1$.
\begin{enumerate}
\item[(i)] \emph{(The parallel extension is unique; proved.)} With $u = \hb^{-1}(a)$, $A(a) \times I_{\rho} = \rho u - S(u) - \beta(a)(\nInf - \rho\,\nO)$, so $D_{a}I_{\rho} = (a \cdot \nabla\rho)\,\nO + \rho u - S(u) - \beta(a)(\nInf - \rho\,\nO)$. Hence $I_{\rho}$ is parallel if and only if $S = \rho\,\mathrm{id}$, $\beta = 0$ and $\rho$ is constant. For every gravitational field, Einstein or not, with or without matter, $A_{\rho}$ keeps $I_{\rho}$ parallel with $\ip{X}{I_{\rho}} = 1$ and constant norm $\Lambda/3$, and it is the only connection of the soldered tractor shape with rotation block $\Omega$ that does.
\item[(ii)] \emph{(Transport differs by the matter term, on shell; proved.)} $D^{T}_{a}I_{\rho} = (\rho - \Sch)(u)$, zero exactly when $\Sch = \rho\,\mathrm{id}$ (the Einstein condition). On shell for the frozen-point functional with the imported matter coupling, $\Sch = \tfrac{\Lambda}{6}\,\mathrm{id} - 4\pi G(T - \tfrac{\tau}{3}\,\mathrm{id})$ (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}(iv)), so
\[
D^{T}_{a}I_{\rho} \;=\; 4\pi G\,\bigl(T - \tfrac{\tau}{3}\,\mathrm{id}\bigr)(u),
\]
and since $T \mapsto T - \tfrac{\tau}{3}\,\mathrm{id}$ is injective on symmetric maps, transport keeps no frozen point parallel in the physical scale wherever $T \neq 0$; $D^{T}$ and $A_{\rho}$ coincide on vacuum regions and differ in the special-conformal slot by $-4\pi G(T - \tfrac{\tau}{3}\,\mathrm{id})$.
\item[(iii)] \emph{(The scale clause is needed; proved.)} Off the Einstein region transport can still carry parallel tractors whose own scale is not the physical one. For the dust field, the dilation field $\hb^{-1}(a) = \tau^{2}a$ with derived metric $g = \tau^{4}(d\tau^{2} - dx^{2})$ (conformal time, $\Lambda = 0$, scalar curvature $12/\tau^{6}$, trace-free Ricci part nonzero), the functions $\sigma = c\,\tau^{2} + h\,\tau^{3}$ are the first slots $\ip{X}{I}$ of $D^{T}$-parallel tractors, of constant norm ($h^{2}$ for $c = 0$, the de Sitter scale; $0$ for $h = 0$, the flat scale), while $\sigma = \tau, \tau^{4}, \tau^{5}$ are not; for none of them is $\ip{X}{I}$ constant, the own-scale tractor $(1, 0, J/4)$ is not parallel and its norm $R/12 = \tau^{-6}$ varies. Rescaling a parallel tractor rescales its norm, so such a tractor fixes no $\Lambda$ of the physical field.
\item[(iv)] \emph{(Existence is never obstructed; proved, the topology argued.)} In any scale $\nInf$ and $\nO$ are global sections, so $I_{\rho}$ is a global section of norm $2\rho$ for every real $\rho$. The orbit map $\xi \mapsto \xi \times I_{\rho}$ on $\so(2,4)$ has rank $5$ for every $\rho$, with image $I_{\rho}^{\perp}$, of signature $(1,4)$ for $\rho > 0$, $(2,3)$ for $\rho < 0$ and degenerate for $\rho = 0$, and stabiliser of dimension $10$; so a section of fixed norm is locally gauge equivalent to the constant one. The level sets of the norm are homotopy equivalent to a circle ($\Lambda > 0$) and a three-sphere ($\Lambda < 0$), but a section exists for every sign on every region with a scale: neither the existence of the reduction nor the sign of $\Lambda$ is constrained, and the content of the field space is the parallelism of (i).
\end{enumerate}
\emph{Reading (argued).} Clause (iii) of Theorem \claimref{dark-energy.vacuum-region-registration-condition}, the one condition of the $w = -1$ prediction, asked in the paper's wording that the frozen point admit a definition on a matter-filled region that keeps it parallel, without naming the connection (since its version 8 the clause names the connection preserving $I$ and the physical scale, the kinematic reading below, and in that form is Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}). Read literally the paper's wording is met for every field: by (i), $A_{\rho}$ keeps $I_{\rho}$ parallel on every region. What (i) and (ii) give is the following. Adopting the field space of connections preserving $I$ as the gravitational connection implies the condition, in the physical scale, the reading in which the norm is the $\Lambda$ of the field equations (by (iii) the scale cannot be dropped). The converse holds when the condition is read kinematically, as fixing which connection carries the frozen point for every configuration: within the soldered tractor shape that connection is $A_{\rho}$, and the condition is then the field-space premise restated. Read only of solutions (the on-shell connection keeps $I$ parallel) it is weaker: on the unreduced space there are functionals whose stationary slot is not $\rho\,\mathrm{id}$, and a line of couplings on which $\rho\,\mathrm{id}$ is stationary for every curvature while the density is the Euler form, so on-shell parallelism and the reduced dynamics come apart (Theorem \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff}, which also proves within its family what a dynamical frozen point gives). On the reduced space, (i) forces $\rho$ constant, so $\Lambda = 6\rho$ is a constant parameter of the field space and the field equation is Einstein's with that constant (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}(iv)): $w = -1$ is then the $\Lambda$CDM equation of state, and a confirmed $w = -1$ is not evidence for the frozen-point reading or the field-space premise independent of $\Lambda$CDM, while a detection of $w \neq -1$ refutes $\Lambda$CDM generally. Nothing here derives the field space, which the store records as Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}. By (iv) the section carries no condition of its own. Transport-absent: the connection that keeps the frozen point parallel off the Einstein region is not the series' transport; the tractor form is a convenience.

## technical
The frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$ is defined in the store as the parallel scale tractor of an Einstein field, and the gravitational action reaches Einstein's equations only when varied over the $\Cl(2,4)$ connections that preserve $I$. This result compares that field space with the one stored request for a parallel frozen point off the Einstein region, the registration condition of the $w = -1$ prediction. In the gauge where $I = \nInf + \rho\nO$ in the physical scale, a connection of the soldered tractor shape, $A(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge S(\hb^{-1}(a)) + \beta(a)\nO \wedge \nInf$, has $A(a) \times I = \rho u - S(u) - \beta(\nInf - \rho\nO)$, so $I$ is parallel exactly for $S = \rho\,\mathrm{id}$, $\beta = 0$, $\rho$ constant: the connection preserving $I$, for every field, matter included. On shell for the frozen-point functional with the imported matter coupling, the series' transport has $D^{T}I = 4\pi G(T - \tfrac{\tau}{3}\,\mathrm{id})$, nonzero wherever matter is. The physical-scale clause matters: the dust field $\hb^{-1}(a) = \tau^{2}a$ (derived metric $\tau^{4}(d\tau^{2} - dx^{2})$) has transport-parallel tractors with scales $c\tau^{2} + h\tau^{3}$ and constant norms, none with constant $\ip{X}{I}$. Sections of every norm and sign exist globally (orbit map of rank $5$). Consequently adopting the field space implies the registration condition; the converse holds for the kinematic reading (which connection carries $I$), where the condition restates the premise, and fails for the on-shell reading. Literally read, the condition is met by $A_{\rho}$ for every field. On the reduced space $\rho$ is constant, so $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state: the registration is not evidence independent of $\Lambda$CDM. Nothing is derived about the field space. Transport-absent.

## lay
The series has a fixed reference direction, the frozen point, whose length is the cosmological constant. It is known to stay fixed in empty space. The prediction that dark energy never changes asks for it to stay fixed where there is matter too, and the gravitational action gives Einstein's equations only if it is allowed to vary just those fields that keep the frozen point fixed. This result shows that, measured in the actual spacetime's own scale, the frozen point stays fixed in the presence of matter only for the connection that the action's field space prescribes; the series' own transport rule differs from it by exactly the matter present. So choosing that field space secures the prediction's condition. The reverse holds only if the condition is taken to say which connection carries the frozen point; taken only as a statement about solutions, it is weaker. It also shows that with this field space the cosmological constant is simply a fixed number, so "dark energy never changes" is the same as the standard cosmological model's assumption and is not separate evidence for the frozen point. Neither question is answered here.

## one-liner
In the gauge where $I_{\rho} = \nInf + \rho\nO$ in the physical scale, a soldered $\Cl(2,4)$ connection has $A(a) \times I_{\rho} = \rho u - S(u) - \beta(\nInf - \rho\nO)$, so the frozen point is parallel exactly for the slot $\rho\,\mathrm{id}$ with no dilation (the connections preserving $I$), for every field, matter included; on shell for the frozen-point functional with the imported matter coupling the series' transport has $D^{T}I = 4\pi G(T - \tfrac{\tau}{3}\,\mathrm{id})$; on the dust field transport-parallel tractors exist but never with constant $\ip{X}{I}$. So adopting the field space implies the registration condition of the $w = -1$ prediction, the converse holding only for the kinematic reading of that condition; on the reduced space $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state, not independent evidence; transport-absent.
