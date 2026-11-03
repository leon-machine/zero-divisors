---
id: lepton.what-self-conjugacy-says-about-thirteenth
kind: claim
version: 3
title: What self-conjugacy says about the thirteenth generator
status: conjectured
region: lepton
subject: standard-model
tags:
- gauge-fields
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
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
lineage:
  motivated_by:
  - lepton.imported-automorphism-group-section-hypercharge-generator
  - lepton.self-conjugacy-forces-determinant-one-group
  - lepton.unit-action-cell-action
  - standard-model.majorana-element
  - standard-model.under-s-composites-state-space-spinor
locators:
  paper: T12-lepton
  number: Obs 3.2
  label: obs:thirteen
  line: 276
extraction:
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Converted the bare and the full twistor to the bare and the full conformal spinor in the formal
      level; the other levels had no twistor language.
  source_title: What self-conjugacy says about the thirteenth generator
  source_formal: 'A gauge symmetry of a theory with antiparticles must map the spectrum to itself and
    commute with conjugation: the conjugate of a state in the spectrum is in the spectrum, with the conjugate
    quantum numbers. The premise, printed: that $\Con$ is the whole constituent state space and is already
    closed under conjugation, the constituents'' antiparticles being constituents; the observed one-handed
    content of the Standard Model is a complex representation, and the requirement applies to its CPT
    completion, so the premise is that $\Con$ is that completion. Under $U(2) \times U(3)$ the constituent
    spectrum $\Con$ fails self-conjugacy (Proposition \claimref{lepton.self-conjugacy-forces-determinant-one-group}):
    the conjugate of a bare twistor in a slot, $\Con_{0}^{*}$, is not a constituent, and the full twistor
    $\Con_{3}$, which has the conjugate content, carries the wrong $K$-charge. So on that premise $K$
    is not a symmetry of the constituents, and the group acting on them is $S(U(2) \times U(3))$, the
    same group Fact \claimref{lepton.imported-automorphism-group-section-hypercharge-generator} derives
    from the cells, on which $K$ is trivial. The two agree, and the canonical section of Section \ref{sec:constituent}
    is the only action of the automorphism group on $\Con$ compatible with conjugation. The same argument
    applies to the five-mode ledger $\Lambda^{\bullet}(\C^{2} \oplus W)$ of T12''s Hypothesis (S) in its
    untwisted action, whose $(j,k)$ component has $K$-weight $j - k$: its dual is the $(2-j, 3-k)$ component
    twisted by $(\det A \cdot \det B)^{-1}$, so self-conjugacy forces the determinant-one group there
    too. T12 now shows that the state space carries the action twisted by $(\det A \cdot \det B)^{-1/2}$,
    in which the $(j,k)$ component has central character $\alpha^{j-1}\beta^{k-3/2}$ on $(\alpha I_{2},
    \beta I_{3})$ and the dual of every component is again a component, so there self-conjugacy does not
    exclude the thirteenth generator: it is the $U(1)_{X}$ of $\mathrm{Spin}(10)$, anomaly-free and broken
    at the intermediate scale by the Majorana term of $\nu^{c}$ \cite[Prop.~5.8(3), Prop.~10.7]{ButlerT12}.
    Either way it is not a cost of (S). Two limits, stated. This is a statement about consistency with
    conjugation, at the level of the CPT theorem it invokes and of the premise just printed, and is recorded
    as an Observation for that reason; T12 reaches the untwisted half of this at proposition level, without
    that premise, from the anomaly conditions: in the untwisted action every abelian generator in the
    span of the two mode numbers other than hypercharge fails three of the four conditions over the derived
    generation \cite[Prop.~5.8(3)(a)]{ButlerT12}. Self-conjugacy also singles out the canonical section
    among the actions of $S(U(2) \times U(3))$ on $\C^{2} \otimes \Sp$ that differ from it by a character:
    twisting the section by $(\det A)^{m}$, $m \in \mathbb{Z}$, shifts every weight by $6m$ (on the section
    $\det A = \lambda^{6}$) and every hypercharge by $m$, giving $Y_{L} = -\tfrac12 + m$; but the twisted
    space is self-dual only if $\Con \cong \Con \otimes (\det A)^{-2m}$, and $\det A$ is onto $U(1)$ on
    the section, so only $m = 0$ survives, as the weight multiset $\{3, 1, -1, -3\}$ shifted by $6m$ is
    closed under negation only at $m = 0$. The agreement $Y_{Q} = \tfrac16$ with the ledger''s one-cell
    states (Proposition \claimref{lepton.unit-action-cell-action}(1)) is then a check, not the argument.
    The script checks the twisted values $Y_{L} = -\tfrac52, \tfrac32$ at $m = \mp 2$ and the closure
    of the shifted multiset under negation for $m \in [-3, 3]$.'
  typing:
    by: ai-typing-pass
    note: 'Left as a conjecture with its existing lineage: the source records it as an Observation resting
      on a printed CPT premise and its script check list excludes it as a reading, not a computation.
      Levels pass: conditions already kept.'
  env: observation
  context_refs:
  - lepton.imported-automorphism-group-section-hypercharge-generator
  - lepton.self-conjugacy-forces-determinant-one-group
  - lepton.unit-action-cell-action
  - standard-model.majorana-element
  - standard-model.under-s-composites-state-space-spinor
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about:
    - obj.standard-model.two-rung-module-sectors-slot-components
    verdict: connected
    note: About the two-rung module, whose sectors (j,k) its argument on the five-mode ledger reads; terminal
      observation otherwise.
