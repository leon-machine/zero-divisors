---
id: synthesis.two-loop-running-cannot-fix-majorana-coupling
kind: claim
version: 2
title: 'Two-loop running cannot fix the Majorana coupling'
status: proved
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, undetermined-input, running-and-unification, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
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
review: draft
derivations:
- name: main
  uses:
  - synthesis.imported-two-loop-yukawa-gauge-terms@1
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.majorana-element@7
  - standard-model.imported-pati-salam-representation-theory-survival@1
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.matching-traces@4
  - standard-model.spectrum-run@6
  - standard-model.chain@8
  - synthesis.majorana-scale-free-on-pati-salam-route@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_component_sums_are_unit_multiples
- kind: check
  ref: check.py::check_yukawa_casimir_vectors
- kind: check
  ref: check.py::check_running_family_never_fixes_eps
- kind: check
  ref: check.py::check_sensitivities
- kind: check
  ref: check.py::check_given_mi_alpha_s_band_in_trace
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.majorana-scale-free-on-pati-salam-route
  - synthesis.majorana-scale-free-input
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complex scalar components Phi_c = (phi_c1 + I_4 phi_c2)/sqrt 2 and the Yukawa matrix Y^{c2} = I_4 (y tensor T^c)/sqrt 2 in the proof are written with I_4 (numbers read in span{1, I_4}); nothing stays. Wording, to clear W222: "Dirac matrices" (the Dirac mass matrices, not gamma matrices) now reads "Dirac mass matrices".'
  open_problem: op.majorana-scale
  note: 'Answers the problem''s second line of attack (two-loop gauge running with Yukawa terms on the chain) in the negative, using the imported Machacek-Vaughn Fact, which no stored result had used. Two findings. First, a selection rule: every Yukawa coupling of Dirac type (psi psi^c with a scalar in any representation; on the chains the bidoublet and the (15,2,2), whichever 10, 120 or 126 they descend from) enters the three Pati-Salam couplings with the same weight (1/4) dim R Tr(y y^dag), which the matching at M_I keeps universal, so it moves alpha_U only; the Majorana coupling f of the (10,1,3) is the only Yukawa that moves M_I and M_U, with the matched vector (6, 0, 15/4) Tr(f f^dag). Second, a count: for every value of the averaged trace the running is a nonsingular linear system in (alpha_U^-1, x, y), so the three measured couplings fix the scales as functions of f and never f. The two-loop terms break the scaling symmetry of the stored relations into a one-parameter family M_I(f), along which the observed m_3 is still the only datum; the premise synthesis.majorana-scale-free-input survives at two loops. Sizes are at the one-loop baseline of the chain (computed exactly, certified pi): Tr(f f^dag) = 1 raises ln M_I by 0.08 to 0.11, comparable with the alpha_s one-sigma move (0.03 to 0.05) and with moving the (10,1,3) threshold off M_I by a factor 1.5 to 1.8; so even a derived M_I would fix Tr(f f^dag) only to about 0.4 per sigma of alpha_s. Normalisation: M_R = v_R f with canonically normalised orthonormal scalar components (stated in the proof); the selection rule and the count do not depend on it. Transport-absent (standard Pati-Salam group theory and running); the transport content is upstream, in the Majorana element and the chain.'
---

