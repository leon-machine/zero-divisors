---
id: obj.standard-model.two-rung-module-sectors-slot-components
kind: object
version: 1
title: The two-rung module; sectors; slot components
status: defined
region: standard-model
subject: standard-model
tags:
- spinor-modules
- ladder-pairs
- hypercharge-and-anomalies
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
locators:
  paper: T12
  number: Def 9.8
  label: def:module
  line: 1562
extraction:
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level has no twistor language; only the lay level''s ''twistor''s own pairs'' became
      ''conformal spinor''s own pairs''. The complexified ambient space V_C and the complex Fock module
      are kept: their complex unit must commute with the odd (vector) action, which I6 does not, so the
      dictionary''s I6 does not apply here.'
  source_title: The two-rung module; sectors; slot components
  source_formal: 'Let $R_{2} = \operatorname{span}(v_{4}, v_{5})$ be the span of the two rungs'' creation
    modes over $\C$ and $\Lambda^{\bullet}(W \oplus R_{2})$ the Fock module of the five mode pairs, three
    of $W$ and two of $R_{2}$, with the Hermitian structure induced by $*$ of Fact \claimref{standard-model.imported-tower-commuting-copies-fock-module}
    on the rung factor and by a fixed $\mathrm{Spin}(2,4)$-invariant Hermitian form on the pair factor.
    The \emph{sector} $(j, k)$ is $\Lambda^{j}R_{2} \otimes \Lambda^{k}W$, $j$ the rung (slot) number
    and $k$ the pair number; the \emph{slot-singlet sectors} are $j \in \{0, 2\}$ and the \emph{slot-doublet
    sectors} $j = 1$. For an orthonormal basis $(e_{a})$ of $\Lambda^{j}R_{2}$, the \emph{slot components}
    of a state $\Psi_{j} = \sum_{a} e_{a} \otimes \psi_{a}$ in rung sector $j$ are the $\psi_{a} \in \Lambda^{\bullet}W$,
    $\binom{2}{j}$ of them. A \emph{product form} on the module is a Hermitian form with $\ip{e_{a} \otimes
    \psi}{e_{b} \otimes \varphi} = \ip{e_{a}}{e_{b}}_{R}\,\ip{\psi}{\varphi}_{W}$; the structure just
    described is one. The \emph{moment} of a bivector $X \in \Lambda^{2}V_{\C}$ on a state $\Psi$ is $M_{X}(\Psi)
    = \ip{\Psi}{X\Psi}$, and for $I \in V$ the grip and the mass-squared of $\Psi$ are Fact \claimref{standard-model.imported-grip-area-casimir-form}(i)
    with this moment.

    In the same module write the mode operators $v_{a}$ (creation) and $w_{a}$ (annihilation), $a = 1,
    \ldots, 5$, modes $1, 2, 3$ those of $W$ and $4, 5$ those of $R_{2}$; \emph{the ten} is their span,
    the complexified transported ambient space $V_{\C} \oplus R_{2} \oplus \overline{R}_{2}$; \emph{rung
    vectors} are $v_{4}, v_{5}, w_{4}, w_{5}$ and \emph{pair vectors} $v_{1}, v_{2}, v_{3}, w_{1}, w_{2},
    w_{3}$. The hypercharge generator is $y = 3N_{R} - 2N_{W}$ and $2T_{3} = N_{4} - N_{5}$ in occupation
    numbers.'
  typing:
    by: ai-typing-pass
    note: Definition; no edges to type.
  env: definition
  context_refs:
  - standard-model.imported-grip-area-casimir-form
  - standard-model.imported-tower-commuting-copies-fock-module
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - standard-model.configuration-sector-carries-higgs-doublets-quantum (about)
    - standard-model.invariant-operators-module (about)
    - standard-model.reduction (about)
    - standard-model.transported-frozen-point-doublet-datum-not (about)
    - standard-model.under-s-frozen-points-split-inverse (about)
    - rungs.transported-module-holds-tuple-one-vector (about)
    - lepton.what-self-conjugacy-says-about-thirteenth (about)
    added_about: []
    verdict: connected
    note: Added about from the claims whose statements use the module's sectors, slot components or slot-doublet
      sectors.
---

