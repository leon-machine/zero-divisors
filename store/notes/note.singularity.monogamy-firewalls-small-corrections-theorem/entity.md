---
id: note.singularity.monogamy-firewalls-small-corrections-theorem
kind: note
version: 2
title: Monogamy, firewalls, and the small-corrections theorem
status: remark
subject: entropy
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Fable 5.2
  role: 'sentence naming the stored three-party trade-off as the inequality behind the use of monogamy, with its caveats'
  version: 2
  source: maintainer pass of 2026-11-10
comments_on:
- singularity.what-event-returns-radiation
- singularity.eviction-window-thermal-product-radiation-entropy
locators:
  paper: T05
  number: Rem 11.9
  label: rem:monogamy
  line: 2314
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. A dated sentence names the stored three-party trade-off of CHSH values (synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two) as the inequality behind the remark''s use of monogamy, with the caveats that result states: the shared party uses the same two observables in both tests, and with one mode per party the observables are parity-odd elements. The remark is otherwise unchanged.'
---

## formal
Two classical objections must be located relative to the eviction mechanism, because the chain's state class invites both. First, monogamy: the firewall argument of \cite{AMPS2013} forbids a late quantum from being maximally entangled with its interior partner and with the early radiation at once. The rate model never asks for that: a window qubit is entangled with its own partner while it is in the window, and its correlation with the early radiation as a whole is acquired at eviction, when the qubit itself is transferred to the radiation sector (Corollary \claimref{singularity.what-event-returns-radiation}), so at no stage does one quantum carry both entanglements. The cost is stated plainly: eviction is a physical transfer of an interior degree of freedom into the radiation, and the smoothness of the horizon it presupposes is asserted by the model, not derived, which is exactly the point \cite{AMPS2013} press. Second, the small-corrections theorem of \cite{Mathur2009} shows that no accumulation of order-$\epsilon$ corrections to the pairwise Hawking process can return the radiation entropy to zero. Eviction does not evade that theorem by small corrections; it violates its locality hypothesis outright, the evicted qubit being an order-one, nonlocal transfer out of the interior. That is a legitimate alternative and a costly one: the falling branch of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} stands or falls with the physical reality of eviction, which is the same commitment the islands programme makes in its own language (Remark \claimref{note.singularity.island-dictionary-one-dissonance}).

\emph{Added 10 November 2026.} For CHSH values the inequality behind this use of monogamy is the three-party trade-off of Theorem \claimref{synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two}: under Premise (P), positivity of values (\claimref{synthesis.premise-positivity-of-values}), two CHSH values that share one party satisfy $\omega(C_{AB})^{2} + \omega(C_{AD})^{2} \le 8$, so a window mode whose pair with its partner has squared value $S^{2}$ leaves any third party a squared value of at most $8 - S^{2}$, which for the pair state of weight parameter $r$ at its best directions is $4r^{2}$ (clause (v) there). Two caveats stated there apply. The shared party must use the same two observables in both tests. And with one mode per party the observables are odd under the total parity: if only parity-even elements are observables, a single window mode has no CHSH value above $2$ and the statement is empty for it.

## technical
pending

## lay
pending

## one-liner
pending