## formal
Take the chains of Proposition \claimref{standard-model.chain} (real bidoublet, complex bidoublet, complex bidoublet with the $(15,2,2)$), with $x = \ln(M_{I}/M_{Z})/2\pi$, $y = \ln(M_{U}/M_{I})/2\pi$, the matching $a_{1} = \tfrac35 a_{2R} + \tfrac25 a_{4}$, $a_{2} = a_{2L}$, $a_{3} = a_{4}$ of Lemma \claimref{standard-model.matching-traces} and the inputs of Proposition \claimref{standard-model.spectrum-run}. Write the Majorana coupling of the $(10,1,3)$ as $-\mathcal{L} \supset \tfrac12 f_{ij}\,\psi^{c}_{i}\psi^{c}_{j}\Delta_{R}$ with $\psi^{c} = (\bar{4},1,2)$ and canonically normalised components, so that $M_{R} = v_{R}f$ (Fact \claimref{standard-model.imported-clebsch-structure-seesaw}), and a Dirac-type coupling as $y_{ij}\,\psi_{i}\psi^{c}_{j}\Phi$ with $\psi = (4,2,1)$ and $\Phi$ in a representation $R \subset (4,2,1)\otimes(\bar{4},1,2)$. Apply Fact \claimref{synthesis.imported-two-loop-yukawa-gauge-terms} on $M_{I} < \mu < M_{U}$.
\begin{enumerate}
\item[(i)] \emph{(Selection rule.)} A Dirac-type coupling contributes $Y_{4} = \tfrac14\dim R\,\mathrm{Tr}(yy^{\dagger})\,(1,1,1)$ to $(SU(4), SU(2)_{L}, SU(2)_{R})$, universal also after the matching; it shifts $\alpha_{U}^{-1}$ and leaves $M_{I}$ and $M_{U}$ unchanged. The scalars light on $(M_{I}, M_{U})$ other than the $(10,1,3)$, the bidoublet ($\dim R = 4$) and the $(15,2,2)$ ($\dim R = 60$), couple only in this way, whichever $10$, $120$ or $126$ they descend from. The $(10,1,3)$ coupling contributes $(\tfrac{15}{4}, 0, \tfrac{15}{2})\,\mathrm{Tr}(ff^{\dagger})$, matched $v = (6, 0, \tfrac{15}{4})\,\mathrm{Tr}(ff^{\dagger})$: it is the only Yukawa coupling of the chains that moves the scales at two loops.
\item[(ii)] \emph{(The running never fixes the coupling.)} With $\varepsilon = \langle\mathrm{Tr}(ff^{\dagger})\rangle/16\pi^{2}$, the average over $\ln\mu$ on $(M_{I}, M_{U})$, the running reads $a_{i}(M_{Z}) = a_{U} + b_{i}^{\mathrm{SM}}x + (b_{i}^{\mathrm{eff}} - \varepsilon v_{i})\,y + u$, with $u$ the universal Dirac-type shift. For each chain its determinant is $D_{0} + \tfrac{201}{4}\varepsilon$, the coefficient $\tfrac{201}{4} = -[6(b^{\mathrm{SM}}_{3} - b^{\mathrm{SM}}_{2}) + \tfrac{15}{4}(b^{\mathrm{SM}}_{2} - b^{\mathrm{SM}}_{1})]$ the same for every chain (it involves only the columns $1$ and $b^{\mathrm{SM}}$), with $D_{0} = \tfrac{364}{15}, \tfrac{386}{15}, \tfrac{114}{5}$, positive for every $\varepsilon \ge 0$, so the three measured couplings fix $(a_{U}, M_{I}, M_{U})$ uniquely as functions of $\varepsilon$ and do not fix $\varepsilon$; $M_{I}$ rises strictly with $\varepsilon$.
\item[(iii)] \emph{(Sizes, one-loop baseline.)} $d\ln M_{I}/d\,\mathrm{Tr}(ff^{\dagger})$ lies in $(0.09, 0.10)$, $(0.08, 0.09)$ and $(0.10, 0.11)$ for the three chains, against a move of $\ln M_{I}$ between $0.03$ and $0.05$, opposite in sign, for $\alpha_{s} \to \alpha_{s} \pm 0.0009$. If $M_{I}$ were supplied (or $M_{U}$, for instance from proton decay), the measured couplings would fix $\mathrm{Tr}(ff^{\dagger})$ near one, but only to within more than $\pm 0.3$ per standard deviation of $\alpha_{s}$. So the statement "never" in (ii) is the count with the three gauge couplings as the only data.
\end{enumerate}
So the two-loop Yukawa terms break the scaling symmetry of Theorem \claimref{synthesis.majorana-scale-free-on-pati-salam-route} only into a one-parameter family $M_{I}(f)$: along it $m_{3} \propto 1/(|\lambda|\,v_{R}(\lambda))$ is strictly monotone, so the observed $m_{3}$ is still the one datum that values the Majorana scale, and the running of the gauge couplings supplies no relation that fixes it. The algebraic companion, filed alongside, is synthesis.majorana-element-is-null-blade-no-frozen-point-condition: no invariant algebraic condition on the Majorana element fixes the scale either.

## technical
The problem asked whether two-loop gauge running with Yukawa terms, which first feel the Yukawa couplings, could fix the Majorana coupling $f$ on the Pati-Salam chain once the weak angle is measured. It cannot. The Yukawa term of the imported two-loop Fact weights each fermion by its quadratic Casimir; for a coupling of a left-handed to a right-handed multiplet the weights come out equal for $SU(4)$, $SU(2)_{L}$ and $SU(2)_{R}$, so every Dirac-type coupling shifts the unified coupling only and none of the scales. Only the Majorana coupling of the $(10,1,3)$, which joins two right-handed multiplets, moves $M_{I}$ and $M_{U}$. But the chain already uses the three measured couplings to solve for three unknowns ($\alpha_{U}$, $M_{I}$, $M_{U}$), and the Yukawa term keeps that system linear and nonsingular for every value of the coupling: the running returns $M_{I}(f)$, not $f$. With the three gauge couplings as the only data the coupling stays free. If $M_{I}$ were supplied from elsewhere, the running would determine the trace of $ff^{\dagger}$, but at the one-loop baseline a unit trace moves $\ln M_{I}$ by only a few times the shift from a one-sigma change of the strong coupling, so the trace would be fixed only to about $0.4$ per sigma of $\alpha_{s}$.

## lay
At very high energies the strengths of the forces drift, and at the second level of precision they also feel the couplings of matter to the Higgs-like fields. One might hope that this drift, compared with the measured strengths, pins down the coupling that sets the heavy neutrino mass. It does not. Couplings that join left-handed to right-handed matter push all three forces equally and change nothing but their common unified strength. The heavy neutrino coupling does move the unification scales, but the measured strengths are already used up in fixing those scales, so the drift tells us the scales once the coupling is known, never the coupling. The heavy neutrino mass therefore stays a number read off the observed neutrino masses.

## one-liner
At two loops every Dirac-type Yukawa shifts the three Pati-Salam couplings equally and moves only $\alpha_{U}$, the $(10,1,3)$ Majorana coupling alone moves $M_{I}$, and since the running stays a nonsingular system for $(\alpha_{U}, M_{I}, M_{U})$ at every value of it, the three measured gauge couplings alone never fix $f$: the Majorana scale stays an input valued by $m_{3}$; a supplied $M_{I}$ would fix $\mathrm{Tr}\,ff^{\dagger}$ only to about $0.4$ per standard deviation of $\alpha_{s}$ (one-loop baseline).
