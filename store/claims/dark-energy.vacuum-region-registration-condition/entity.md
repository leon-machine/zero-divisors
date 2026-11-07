---
id: dark-energy.vacuum-region-registration-condition
kind: claim
version: 8
title: $w = -1$ on the vacuum region; the registration, and its condition
status: proved
region: dark-energy
subject: dark-energy
tags: [live-prediction, frozen-point, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - dark-energy.imported-frozen-point-geometry@7
  assumes:
  - synthesis.field-space-premise-parallel-frozen-point@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:w
- kind: check
  ref: check.py::check_norm_constant_and_w_minus_one
- kind: check
  ref: check.py::check_general_scale_tractor_norm_is_r_over_twelve
locators:
  paper: T10
  number: Prop 4.2
  label: prop:w
  line: 808
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_2026_11_01:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 7 -> 8, at Leon''s decision of 2026-11-01 (link and deflate): clause (iii) is reworded to name the connection (the Cl(2,4) connection preserving the frozen point) and the physical scale (<X, I> = 1), and in that form its condition is the new field-space premise synthesis.field-space-premise-parallel-frozen-point, to which an assumes edge is added; a marked note records the paper''s wording, why it needed both names, and that on the reduced field space w = -1 is the LambdaCDM equation of state, so a confirmed w = -1 is not independent evidence for the premise while a confirmed w != -1 refutes it. Clauses (i) and (ii) are unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: metric preservation and the w = -1 stress tensor on the de Sitter field, and Q(I_g) = R/12 with I_g parallel only on the Einstein field. Version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Einstein region and the general metric are those of gravitational fields on flat spacetime (derived metrics), the frozen point is the Cl(2,4) vector parallel for the tractor gauge field, and the Einstein equation is the store-sign GTG field equation; clause (iii) and its registration unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Clause (i) sign: in the store convention (Ric = Lambda g for de Sitter in (+,-,-,-), so Ric + 8 pi G T = (Lambda + 4 pi G tau) g as in synthesis.einstein-condition-is-infinity-vacuum-incidence and interior.sign-fixed-internally) moving Lambda to the source side gives T^Lambda = +(Lambda/8 pi G) g, energy density Lambda/8 pi G > 0; the old minus sign was a negative (anti-de Sitter) vacuum energy. w = -1 and clauses (ii), (iii) are unchanged; the proof now states the sign step. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.frozen-point-makes-stelle-west-vector
    - dark-energy.imported-frozen-point-geometry
    note: 'Added the frozen-point fact (parallelism and the tractor connection and metric used in (i)
      and (ii)) and the action theorem, which clause (iii) names in its hypothesis; the constant-Lambda
      equation of state is textbook but the source states no separate standard route and none is in the
      store. Levels pass: lay now states the parallel-extension condition of (iii) precisely and notes
      that the naive extension of (ii) fails it.'
  env: proposition
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.imported-frozen-point-geometry
  eqrefs: 3
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - dark-energy.frozen-point-makes-stelle-west-vector
    note: 'Clause (iii) is a registration with no computational step, so the premise is given its role in a closing clause rather than cited at a step.'
---

