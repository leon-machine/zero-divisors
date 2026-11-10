---
id: dark-matter.mirror-tower-copy-one
kind: claim
version: 10
title: The mirror tower is a copy of this one
status: proved
region: dark-matter
subject: dark-matter
tags: [mirror-sector, dark-matter-ratio, premises-p1-p5, gauge-fields]
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
- name: Claude Opus 5.5
  role: GA rewrite (Hodge star as duality with the pseudoscalar)
  version: 9
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, restatement of (iv) onto the common-ceiling-coupling premise and the T14c caveat at Leon''s decisions'
  version: 9
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'clause (v) given its stated premises (common N of P1, the charge reading), Premise P4 retired as a postulate in its favour'
  version: 10
  source: maintainer pass of 2026-11-10
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-inputs-standard-model-chain@6
  - dark-matter.type-residue-what-each-tower-can@5
  assumes:
  - dark-matter.p1-single-frozen-point@2
  - dark-matter.p2-indifference@2
  - synthesis.common-ceiling-coupling-premise@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:thm:mirror
- kind: check
  ref: check.py::check_even_subalgebras_and_spin_groups_agree
- kind: check
  ref: check.py::check_complexified_fibres_and_ground_types
- kind: check
  ref: check.py::check_standard_model_running_and_mean_mass_ratio
- kind: check
  ref: check.py::check_p2_caveat_mirror_at_our_temperature
