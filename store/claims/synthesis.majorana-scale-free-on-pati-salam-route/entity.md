---
id: synthesis.majorana-scale-free-on-pati-salam-route
kind: claim
version: 4
title: 'The Majorana scale is free on the Pati-Salam route'
status: proved
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, undetermined-input, neutrino-premises, flavour-and-mixing]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: strengthened check and wording
  version: 3
  source: maintainer pass of 7 November 2026
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - standard-model.imported-clebsch-structure-seesaw@1
  - synthesis.majorana-scale-is-126-doublet-vev@2
  - synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition@1
  - standard-model.fits-record-level@6
  - standard-model.what-angle-asks-neutrino-sector@4
  - standard-model.chain@8
  - neutrino.rank-one-seesaw-ordering-sum-double@8
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dirac_matrices_invariant_majorana_scales
- kind: check
  ref: check.py::check_light_masses_scale_mixing_invariant
- kind: check
  ref: check.py::check_ew_and_dirac_reading_of_u_invariant
- kind: check
  ref: check.py::check_fit_observables_one_scale
- kind: check
  ref: check.py::check_stored_inequalities_leave_an_interval
- kind: check
  ref: check.py::check_electroweak_normalisation_restored
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.majorana-scale-is-126-doublet-vev
  - neutrino.m-framework-realises-majorana-term-scale
  - standard-model.what-angle-asks-neutrino-sector
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complex test values of the scale lambda in the proof are written with I_4: {7/3, 2 + I_4, -1/5 + 3 I_4/4} (numbers, and C, read in span{1, I_4}); nothing stays.'
  maintainer_pass_warnings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3: check_light_masses_scale_mixing_invariant now also checks the explicit scale 2 (I1 falls by 4, the determinant by 64), so the mutation test has literals to perturb; the fermion mass matrices are now called Dirac mass matrices throughout, to avoid confusion with gamma matrices.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)); a marked note says that the registered free numbers are now N and the level xi G (synthesis.rung-unit-second-free-number version 3) and that clause (v), stated at fixed N and v/H, holds in either register. Nothing else is changed.'
  open_problem: op.majorana-scale
  note: 'Independence result for the problem''s second success branch. The stored work reduced the Majorana scale to one unknown (the 126 doublet admixture w_u); this shows that unknown is free with respect to every stored relation: a one-parameter group (f to lam f, w_u and w_d to w/lam, triplet vev, 10 and 120 data fixed) leaves the four Dirac mass matrices, (EW), the Dirac-eigenvalue reading of Hypothesis (U), the chain and seventeen of the eighteen fitted observables unchanged, and moves only M_R (by lam) and the light masses (by 1/lam). So the only stored datum that fixes the scale is the observed m_3, and the problem''s premise that one vev sets both M_I and M_R, so that deriving it would predict the weak angle, holds for v_R and not for M_R: the vev and the Majorana coupling are two numbers. Neither N nor v/H enters any relation the group acts on, so M is an input beside the two registered free numbers, related to neither by any stored relation. The electroweak normalisation of the doublet vevs, not a stored relation, is restored by composing with a rescaling of the 10 (and 120) couplings against their vevs. The symmetry is of the stored relations only: the two-loop gauge running with Yukawa terms (not in the store) would break it at order Tr(f f^dag)/(16 pi^2) relative to the one-loop terms, a weak over-determination that has not been computed. Transport-absent (standard Pati-Salam Clebsch algebra); the transport content is upstream, in the Majorana element and the chain.'
---

