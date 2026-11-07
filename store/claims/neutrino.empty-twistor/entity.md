---
id: neutrino.empty-twistor
kind: claim
version: 5
title: The empty conformal spinor (the empty twistor)
status: proved
region: neutrino
subject: neutrinos
tags:
- conformal-spinors
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
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  uses:
  - neutrino.imported-ceiling-under-hypothesis-u-arrow@6
  - neutrino.imported-derived-content-singlets@8
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T15.py
  tags:
  - label:prop:empty
- kind: check
  ref: check.py::check_single_spinor_singlets
- kind: check
  ref: check.py::check_anomaly_solution_set_is_the_span
- kind: check
  ref: check.py::check_ray_family_and_collapse
- kind: check
  ref: check.py::check_anomaly_invisible_on_the_lattice
locators:
  paper: T15
  number: Prop 3.1
  label: prop:empty
  line: 580
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: neutrino.imported-derived-content-singlets repinned 7 -> 8 after reviewing its G3 restatement (Hypothesis (S) is now derived in the store from the slot-module premise, where it was called open; the derived content is unchanged); the use here holds as cited.'
  env: proposition
  context_refs:
  - neutrino.imported-ceiling-under-hypothesis-u-arrow
  typing:
    by: ai-typing-pass
    added:
    - neutrino.imported-ceiling-under-hypothesis-u-arrow
    note: 'added the imported flag covariance, which part (3) uses to discharge the orientation dependency;
      the paper calls the anomaly family textbook, but the store has no imported claim for that solution
      set (only the anomaly conditions), so no standard route was added. Levels pass: conditions already
      kept.'
  source_title: The empty twistor
  source_formal: 'Three statements.

    \begin{enumerate}

    \item \emph{(The identification; imported.)} The single-twistor sector of Fact \claimref{neutrino.imported-derived-content-singlets}
    carries two colour singlets, at grades zero and three, and the observed comparison column ($\bar{3}
    \oplus \bar{3} \oplus 1 \oplus 1$) always contained two: the right-handed neutrino was in the comparison
    from the start. In the Standard-Model paper''s listing, $\nu_{R}$ (as $\nu^{c}$) is the grade-zero
    state of the single-twistor sector, the \emph{empty twistor} in this paper''s usage (T12 uses the
    same phrase for the one-slot, no-pair doublet state, a different object), the pair system with no
    rung occupied, and its hypercharge is $Y = -0/3 = 0$ by the weight rule; the grade-three state, the
    filled twistor, has $Y = -1$ and is $e^{c}$ after conjugation. Where the Standard Model treats $\nu_{R}$
    as optional, this content carries it necessarily.

    \item \emph{(Anomalies could not have fixed it; proved.)} For the content $Q = (2,3)$, $L = (2,1)$,
    $u^{c}, d^{c} = (1,\bar{3})$, $e^{c} = (1,1)$ and a fourth singlet $N$ of hypercharge $Y_{N}$, all
    in one handedness, with $Y_{Q} \neq 0$, the solutions of the four anomaly conditions ($[SU(3)]^{2}U(1)$,
    $[SU(2)]^{2}U(1)$, gravitational, cubic) are \emph{exactly} the two-dimensional span $\{sY + t(B -
    L)\}$ with $Y_{Q} = \tfrac{s}{6} + \tfrac{t}{3} \neq 0$, up to the relabelling $u^{c} \leftrightarrow
    d^{c}$, where $Y$ is the derived spectrum with $Y_{N} = 0$ and $B - L$ takes the values $\tfrac13,
    -\tfrac13, -\tfrac13, -1, 1, 1$ on $Q, u^{c}, d^{c}, L, e^{c}, N$; up to normalisation this is the
    family $Y + t(B - L)$, with $Y_{N} = t$, together with the ray of $B - L$ itself, on which $Y_{N}/Y_{Q}
    = 3$. So anomaly cancellation leaves $Y_{N}$ free, and the zero of (1) is a computation of the content
    derivation, not a consistency condition. With $Y_{N} = 0$ imposed the family collapses to the derived
    spectrum (Fact \claimref{neutrino.imported-derived-content-singlets}), which is why the Standard-Model
    paper''s uniqueness theorem carries that hypothesis. (Witten''s global $SU(2)$ anomaly imposes nothing
    here: the doublet count is even and a singlet does not enter it.)

    \item \emph{(Anomaly-invisible, on the lattice; proved.)} At $Y_{N} = 0$ the fourth singlet contributes
    to none of the four sums, so deleting it from the spectrum changes none of them, and the $\mathbb{Z}_{6}$
    lattice admits its entry. The orientation dependency of the identification is discharged by the flag
    covariance of Fact \claimref{neutrino.imported-ceiling-under-hypothesis-u-arrow}.

    \end{enumerate}'
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: Converted the single-twistor sector and the empty and filled twistors to the single-spinor sector
      and the empty and filled conformal spinors (title, formal, technical, one-liner), keeping the twistor
      names once in parentheses, and the remark that T12 uses ``empty twistor'' for a different object.
      The anomaly computation and the proof are unchanged.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - neutrino.imported-ceiling-under-hypothesis-u-arrow
  small_findings_pass:
    by: ai-small-findings-pass
    date: '2026-10-22'
    finding: CONTRADICTIONS_STRUCTURE M3
    note: 'Namesake disclaimer brought up to date after the GA conversion: T12 now writes "empty/full
      conformal spinor" (not "empty twistor") for the (1,0) and (1,3) doublet components; the disclaimer
      names both phrases and now also appears at the technical level. Content unchanged.'
    open_problem: op.small-findings
  open_problem: op.small-findings
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the grades of Lambda(C^3) and their hypercharges, the anomaly solution set as the span of Y and B - L (closed form, cubic factorisation, completeness on a grid, Y_Q != 0 control), the ray and the collapse, and deletion of N with the Z6 lattice. Version 4 -> 5.'
---

