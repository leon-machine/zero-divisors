---
id: scrambling.intrinsic-clock-ic-flagged-premise
kind: claim
version: 3
title: Intrinsic clock (IC), flagged premise
status: postulate
region: scrambling
subject: entropy
tags: [entropy-premises, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
locators:
  paper: T08
  number: Principle 4.1
  label: prin:ic
  line: 673
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Version 3 adds a scope sentence, at Leon's decision of 23 October (cutoff premises as a Schwarzschild calibration only), that (IC), with (C1) and (C2), is read as a calibration on the Schwarzschild family, where it gives the counted epoch as the modular period; read with a horizon's modular period on Schwarzschild-de Sitter the count is u/(3u-2) times A_b/4 and no horizon period gives the area law (synthesis.cutoff-count-is-not-a-local-density-on-sds), and the literal cutoff count also misses the area law on Kerr (synthesis.kerr-ring-count-misses-area-law). The premise itself is unchanged on the Schwarzschild family.
  env: principle
  unresolved_refs:
  - rem:fence
  flags:
  - 'summary principle: derivation is its cited theorems'
  typing:
    by: ai-typing-pass
    removed:
    - scrambling.epoch-modular-period-two-unknowns-become
    note: 'Made a postulate: the paper states this as a premise, not a theorem; the derivation, checked_by
      and proof file (which only repeated the statement) were removed and dependants now take it under
      assumes.'
---

## formal
The counted epoch is intrinsic to the boundary modes: whatever span of Killing time the count is taken over is determined by the dynamical structure of the boundary modes themselves, not by an external choice. This is a naturality premise, not a theorem; its named failure mode is stated in Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}, and the circularity fence of Remark \ref{rem:fence} protects it from self-confirmation.

\emph{Scope (Schwarzschild calibration).} This premise, with Premises \claimref{singularity.c1-curvature-cutoff} and \claimref{singularity.c2-cell-density}, is read as a calibration of the count on the Schwarzschild family only, where it makes the counted epoch the modular period (Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}). Read with a horizon's modular period on a Schwarzschild-de Sitter hole, the literal cutoff count with the density fixed at $\Lambda = 0$ is $u/(3u - 2)$ times $A_{b}/4$, $u = 2M/r_{b}$, for every $\Lambda > 0$, and neither horizon's period gives $A_{b}/4$ (Theorem \claimref{synthesis.cutoff-count-is-not-a-local-density-on-sds}); the literal cutoff count also misses the area law for spinning holes with $a \ge 2(2M)^{2/3}$ (Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}). Away from the Schwarzschild family the count is read through the horizon placement of clause (Loc) of Premise \claimref{synthesis.c-loc-local-horizon-premise}, with a density fixed by flat tangent data.

## technical
The intrinsic-clock premise (IC) states that the span of Killing time over which the boundary modes are counted is fixed by the dynamical structure of the boundary modes themselves, not chosen from outside. It is a naturality premise, not a theorem.

Its failure mode is explicit: under (IC) the epoch is the modular period $\beta$ and the density must be $\nu = 1/16\pi$ in the 1-nat convention, so a calibration returning any other value refutes it. A circularity fence keeps it from confirming itself.

It is read as a calibration on the Schwarzschild family only. Read with a horizon's own modular period on a Schwarzschild-de Sitter hole, the cutoff count exceeds a quarter of the horizon area by the factor $u/(3u - 2)$, $u = 2M/r_{b}$, and neither horizon's period removes the excess; the literal cutoff count also misses the area law for fast-spinning holes.

## lay
This is an assumption, not a result: the time over which a black hole's interior modes are counted is set by those modes' own internal clock rather than picked by hand. It is flagged openly so that its consequences can test it. If the numbers it leads to fail, the assumption fails with them. It is used only for non-rotating black holes in otherwise empty space: with a positive cosmological constant, the same reading of the clock gives the wrong entropy.

## one-liner
Premise (IC): the counted epoch is determined by the boundary modes' own dynamics, not by an external choice; read as a Schwarzschild calibration only.
