---
id: neutrino.seesaw-what-gauge-invariance-proves-what
kind: claim
version: 4
title: 'The seesaw: what gauge invariance proves, and what is assumed'
status: proved
region: neutrino
subject: neutrinos
tags: [refutation, seesaw-and-majorana, cosmological-constant, ledger-audit]
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
review: typed
derivations:
- name: main
  uses:
  - mass.exact-join@8
  - neutrino.imported-derived-content-singlets@7
  assumes:
  - neutrino.m-framework-realises-majorana-term-scale@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T15.py
  tags:
  - label:prop:seesaw
- kind: check
  ref: check.py::check_cosmological_term_magnitudes
- kind: check
  ref: check.py::check_unique_neutral_bilinear
- kind: check
  ref: check.py::check_block_elimination
- kind: check
  ref: check.py::check_scalar_seesaw_bound
locators:
  paper: T15
  number: Prop 4.1
  label: prop:seesaw
  line: 599
extraction:
  env: proposition
  context_refs:
  - mass.exact-join
  - neutrino.imported-mass-bracket-quantum-numbers
  unresolved_refs:
  - rem:valuation
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - mass.exact-join
    - neutrino.imported-derived-content-singlets
    - neutrino.m-framework-realises-majorana-term-scale
    note: 'the proof existed after the embedded premise and was copied verbatim; the mass-bracket fact
      is cited only to say it is not used; the paper calls (2) textbook and (3) is the type-I seesaw,
      but the store''s only imported seesaw cites this paper for it and nothing imports the neutral-bilinear
      statement, so no standard route was added. Levels pass: lay names Premise (M), and lay and one-liner
      keep the leading-order qualifier of clause (3).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - neutrino.m-framework-realises-majorana-term-scale
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Lambda-term magnitudes in Q(sqrt 2) and by squared bounds, the unique neutral bilinear among 21, the block elimination identity (2 x 2 and 3 x 3), and the scalar eigenvalue within m^4/M^3. Version 2 -> 3. Check strengthened: f(t) pinned, the m^4/M^3 bound shown sharp to a factor two, the vertex M/2 pinned; grid samples moved to module level. Version 3 -> 4.'
---