## formal
Assume Fact \claimref{standard-model.imported-clebsch-structure-seesaw}: with $10$ couplings $Y_{a}$, one $126$ coupling $f$ (symmetric) and one $120$ coupling $h$ (antisymmetric), $M_{u} = \sum_{a}v_{u}^{a}Y_{a} + w_{u}f + c_{u}h$, $M_{\nu} = \sum_{a}v_{u}^{a}Y_{a} - 3w_{u}f + c_{\nu}h$, $M_{d} = \sum_{a}v_{d}^{a}Y_{a} + w_{d}f + c_{d}h$, $M_{e} = \sum_{a}v_{d}^{a}Y_{a} - 3w_{d}f + c_{e}h$, $M_{R} = v_{R}f$ and $m_{\nu} = -M_{\nu}M_{R}^{-1}M_{\nu}^{\mathsf{T}}$. For $\lambda \in \C^{\times}$ let $g_{\lambda}$ act on the data by $f \mapsto \lambda f$, $(w_{u}, w_{d}) \mapsto (w_{u}/\lambda, w_{d}/\lambda)$, with $Y_{a}$, $h$, $v_{u}^{a}$, $v_{d}^{a}$, the four $c$'s and $v_{R}$ fixed. The electroweak normalisation of the doublet vevs is not among the stored relations and is not invariant under $g_{\lambda}$; composing $g_{\lambda}$ with $(Y_{a}, v^{a}_{u}, v^{a}_{d}) \mapsto (\mu_{a}Y_{a}, v^{a}_{u}/\mu_{a}, v^{a}_{d}/\mu_{a})$ on the $10$s (and likewise $(h, c) \mapsto (\nu h, c/\nu)$ on the $120$ data), which fixes every Dirac matrix, restores it, and (i) to (v) hold for the composite.
\begin{enumerate}
\item[(i)] \emph{(What moves.)} $M_{u}, M_{\nu}, M_{d}, M_{e}$ are invariant; $M_{R} \mapsto \lambda M_{R}$ and $m_{\nu} \mapsto \lambda^{-1}m_{\nu}$. Hence $m_{\nu}m_{\nu}^{\dagger} \mapsto |\lambda|^{-2}m_{\nu}m_{\nu}^{\dagger}$: the lepton mixing and every ratio of light masses are invariant, the heavy masses scale by $|\lambda|$ and the light ones by $|\lambda|^{-1}$.
\item[(ii)] \emph{(What the store fixes is invariant.)} Premise (EW), $4w_{u}f_{33} = m_{t}$ with $(M_{\nu})_{33} = 0$, is invariant; so is Hypothesis (U) in its Dirac-eigenvalue reading, a condition on the singular values of $M_{\nu}$ (Theorem \claimref{synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition}). The chain (Proposition \claimref{standard-model.chain}) and the triplet vev $v_{R} = M_{I}/g_{R}$ it gives (Proposition \claimref{standard-model.what-angle-asks-neutrino-sector}) are determined by the gauge content and the gauge coefficients, so they are invariant. Of the eighteen observables the fits of Proposition \claimref{standard-model.fits-record-level} reproduce, seventeen (nine charged-fermion masses, four CKM numbers, three lepton angles, $m_{3}/m_{2}$) are invariant and one, $m_{3}$, scales by $|\lambda|^{-1}$.
\item[(iii)] \emph{(The scale is valued, not derived.)} Consequently, if any one model of these relations reproduces the record, the orbit $\{g_{\lambda}\}$ of that model satisfies every stored equality except the value of $m_{3}$, and the stored relations determine the Majorana scale only through the observed $m_{3}$: the heavy-direction entry $(M_{R})_{33} = m_{t}v_{R}/(4w_{u})$ (Theorem \claimref{synthesis.majorana-scale-is-126-doublet-vev}) is a free input on the stored relations. Its admissible range is set by inequalities: perturbativity $|f_{33}| \le 4\pi$ and $|w_{u}| \le v$ give $m_{t}v_{R}/(4v) \le |(M_{R})_{33}| \le 4\pi v_{R}$, a range wider than a factor $83$ for $m_{t}(M_{I}) \le 100$ GeV, and the gravitational-seeding window for the odd towers under Premise (R), $M_{3} > 1.36 \times 10^{12}$ GeV, lies wholly above it.
\item[(iv)] \emph{(One vev, two numbers.)} On this route the triplet vev sets $M_{I}$ through the gauge coupling and $M_{R}$ through the Yukawa coupling $f$. A derivation of $v_{R}$ would make $\sin^{2}\theta_{W}$ a prediction (one more equation for the chain's three unknowns) and would leave $M_{R}$ free; a derivation of $M_{R}$ alone fixes $\lambda$ and predicts nothing about $\sin^{2}\theta_{W}$. Only a relation fixing $f$ (or $w_{u}$) in terms of the gauge data would do both.
\item[(v)] \emph{(Not a function of $N$ or $v/H$.)} Neither $N = M_{P}/H$ nor the rung unit $v/H$ appears in any relation of (i) to (iii), so $g_{\lambda}$, composed as above when the electroweak normalisation is imposed, acts at fixed $N$ and $v/H$: on the stored relations the Majorana scale is an input beside them, not a function of them.
\end{enumerate}

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). No number here depends on the choice. \emph{Note (register, 2026-11-01).} The two registered free numbers are $N$ and, since version 3 of \claimref{synthesis.rung-unit-second-free-number}, the D-term level $\xi G$ in place of $v/H$; the group of (v) acts at fixed $N$ and $v/H$, hence at fixed $v/M_{P} = (v/H)/N$, so (v) holds in either register.

