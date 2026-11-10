---
id: dark-matter.asymmetry-arrow-counted-fifteenth-refutation
kind: claim
version: 8
title: 'The asymmetry: the arrow counted, and the fifteenth refutation'
status: proved
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, refutation, undetermined-input]
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
  role: 'pin review, the remark on the mirror''s angle in (ii) now names the common ceiling coupling of the copy theorem''s (iv), where it quoted P2'
  version: 6
  source: maintainer pass 2026-11-07 (pin review)
- name: Claude Opus 5.5
  role: 'extraction note recording Leon''s confirmation of the theta-angle reading (second-round decisions)'
  version: 7
  source: maintainer pass 2026-11-07 (decisions, second round)
- name: Claude Fable 5.2
  role: 'Premise P4 retired: the assumes edge removed, the common value cited from the copy theorem''s clause (v)'
  version: 8
  source: maintainer pass of 2026-11-10
review: typed
derivations:
- name: main
  uses:
  - dark-matter.flag-bit-exists-exactly-tower-dimension@3
  - dark-matter.imported-derived-generation-flag@6
  - dark-matter.imported-trichotomy-descents-data@6
  - dark-matter.mirror-tower-copy-one@10
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:arrow
- kind: check
  ref: check.py::check_flag_conjugate_is_particle_antiparticle
- kind: check
  ref: check.py::check_theta_exists_exactly_where_the_bit_does
- kind: check
  ref: check.py::check_asymmetry_confined_to_this_tower_and_the_mirror
locators:
  paper: T14
  number: Prop 5.1
  label: prop:arrow
  line: 504
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 7 -> 8. Leon''s decision 10 of 10 November 2026: Premise P4 (dark-matter.p4-democracy-asymmetry-over-oriented-towers) is retired as a postulate; clause (iii) used only its mirror instance, which is clause (v) of dark-matter.mirror-tower-copy-one (repinned 9 -> 10, where (v) now states its premises). The assumes edge is removed, (iii) and the other levels say so, and the fork clause is kept as a remark. The check is unchanged (it never touched P4); coverage.yaml loses the untouched-premise line.'
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7, record only. Leon''s second-round answer 3 confirms the reading the pin review made: the common ceiling-coupling premise covers the mirror''s theta angle ("every other coupling"), so the remark in (ii) that the mirror''s angle equals ours only by the common ceiling coupling stands as it reads. No level, edge or check changed.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.imported-trichotomy-descents-data repinned 5 -> 6 after reviewing its restatement of clause (2) (the norm of the frozen point is not a field, fixed by a constraint with pure-gauge fluctuations, where it said the frozen action is N-insensitive); clauses (1), (3) and (4) are unchanged; the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the remark in (ii) that the mirror''s angle equals ours only by P2 along the reversal orbit quoted the old (iv) and now names the common ceiling coupling of (iv), a premise of its own there; the claim is unchanged. Version 5 -> 6.'
  maintainer_pass_xi_ledger:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 4 -> 5 (Leon''s register decision of 2026-11-01, epsilon registered as a postulate as xi G is): a marked note in (iv) and in the technical level points to the new premise synthesis.matter-asymmetry-registered-free-input, which registers the value epsilon as a free input with the stance''s refutation condition. The stance itself, the proposition and its checks are unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: flag conjugate e3 e4 e5 exchanges complementary Fock states; at the P3 representatives a theta-term (even degree) exists exactly where the flag bit does; oriented causal towers are r = 6, 2. Version 2 -> 3. Wording fix (Leon 2026-10-23): (ii) now says that at the P3 representatives a theta-term exists exactly where a flag bit does (dimensions 2 and 6, e.g. (1,1), (1,5), have a theta-term and no bit). Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  env: proposition
  context_refs:
  - dark-matter.imported-derived-generation-flag
  - dark-matter.orientation-arrow-seventeenth-refutation
  unresolved_refs:
  - rem:flaglives
  outside_pilot_cites:
  - ButlerT1
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.imported-derived-generation-flag
    note: 'Added the derived-generation fact because clause (i) rests on its identification of the Witt
      flag with the particle-antiparticle distinction; the seventeenth-refutation proposition is cited
      only to name a further datum, so it is not an edge. Levels pass: the lay level now marks initial
      data of the descent as a flagged, refutable stance and names premise P4 for the common value; the
      one-liner names P4 and the stance.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - dark-matter.imported-derived-generation-flag
---