locators:
  paper: T14
  number: Thm 4.3
  label: thm:mirror
  line: 325
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 9 -> 10. Leon''s decision 10 of 10 November 2026. Clause (v), first route: the phrase ''the stored charge being a sector label'' pointed without an edge to dark-matter.stored-asymmetry-charge-not-number (i), a result downstream of this theorem; the clause now states the two premises that reading needs (the common-N clause of P1, already an assumes edge, and the charge reading (C epsilon), the stance registered as synthesis.matter-asymmetry-registered-free-input, held as an in-statement hypothesis of the first route, with no assumes edge drawn) and cites the downstream proposition as a later elaboration that is not used. Premise P4 (dark-matter.p4-democracy-asymmetry-over-oriented-towers) is retired as a postulate in favour of this clause: every stored use of it was its mirror instance; its fork clause (a premise only at r = 0, used by nothing stored) is kept as a remark in (v). Clause (iii), technical, lay, one-liner and proof to match.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 9 (already raised in this run). Leon''s answer 2 (C1): clause (iv) now names the new premise synthesis.common-ceiling-coupling-premise for the common ceiling and coupling, with an assumes edge to it, since P2 at version 2 (labels, not states) does not reach a coupling (synthesis.tower-charge-sector-label-temperature-not, Reading); (v)s first route reads P2 on the stored charge, a sector label; the closing sentence of (v) names the new premise; and the T14c caveat says the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaving xi free, the cold mirror then needing a non-equilibrium descent (decision item G1). Restatement of (iv) at Leon''s decision; levels and proof to match.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA in the proof: the Hodge star on two-forms is multiplication by the pseudoscalar I on the bivector field F, and the densities F ^ *F and F ^ F are <F^2>_0 and <I F^2>_0 times the volume factor; their reversal invariance is shown from the even number of vector squares in each term; the component formula of the star stays as a labelled reading. Checked exactly with lib/GA.py in the maintainer scratch: for five sample component arrays F_ab both densities agree in Cl(1,3) and Cl(3,1). Statement unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: even subalgebras of (2,4)/(4,2) and (1,3)/(3,1) isomorphic blade by blade, same complex types and complexified fibres, different ground types; one-loop b = (41/10, -19/6, -7); mean mass ratio; P2 caveat Delta N_eff in (7.44, 7.45). Version 5 -> 6. Check entries synced with check.py: +1, -1 (added check_standard_model_running_and_mean_mass_ratio; removed check_running_and_share_of_one). Version 6 -> 7. Check strengthened: Delta N_eff at xi = 1 pinned to five decimals and its ratio to the cap pinned at 24; cube-root bracket pinned exactly. Version 7 -> 8.'
  superseded_in_part_by:
  - dark-tower-matter.mirrors-temperature-p2
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: [1, 8]
    note: 'Superseded in part by T14c Prop 8.2 (dark-tower-matter.mirrors-temperature-p2): applied with
      the reach of clauses (iv) and (v), P2 also fixes the mirror deposit per unit charge and gives xi = 1,
      excluded, so the cold mirror is an unstated exception to P2. Formal narrowed: (iv) no longer calls
      the common coupling "the one place P2 applies across towers"; a closing caveat cites the T14c result
      and keeps (i) to (iii) and the conditional equalities of (iv), (v). Decision 8 (P4): (iii) now says
      that (v) discharges P4 for the mirror (the assumes edge was already removed). Original in source_formal.'
  env: theorem
  context_refs:
  - dark-matter.mirror-share-one-how-fragile
  typing:
    by: ai-typing-pass
    note: 'Edges unchanged; the fragility proposition is cited only for the half-percent composition figure
      and already uses this theorem, and the link to the mirror-matter literature is a comparison with
      a posit, not a standard derivation, so no standard route. Levels pass: per review item 7, lay and
      one-liner now keep the common ceiling M and state that the share rests on P1, P2 and the copy with
      P4 discharged (technical likewise), and lay names P1, P2 and (S); the P4 assumes edge the review
      questions is left for an edge pass. Edge fix after review: P4 removed from assumes, since clause
      (v) discharges it for the mirror (T14 line 332).'
  source_title: 'The mirror tower is a copy of this one'
  source_formal: |-
    Every item of Fact \claimref{dark-matter.imported-inputs-standard-model-chain} is invariant under the signature reversal $(p,q) \mapsto (q,p)$ that carries this tower's signature $(1,3)$ to the mirror's $(3,1)$ (the proof runs the list item by item; the tractor bundle over a $(3,1)$ conformal structure has ambient $\R^{4,2}$ and the same complexified fibre, Hypothesis (S) has no signature in it, and one-loop running depends on the content alone). Hence:
    \begin{enumerate}
    \item[(i)] the mirror tower's derived content is a copy of this tower's: gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$, the same global form, the same generation with the same hypercharges and the same chirality halves, including a massless mirror photon and mirror neutrinos;
    \item[(ii)] the ground type (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}: $\R$ for the mirror, $\mathbb{H}$ for this tower) does not enter: the derivation uses the conformal spin group and its complex representations, never the tower's real Clifford module;
    \item[(iii)] the mirror's light content, and therefore its $\beta$-functions at every scale, equal this tower's, so that with a common ceiling $M$ and a common coupling there its confinement scale and composite spectrum equal ours exactly, $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$, and under P4 its tower factor is $f_{2} = 1$ up to the ratio of mean mass per baryon of the two sectors, which their nuclear histories set (one on the proton-only branch, $0.995$ on the burning branch, Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)): $\Omega_{\mathrm{mirror}} = \Omega_{b}$ to half a percent;
    \item[(iv)] the common coupling in (iii) is the one place P2 applies across towers: the reversal is the automorphism of the configuration along whose orbit Premise \claimref{dark-matter.p2-indifference} equates, so a coupling difference at the ceiling would be an uncaused distinction between the two members of one orbit, which the audit forbids; the odd towers, off that orbit relative to this one, get no such licence;
    \item[(v)] the asymmetry per mode is equal in the two towers, $\epsilon_{2} = \epsilon_{6}$, by two routes, both carried: by the audit, as in (iv), a difference between two continuous data of one reversal orbit being an uncaused distinction; and, more weakly (isomorphic theories share the function, not thereby the value of a datum of theory plus initial condition), by inheritance, both towers being oriented by the one flag under Premise \claimref{dark-matter.p1-single-frozen-point}'s orientation clause. So Premise \claimref{dark-matter.p4-democracy-asymmetry-over-oriented-towers} is discharged for the mirror, and the share of one in (iii) rests on P1, P2 and the copy.
    \end{enumerate}
    This is mirror matter in the sense of the literature \cite{FootMirror2004}, derived rather than posited: the framework's $r = 2$ tower is a second Standard Model.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor representation to the representation on the conformal spinor space $\CS$ (technical level and proof). Kept the complexification $\R^{2,4} \otimes \C = \R^{4,2} \otimes \C$ and the complexified fibre: the argument is that a quadratic space has no signature over $\C$, which is a complexification of the vector space, not the $I_6$-structure on spinors, so the dictionary''s renaming does not apply.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - dark-matter.p1-single-frozen-point
    note: The proof text has no step for clause (v), so P1 (its second route) is given a closing role sentence.