## formal
Three statements and one premise.
\begin{enumerate}
\item \emph{(The sixteenth refutation, by magnitude; proved.)} The cosmological term of the deformed bracket (Fact \claimref{mass.exact-join}) cannot supply the neutrino mass. For a composite of extent $l$ and constituent momentum scale $p$, $|[\omega^{1}\omega^{2}]| \sim l^{2}p$ and $|\br{\pi^{1}\pi^{2}}| \sim p$, so the cosmological term lies below the flat term by the factor $\Lambda l^{2}/6$, which reaches one only at $l = \sqrt{6/\Lambda} = \sqrt{2}\,\LH$ with $\LH = \sqrt{3/\Lambda}$ the Hubble length: the $\Lambda$ term never dominates for anything smaller than the horizon. Read as a mass on its own (a composite with $\br{\pi^{1}\pi^{2}} = 0$ and scalar Gram matrix, $m = \sqrt{2}\,\tfrac{\Lambda}{6}\,|[\omega^{1}\omega^{2}]|$), a $\Lambda$-term neutrino of $0.05$ eV with constituents at its own momentum scale has extent $l = 2^{1/4}\LH \approx 1.19\,\LH$, and with weak-scale constituents an extent of order $10^{20}$ m. The Casimir branch is no better: $m^{2} = \tfrac{\Lambda}{3}C$ at $0.05$ eV needs $C$ of order $10^{63}$. The scope is exact: this refutes the cosmological term as a neutrino mass mechanism; it is not a statement about a compositeness floor, which Fact \claimref{mass.exact-join} says does not exist.
\item \emph{(The neutral bilinear; elementary, proved.)} In the field-theory reading of the derived content, the hypercharge of a fermion bilinear is the sum of the two fields' hypercharges. Among the derived fermions, the bilinear $N N$ of the total singlet with itself is the unique neutral one, hence the unique fermion mass term that gauge invariance permits without a condensate; every other bilinear, the Dirac neutrino term $L N$ included, carries a nonzero hypercharge that only the condensate can absorb, and forms at the electroweak condensate scale $v \approx 246$ GeV \cite{PDG2024}. This is the textbook statement and uses nothing from the framework's bracket, which says nothing about that bilinear (Fact \claimref{neutrino.imported-mass-bracket-quantum-numbers}).
\end{enumerate}
\begin{premise}[M: the framework realises the Majorana term, at a scale $M \gg v$]
The neutral bilinear of (2) is realised by the framework, is nonzero, and its scale $M$ lies far above $v$. What (2) proves is that nothing forbids the term; gauge invariance says nothing about whether it forms or about its magnitude ($M = 0$, Dirac neutrinos; $M \sim v$; $M \sim$ eV are all consistent with it), and the framework's own mass bracket, computed only on slot states, undefined for excited composites, and of unsettled relation to the order parameter (Fact \claimref{neutrino.imported-mass-bracket-quantum-numbers}), has not been identified with it, nor shown to differ from it. This paper takes (M) as a premise, values $M$ from the observed masses in Remark \ref{rem:valuation}, and names its derivation as a successor problem.
\end{premise}
\begin{enumerate}
\setcounter{enumi}{2}
\item \emph{(Block inversion; proved.)} Under (M), for the mass matrix $\begin{psmallmatrix} 0 & \mD \\ \mD^{\mathsf{T}} & M_{R}\end{psmallmatrix}$ with $M_{R}$ invertible and $\|\mD\| \ll \|M_{R}\|$, the light block is $-\mD M_{R}^{-1}\mD^{\mathsf{T}}$ at leading order, symmetric (Majorana); the sign is a Majorana phase and is dropped hereafter. In the one-generation case, with $m_{D}$ and $M_{R}$ scalars,
\begin{equation}
m_{\nu} \;=\; \frac{m_{D}^{2}}{M_{R}} ,
\end{equation}
with the exact small eigenvalue differing from it by less than $m_{D}^{4}/M_{R}^{3}$.
\end{enumerate}

## technical
(1) The cosmological term of the deformed bracket cannot supply the neutrino mass: for a composite of extent $l$ it lies below the flat term by the factor $\Lambda l^{2}/6$, which reaches one only at $l = \sqrt{2}\,L_{H}$, so it never dominates below the horizon; a $0.05$ eV neutrino from it alone would need an extent of about $1.19\,L_{H}$, or of order $10^{20}$ m with weak-scale constituents, and the Casimir branch needs $C$ of order $10^{63}$. (2) A bilinear's hypercharge is the sum of its fields', so the singlet's $NN$ is the unique neutral fermion bilinear, the one mass term gauge invariance permits without a condensate; the Dirac term $LN$ forms at $v \approx 246$ GeV.

(3) Under Premise (M), for the mass matrix $\begin{psmallmatrix} 0 & \mD \\ \mD^{\mathsf{T}} & M_{R}\end{psmallmatrix}$ with $M_{R}$ invertible and $\|\mD\| \ll \|M_{R}\|$, the light block is $-\mD M_{R}^{-1}\mD^{\mathsf{T}}$ at leading order, symmetric (Majorana); in one generation $m_{\nu} = m_{D}^{2}/M_{R}$, with the exact small eigenvalue within $m_{D}^{4}/M_{R}^{3}$ of it.

## lay
The paper first rules out one idea: the cosmological constant's tiny effect on the framework's mass formula is far too weak to give neutrinos their mass. It then recalls that gauge symmetry allows exactly one fermion mass that needs no Higgs field, a Majorana mass for the right-handed neutrino. Assuming, as Premise (M), that the framework realises that mass and makes it large, the familiar seesaw follows at leading order: the light neutrino mass is the square of an ordinary mass divided by the huge one.

## one-liner
The cosmological term cannot give the neutrino mass, the singlet's Majorana term is the one mass gauge invariance allows without a condensate, and under (M) the leading-order one-generation seesaw gives $m_{\nu} = m_{D}^{2}/M_{R}$.
