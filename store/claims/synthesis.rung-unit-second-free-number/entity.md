---
id: synthesis.rung-unit-second-free-number
kind: claim
version: 3
title: 'The weak scale as a second free number beside $N$'
status: postulate
region: synthesis
subject: standard-model
tags: [the-number-n, undetermined-input, symmetry-breaking]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
lineage:
  motivated_by:
  - synthesis.rung-unit-is-frame-boost
  - synthesis.rung-unit-transverse-to-norm
  - standard-model.what-derived-what-not
  - programme.n-parameter-of-the-laws
  - synthesis.einstein-route-makes-n-initial-data
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
  - synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion
extraction:
  maintainer_pass_3:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 3 (Leon''s register decision of 2026-11-01): restated. The stored D-term action with its level a constant of the action, read under the Henneaux-Teitelboim promotion, met the refutation condition of version 2 (a dynamics of the rung component under which v/H is initial data rather than a parameter of the laws; synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion). The premise now holds the level xi (strictly xi G) as the constant of the laws: v/M_P is the law up to relative order (H/v)^4, v/H is initial data under the promotion, and G v^2 N^2 = (v/H)^2 is an identity, not a law. A new refutation condition replaces the old one; the transport facts (the frame invisible to the tractor norm, the balanced frame 44 orders too low) are kept. The Hubble unit is stated in a marked note: H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0 (a factor of order one, about 0.2 in ln(v/H)).'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Version 2 (Leon's decision 3 of 2026-10-23, the Henneaux-Teitelboim promotion adopted with v/H kept as the law) adds the consequence for the register, from synthesis.einstein-route-makes-n-initial-data (iii) - with N initial data, v/M_P = (v/H)/N is initial data and G v^2 N^2 = (v/H)^2 holds as a law - and restates "beside N" since N is no longer a parameter of the laws; the premise itself (v/H a parameter of the laws, not derived and not a function of N) is unchanged. Version 1 note follows. New postulate, adopted by Leon's decision to register the rung-frame boost as a second free number beside N in the premise register. N itself is recorded as a parameter of the laws by programme.n-parameter-of-the-laws (a conjectured placement under the action as written); the rung unit has no such action-level argument, so it is registered as a premise, with the refutation condition stated, so that every result that uses a value of the weak scale can name it in holds_given.
---
## formal
\emph{Premise (rung unit), version 3.} Let $\mu > 0$ be the rung unit, the boost of the rung frame against the lift's null pair (Theorem \claimref{synthesis.rung-unit-transverse-to-norm}: $X_{\mu} = B_{1/\mu}\circ X_{1}$, rung component $c_{\mu} = -\mu w + \tfrac{\Lambda}{3\mu}v$; Theorem \claimref{synthesis.rung-unit-is-frame-boost}(4), where it is the boost $\lambda$), whose value in Hubble units is the ratio $v/H \approx 10^{44}$ of the weak scale to the Hubble scale (Proposition \claimref{standard-model.what-derived-what-not}(2)), with $H^{2} = \Lambda/3$. Transport does not fix the weak scale: every clause of totality holds in every frame and the rung component's tractor norm $-\Lambda/3$ is the same for every $\mu$ (Theorem \claimref{synthesis.rung-unit-transverse-to-norm}(1)), a change of $\mu$ is transverse to the norm mode through which $N = M_{P}/H$ enters (Theorem \claimref{synthesis.rung-unit-transverse-to-norm}(2)), and the only frame the structure singles out, the balanced frame $\mu = H$ in which the rung component lies in a $U(2)$-invariant real form up to a phase (Theorem \claimref{synthesis.rung-unit-is-frame-boost}(5), Theorem \claimref{synthesis.rung-unit-transverse-to-norm}(3)), would put the rung unit at the Hubble scale, about $44$ orders of magnitude below the observed weak scale. In the hypercharge D-term action of the rung field the frame is set by the level $\xi$, through the vacuum moment map $m^{*} = g'^{2}\xi/(g^{2} + g'^{2})$, a constant of the action that nothing in the stored structure fixes (Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}(2)). The premise: the level $\xi$, strictly the dimensionless $\xi G$ with $G = M_{P}^{-2}$, is a constant of the laws in the sense of clause (P) of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape}, fixed before variation and constant on each solution space, not derived and not a function of $N$: a second free number beside $N$. Consequently, under the Henneaux-Teitelboim promotion, which the series adopts (\claimref{programme.n-parameter-of-the-laws}) and under which $N$ is initial data:
\begin{enumerate}
\item[(a)] $v/M_{P}$ is the law: it is the same on every solution up to a relative change of order $(H/v)^{4}$, since on the boundary of the orbit space the D-term potential does not contain $H$ (Theorem \claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}(1), (2));
\item[(b)] $v/H = (v/M_{P})N$ is initial data, the branch of Theorem \claimref{synthesis.einstein-route-makes-n-initial-data}(iii) in which $v/M_{P}$ is held;
\item[(c)] $Gv^{2}N^{2} = (v/H)^{2}$ is an identity, $(v/H)^{2}$ times $G\Lambda = 3N^{-2}$, not a law: its left side is a constant of the laws exactly when $v/H$ is (Theorem \claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}(3)).
\end{enumerate}
Under the action as written, where $N$ is a parameter of the laws, $v/M_{P}$ and $v/H$ are both constant on each solution space.

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$. The two differ by the factor $\sqrt{\Omega_{\Lambda}}$, of order one: $v/H \approx 2.1 \times 10^{44}$ with $H^{2} = \Lambda/3$ and $v/H_{0} \approx 1.7 \times 10^{44}$, so $\ln(v/H)$ changes by about $0.2$. The orders of magnitude quoted here hold for both.

