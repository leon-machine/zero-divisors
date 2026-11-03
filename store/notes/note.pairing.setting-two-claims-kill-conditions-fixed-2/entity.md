---
id: note.pairing.setting-two-claims-kill-conditions-fixed-2
kind: note
version: 1
title: The two claims, and the kill conditions fixed before computation
status: setting
subject: einstein
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
comments_on:
- pairing.imported-schwarzschild-connection-curvature
locators:
  paper: T05-pairing
  number: Setting
  section: The two claims, and the kill conditions fixed before computation
  line: 216
---

## formal
\textbf{Claim R2 (the pairing generator).} The framework's own connection, relative to the framework's own vacuum field, has a nonzero pairing class along some directions, and that class is fixed by data the framework supplies: the vacuum field selected by the curvature (the radial pair of Fact \claimref{pairing.imported-schwarzschild-connection-curvature}, its radial member by the sign of the square, and a null direction in it by the flag bit) and the connection. A pairing generator exists and is derived, not premised, up to the flag bit.

\begin{itemize}
\item[K2.1] (nothing pairs) If the pairing class vanishes for every direction at every radius, the connection preserves the vacuum field and the claim is dead.
\item[K2.2] (frame artefact) If the class is nonzero but is not the transverse derivative $\ip{\nabla_X \ell}{m}$ of the vacuum's null direction, it is a property of the frame and not of the vacuum field, and the result is a reading, not a derivation. Test: the identity must hold in $\Q(F)$, and the vanishing locus must be invariant under $\ell \mapsto \lambda\ell$.
\item[K2.3] (consistency with the singularity paper) If the class along $\partial_t$ or $\partial_r$ is nonzero, the diagonality of that paper's supplied class \cite[Prop.~7.31, Thm.~C.8]{ButlerT5} is contradicted at the pre-ascent level; this would kill that paper's statement, not the claim, and would be reported as such.
\item[K2.4] (intra-fibre only) If every class found acts within the fibre at one point, and no component of the connection pairs the ladder at $x$ with the ladder at $y \neq x$, the cross-point clause of (L$_E$) is untouched and the claim closes only in the intra-fibre sense. Parallel transport along a path identifies the fibre at $x$ with the fibre at $y$, so ``transport, then compare'' is the intra-fibre result along a path; the cross-point object is a generator in $\so(V_{x} \oplus V_{y})$ for the completion's independent ladders, which no connection supplies. This condition bounds the claim and was expected to trigger.
\end{itemize}
Predictions, as registered: the class vanishes along $\partial_t$ and $\partial_r$, is proportional to $\sqrt f/r$ in the transverse directions, vanishes at the horizon and changes sign across it (P2.1); it equals $\ip{\nabla_X\ell}{m}$ (P2.2); the mixed-plane curvature has ``nonzero pairing class in the $n$-$m$ planes and zero in the $\ell$-$m$ planes'', and the radial and angular planes have none (P2.3); in the flat conformal model the classes of a displacement $dx$ are $(\ip{dx}{\ell}, \ip{dx}{m}, 0)$ and vanish only along the ray (P2.4).

## technical
pending

## lay
pending

## one-liner
pending