## formal
Three clauses, at three levels. Gravity is a gravitational field $(\hb, \Omega)$ on flat spacetime with derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}); the tractor connection is its $\Cl(2,4)$ gauge field (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}).
\begin{enumerate}
\item[(i)] \emph{(Proved.)} On the Einstein region the frozen point is parallel (Fact \claimref{dark-energy.imported-frozen-point-geometry}) and the tractor connection preserves the fibre metric, so $\partial_aQ(I) = 2\ip{\nabla_a I}{I} = 0$: the norm $\Lambda/3$ cannot vary in space or time. A constant $\Lambda$ enters the Einstein equations as the stress-energy $T^{\Lambda}_{ab} = (\Lambda/8\pi G)\,g_{ab}$, that is $T^{\Lambda}(a) = (\Lambda/8\pi G)\,a$ (in the store's convention, where de Sitter space has $\Ric = \Lambda g$ in signature $(+,-,-,-)$, field strength $\mathcal{R}(a) = \Lambda a$, and the Einstein equation reads $\Ric + 8\pi G\,T = (\Lambda + 4\pi G\,g^{ab}T_{ab})\,g$), with energy density $\rho = \Lambda/8\pi G > 0$ for $\Lambda > 0$ and pressure $p = -\rho$ identically: $w = -1$.
\item[(ii)] \emph{(Proved.)} Off the Einstein region write $I_g$ again for the scale tractor of a general field's derived metric $g$ in its own scale, $I_g = (1, 0, J/4) = \nInf + \tfrac{J}{4}\nO$ (the object written $I$ above is its Einstein case, $J/4 = \Lambda/6$), with $J = P_a{}^a$ the trace of the Schouten tensor, the slot that makes $I_g$ parallel exactly when $g$ is Einstein (proved below); by \eqref{eq:tractormetric}, $Q(I_g) = J/2 = R/12$, which equals $\Lambda/3$ precisely when $R = 4\Lambda$. On a matter-dominated cosmology $R$ is not constant, so the naive extension of the identification to the epochs at which $w$ is measured does not give a constant.
\item[(iii)] \emph{(Registered, conditional, under Premise (FS).)} If dark energy is the norm of the frozen point (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}), and if on matter-filled regions the frozen point is kept parallel by the gravitational connection, the $\Cl(2,4)$ connection that preserves $I$, in the physical scale, $\ip{X}{I} = 1$ (successor problem (3) of Section \ref{sec:verdict}; this is Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}, which the store adopts), then $w = -1$ exactly, at every epoch, with no evolution and no quintessence. This is a maximally rigid stance in a field of flexible proposals: most dark-energy models add freedom to $\Lambda$CDM, this one removes it. \emph{The confrontation, recorded as of 2026:} the second data release of the Dark Energy Spectroscopic Instrument \cite{DESI2025}, combining baryon-acoustic-oscillation, cosmic-microwave-background and supernova data, reports a preference for an evolving equation of state at roughly three to four standard deviations, with significance depending on the supernova compilation. The preference is contested on three grounds (it concentrates in the derivative of $w$ rather than any mean offset from $-1$; it is prior-sensitive; the driving dataset combinations exhibit internal tensions), so it is not a detection. The framework does not rely on the dispute and states its exposure plainly: a confirmed detection of $w \neq -1$ at any epoch refutes the frozen-point reading of dark energy, with no parameter available to absorb the result. The condition in (iii) is the one way the reading could avoid such a refutation, and the paper names it rather than uses it: a definition of the frozen point off the vacuum region that made the norm track $R/12$ would be refuted already.
\end{enumerate}
\emph{Note (the wording of the condition, version 8).} The paper's wording of the condition, that the frozen point admits a definition on a matter-filled region that keeps it parallel, names neither the connection nor the scale. Read literally it is met for every field by the connection that preserves $I$, and without the scale clause by transport-parallel tractors whose own scale is not the physical one and whose norm is unrelated to the $\Lambda$ of the field equations (Theorem \claimref{synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise}(i), (iii)); for the series' transport, the tractor gauge field, it fails wherever matter is (part (ii) there). Worded with the connection and the physical scale, as above, it is Premise (FS): adopting (FS) implies it, and read as fixing which connection carries the frozen point it is (FS) restated (same theorem, Reading). On the reduced field space $\rho$ is constant, so $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state: a confirmed $w = -1$ supports $\Lambda$CDM with a frozen point and is not independent evidence for (FS), while a confirmed $w \neq -1$ would refute (FS), and $\Lambda$CDM with it.

## technical
For a gravitational field on flat spacetime, on the Einstein region the frozen point is parallel for the tractor gauge field, which preserves the fibre metric, so $\partial_aQ(I) = 2\langle\nabla_aI, I\rangle = 0$ and the norm $\Lambda/3$ cannot vary in space or time; a constant $\Lambda$ acts as the stress-energy $T^\Lambda(a) = (\Lambda/8\pi G)\,a$ in the store's curvature convention (de Sitter has $\Ric = \Lambda g$), a positive energy density with $p = -\rho$, so $w = -1$. Off the Einstein region the scale tractor $I_g = (1,0,J/4)$ of a general field's derived metric is parallel exactly when $g$ is Einstein, and $Q(I_g) = J/2 = R/12$, which is not constant on a matter-dominated cosmology.

The registration is conditional: if dark energy is the norm of the frozen point, and if on matter-filled regions the frozen point is kept parallel, in the physical scale ($\ip{X}{I} = 1$), by the gravitational connection, the $\Cl(2,4)$ connection that preserves $I$ (the field-space premise (FS), which the store adopts), then $w = -1$ exactly at every epoch. On that field space $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state, so a confirmed $w = -1$ is not independent evidence for (FS). A confirmed detection of $w\neq -1$ at any epoch would refute the frozen-point reading; the evolving-$w$ preference in the 2025 survey data is recorded as contested, not a detection.

## lay
Where space is empty apart from the cosmological constant, the frozen point's length cannot change as the gravitational gauge fields carry it across flat spacetime, so dark energy behaves exactly like a cosmological constant, with pressure equal to minus its energy density. The paper goes further, on a stated condition: if dark energy is this length, and if the gravitational field is of the kind that keeps the frozen point fixed in regions full of matter, measured in the spacetime's own scale (an assumption the series now adopts; its own transport rule does not do this), then dark energy never evolves. With that assumption the cosmological constant is simply a fixed number, the standard cosmological model's assumption, so finding that dark energy never changes would not be separate evidence for it. That is a rigid, testable stance, and a confirmed measurement of evolving dark energy would refute it.

## one-liner
On the Einstein region the frozen point's norm is constant, giving $w = -1$; conditionally on the gravitational connection keeping the frozen point parallel on matter-filled regions in the physical scale (Premise (FS)), $w = -1$ at every epoch, a registration that a confirmed $w\neq -1$ would refute; on that field space $w = -1$ is the $\Lambda$CDM equation of state, not independent evidence for (FS).