---

## formal
Every item of Fact \claimref{dark-matter.imported-inputs-standard-model-chain} is invariant under the signature reversal $(p,q) \mapsto (q,p)$ that carries this tower's signature $(1,3)$ to the mirror's $(3,1)$ (the proof runs the list item by item; the tractor bundle over a $(3,1)$ conformal structure has ambient $\R^{4,2}$ and the same complexified fibre, Hypothesis (S) has no signature in it, and one-loop running depends on the content alone). Hence:
\begin{enumerate}
\item[(i)] the mirror tower's derived content is a copy of this tower's: gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$, the same global form, the same generation with the same hypercharges and the same chirality halves, including a massless mirror photon and mirror neutrinos;
\item[(ii)] the ground type (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}: $\R$ for the mirror, $\mathbb{H}$ for this tower) does not enter: the derivation uses the conformal spin group and its complex representations, never the tower's real Clifford module;
\item[(iii)] the mirror's light content, and therefore its $\beta$-functions at every scale, equal this tower's, so that with a common ceiling $M$ and a common coupling there its confinement scale and composite spectrum equal ours exactly, $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$, and with the equal asymmetry per mode of (v) its tower factor is $f_{2} = 1$ up to the ratio of mean mass per baryon of the two sectors, which their nuclear histories set (one on the proton-only branch, $0.995$ on the burning branch, Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)): $\Omega_{\mathrm{mirror}} = \Omega_{b}$ to half a percent;
\item[(iv)] the common ceiling and the common coupling in (iii) are Premise \claimref{synthesis.common-ceiling-coupling-premise}, which equates them along the reversal orbit only: Premise \claimref{dark-matter.p2-indifference}, scoped to sector labels and not states, does not reach the coupling, which is neither (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), so the equality is a premise of its own; the odd towers, off that orbit relative to this one, get no such premise;
\item[(v)] the asymmetry per mode is equal in the two towers, $\epsilon_{2} = \epsilon_{6}$, by two routes, both carried: by the audit of Premise \claimref{dark-matter.p2-indifference} applied to the stored charge, under two premises stated here: the common-$N$ clause of Premise \claimref{dark-matter.p1-single-frozen-point} (the number $N$ is common to the towers), and the charge reading (C$\epsilon$), that $\epsilon$ is a datum of the descent and not of a tower's state, inherited and not generated, which is the stance registered as Premise \claimref{synthesis.matter-asymmetry-registered-free-input} and is taken here as a hypothesis of this route; under them the asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, a sector label of the descent, so that a difference between the two members of one reversal orbit would be an uncaused distinction (the reading is worked out, with its consequences, in Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i), which comes after this theorem and is not used here); and, more weakly (isomorphic theories share the function, not thereby the value of a datum of theory plus initial condition), by inheritance, both towers being oriented by the one flag under the orientation clause of Premise \claimref{dark-matter.p1-single-frozen-point}. This equality is the instance on the mirror of the former Premise P4 (democracy of the asymmetry over the oriented towers), which is retired as a postulate: it was this clause on the mirror, void on the odd residues, and a premise only on the fork $r = 0$, where no stored result uses it. The share of one in (iii) rests on P1, P2, the common ceiling coupling, the charge reading (C$\epsilon$) on the first route, and the copy.
\end{enumerate}
This is mirror matter in the sense of the literature \cite{FootMirror2004}, derived rather than posited: the framework's $r = 2$ tower is a second Standard Model.

