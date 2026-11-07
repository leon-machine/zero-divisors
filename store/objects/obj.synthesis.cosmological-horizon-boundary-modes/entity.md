---
id: obj.synthesis.cosmological-horizon-boundary-modes
kind: object
version: 2
title: The boundary modes of the cosmological horizon
status: defined
region: synthesis
subject: thermality
tags: [boundary-modes, car-algebra, horizons, ladder-pairs]
proposed_by:
  kind: ai
  session: de-sitter-temperature-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'unit resolution pass, the complexification written with the central unit of the odd extension'
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.tower.tower
lineage:
  motivated_by:
  - synthesis.cosmological-horizon-completed-pair
  - standard-model.what
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the definition takes the boundary-mode algebra to be the complexification of Cl(|J|, |J|), and the complexification of a Clifford algebra is its odd extension: the unit is hat-I = I_V e, V the span of the mode planes (I_V^2 = +1), e orthogonal with Q(e) = -1, central with square -1, so B_Lambda(J) = Cl(|J|, |J|+1) and the static Killing flow is Ad exp(hat-I t sum omega_j K_j), v_j -> e^{-hat-I t omega_j} v_j (std-algebra.complexification-is-the-odd-extension, cited as a mention). The letter J stays the mode set. The radial atom''s transverse unit (U2) is not used: Pi_Lambda lies in the conformal ambient space, where no single transverse plane is singled out, and the definition''s algebra contains none; hat-I is not identified with it. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the static Killing flow v_j -> e^{-it omega_j}v_j is the scalar phase of the complexification of Cl(|J|,|J|), which the definition takes as the algebra and which contains no I_4.'
  note: The algebra the de Sitter temperature conjecture lacked. Each mode is a copy of the completed pair that the static observer's geometry supplies; the number of modes, on which the horizon's entropy count of T12's Observation 'What N is' depends, is left open, as the singularity paper's cell calibration is.
  flow_note: phase flow e^{-i omega_j t} on the modes (the T05 Thm 7.16 sense), the static Killing flow continued to imaginary rapidity.
  unit_note: The mode algebra is the plain complexification of the atom. The field unit I_4 anticommutes with e_0, which lies in the plane, so it is not the unit here (store/conventions.md, the imaginary units, known limit 1).
---

## formal
Let $\Lambda > 0$, fix a static observer, and let $(v_{\Lambda}, v_{\Lambda}^{*})$ be the completed pair of the cosmological horizon in the plane $\Pi_{\Lambda} = \mathrm{span}\{e_{0}, e_{W}\}$ of the static Killing generator (Theorem \claimref{synthesis.cosmological-horizon-completed-pair}). For a finite set $J$, the \emph{boundary modes of the cosmological horizon} on $J$ are pairs $(v_{j}, v_{j}^{*})$, $j \in J$, each a copy of $(v_{\Lambda}, v_{\Lambda}^{*})$ in its own copy $\Pi_{j} = \mathrm{span}\{a_{j}, b_{j}\}$ of $\Pi_{\Lambda}$ ($Q(a_{j}) = 1$, $Q(b_{j}) = -1$, $v_{j} = \tfrac12(a_{j} + b_{j})$, $v_{j}^{*} = \tfrac12(a_{j} - b_{j})$), the copies mutually orthogonal, so that the $v_{j}, v_{j}^{*}$ generate $\Cl(|J|, |J|)$ and satisfy the canonical anticommutation relations
\[
v_{i}v_{j}^{*} + v_{j}^{*}v_{i} = \delta_{ij}, \qquad v_{i}v_{j} + v_{j}v_{i} = 0 ,
\]
the construction of the tower (Definition \claimref{obj.tower.tower}) with one plane per mode. The \emph{boundary-mode algebra} $\mathfrak{B}_{\Lambda}(J)$ is its complexification $\Cl(|J|, |J|) \oplus \Cl(|J|, |J|)\hat{I} = \Cl(|J|, |J| + 1)$, with complex unit $\hat{I} = I_{V}e$, the central unit of the odd extension: $V = \bigoplus_{j}\Pi_{j}$, $I_{V}$ its pseudoscalar ($I_{V}^{2} = +1$), $e$ orthogonal to $V$ with $Q(e) = -1$, so that $\hat{I}^{2} = -1$ and $\hat{I}$ commutes with every $v_{j}$, $v_{j}^{*}$ (Theorem \claimref{std-algebra.complexification-is-the-odd-extension}); numbers are read in $\mathrm{span}\{1, \hat{I}\}$. The algebra has occupation boosts $\sigma_{j} = v_{j}^{*}v_{j} - v_{j}v_{j}^{*}$, boost generators $K_{j} = \sigma_{j}/2 = N_{j} - \tfrac12$, and the static Killing flow
\[
\alpha_{t} \;=\; \operatorname{Ad}\exp\Bigl(\hat{I}t\sum_{j \in J}\omega_{j}K_{j}\Bigr), \qquad \alpha_{t}(v_{j}) = e^{-\hat{I}t\omega_{j}}v_{j},
\]
$\omega_{j} > 0$ the Killing frequency of mode $j$. The geometry supplies one such plane, $\Pi_{\Lambda}$; the further copies are tower planes isometric to it, not realised in the ambient space, and the definition fixes neither $|J|$, the cell calibration on which the horizon's entropy count depends, nor the $\omega_{j}$.

## technical
The boundary modes of the cosmological horizon are copies of one building block: the completed pair that the static observer's boost plane carries. Each mode gets its own copy of the plane, the copies are orthogonal, and the resulting creation and annihilation operators obey the canonical anticommutation relations, exactly as the tower builds its modes, one plane per rung. The algebra is the complexification, with the central unit $\hat{I}$ of the odd extension of $\Cl(|J|, |J|)$ as its complex unit, each mode's occupation boost $\sigma_{j}$ gives its boost generator $K_{j} = N_{j} - \tfrac12$, and the static Killing flow turns each mode's annihilator by the phase $e^{-\hat{I}t\omega_{j}}$. How many modes there are, which the horizon's entropy count needs, is not part of the definition.

## lay
This defines the quantum modes that the cosmological horizon carries in the series' language. Each mode is one copy of the pair of operators that the horizon's geometry supplies, one that removes an excitation and one that adds it, and different modes are kept independent in the standard way for fermions. The observer's clock turns each mode at its own frequency. The definition does not say how many modes there are; that number is what a count of the horizon's entropy would need.

## one-liner
The cosmological horizon's boundary modes are mutually orthogonal copies of its completed pair, generating a CAR algebra on which the static Killing flow acts by $v_{j} \mapsto e^{-\hat{I}t\omega_{j}}v_{j}$, $\hat{I}$ the central unit of the odd extension of $\Cl(|J|, |J|)$.