\emph{Version note.} Version 2 of this premise held $v/H$ as the parameter of the laws and $v/M_{P}$ as initial data under the promotion, with refutation condition a derivation of $v/H$ or a dynamics of the rung component under which $v/H$ would be initial data. The stored D-term action with its level a constant of the action, read under the promotion, is such a dynamics (Theorem \claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}): it met that condition, and the premise is restated here with the level as the constant of the laws.

\emph{Refutation condition.} The premise is false if the weak scale is derived, that is if $\xi G$ (equivalently $v/M_{P}$ up to relative order $(H/v)^{4}$) is computed from the transport structure, from another premise of the register, or from a dynamics with no further free dimensionless constant (for example a breaking pattern of the Pati-Salam stage that fixes the level, or a transmutation scale fixed by the couplings alone); or if it is shown to be a function of $N$; or if the rung action is coupled to the promoted $\Lambda$ so that the level is proportional to $\Lambda$ (a level $\hat{\xi}\Lambda$), under which $v/H$, not $v/M_{P}$, would be the law.

## technical
In the lift of the frozen point to the rung directions, the scale of the rung component, which sets the weak scale, is the boost of the rung frame against the lift's null pair. Transport cannot see it: every clause of totality holds in every boosted frame, the rung component's tractor norm is $-\Lambda/3$ whatever the boost, and a change of the boost moves the component along a level set of that norm, transverse to the direction in which $\Lambda$, and so $N$, would move it. The one frame the structure singles out, the balanced one, would put the weak scale at the Hubble scale, which is off by about $10^{44}$. In the rung field's D-term action the frame is set by the level, a constant of the action.

This premise records the decision: the level, made dimensionless as $\xi G$, is a second free number of the laws beside $N$, not derived and not a function of $N$. Under the Henneaux-Teitelboim promotion, which the series adopts, $N$ is initial data; the D-term potential at the vacuum does not contain the Hubble rate, so the weak scale against the Planck mass, $v/M_{P}$, is the law up to a relative correction of order $(H/v)^{4}$, and the rung-frame boost $v/H$ is initial data. The relation $Gv^{2}N^{2} = (v/H)^{2}$ is an identity in the units used, not a law. An earlier version held $v/H$ as the law; the D-term action read under the promotion met its refutation condition, and it is restated here. The premise would be refuted by a derivation of $\xi G$, from the transport structure, another premise, or a dynamics with no further free constant, by a proof that it is a function of $N$, or by a coupling of the rung action to the promoted $\Lambda$ that makes the level proportional to it.

## lay
In this framework almost every hierarchy of scales comes from one huge number, N, the ratio of the Planck mass to the scale set by the cosmological constant. The strength of the weak force's symmetry breaking, about 246 GeV, does not: it is set by how a particular reference frame in the extra dimensions is stretched, and the framework's construction works equally well for every stretch. The only stretch the structure itself prefers gives a weak scale far too small, by 44 powers of ten. In the field theory written for the Higgs field the stretch is fixed by one constant, and this assumption accepts that constant as a second basic number of the laws, put in by hand beside N. Since the framework treats N as a fact about the universe's history, the weak scale measured against the Planck mass is then the law, and the weak scale measured against the cosmological scale is a historical fact. It would be overturned if anyone derived the constant, showed it follows from N, or tied it to the cosmological constant.

## one-liner
Premise, version 3: the weak scale's constant of the laws is the D-term level $\xi$ (strictly $\xi G$), not derived and not a function of $N$; under the promoted action $v/M_{P}$ is the law up to relative order $(H/v)^{4}$, $v/H \approx 10^{44}$ ($H^{2} = \Lambda/3$) is initial data, and $Gv^{2}N^{2} = (v/H)^{2}$ is an identity, not a law.
