---
id: synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion
kind: claim
version: 2
title: Under the Henneaux-Teitelboim promotion, the rung field's D-term action with its level a constant of the action fixes $\xi G$, hence the weak scale against the Planck mass up to relative order $(H/v)^{4}$, while $v/H$ is initial data; $v/H$ is the same on every solution only if the level is proportional to $\Lambda$, and $Gv^{2}N^{2} = (v/H)^{2}$ is an identity, a constant of the laws exactly when $v/H$ is, so it does not decide the branch
status: proved
region: synthesis
subject: standard-model
tags: [the-number-n, undetermined-input, symmetry-breaking]
proposed_by:
  kind: ai
  session: 2026-11-01-weak-scale
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@3
  - synthesis.einstein-route-makes-n-initial-data@4
  - synthesis.smallness-monomials-exact-hierarchy-casimir@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_level_vacuum_moment_map_independent_of_h
- kind: check
  ref: check.py::check_ratio_fixed_by_the_laws
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-unit-second-free-number
  - programme.n-parameter-of-the-laws
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 (Leon''s register decision of 2026-11-01): a marked note records that synthesis.rung-unit-second-free-number version 3 adopts the assignment this result derives, so the technical level, the lay text and the one-liner now say that the premise met here is its version 2. The clauses are unchanged.'
  open_problem: op.rung-unit
  note: >-
    Taken adversarially: the D-term result reads its level xi as the rung-unit premise in dynamical form,
    and the premise (version 2) says that under the promotion the series adopts v/H is a parameter of the
    laws and v/M_P initial data. The two do not match. On the boundary of the orbit space N^2 - m^2 = H^4
    the stored D-term potential has no H at all, so its vacuum moment map m* = g'^2 xi/(g^2 + g'^2) is the
    same on every solution of the promoted theory, and N* = sqrt(m*^2 + H^4) follows Lambda only at relative
    order H^4/m*^2, of order (H/v)^4. With g, g', xi and G constants of the action, xi G (equivalently m* G)
    is fixed by the laws, M_W/M_P is constant on the solution set up to relative order (H/v)^4, and M_W/H is
    initial data: the second branch of synthesis.einstein-route-makes-n-initial-data (iii), under which that
    entity records that the rung-unit premise as worded fails. Read under the promotion, the stored D-term
    action therefore meets the refutation condition of synthesis.rung-unit-second-free-number (version 2): a
    dynamics of the rung component under which v/H is initial data rather than a parameter of the laws. The premise's branch needs a level
    proportional to Lambda, a coupling of the rung action to the promoted Lambda (argued: it would add the
    rung's moment-map density to the equation of the conjugate time). The relation G v^2 N^2 = (v/H)^2 is
    (v/H)^2 times the identity G Lambda = 3 N^-2: an identity, whose left side is a constant of the laws exactly
    when v/H is, so it does not decide between the branches. Transport-absent in content; it
    bears on how the premise register states the weak scale. No value of v/H is computed.
---
## formal
Let the rung field have the D-term action of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}, with the couplings $g$, $g'$ and the level $\xi \neq 0$ constants of the action, on the locus $L = \{Q(c) = -H^{2}\}$, $H^{2} = \Lambda/3$, and read the theory under the Henneaux-Teitelboim promotion, so that $\Lambda$, and with it $N = M_{P}/H$, is initial data while $G = M_{P}^{-2}$ is a constant of the action (Theorem \claimref{synthesis.einstein-route-makes-n-initial-data}(ii), (iii)).
\begin{enumerate}
\item \emph{(The vacuum moment map does not see $\Lambda$.)} On the boundary $N^{2} - m^{2} = H^{4}$ of the orbit space, $V_{D} = \tfrac12\bigl(\tfrac{g^{2}}{4}m^{2} + g'^{2}(\tfrac{m}{2} - \zeta)^{2}\bigr)$, $\xi = 2\zeta$, with no dependence on $H$. Its minimum $m^{*} = g'^{2}\xi/(g^{2} + g'^{2})$ is therefore the same on every solution, and $N^{*} = \sqrt{m^{*2} + H^{4}}$ satisfies $0 < N^{*} - |m^{*}| \le H^{4}/(2|m^{*}|)$.
\item \emph{(Which ratio the laws fix.)} Consequently $\xi G$, equivalently $m^{*}G$, is fixed by the laws, and $M_{W}^{2}/M_{P}^{2} = \tfrac12 g^{2}N^{*}G$ is the same on every solution up to a relative change at most $H^{4}/(2m^{*2})$, of order $(H/v)^{4}$, while $N^{*}/H^{2} = \sqrt{1 + m^{*2}/H^{4}}$ is strictly decreasing in $H$: the weak scale in Hubble units takes different values on different solutions. The D-term action with a constant level is thus the branch of Theorem \claimref{synthesis.einstein-route-makes-n-initial-data}(iii) in which $v/M_{P}$ is held and $v/H$ is initial data. $N^{*}/H^{2}$ is the same on every solution exactly when $m^{*}/H^{2}$ is, that is, when the level is proportional to $\Lambda$.
\item \emph{(The relation is an identity.)} With $G = M_{P}^{-2}$ and $N = M_{P}/H$, $Gv^{2}N^{2} = (v/H)^{2}$ is an identity, $(v/H)^{2}$ times the identity $G\Lambda = 3N^{-2}$ of Proposition \claimref{synthesis.smallness-monomials-exact-hierarchy-casimir}(i). Its left side is a constant of the laws exactly when $v/H$ is, so it does not decide between the branches of Theorem \claimref{synthesis.einstein-route-makes-n-initial-data}(iii).
\end{enumerate}

\emph{Note (register, 2026-11-01).} The rung-unit premise has been restated on this branch: its version 3 (\claimref{synthesis.rung-unit-second-free-number}) holds the level $\xi G$ as the constant of the laws, $v/M_{P}$ as the law up to relative order $(H/v)^{4}$, $v/H$ as initial data, and $Gv^{2}N^{2} = (v/H)^{2}$ as an identity. The refutation condition met here is that of its version 2.

## technical
The rung field's D-term action puts its vacuum on the boundary of the orbit space, where the norm and the hypercharge moment map are tied by $N^{2} - m^{2} = H^{4}$. On that boundary the potential depends on the moment map alone, with no trace of the cosmological constant, so the vacuum moment map is fixed by the level and the couplings, and the norm follows the cosmological constant only through a correction of relative size $H^{4}/m^{*2}$. Under the Henneaux-Teitelboim promotion the cosmological constant is initial data while the level, the couplings and Newton's constant stay constants of the action. The level times Newton's constant is then fixed by the laws, so the weak scale against the Planck mass is fixed up to a relative correction of order $(H/v)^{4}$, and the weak scale against the Hubble scale is initial data: the opposite of the assignment version 2 of the rung-unit premise made, which this dynamics met as its refutation condition (version 3 of the premise adopts this assignment). The premise's assignment holds only if the level scales with the cosmological constant, a coupling the stored action does not have. The relation $Gv^{2}N^{2} = (v/H)^{2}$ that the register cites is an identity in the units used; it is a constant of the laws exactly when $v/H$ is, so it does not decide between the branches.

## lay
The framework treats one number, the ratio of the Planck mass to the scale of the cosmological constant, as a fact about the history of the universe rather than a law. A second number, the strength of the Higgs field, is supposed to be a law when it is measured against the cosmological scale. But the framework's own candidate equation for the Higgs field contains a fixed constant that does not know about the cosmological scale at all. Read with the history-dependent cosmological constant, that equation makes the Higgs strength a law when measured against the Planck mass instead, and a historical fact when measured against the cosmological scale. The two statements are incompatible: either the stated law is changed to the Planck-mass ratio, or the constant in the equation must be tied to the cosmological constant. The framework has since changed the stated law to the Planck-mass ratio.

## one-liner
On the orbit-space boundary the stored D-term potential has no $H$, so with a constant level $m^{*}$ is the same on every promoted solution and $N^{*} = \sqrt{m^{*2} + H^{4}}$: under the promotion $\xi G$ is fixed, $v/M_{P}$ is fixed up to relative order $(H/v)^{4}$ and $v/H$ is initial data, against version 2 of the rung-unit premise (its refutation condition; version 3 adopts this assignment), unless the level is proportional to $\Lambda$; $Gv^{2}N^{2} = (v/H)^{2}$ is an identity that does not decide the branch.