## formal
Three statements.
\begin{enumerate}
\item \emph{(The identification; imported.)} The single-spinor sector (single-twistor sector) of Fact \claimref{neutrino.imported-derived-content-singlets}, the states of one conformal spinor $Z \in \CS$, carries two colour singlets, at grades zero and three, and the observed comparison column ($\bar{3} \oplus \bar{3} \oplus 1 \oplus 1$) always contained two: the right-handed neutrino was in the comparison from the start. In the Standard-Model paper's listing, $\nu_{R}$ (as $\nu^{c}$) is the grade-zero state of the single-spinor sector, the \emph{empty conformal spinor} (the empty twistor) in this paper's usage (the Standard-Model paper uses the same phrases, ``empty conformal spinor'' and ``full conformal spinor'', formerly ``empty twistor'' and ``full twistor'', for the doublet components $(1,0)$ and $(1,3)$ of its one-slot listing, the no-pair doublet $(2,1)_{1/2}$ and the lepton doublet: different objects from the grade-zero and grade-three singlets named here), the pair system with no rung occupied, and its hypercharge is $Y = -0/3 = 0$ by the weight rule; the grade-three state, the filled conformal spinor (filled twistor), has $Y = -1$ and is $e^{c}$ after conjugation. Where the Standard Model treats $\nu_{R}$ as optional, this content carries it necessarily.
\item \emph{(Anomalies could not have fixed it; proved.)} For the content $Q = (2,3)$, $L = (2,1)$, $u^{c}, d^{c} = (1,\bar{3})$, $e^{c} = (1,1)$ and a fourth singlet $N$ of hypercharge $Y_{N}$, all in one handedness, with $Y_{Q} \neq 0$, the solutions of the four anomaly conditions ($[SU(3)]^{2}U(1)$, $[SU(2)]^{2}U(1)$, gravitational, cubic) are \emph{exactly} the two-dimensional span $\{sY + t(B - L)\}$ with $Y_{Q} = \tfrac{s}{6} + \tfrac{t}{3} \neq 0$, up to the relabelling $u^{c} \leftrightarrow d^{c}$, where $Y$ is the derived spectrum with $Y_{N} = 0$ and $B - L$ takes the values $\tfrac13, -\tfrac13, -\tfrac13, -1, 1, 1$ on $Q, u^{c}, d^{c}, L, e^{c}, N$; up to normalisation this is the family $Y + t(B - L)$, with $Y_{N} = t$, together with the ray of $B - L$ itself, on which $Y_{N}/Y_{Q} = 3$. So anomaly cancellation leaves $Y_{N}$ free, and the zero of (1) is a computation of the content derivation, not a consistency condition. With $Y_{N} = 0$ imposed the family collapses to the derived spectrum (Fact \claimref{neutrino.imported-derived-content-singlets}), which is why the Standard-Model paper's uniqueness theorem carries that hypothesis. (Witten's global $SU(2)$ anomaly imposes nothing here: the doublet count is even and a singlet does not enter it.)
\item \emph{(Anomaly-invisible, on the lattice; proved.)} At $Y_{N} = 0$ the fourth singlet contributes to none of the four sums, so deleting it from the spectrum changes none of them, and the $\mathbb{Z}_{6}$ lattice admits its entry. The orientation dependency of the identification is discharged by the flag covariance of Fact \claimref{neutrino.imported-ceiling-under-hypothesis-u-arrow}.
\end{enumerate}

## technical
Three statements. First (imported), the sector of a single conformal spinor carries two colour singlets, at grades zero and three: the grade-zero state, the empty conformal spinor with no rung occupied (in this paper's usage; the Standard-Model paper's ``empty conformal spinor'' is the doublet component $(1,0)$), is the right-handed neutrino with hypercharge $Y = 0$, and the grade-three state, with $Y = -1$, is $e^{c}$ after conjugation, so this content carries $\nu_{R}$ necessarily.

Second, for $Q, L, u^{c}, d^{c}, e^{c}$ and a singlet $N$ of hypercharge $Y_{N}$, all of one handedness and with $Y_{Q} \neq 0$, the four anomaly conditions are solved exactly by the span $\{sY + t(B - L)\}$, up to exchanging $u^{c}$ and $d^{c}$: the family $Y + t(B - L)$ with $Y_{N} = t$, together with the ray of $B - L$. Anomaly cancellation thus leaves $Y_{N}$ free, and $Y_{N} = 0$ is a result of the content derivation, not a consistency condition. Third, at $Y_{N} = 0$ the singlet enters none of the four anomaly sums, the $\mathbb{Z}_{6}$ lattice admits it, and the orientation dependence of the identification is discharged by the imported flag covariance.

## lay
The framework's list of particles contains a state that behaves exactly like a right-handed neutrino, a particle the Standard Model treats as optional. The paper also shows that the usual consistency checks on particle charges could not have forced this particle's charge to be zero, since they allow a whole family of values. The zero comes from the framework's own construction, and at that value the particle is invisible to all the consistency checks.

## one-liner
The empty conformal spinor, the state with no pair mode occupied, is a necessary right-handed neutrino of zero hypercharge, a value that anomaly cancellation alone leaves free.
