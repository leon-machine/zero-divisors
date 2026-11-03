---
id: synthesis.majorana-scale-free-input
kind: claim
version: 2
title: 'The Majorana scale along the heavy direction (the $126$ Yukawa coupling, equivalently the $126$ doublet admixture $w_{u}$) is an input of the laws beside $N$ and $v/H$, fixed in value by $m_{3}$'
status: postulate
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, undetermined-input, neutrino-premises]
proposed_by:
  kind: ai
  session: maintainer-2026-10-23
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
  - synthesis.majorana-scale-free-on-pati-salam-route
  - synthesis.majorana-scale-is-126-doublet-vev
  - synthesis.rung-unit-second-free-number
  - neutrino.m-framework-realises-majorana-term-scale
  - synthesis.majorana-scale-not-carried-by-rung-frame-boost
extraction:
  maintainer_pass_weak_scale:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: synthesis.majorana-scale-not-carried-by-rung-frame-boost is added to the lineage, with a marked note that the rung-frame boost does not tie the Majorana scale to v/H (the frame-tied relation is excluded by the record for order-one couplings, and the stored null Majorana element is not tied at all), so the scale stays an input; a marked register note reads ''beside N and v/H'' as ''beside N and the rung unit''s level'' after synthesis.rung-unit-second-free-number version 3; a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)). The premise is unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'New postulate, adopted by Leon''s decisions 8 and 16 of 2026-10-23 to register the Majorana scale as an input of the laws beside N and v/H, modelled on synthesis.rung-unit-second-free-number. It rests on synthesis.majorana-scale-free-on-pati-salam-route, which shows the scale is free on every stored relation and fixed only by the observed m_3; it registers that freedom as a premise, with a refutation condition, so that results using a value of the Majorana scale can name it in holds_given. No premise that the Majorana coupling is one (f_J = 1) is taken. No result is given an assumes edge to it in this pass.'
---

## formal
\emph{Premise (Majorana scale).} On the Pati-Salam route with the Clebsch structure of Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, let the \emph{Majorana scale} be the heavy-direction entry $(M_{R})_{33} = v_{R}f_{33}$ of the right-handed Majorana matrix $M_{R} = v_{R}f$, set by the $126$ Yukawa coupling $f$ along the heavy direction; under Premise (EW) it equals $m_{t}v_{R}/(4w_{u})$, so it is equivalently the $126$ doublet admixture $w_{u}$ (Theorem \claimref{synthesis.majorana-scale-is-126-doublet-vev}). Then the Majorana scale is an input of the laws beside $N = M_{P}/H$ and the rung unit $v/H$ (Premise \claimref{synthesis.rung-unit-second-free-number}): a number the laws take as given, which no relation of the series derives and which is not a function of $N$, $v/H$ or the gauge data. Its value is fixed by the observed light-neutrino scale $m_{3}$: on the stored relations the one-parameter group $f \mapsto \lambda f$, $(w_{u}, w_{d}) \mapsto (w_{u}, w_{d})/\lambda$ (composed with a rescaling of the $10$ and $120$ couplings against their vevs when the electroweak normalisation of the doublet vevs is imposed) fixes every Dirac matrix, (EW), the Dirac-eigenvalue reading of Hypothesis (U), the chain and the triplet vev, and seventeen of the eighteen fitted observables, and moves only $M_{R}$ by $\lambda$ and $m_{3}$ by $|\lambda|^{-1}$ (Theorem \claimref{synthesis.majorana-scale-free-on-pati-salam-route}).

\emph{What it is for.} It records as a decision what Theorem \claimref{synthesis.majorana-scale-free-on-pati-salam-route} shows of the stored relations: the Majorana scale is valued, not derived, so results that use a value of the heavy neutrino masses on the Pati-Salam route (the seesaw valuations of the neutrino sector, the seeding window and the caps on the lightest heavy neutrino) can name this premise in their holds-given instead of an unstated input. It does not say that the scale is independent of $N$ and $v/H$ in every completion of the theory, only that no relation of the series ties them, and it adds no relation fixing the coupling: in particular it does not take the Majorana coupling to be one. On this route the fits already have more couplings than observables, so the scale is one more fitted input among several; what the premise singles out is that it is the one input the stored relations fix only through $m_{3}$.

\emph{Note (the rung-frame boost, 2026-11-01).} Theorem \claimref{synthesis.majorana-scale-not-carried-by-rung-frame-boost} shows that the rung-frame boost does not tie the Majorana scale to $v/H$: a Majorana vev whose size is fixed in Hubble units in one frame and read in the weak frame is excluded by the record for order-one couplings, under each of the three extensions of the boost it considers, and the stored Majorana element is null, so the frame fixes no size for it. The scale stays an input, whatever the status of $v/H$.

\emph{Note (register, 2026-11-01).} Version 3 of \claimref{synthesis.rung-unit-second-free-number} registers the weak scale's constant of the laws as the D-term level $\xi G$, with $v/M_{P}$ the law and $v/H$ initial data under the promotion; ``beside $N$ and the rung unit $v/H$'' above reads ``beside $N$ and the rung unit's level''. What this premise asserts of the Majorana scale is unchanged.

\emph{Refutation condition.} The premise is false if the Majorana scale is derived: from the series' own dynamics (a potential at the intermediate scale that fixes $w_{u}$, a norm or incidence condition on the Majorana element of the kind that fixes the frozen point's norm, or a relation fixing $f$ in terms of the gauge data), from another premise of the register, or as a function of $N$ or $v/H$; or if a relation outside the stored ones that the physics requires, such as the two-loop gauge running with Yukawa terms, is shown to break the scaling of Theorem \claimref{synthesis.majorana-scale-free-on-pati-salam-route} strongly enough that the gauge data and the measured weak angle fix $f$ and with it the scale.

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). No number here depends on the choice.

## technical
On the Pati-Salam route the heavy right-handed neutrino masses are the triplet vev times the $126$ Yukawa coupling. The triplet vev is fixed by the measured weak angle through the chain, but the coupling is not: every relation the store holds is unchanged if the coupling along the heavy direction is scaled up and the $126$ doublet admixture down by the same factor, except the light neutrino masses, which scale inversely. So the store fixes the Majorana scale only through the observed $m_{3}$.

This premise records that as a decision: the Majorana scale, equivalently the $126$ doublet admixture $w_{u}$, is an input of the laws beside $N$ and the rung unit $v/H$, fixed in value by $m_{3}$ and not by any relation of the series. No unit coupling is assumed. It would be refuted by a derivation of the scale from the series' dynamics or from another premise, by a proof that it is a function of $N$ or $v/H$, or by a relation the store does not yet contain, such as two-loop running with Yukawa terms, that breaks the scaling and fixes the coupling.

## lay
In the version of the theory where the strong force and the leptons unify at an intermediate stage, the mass of the heavy neutrinos is a Higgs field's value times a coupling. The field's value is fixed by the measured strength of the weak force, but nothing in the theory fixes the coupling: it can be traded against another unmeasured quantity without changing anything the theory predicts, except the masses of the light neutrinos. This assumption accepts that the heavy neutrino scale is one more basic number put in by hand, beside the two the framework already has, and reads its value off the observed neutrino masses. It would be overturned if anyone derived it from the framework.

## one-liner
Premise: the Majorana scale along the heavy direction (the $126$ Yukawa coupling there, equivalently the $126$ doublet admixture $w_{u}$) is an input of the laws beside $N$ and $v/H$, fixed in value by the observed $m_{3}$ and derived by no relation of the series.