## formal
The framework does not generate its asymmetry; it inherits it.
\begin{enumerate}
\item[(i)] \emph{(Sakharov.)} The Sakharov conditions are for generating an asymmetry dynamically from a symmetric state; a universe whose asymmetry is initial data does not need them. The descent supplies the reason the initial data need not be symmetric: it is irreversible (the lossy projection of the taxonomy paper's descent theorem \cite{ButlerT1}), it creates the tower charges, and it makes one orientation choice, the Witt flag, which is what particle-versus-antiparticle means (Fact \claimref{dark-matter.imported-derived-generation-flag}). Each matches a Sakharov condition in name; none is a mechanism producing a number.
\item[(ii)] \emph{(The fifteenth refutation.)} A pre-descent $\theta$-term would source asymmetry through the topology of gauge bundles; but it integrates a characteristic class, of even degree, so the odd-dimensional towers carry no continuous $\theta$, and at the P3 representatives a $\theta$-term exists exactly where a flag bit does. In this tower it is excluded empirically: a $\theta$-routed asymmetry needs an angle of order one at the descent that does not relax before it acts, and the neutron dipole bound $|d_{n}| < 1.8 \times 10^{-26}\,e\,$cm \cite{Abel2020} gives $|\theta| \lesssim 10^{-10}$ today (through a hadronic matrix element with its own uncertainty). Not excluded, and not claimed: an angle that relaxes or rolls; and the mirror's angle, which equals ours only by the common ceiling coupling along the reversal orbit (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), a premise of its own there, not P2), the copy being of the functional, not its coefficient. Internally the paper says only that the orientation is the one mechanism the framework itself supplies; that locates the mechanism and does not refute the alternative.
\item[(iii)] \emph{(Confinement and universality.)} The orientation route is one bit spent once (uniqueness among all conceivable mechanisms is not claimed). A flag exists on every rung of every tower (Remark \ref{rem:flaglives}), but the flag \emph{bit} only in the even residues at their P3 representatives (Theorem \claimref{dark-matter.flag-bit-exists-exactly-tower-dimension}), so the asymmetry is confined to the oriented causal towers, this one and the mirror, and the odd towers carry none by either route. The value is common to this tower and the mirror by Theorem \claimref{dark-matter.mirror-tower-copy-one}(v), under that clause's premises. No universality beyond the reversal pair is assumed: the former Premise P4 (democracy of the asymmetry over the oriented towers), retired as a postulate, was that theorem on the mirror, void on the odd residues, which carry no flag bit, and a premise only on the fork $r = 0$, where nothing stored uses it; the equality is not extendable to inequivalent towers, the asymmetry per mode depending on the tower's own charge structure.
\item[(iv)] \emph{(The value, a stance.)} $\epsilon$ is not derived here and not classified. The trichotomy's kinematic clause runs for it as for $N$ ($\epsilon$ is continuous), at that Fact's observation level; the dynamical clause does not, since generating an asymmetry from CPT-invariant dynamics is exactly what the Sakharov mechanism does. \emph{Stance, flagged and attacked in Section \ref{sec:premises}:} the framework inherits its asymmetry, and $\epsilon$ is initial data of the descent, refuted by any in-framework calculation that produces $\epsilon$ dynamically. The count uses only the equality of $\epsilon$ across the reversal orbit (Theorem \claimref{dark-matter.mirror-tower-copy-one}(v)), not its provenance. On the stance the unexplained numbers are two, $N$ and $\epsilon$, with the orientation bit of Proposition \claimref{dark-matter.orientation-arrow-seventeenth-refutation} a third datum of the same event. \emph{Note (register, 2026-11-01).} The value $\epsilon$ is now a registered free input of the series, Premise \claimref{synthesis.matter-asymmetry-registered-free-input}, which takes this stance as its statement and its refutation condition; the stance is unchanged.
\end{enumerate}

## technical
The framework inherits its asymmetry rather than generating it. The descent is irreversible, creates the tower charges and makes one orientation choice, the Witt flag, which is what particle against antiparticle means; each matches a Sakharov condition in name, but none is a mechanism producing a number. A pre-descent $\theta$-term would integrate a characteristic class of even degree, so the odd-dimensional towers carry no continuous $\theta$. In this tower a $\theta$-routed asymmetry needing an unrelaxed angle of order one at the descent is excluded empirically, since the neutron dipole bound gives $|\theta| \lesssim 10^{-10}$ today; an angle that relaxes or rolls, and the mirror's angle, are not excluded.

The flag bit exists only in the even residues at their nearest-dimension representatives, so the asymmetry is confined to this tower and the mirror, and the odd towers carry none. Equality of the value across this tower and the mirror is a clause of the copy theorem, under its premises; the former democracy-of-the-asymmetry premise P4, retired as a postulate, added to it only a premise on the fork $r = 0$ that nothing stored uses. The value $\epsilon$ is not derived; the stance, flagged as refutable by any in-framework dynamical calculation of $\epsilon$, is that it is initial data of the descent, and the count uses only $\epsilon_{2} = \epsilon_{6}$. On that stance the unexplained numbers are $N$ and $\epsilon$, with the orientation bit a third datum of the same event. (Note, 2026-11-01: $\epsilon$ is now registered as a free input of the series, with this stance's refutation condition.)

## lay
In this framework the excess of matter over antimatter is not produced by any process after the start. On a stance the paper flags, and which any calculation inside the framework that produced the excess would refute, it is part of the initial conditions the descent sets. A well-known alternative source, a constant angle in the strong force, is ruled out for our world by measurements of the neutron, although an angle that changed over time is not ruled out. The excess can only live in our world and its mirror twin; that it has the same size in the two follows from the mirror being a copy, under that result's assumptions (a wider assumption of equal size in every such world, P4, is no longer carried, since nothing used it beyond the mirror), and its size is left as an unexplained input.

## one-liner
The framework inherits rather than generates its asymmetry, which is confined to this tower and the mirror, with a common value by the copy theorem's clause (v); a constant early $\theta$-angle as its source is excluded by the neutron dipole bound, and, on a flagged stance, the value $\epsilon$ is assumed to be initial data of the descent.
