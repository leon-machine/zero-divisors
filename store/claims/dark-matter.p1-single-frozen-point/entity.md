---
id: dark-matter.p1-single-frozen-point
kind: claim
version: 3
title: 'P1: the single frozen point'
status: postulate
region: dark-matter
subject: dark-matter
tags: [premises-p1-p5, frozen-point]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Fable 5.2
  role: 'split into its three clauses (metric, orientation, common N) within the entity, with the status of each'
  version: 2
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'note naming the connection of clause (P1a) under the field-space premise'
  version: 3
  source: 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'
amendments:
- version: 3
  kind: restatement
  defect: 'the status paragraph of (P1a) did not name its connection and cited only theorems about the normal tractor connection, which under (FS) does not carry the frozen point in the physical scale on matter regions'
  evidence: 'synthesis.frozen-point-unique-for-the-field-space-connection: check.py::check_field_strength_and_kernels_on_de_sitter_fluid_and_schwarzschild_fields'
review: typed
about:
- obj.dark-matter.witt-flag
locators:
  paper: T14
  number: Premise 2.1
  label: prem:single
  line: 96
extraction:
  maintainer_pass_2026_11_11:
    by: maintainer-2026-11-11
    date: '2026-11-11'
    note: 'Version 2 -> 3. A note is added to the formal level: under (FS) the status of (P1a) is given by synthesis.frozen-point-unique-for-the-field-space-connection; what is postulated is unchanged (the one connection and the normalisation). The three clauses and their wording are untouched.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Leon''s decision 10 of 10 November 2026: P1 is split into its three clauses within the entity, (P1a) metric, (P1b) orientation, (P1c) common N, each with its status as stored or as argued: (P1a) a theorem up to normalisation where the Weyl tensor has no kernel vector and an independent choice on conformally flat regions (two stored theorems); (P1b) substitutable by P2 on the orientation bit and not needed by the total (argued); (P1c) postulated, no derivation found. The common-N clause was not in the version-1 text, although dark-matter.stored-asymmetry-charge-not-number assumes P1 for it: it is now stated. No separate entities were created; the opening statement is unchanged.'
  typing:
    by: ai-typing-pass
    note: "Postulate: no edges to type; levels only."
  env: premise
  context_refs:
  - interior.scale-tractor-leaves-cone
  outside_pilot_cites:
  - ButlerT12
---

## formal
The descent was one event freezing one $I$ and making one orientation choice: all towers couple to one metric and are oriented, where they can be, by the one Witt flag of that event (Definition \claimref{obj.dark-matter.witt-flag}). The orientation clause is used only on the reversal orbit, where the identification of the flag across the two towers is canonical. \emph{Support:} \cite[Thm.~4.7]{ButlerT6}, \cite[Obs.~7.4]{ButlerT12}; the orientation clause is this paper's. Structural premise.

\emph{The three clauses and their status.} The premise is three statements, used separately.
\begin{enumerate}
\item[(P1a)] \emph{(Metric.)} One frozen point: all towers couple to one metric. Status: a theorem up to a common normalisation wherever the Weyl tensor has no kernel vector, given that every tower's frozen point is parallel for one tractor connection (Theorem \claimref{synthesis.frozen-point-unique-where-weyl-has-no-kernel}); an independent choice on conformally flat regions, the de Sitter vacuum included (Theorem \claimref{synthesis.two-frozen-points-conformally-flat}). What stays postulated is the one tractor connection, the normalisation, and the clause on conformally flat regions. This is the clause read as the sourcing rule (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}), and the one most widely used.
\item[(P1b)] \emph{(Orientation.)} Where towers can be oriented they are oriented by the one Witt flag; used only on the reversal orbit. Status: substitutable. The sign of the mirror's asymmetry is fixed by this clause or by Premise \claimref{dark-matter.p2-indifference} applied to the orientation bit (Theorem \claimref{synthesis.mirror-asymmetry-route-one}; Theorem \claimref{dark-matter.mirror-tower-copy-one}(v)), so under P2 as scoped to labels the clause is redundant on the reading that the bit is a label (argued). The mirror's share is even in that sign, so the dark-to-baryon total needs the clause under neither route (argued).
\item[(P1c)] \emph{(Common $N$.)} The number $N$ is common to the towers. Status: postulated, with no derivation found; it is used by the charge reading of the stored asymmetry (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; Theorem \claimref{dark-matter.mirror-tower-copy-one}(v), first route). Whether a second tower can carry its own frozen-point norm is undecided; the conformally flat counter-model of (P1a) suggests it can (argued).
\end{enumerate}
The clauses are kept in one entity; results that assume P1 use the clause their text names.

\emph{Note (which connection, 2026-11-11).} The ``one tractor connection'' of (P1a) is not named above, and the two theorems cited there are about the normal tractor connection, for which a tractor is parallel in the physical scale only on Einstein regions. Under Premise \claimref{synthesis.field-space-premise-parallel-frozen-point} (FS) the frozen point is parallel, with unit pairing with $X$, for the varied connection $A_{\rho}$ on every field, matter included. For that connection the status of (P1a) is given by Theorem \claimref{synthesis.frozen-point-unique-for-the-field-space-connection}: if every tower's frozen point is parallel for the one $A_{\rho}$ on a connected part of the invertible region that contains one point where $-(\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id})$ has no kernel vector (any point with isotropic matter other than $w = -\tfrac13$; on Einstein regions the Weyl condition above), the frozen points agree up to constants $c_{r}$, and the independent choice is confined to a component that is de Sitter at that $\Lambda$, not to every conformally flat region. What stays postulated is unchanged: the one connection, and the normalisation $c_{r} = \pm 1$, to which the common $N$ of (P1c) is equivalent given one $G$; (FS) normalises one tractor and does not supply it. For the tower of reversed signature the connection can be shared up to the sign of the frozen point or the discrete element $\operatorname{Ad}(I_{4})$ (the Remark of that Theorem); whether that element bears on the orientation clause (P1b) is not examined. The premise is unchanged.

## technical
The premise states that the descent was a single event that froze one point $I$ and made one orientation choice. All towers couple to the one metric of that event and, where they can be oriented, are oriented by its single Witt flag. The orientation clause is used only on the reversal orbit $r \mapsto -r$, where the identification of the flag across the two towers is canonical. It is a structural premise, supported by earlier results of the series, with the orientation clause added here.

The premise has three clauses with three statuses. The metric clause (one metric for all towers) is a theorem up to a common normalisation wherever the Weyl tensor has no kernel vector, given one tractor connection, and an independent choice on conformally flat regions, de Sitter included. The orientation clause is substitutable: indifference applied to the orientation bit does the same work on the reversal orbit, and the dark-to-baryon total does not see the sign (argued). The common-$N$ clause is postulated with no derivation found, and is what the charge reading of the stored asymmetry uses.

## lay
This assumption says the origin of the universe happened once, in one way, for everything. Every hidden sector feels the same gravity, and every sector that can have a handedness received the same one. It is assumed, not derived. The assumption has three parts of different standing: that all sectors feel one gravity (partly provable, partly a choice), that they share one handedness (replaceable by another assumption, and not needed for the dark-matter total), and that one large number is common to all of them (assumed, with no derivation).

## one-liner
Premise in three clauses: the descent was one event, so all towers share one metric (a theorem up to normalisation where the Weyl tensor has no kernel vector, a choice on conformally flat regions), where they can be oriented one Witt flag (substitutable by indifference on the reversal orbit), and one number $N$ (postulated).