Caveat (T14c): applied with its version-1 reach, the reach the paper used in (iv) and (v), Premise P2 also equates a third datum of the descent along the same orbit, the energy deposited per unit charge, and so gives $\xi = T'/T = 1$ and $\Delta\Neff = 7.45$ at recombination, which the record excludes (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}). The cold mirror the paper carries is an exception to P2 at its version-1 reach; P2 as scoped leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}). (i) to (iii) stand; (iv) is the common-ceiling-coupling premise, which equates no state, and (v) holds under P2 as scoped, given its two stated premises.

## technical
Every input of the Standard-Model chain is invariant under the signature reversal $(p,q) \mapsto (q,p)$ that carries this tower's $(1,3)$ to the mirror's $(3,1)$: the complexified fibre is the same, both conformal spin groups are $SU(2,2)$ with the same representation on the conformal spinor space, Hypothesis (S) has no signature in it, and one-loop running depends on content alone. So the mirror's derived content copies ours: gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ with the same global form, generation, hypercharges and chirality halves, including a massless mirror photon and mirror neutrinos; the ground type ($\R$ for the mirror, $\HH$ here) never enters.

With equal light content the $\beta$-functions agree at every scale, so a common ceiling $M$ and a common coupling there give $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$, and with the equal asymmetry per mode $f_{2} = 1$ up to the ratio of mean mass per baryon set by the two nuclear histories, so $\Omega_{\mathrm{mirror}} = \Omega_{b}$ to half a percent. The common ceiling and coupling are a premise of their own, the common-ceiling-coupling premise, along the reversal orbit only: indifference, scoped to sector labels and not states, does not reach a coupling, and the odd towers get no such premise. The asymmetry per mode is equal, $\epsilon_{2} = \epsilon_{6}$, by the indifference audit applied to the stored charge, which is a sector label given that the number $N$ is common to the towers (a clause of the single frozen point) and that $\epsilon$ is a datum of the descent and not of a tower's state (the charge reading, the registered stance, a hypothesis of this route), and, more weakly, by both towers being oriented by the one flag under the single frozen point. This is the mirror instance of the former democracy premise P4, retired as a postulate. The share of one rests on the single frozen point, indifference, the common ceiling coupling, the charge reading and the copy.

Caveat: the T14c note shows (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}) that indifference at its version-1 reach also equates the energy the descent deposits per unit charge, giving $\xi = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$, which the record excludes; the cold mirror the paper carries is an exception to indifference at that reach. Indifference as scoped leaves $\xi$ free, and the cold mirror then needs a non-equilibrium descent; the common-ceiling-coupling premise equates no state.

## lay
Swapping which directions count as time and which as space turns our world into a mirror world, and this result shows that every ingredient used to derive our particle physics survives the swap. So the mirror world has its own copy of the Standard Model as the series derives it (under Hypothesis (S)), with mirror photons and mirror neutrinos. If the two worlds share one cutoff scale and start with equal force strengths there (an assumption of its own, the common ceiling coupling), and under the framework's premises of a single frozen point (P1) and indifference (P2), which give an equal matter excess once that excess is read as a quantity fixed at the origin and not by temperature, it also has the same particle masses and the same matter excess, so its matter equals our ordinary matter to within half a percent, the gap coming from the two worlds' nuclear histories. A later note (T14c) shows that the indifference principle, applied as widely as the paper first applied it, would also make the mirror world as hot as ours, which observations rule out; as now worded it leaves the mirror's temperature open, and a cold mirror then needs a birth out of equilibrium.

## one-liner
Every input of the Standard-Model chain is invariant under signature reversal, so the mirror tower carries a copy of the derived Standard Model and, with a common ceiling $M$ and equal couplings there (the common-ceiling-coupling premise) and under the single frozen point and indifference (which give the equal asymmetry per mode on the charge reading), $\Omega_{\mathrm{mirror}} = \Omega_{b}$ to half a percent; indifference at its first reach would also make the mirror as hot as ours, and as scoped it leaves the temperature free.
