---
id: families.selectivity-observation-level
kind: claim
version: 4
title: Selectivity, at observation level
status: conjectured
region: families
subject: generations
tags:
- flavour-and-mixing
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
lineage:
  motivated_by:
  - families.imported-one-derived-generation-hypothesis-s
  - families.koide-nullity-condition-one-member-invariant
  - synthesis.mass-ordered-dressing-cannot-spoil-koide
locators:
  paper: T13
  number: Obs 7.3
  label: obs:selectivity
  line: 875
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 4 (Leon''s acceptance of synthesis.mass-ordered-dressing-cannot-spoil-koide, 2026-10-26): the observation no longer attributes the quarks'' failure of the relation to the strong dressing, since a dressing that is flavour-blind or favours the lighter quarks can only lower the Koide quotient and perturbative QCD running, pole conversion and constituent dressing are of that kind (argued, standard QCD); it now records the asymmetry, says the dressing does not account for the failure at that level, and names the case the result leaves open. The neutrino exemption is unchanged. Status stays conjectured (observation level); the paper''s wording is kept under source_formal.'
  env: observation
  context_refs:
  - families.imported-one-derived-generation-hypothesis-s
  outside_pilot_cites:
  - ButlerT15
  typing:
    by: ai-typing-pass
    note: 'Observation left conjectured with its existing motivated_by (the derived generation under Hypothesis
      (S)). Levels pass: lay rewritten to keep Hypothesis (S) and the observation level, and to say neutrinos
      are exempt rather than that the relation fails for them.'
  source_title: Selectivity, at observation level
  source_formal: 'The quarks fail the relation at pole masses, and the framework contains the structural
    asymmetry a selective mechanism needs: under Hypothesis (S) the leptons are whole-twistor states,
    colour singlets whose brackets are physical masses undressed, while quarks are pair-level cells, their
    pole masses dressed by the strong interaction (Fact \claimref{families.imported-one-derived-generation-hypothesis-s}).
    The neutrinos are exempt structurally: their masses are seesaw-composed, quadratic again in the bracket-linear
    objects, so the null condition constrains the unobservable Dirac layer and imposes nothing on the
    physical $m_{\nu}$ (the neutrino paper T15 \cite{ButlerT15} carries the neutrino mass sector and does
    not treat the relation; the exemption is this paper''s observation). Both statements are consistencies,
    not derivations, and are flagged at observation level; a genuine account would compute the dressing.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Whole-twistor states are now whole-spinor states (states of a whole conformal spinor); nothing
      else was in twistor form.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - families.koide-nullity-condition-one-member-invariant (motivated_by)
    added_dependants: []
    added_about: []
    verdict: connected
    note: Lineage now includes the nullity proposition, the null condition it says the neutrino exemption
      leaves unconstrained.
---

## formal
The quarks fail the relation at pole masses, and under Hypothesis (S) the framework contains a structural asymmetry between leptons and quarks: the leptons are whole-spinor states (each a whole conformal spinor), colour singlets whose brackets are physical masses undressed, while quarks are pair-level cells, their masses dressed by the strong interaction (Fact \claimref{families.imported-one-derived-generation-hypothesis-s}). The asymmetry does not account for the quarks' failure at the level of the known strong dressing: a dressing that is flavour-blind or favours the lighter quarks can only lower the Koide quotient, the measured quark quotients already exceed $\tfrac23$ in both sectors at every standard mass definition, and perturbative QCD running, pole conversion and constituent dressing are of that kind (argued, standard QCD), so they cannot turn Koide brackets into the measured quark masses; a Koide bracket would need a dressing favouring the heaviest quark over a lighter one by a factor of at least $1.88$ (down sector) and $8.67$ (up sector, own-scale masses), and a dressing that raises the middle mass and lowers the lightest relative to the heaviest is not excluded (Theorem \claimref{synthesis.mass-ordered-dressing-cannot-spoil-koide}). The neutrinos are exempt structurally: their masses are seesaw-composed, quadratic again in the bracket-linear objects, so the null condition constrains the unobservable Dirac layer and imposes nothing on the physical $m_{\nu}$ (the neutrino paper T15 \cite{ButlerT15} carries the neutrino mass sector and does not treat the relation; the exemption is this paper's observation). Both statements are flagged at observation level: the first records the quarks' failure and that the strong dressing, as far as it is known, does not explain it, so whether the quark brackets satisfy the relation at all is open; the second is a consistency, not a derivation.

## technical
The quarks fail the Koide relation at pole masses. Under Hypothesis (S) leptons are whole-spinor colour-singlet states whose brackets are physical masses undressed, while quarks are pair-level cells whose masses are dressed by the strong interaction. That asymmetry was read as the reason for the quarks' failure, but the dressing moves the quotient the wrong way: the quotient is unchanged by a common factor and lowered by raising the lighter masses, perturbative strong dressing is of that kind (argued from standard QCD), and the measured quark quotients are already above $\tfrac23$. So the strong dressing, perturbative or constituent, does not explain the failure; a Koide bracket would need a dressing favouring the heaviest quark by at least $1.88$ (down) and $8.67$ (up), and only a dressing that raises the middle mass while lowering the lightest is left untreated. Neutrino masses are seesaw-composed, quadratic again in the bracket-linear objects, so the null condition would constrain only the unobservable Dirac layer and nothing in the physical $m_{\nu}$.

Both statements are flagged at observation level; whether the quark brackets satisfy the relation at all is open.

## lay
The Koide relation works for the charged leptons but fails for quarks at their measured masses, and it says nothing about the physical neutrino masses. Under the paper's slot hypothesis (S), the framework treats these particles differently: charged leptons are complete units whose masses are seen directly, quark masses are altered by the strong force, and neutrino masses arise through an extra step, so for them the relation could only constrain a hidden layer. The strong force was the natural suspect for the quarks' failure, but it can only lower the formula's key number, and the measured quark values already sit above the value the formula predicts: quarks that obeyed the formula before the strong force acted would end up below it, not where they are. So the strong force, as far as it is understood, does not explain the failure. This remains an observation, not a derivation.

## one-liner
Under Hypothesis (S) leptons are undressed colour singlets and quarks strongly dressed, but the known strong dressing can only lower the Koide quotient and the quarks are already above $\tfrac23$, so it does not explain the quarks' failure; seesaw-composed neutrinos are exempt; at observation level.
