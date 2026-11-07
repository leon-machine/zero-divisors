---
id: neutrino.rank-one-seesaw-ordering-sum-double
kind: claim
version: 9
title: 'The rank-one seesaw: ordering, sum, and the double-beta values'
status: proved
region: neutrino
subject: neutrinos
tags: [seesaw-and-majorana, live-prediction]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 9
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - neutrino.imported-indifference-faces-democratic-alignment-rank@6
  - neutrino.invariant-symmetric-matrices@2
  - neutrino.seesaw-what-gauge-invariance-proves-what@4
  assumes:
  - neutrino.h-second-stage-hierarchical@1
  - neutrino.m-framework-realises-majorana-term-scale@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T15.py
  tags:
  - label:prop:rankone
- kind: check
  ref: check.py::check_democratic_block_decomposition
- kind: check
  ref: check.py::check_normal_ordering
- kind: check
  ref: check.py::check_sum_and_floor
- kind: check
  ref: check.py::check_double_beta_values
locators:
  paper: T15
  number: Prop 4.4
  label: prop:rankone
  line: 630
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The PMNS and Majorana phases in the formal level, (3), and in the proof are written with I_4 (numbers read in span{1, I_4}): e^{I_4 phi/2}, e^{-I_4 delta_CP}, e^{I_4 phi}, e^{I_4 phi prime}; nothing stays.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the PMNS entries e^{i phi/2}, e^{-i delta_CP} and the Majorana phases in m_beta beta: phases of complex matrix entries (numbers)'
  env: proposition
  context_refs:
  - neutrino.breaking-relation
  - neutrino.imported-indifference-faces-democratic-alignment-rank
  - neutrino.imported-mass-bracket-quantum-numbers
  - neutrino.invariant-symmetric-matrices
  - neutrino.leptogenesis-suppressed-alignment-reheating-premise-new
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - neutrino.imported-indifference-faces-democratic-alignment-rank
    - neutrino.invariant-symmetric-matrices
    - neutrino.seesaw-what-gauge-invariance-proves-what
    - neutrino.h-second-stage-hierarchical
    - neutrino.m-framework-realises-majorana-term-scale
    note: 'the proof existed after the embedded premise and was copied verbatim; (H) and (M) are assumed;
      the mass-bracket fact is a caveat, the breaking lemma appears only inside (H), and the leptogenesis
      real-breaking assumption is a conditional of (3) whose edge would close a cycle, so none of the
      three was added. Levels pass: the lay now names Premises (M) and (H), the structural level, the
      small-breaking condition on the ordering, the lower-bound reading without (H) and the conditional
      absence of double-beta decay; the one-liner names (M) and leading order; the technical names the
      structural level and (M).'
  source_title: 'The rank-one seesaw: ordering, sum, and the double-beta values'
  source_formal: |-
    Let $Y_{D}$ be the Dirac neutrino Yukawa matrix and $\mD = vY_{D}$ the Dirac mass matrix. The Dirac neutrino brackets are face-valued like every Yukawa (Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank}, extended here to the bracket of $L$ with $N$, this paper's step, and one that reaches past Fact \claimref{neutrino.imported-mass-bracket-quantum-numbers}'s caveat, $L$ being the full twistor with all three pair modes occupied) and inherit the vacuum's democratic alignment, so $\mD = d\,\J$ at leading order, with the single Dirac eigenvalue $m_{D} := 3d$ along $u'$. The Majorana matrix $M_{R}$ involves no condensate, so the indifference instrument applied to it (a structural-level application, at the level Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank} holds the instrument) forbids any face anisotropy at leading order: $M_{R}$ is $S_{3}$-invariant, hence $M_{R} = \alpha\mathbf{1} + \beta\J$ by Lemma \claimref{neutrino.invariant-symmetric-matrices}, with $u'$ an eigenvector of eigenvalue $M_{3} = \alpha + 3\beta$; and if the Gram-square reading, which the families paper states for the condensate's source, is extended to the condensate-free $M_{R}$ (this paper's extension of that reading beyond the object it was stated for, at the same structural level), then $M_{R} \propto \J$ at leading order, so $\alpha = 0$ there and $\alpha$ is of the order of the breaking. Only $M_{3} \neq 0$ is assumed in (0).
    \begin{enumerate}
    \setcounter{enumi}{-1}
    \item \emph{(The leading-order scalar seesaw on the democratic block; proved.)} The Dirac coupling $\mD$ annihilates $u'^{\perp}$ on the right, so the neutrino system splits into the democratic block, spanned by $\nu_{u'}$ and $N_{u'}$ with mass matrix $\begin{psmallmatrix} 0 & m_{D} \\ m_{D} & M_{3}\end{psmallmatrix}$, and the two states $N_{\perp}$ of $u'^{\perp}$, of Majorana mass $\alpha$ and no Dirac coupling. The light matrix is therefore exactly rank one along $u'$, with the single light mass
    \[
    m_{3} \;=\; \frac{m_{D}^{2}}{M_{3}} \qquad(\text{leading order in } m_{D}/M_{3}),
    \]
    whatever $\alpha$ is, $\alpha = 0$ included, in which case $N_{\perp}$ are two exactly massless, exactly decoupled sterile states at leading order.
    \item \emph{(Ordering.)} Normal. Inverted ordering needs its two heaviest states degenerate to two percent ($m_{1}/m_{2} \ge 0.98$ at the measured splittings); a rank-one light matrix has one nonzero eigenvalue, and corrections small compared with it give one heavy state and two light, not a degenerate pair. Excluded by rank plus the smallness of the breaking, not by fit.
    \item \emph{(The sum.)} At leading order $m_{1} = m_{2} = 0$. For any spectrum with $m_{1} \ge 0$ and normal ordering the sum obeys the kinematic bound $\mnu \ge \sqrt{\Delta m^{2}_{21}} + \sqrt{\Delta m^{2}_{31}}$, which at the splittings $\Delta m^{2}_{21} \in (7.3, 7.7) \times 10^{-5}$ eV$^{2}$ and $\Delta m^{2}_{31} \in (2.45, 2.55) \times 10^{-3}$ eV$^{2}$ \cite{PDG2024, NuFIT2024} is the floor $0.0580$-$0.0593$ eV; the residue is $\mnu - \text{floor} \approx m_{1}$ at small $m_{1}$, and the script certifies the sum inside $(0.0591, 0.0604)$ eV at $m_{1} = 1$ meV, above $0.0616$ eV at $3$ meV, and above $0.0736$ eV at $10$ meV.
    \end{enumerate}
    \begin{premise}[H: the second stage is hierarchical]
    The breaking $S_{3} \to S_{2} \to 1$ lifts $m_{1}$ by a factor small compared with the factor that lifts $m_{2}$: $m_{1}/m_{2} \lesssim 0.01$, that is $m_{1} \lesssim 0.1$ meV. The charged sectors supply the analogy at $m_{e}/m_{\mu} \approx 0.005$ and $m_{u}/m_{c} \approx 0.002$ \cite{PDG2024}; by Lemma \claimref{neutrino.breaking-relation} the light masses go as the \emph{squared} singular values of the compressed breaking where the charged masses go as the singular values themselves, so a shared direction would give $m_{1}/m_{2} \approx (m_{e}/m_{\mu})^{2}$, far below what (H) needs, and if the directions are not shared the analogy is only that hierarchies are the rule. Under (H) the sum is the floor to within about $0.1$ meV ($0.1007$ meV at the premise's boundary, the residue being $m_{1}$ plus the small lift of $m_{2}$ and $m_{3}$), and the double-beta values of (3) hold to within $0.1$ meV; without it the sum is a lower bound, with $m_{1}$ free up to order $m_{2}$, where it would reach roughly $0.07$ eV.
    \end{premise}
    \begin{enumerate}
    \setcounter{enumi}{2}
    \item \emph{(The double-beta values.)} $m_{\beta\beta} = |\sum_{i}U_{ei}^{2}m_{i}|$ with $U_{e1} = c_{12}c_{13}$, $U_{e2} = s_{12}c_{13}e^{i\phi/2}$, $U_{e3} = s_{13}e^{-i\delta_{CP}}$ up to the second Majorana phase; under (H) the $m_{1}$ term is below $0.1$ meV. If the breaking is real in the vacuum's basis (the real-breaking assumption of Proposition \claimref{neutrino.leptogenesis-suppressed-alignment-reheating-premise-new}(3)), the phases are $0$ or $\pi$ and $m_{\beta\beta}$ is one of two values: $3.5$-$3.9$ meV at relative phase $0$ or $1.3$-$1.7$ meV at relative phase $\pi$, at $\sin^{2}\theta_{12} \in (0.295, 0.319)$ and $\sin^{2}\theta_{13} \in (0.0216, 0.0227)$ \cite{NuFIT2024}; without that assumption it ranges over the hull, $1.3$-$3.9$ meV. Either way the decay exists, the masses being Majorana under (M), and lies below the reach of the next generation of searches, whose projected sensitivity is a band near $10$-$20$ meV, its width the nuclear matrix element, against a current limit of $28$-$122$ meV \cite{LEGEND2021, KamLANDZen2023}: a conditional absence.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the one twistor phrase in the formal level (the full twistor, now the full conformal spinor with the twistor name in parentheses); the complex phases of the mixing matrix are physics conventions, not twistor machinery, and are kept, as is the proof.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - neutrino.imported-indifference-faces-democratic-alignment-rank
    - neutrino.invariant-symmetric-matrices
    - neutrino.m-framework-realises-majorana-term-scale
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the democratic block decomposition in the (u'', u''^perp) basis, normal ordering by inertia, the sum floor and residues, and the two double-beta values by exact square-root brackets. Version 5 -> 6. The formal level restated: Premise (H) residue 0.1007 meV is computed at m_1 = 0.1 meV (the rounded boundary; m_1/m_2 = 0.01 is about 0.087 meV): say so instead of ''at the premise''s boundary'' (fix round 2026-10-23). Version 6 -> 7. Check strengthened: m_bb range ends, the m_1 term and the shift at m_1 = 0.1 meV pinned to seven figures. Version 7 -> 8.'
---

## formal
Let $Y_{D}$ be the Dirac neutrino Yukawa matrix and $\mD = vY_{D}$ the Dirac mass matrix. The Dirac neutrino brackets are face-valued like every Yukawa (Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank}, extended here to the bracket of $L$ with $N$, this paper's step, and one that reaches past Fact \claimref{neutrino.imported-mass-bracket-quantum-numbers}'s caveat, $L$ being the full conformal spinor (the full twistor) with all three pair modes occupied) and inherit the vacuum's democratic alignment, so $\mD = d\,\J$ at leading order, with the single Dirac eigenvalue $m_{D} := 3d$ along $u'$. The Majorana matrix $M_{R}$ involves no condensate, so the indifference instrument applied to it (a structural-level application, at the level Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank} holds the instrument) forbids any face anisotropy at leading order: $M_{R}$ is $S_{3}$-invariant, hence $M_{R} = \alpha\mathbf{1} + \beta\J$ by Lemma \claimref{neutrino.invariant-symmetric-matrices}, with $u'$ an eigenvector of eigenvalue $M_{3} = \alpha + 3\beta$; and if the Gram-square reading, which the families paper states for the condensate's source, is extended to the condensate-free $M_{R}$ (this paper's extension of that reading beyond the object it was stated for, at the same structural level), then $M_{R} \propto \J$ at leading order, so $\alpha = 0$ there and $\alpha$ is of the order of the breaking. Only $M_{3} \neq 0$ is assumed in (0).
\begin{enumerate}
\setcounter{enumi}{-1}
\item \emph{(The leading-order scalar seesaw on the democratic block; proved.)} The Dirac coupling $\mD$ annihilates $u'^{\perp}$ on the right, so the neutrino system splits into the democratic block, spanned by $\nu_{u'}$ and $N_{u'}$ with mass matrix $\begin{psmallmatrix} 0 & m_{D} \\ m_{D} & M_{3}\end{psmallmatrix}$, and the two states $N_{\perp}$ of $u'^{\perp}$, of Majorana mass $\alpha$ and no Dirac coupling. The light matrix is therefore exactly rank one along $u'$, with the single light mass
\[
m_{3} \;=\; \frac{m_{D}^{2}}{M_{3}} \qquad(\text{leading order in } m_{D}/M_{3}),
\]
whatever $\alpha$ is, $\alpha = 0$ included, in which case $N_{\perp}$ are two exactly massless, exactly decoupled sterile states at leading order.
\item \emph{(Ordering.)} Normal. Inverted ordering needs its two heaviest states degenerate to two percent ($m_{1}/m_{2} \ge 0.98$ at the measured splittings); a rank-one light matrix has one nonzero eigenvalue, and corrections small compared with it give one heavy state and two light, not a degenerate pair. Excluded by rank plus the smallness of the breaking, not by fit.
\item \emph{(The sum.)} At leading order $m_{1} = m_{2} = 0$. For any spectrum with $m_{1} \ge 0$ and normal ordering the sum obeys the kinematic bound $\mnu \ge \sqrt{\Delta m^{2}_{21}} + \sqrt{\Delta m^{2}_{31}}$, which at the splittings $\Delta m^{2}_{21} \in (7.3, 7.7) \times 10^{-5}$ eV$^{2}$ and $\Delta m^{2}_{31} \in (2.45, 2.55) \times 10^{-3}$ eV$^{2}$ \cite{PDG2024, NuFIT2024} is the floor $0.0580$-$0.0593$ eV; the residue is $\mnu - \text{floor} \approx m_{1}$ at small $m_{1}$, and the script certifies the sum inside $(0.0591, 0.0604)$ eV at $m_{1} = 1$ meV, above $0.0616$ eV at $3$ meV, and above $0.0736$ eV at $10$ meV.
\end{enumerate}
\begin{premise}[H: the second stage is hierarchical]
The breaking $S_{3} \to S_{2} \to 1$ lifts $m_{1}$ by a factor small compared with the factor that lifts $m_{2}$: $m_{1}/m_{2} \lesssim 0.01$, that is $m_{1} \lesssim 0.1$ meV. The charged sectors supply the analogy at $m_{e}/m_{\mu} \approx 0.005$ and $m_{u}/m_{c} \approx 0.002$ \cite{PDG2024}; by Lemma \claimref{neutrino.breaking-relation} the light masses go as the \emph{squared} singular values of the compressed breaking where the charged masses go as the singular values themselves, so a shared direction would give $m_{1}/m_{2} \approx (m_{e}/m_{\mu})^{2}$, far below what (H) needs, and if the directions are not shared the analogy is only that hierarchies are the rule. Under (H) the sum is the floor to within about $0.1$ meV ($0.1007$ meV at $m_{1} = 0.1$ meV, the residue being $m_{1}$ plus the small lift of $m_{2}$ and $m_{3}$), and the double-beta values of (3) hold to within $0.1$ meV; without it the sum is a lower bound, with $m_{1}$ free up to order $m_{2}$, where it would reach roughly $0.07$ eV.
\end{premise}
\begin{enumerate}
\setcounter{enumi}{2}
\item \emph{(The double-beta values.)} $m_{\beta\beta} = |\sum_{i}U_{ei}^{2}m_{i}|$ with $U_{e1} = c_{12}c_{13}$, $U_{e2} = s_{12}c_{13}e^{I_4\phi/2}$, $U_{e3} = s_{13}e^{-I_4\delta_{CP}}$ up to the second Majorana phase (numbers are read in $\mathrm{span}\{1, I_4\}$); under (H) the $m_{1}$ term is below $0.1$ meV. If the breaking is real in the vacuum's basis (the real-breaking assumption of Proposition \claimref{neutrino.leptogenesis-suppressed-alignment-reheating-premise-new}(3)), the phases are $0$ or $\pi$ and $m_{\beta\beta}$ is one of two values: $3.5$-$3.9$ meV at relative phase $0$ or $1.3$-$1.7$ meV at relative phase $\pi$, at $\sin^{2}\theta_{12} \in (0.295, 0.319)$ and $\sin^{2}\theta_{13} \in (0.0216, 0.0227)$ \cite{NuFIT2024}; without that assumption it ranges over the hull, $1.3$-$3.9$ meV. Either way the decay exists, the masses being Majorana under (M), and lies below the reach of the next generation of searches, whose projected sensitivity is a band near $10$-$20$ meV, its width the nuclear matrix element, against a current limit of $28$-$122$ meV \cite{LEGEND2021, KamLANDZen2023}: a conditional absence.
\end{enumerate}

## technical
The Dirac brackets inherit the democratic alignment, extended here to the bracket of $L$ with $N$, so $\mD = d\J$ with single Dirac eigenvalue $m_{D} = 3d$ on $u'$; the indifference instrument, applied at structural level, makes the Majorana matrix $S_{3}$-invariant at leading order, $M_{R} = \alpha\mathbf{1} + \beta\J$ with $M_{3} = \alpha + 3\beta \neq 0$ (Premise (M)). The system splits into the democratic block $\begin{psmallmatrix} 0 & m_{D} \\ m_{D} & M_{3}\end{psmallmatrix}$ and two states $N_{\perp}$ of Majorana mass $\alpha$ with no Dirac coupling, so the light matrix is exactly rank one with $m_{3} = m_{D}^{2}/M_{3}$ at leading order, whatever $\alpha$ is.

Consequences: the ordering is normal, since inverted ordering needs two states degenerate to two percent, which a rank-one matrix with small corrections cannot give; at leading order $m_{1} = m_{2} = 0$, and the sum obeys $\mnu \ge \sqrt{\Delta m^{2}_{21}} + \sqrt{\Delta m^{2}_{31}}$, a floor of $0.0580$ to $0.0593$ eV, which under Premise (H) it meets to within about $0.1$ meV. Under (H) and the real-breaking assumption $m_{\beta\beta}$ is $3.5$ to $3.9$ meV or $1.3$ to $1.7$ meV, and otherwise lies in the hull $1.3$ to $3.9$ meV; under (M) the decay exists but lies below next-generation reach.

## lay
Assuming the framework supplies the heavy neutrino's Majorana mass at a scale far above the electroweak one (Premise (M)), and because the framework's neutrino couplings treat the three families identically at first approximation (a structural-level reading), only one light neutrino gets a mass, through the seesaw. Provided the corrections that break that symmetry are small, that fixes the mass ordering as normal; if the second stage of those corrections is also hierarchical (Premise (H)), the total mass sits at the smallest value oscillation experiments allow, about 0.059 eV, and otherwise that value is only a lower bound. Under the same premises neutrinoless double-beta decay occurs, at rates too small for the next generation of experiments to see: a conditional absence.

## one-liner
Under (M), the democratic Dirac matrix gives a rank-one seesaw at leading order: normal ordering, the sum at the oscillation floor under (H), and $m_{\beta\beta}$ of a few meV under (H).