## technical
Every quantity that the Pati-Salam Clebsch structure feeds into the store's Dirac sector contains the $126$ coupling only through the products $w_{u}f$ and $w_{d}f$. So rescaling $f$ by $\lambda$ and both $126$ doublet admixtures by $1/\lambda$ changes no Dirac mass matrix, multiplies the Majorana matrix $M_{R} = v_{R}f$ by $\lambda$, and divides the light matrix by $\lambda$. Premise (EW), the Dirac reading of Hypothesis (U), the chain's scales, and seventeen of the eighteen fitted observables are unchanged; only the overall light scale $m_{3}$ moves. The check verifies this exactly on complex rational instances with two $10$s, a $126$ and a $120$, for three values of $\lambda$ (one complex), including an instance with (EW) imposed, and verifies that scaling $f$ alone is not a symmetry.

So the Majorana scale is fixed on the stored relations only by the observed $m_{3}$, and between the bounds perturbativity and $|w_{u}| \le v$ put on it, which span about two orders of magnitude. The triplet vev of the chain sets $M_{I}$ through the gauge coupling and $M_{R}$ through $f$: deriving the vev would predict the weak angle and leave $M_{R}$ open, so "one vev sets both" is one vev and two numbers. Neither $N$ nor $v/H$ enters these relations; the electroweak normalisation of the doublet vevs, which is not stored, is kept by composing with a rescaling of the $10$ and $120$ couplings against their vevs. The symmetry is of the stored relations only; two-loop Yukawa terms in the gauge running, which the store does not include, would break it weakly.

## lay
In the version of the theory where the strong force and the leptons unify at an intermediate stage, the heavy neutrino mass is a Higgs field's value times a coupling. The value is fixed by the measured strength of the weak force, but the coupling is not: every relation the theory has stored stays exactly true if the coupling is doubled and another, unmeasured Higgs mixing is halved, except the light neutrino masses, which halve. So the heavy neutrino scale is read off the observed neutrino masses, not derived: on this route it is one more input of the theory, which no stored relation ties to the two numbers already registered.

## one-liner
On the Pati-Salam route every stored relation is invariant under $f \mapsto \lambda f$, $w_{u,d} \mapsto w_{u,d}/\lambda$ except the light masses, which scale by $\lambda^{-1}$, so the Majorana scale is fixed only by the observed $m_{3}$, between bounds about two orders apart; deriving the triplet vev would predict $\sin^{2}\theta_{W}$ and leave $M_{R}$ free, and neither $N$ nor $v/H$ enters.