## formal
Let $R_{2} = \operatorname{span}(v_{4}, v_{5})$ be the span of the two rungs' creation modes over $\C$ and $\Lambda^{\bullet}(W \oplus R_{2})$ the Fock module of the five mode pairs, three of $W$ and two of $R_{2}$, with the Hermitian structure induced by $*$ of Fact \claimref{standard-model.imported-tower-commuting-copies-fock-module} on the rung factor and by a fixed $\mathrm{Spin}(2,4)$-invariant Hermitian form on the pair factor. The \emph{sector} $(j, k)$ is $\Lambda^{j}R_{2} \otimes \Lambda^{k}W$, $j$ the rung (slot) number and $k$ the pair number; the \emph{slot-singlet sectors} are $j \in \{0, 2\}$ and the \emph{slot-doublet sectors} $j = 1$. For an orthonormal basis $(e_{a})$ of $\Lambda^{j}R_{2}$, the \emph{slot components} of a state $\Psi_{j} = \sum_{a} e_{a} \otimes \psi_{a}$ in rung sector $j$ are the $\psi_{a} \in \Lambda^{\bullet}W$, $\binom{2}{j}$ of them. A \emph{product form} on the module is a Hermitian form with $\ip{e_{a} \otimes \psi}{e_{b} \otimes \varphi} = \ip{e_{a}}{e_{b}}_{R}\,\ip{\psi}{\varphi}_{W}$; the structure just described is one. The \emph{moment} of a bivector $X \in \Lambda^{2}V_{\C}$ on a state $\Psi$ is $M_{X}(\Psi) = \ip{\Psi}{X\Psi}$, and for $I \in V$ the grip and the mass-squared of $\Psi$ are Fact \claimref{standard-model.imported-grip-area-casimir-form}(i) with this moment.
In the same module write the mode operators $v_{a}$ (creation) and $w_{a}$ (annihilation), $a = 1, \ldots, 5$, modes $1, 2, 3$ those of $W$ and $4, 5$ those of $R_{2}$; \emph{the ten} is their span, the complexified transported ambient space $V_{\C} \oplus R_{2} \oplus \overline{R}_{2}$; \emph{rung vectors} are $v_{4}, v_{5}, w_{4}, w_{5}$ and \emph{pair vectors} $v_{1}, v_{2}, v_{3}, w_{1}, w_{2}, w_{3}$. The hypercharge generator is $y = 3N_{R} - 2N_{W}$ and $2T_{3} = N_{4} - N_{5}$ in occupation numbers.

## technical
Let $R_{2} = \operatorname{span}(v_{4}, v_{5})$ and take the Fock module $\Lambda^{\bullet}(W \oplus R_{2})$ of five mode pairs, three of $W$ and two rung (slot) modes, with a product Hermitian structure. The sector $(j, k)$ is $\Lambda^{j}R_{2} \otimes \Lambda^{k}W$, with $j \in \{0, 2\}$ the slot-singlet sectors and $j = 1$ the slot-doublet sectors; a state in rung sector $j$ has $\binom{2}{j}$ slot components in $\Lambda^{\bullet}W$.

The moment of a bivector $X \in \Lambda^{2}V_{\C}$ on a state is $M_{X}(\Psi) = \ip{\Psi}{X\Psi}$, which defines the grip and the mass-squared of $\Psi$. The ten mode operators span $V_{\C} \oplus R_{2} \oplus \overline{R}_{2}$, split into rung vectors and pair vectors, and in occupation numbers the hypercharge generator is $y = 3N_{R} - 2N_{W}$ and $2T_{3} = N_{4} - N_{5}$.

## lay
This definition sets up the state space used for matter with two extra rungs of the transport tower: five pairs of creation and annihilation operations, three from the conformal spinor's own pairs and two from the rungs. States are sorted by how many rung modes and how many pair modes are occupied, and a state's pieces along the rung directions are its slot components. Hypercharge and weak isospin are then simple counts of occupied modes.

## one-liner
The two-rung module is the five-mode Fock module $\Lambda^{\bullet}(W \oplus R_{2})$, graded into sectors $(j, k)$ by rung and pair number, with slot components, a product form, moments and hypercharge $y = 3N_{R} - 2N_{W}$.
