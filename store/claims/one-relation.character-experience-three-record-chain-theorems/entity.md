---
id: one-relation.character-experience-three-record-chain-theorems
kind: claim
version: 5
title: 'The character of experience: three record-chain theorems, and the final limit'
status: proved
region: one-relation
subject: one-relation
tags: [measurement-and-records]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, the recording remark entered as a premise and assumed, at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - one-relation.imported-flag-arrow-superselection@7
  - one-relation.imported-single-mode-thermality-modular-period@6
  - standard-model.hyp-s-slot-statistics@9
  assumes:
  - one-relation.recording-irreversible-stated-so-it-can@1
  - one-relation.supervenience-stated-so-it-can-be@1
  - one-relation.recorded-sectors-superselected-premise@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T16
  number: Prop 7.2
  label: prop:experience
  line: 851
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Leon''s answer 6 (B3): Singleness (1) rested on T16''s Remark rem:recording, not a store entity; it now cites and assumes the postulate one-relation.recorded-sectors-superselected-premise (new assumes edge), rem:recording dropped from unresolved_refs, the closing conditionality names it; status stays proved, given it. Levels name the premise.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Edges kept as stated premises; the self-location clause agrees with the Everett literature
      (Saunders, Wallace), but no such standard result is in the store, so no standard-route derivation
      was added. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement
      holds under Hypothesis (S). Levels pass: lay and one-liner now keep Hypothesis (S), an assumes edge,
      for the arrow clause.'
    added:
    - standard-model.hyp-s-slot-statistics
  source_title: 'The character of experience: three record-chain theorems, and the final limit'
  source_formal: |-
    Grant Premise \claimref{one-relation.supervenience-stated-so-it-can-be}. Three statements follow about what any such subject must be like.
    \begin{enumerate}
    \item \emph{(Singleness.)} A record chain reads only its own records, by the superselection of Remark \ref{rem:recording} under Premise \claimref{one-relation.recording-irreversible-stated-so-it-can}, so no self can find, remember, or feel a sibling branch: experience must present as a single history however many the branches.
    \item \emph{(Flow.)} A record chain writes in one direction on the modular period and never unwrites (Premise \claimref{one-relation.recording-irreversible-stated-so-it-can}), so experience must present as passage; and the direction of the felt passage is the flag itself. The arrow one experiences is the orientation bit of Fact \claimref{one-relation.imported-flag-arrow-superselection}, read from inside, under Hypothesis (S) as that Fact records.
    \item \emph{(The question dissolves.)} ``Why am I in this branch'' presupposes a branch-transcendent self that could have been located elsewhere, and no such object exists in the record structure: the self is individuated by the very records that constitute the branch, so each branch's subject asks the question and each is correct that this one is theirs. The question does not go unanswered; it goes unasked by anything real. This is the self-location analysis standard in the Everett literature \cite{Saunders2010, Wallace2012}, arrived at here from the record chain rather than postulated alongside it.
    \end{enumerate}
    The consequence is that the felt strangeness of quantum mechanics, that experience seems single, flowing, and unique despite the branching, is not residual strangeness at all: it is exactly what the branching structure looks like from inside one record chain. What remains, and is hereby declared the framework's final limit, is the hard problem proper: why there is anything it is like to be a record chain at all. On this the framework asserts nothing and derives nothing, and observes only that the question is invariant across every branch, every tower, and every physical theory yet written; it is not a residue of this framework but of physics. Structural level, conditional on Premises \claimref{one-relation.supervenience-stated-so-it-can-be} and \claimref{one-relation.recording-irreversible-stated-so-it-can}; refutation condition: exhibit experiential access to a sibling branch, or a felt arrow decoupled from the recording direction, and the identification fails.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Only the lay level named twistors (in glossing Hypothesis (S)); it now speaks of the slots of the conformal spinors. Formal level and proof unchanged.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Grant Premise \claimref{one-relation.supervenience-stated-so-it-can-be}. Three statements follow about what any such subject must be like.
\begin{enumerate}
\item \emph{(Singleness.)} A record chain reads only its own records, by the superselection of the recorded sectors (Premise \claimref{one-relation.recorded-sectors-superselected-premise}) under Premise \claimref{one-relation.recording-irreversible-stated-so-it-can}, so no self can find, remember, or feel a sibling branch: experience must present as a single history however many the branches.
\item \emph{(Flow.)} A record chain writes in one direction on the modular period and never unwrites (Premise \claimref{one-relation.recording-irreversible-stated-so-it-can}), so experience must present as passage; and the direction of the felt passage is the flag itself. The arrow one experiences is the orientation bit of Fact \claimref{one-relation.imported-flag-arrow-superselection}, read from inside, under Hypothesis (S) as that Fact records.
\item \emph{(The question dissolves.)} ``Why am I in this branch'' presupposes a branch-transcendent self that could have been located elsewhere, and no such object exists in the record structure: the self is individuated by the very records that constitute the branch, so each branch's subject asks the question and each is correct that this one is theirs. The question does not go unanswered; it goes unasked by anything real. This is the self-location analysis standard in the Everett literature \cite{Saunders2010, Wallace2012}, arrived at here from the record chain rather than postulated alongside it.
\end{enumerate}
The consequence is that the felt strangeness of quantum mechanics, that experience seems single, flowing, and unique despite the branching, is not residual strangeness at all: it is exactly what the branching structure looks like from inside one record chain. What remains, and is hereby declared the framework's final limit, is the hard problem proper: why there is anything it is like to be a record chain at all. On this the framework asserts nothing and derives nothing, and observes only that the question is invariant across every branch, every tower, and every physical theory yet written; it is not a residue of this framework but of physics. Structural level, conditional on Premises \claimref{one-relation.supervenience-stated-so-it-can-be}, \claimref{one-relation.recording-irreversible-stated-so-it-can} and \claimref{one-relation.recorded-sectors-superselected-premise}; refutation condition: exhibit experiential access to a sibling branch, or a felt arrow decoupled from the recording direction, and the identification fails.

## technical
Granting the supervenience premise (a self is a record chain), the irreversible-recording premise and the premise that recorded sectors are superselected in the recording limit, three structural statements follow. Singleness: a record chain reads only its own records, which are superselected from sibling branches, so experience presents as one history. Flow: records are written in one direction on the modular period and never unwritten, so experience presents as passage, and the felt direction is the flag's orientation bit read from inside, under Hypothesis (S). Dissolution: asking why I am in this branch presupposes a branch-transcendent self, which the record structure does not contain, so the question goes unasked by anything real.

What remains is declared the framework's final limit: the hard problem, why there is anything it is like to be a record chain, on which nothing is asserted or derived. The result is structural and conditional on these premises; it fails if experiential access to a sibling branch, or a felt arrow decoupled from the recording direction, is exhibited.

## lay
If a conscious self is nothing more than a chain of permanent records, recording cannot be undone, and recorded outcomes can no longer interfere, then a self in a branching quantum world should feel exactly as we do. It sees one history, feels time passing in one direction (read as the framework's arrow, which also assumes that the slots of the conformal spinors behave like the pairs, Hypothesis (S)), and has no real question about why it is in this branch rather than another. The framework says nothing about why there is any experience at all, and calls that its final limit.

## one-liner
Under the supervenience, irreversible-recording and recorded-sector premises (with Hypothesis (S) for reading the felt arrow as the flag), experience must present as single, flowing and branch-indexical, leaving only the hard problem untouched.