about:
- obj.standard-model.two-rung-module-sectors-slot-components
---

## formal
A gauge symmetry of a theory with antiparticles must map the spectrum to itself and commute with conjugation: the conjugate of a state in the spectrum is in the spectrum, with the conjugate quantum numbers. The premise, printed: that $\Con$ is the whole constituent state space and is already closed under conjugation, the constituents' antiparticles being constituents; the observed one-handed content of the Standard Model is a complex representation, and the requirement applies to its CPT completion, so the premise is that $\Con$ is that completion. Under $U(2) \times U(3)$ the constituent spectrum $\Con$ fails self-conjugacy (Proposition \claimref{lepton.self-conjugacy-forces-determinant-one-group}): the conjugate of a bare conformal spinor (twistor) in a slot, $\Con_{0}^{*}$, is not a constituent, and the full conformal spinor $\Con_{3}$, which has the conjugate content, carries the wrong $K$-charge. So on that premise $K$ is not a symmetry of the constituents, and the group acting on them is $S(U(2) \times U(3))$, the same group Fact \claimref{lepton.imported-automorphism-group-section-hypercharge-generator} derives from the cells, on which $K$ is trivial. The two agree, and the canonical section of Section \ref{sec:constituent} is the only action of the automorphism group on $\Con$ compatible with conjugation. The same argument applies to the five-mode ledger $\Lambda^{\bullet}(\C^{2} \oplus W)$ of T12's Hypothesis (S) in its untwisted action, whose $(j,k)$ component has $K$-weight $j - k$: its dual is the $(2-j, 3-k)$ component twisted by $(\det A \cdot \det B)^{-1}$, so self-conjugacy forces the determinant-one group there too. T12 now shows that the state space carries the action twisted by $(\det A \cdot \det B)^{-1/2}$, in which the $(j,k)$ component has central character $\alpha^{j-1}\beta^{k-3/2}$ on $(\alpha I_{2}, \beta I_{3})$ and the dual of every component is again a component, so there self-conjugacy does not exclude the thirteenth generator: it is the $U(1)_{X}$ of $\mathrm{Spin}(10)$, anomaly-free and broken at the intermediate scale by the Majorana term of $\nu^{c}$ \cite[Prop.~5.8(3), Prop.~10.7]{ButlerT12}. Either way it is not a cost of (S). Two limits, stated. This is a statement about consistency with conjugation, at the level of the CPT theorem it invokes and of the premise just printed, and is recorded as an Observation for that reason; T12 reaches the untwisted half of this at proposition level, without that premise, from the anomaly conditions: in the untwisted action every abelian generator in the span of the two mode numbers other than hypercharge fails three of the four conditions over the derived generation \cite[Prop.~5.8(3)(a)]{ButlerT12}. Self-conjugacy also singles out the canonical section among the actions of $S(U(2) \times U(3))$ on $\C^{2} \otimes \Sp$ that differ from it by a character: twisting the section by $(\det A)^{m}$, $m \in \mathbb{Z}$, shifts every weight by $6m$ (on the section $\det A = \lambda^{6}$) and every hypercharge by $m$, giving $Y_{L} = -\tfrac12 + m$; but the twisted space is self-dual only if $\Con \cong \Con \otimes (\det A)^{-2m}$, and $\det A$ is onto $U(1)$ on the section, so only $m = 0$ survives, as the weight multiset $\{3, 1, -1, -3\}$ shifted by $6m$ is closed under negation only at $m = 0$. The agreement $Y_{Q} = \tfrac16$ with the ledger's one-cell states (Proposition \claimref{lepton.unit-action-cell-action}(1)) is then a check, not the argument. The script checks the twisted values $Y_{L} = -\tfrac52, \tfrac32$ at $m = \mp 2$ and the closure of the shifted multiset under negation for $m \in [-3, 3]$.

## technical
On the printed premise that the constituent space $\Con$ is the CPT completion of the observed content, closed under conjugation, its failure of self-conjugacy under $U(2) \times U(3)$ means the kernel $K$ is not a symmetry of the constituents, so the acting group is $S(U(2) \times U(3))$, the same group derived from the cells, and the canonical section is the only action compatible with conjugation. The same argument forces the determinant-one group on the five-mode ledger of Hypothesis (S) in its untwisted action.

In the action twisted by $(\det A \cdot \det B)^{-1/2}$ that the Standard-Model paper now uses, the dual of every component is a component, so self-conjugacy does not exclude the thirteenth generator: it is the anomaly-free $U(1)_{X}$ of $\mathrm{Spin}(10)$, broken at the intermediate scale by the Majorana term of $\nu^{c}$. Self-conjugacy also excludes twisting the section by $(\det A)^{m}$ for $m \neq 0$, since the weights $\{3, 1, -1, -3\}$ shifted by $6m$ are closed under negation only at $m = 0$. The argument stands at the level of the CPT premise.

## lay
Assume the constituents already include their own antiparticles. Then requiring the symmetry to respect particle-antiparticle conjugation picks out the twelve-dimensional Standard Model group and a unique way for it to act. In the version of the state space the series now prefers, this argument no longer rules out a thirteenth symmetry direction, which turns out to be a known one from grand unification, broken at a high scale by the right-handed neutrino's mass. This is a consistency argument resting on a stated premise, not a full derivation.

## one-liner
On the premise that the constituent space is its own CPT completion, self-conjugacy selects $S(U(2) \times U(3))$ and its canonical section in the untwisted action, while in the twisted action it leaves the thirteenth generator as the anomaly-free $U(1)_{X}$.
