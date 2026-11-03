---
id: standard-model.largeness-number-universes-boundary-modes
kind: claim
version: 3
title: The largeness of $N$ is the size of the universe's boundary mode space
status: conjectured
region: standard-model
subject: dark-energy
tags:
- the-number-n
- boundary-modes
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
lineage:
  motivated_by:
  - standard-model.dating-descent
  - standard-model.one-number-explain
  - standard-model.what
  - standard-model.why-large
locators:
  paper: T12
  number: Obs 7.5
  label: obs:length
  line: 1255
extraction:
  env: observation
  context_refs:
  - standard-model.dating-descent
  - synthesis.de-sitter-mode-count
  - synthesis.de-sitter-entropy-pi-n-squared
  - synthesis.imported-gibbons-hawking-entropy
  - dark-energy.frozen-point-makes-stelle-west-vector
  - standard-model.one-number-explain
  - standard-model.what
  typing:
    by: ai-typing-pass
    added:
    - standard-model.why-large
    note: 'Added the why-large observation to motivated_by, since the statement draws on the observations
      from what-N-is through dating, which includes it. Levels pass: conditions already kept.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Terminal observation of the N line, with lineage to the observations it unifies.
  source_formal: 'Observations \claimref{standard-model.what} through \claimref{standard-model.dating-descent}
    force a unification of questions: `why is $N$ large'' is `why does the universe have so many boundary
    modes'', which is the dating question just registered. The three smallness problems compressed into
    $N$ by Observation \claimref{standard-model.one-number-explain}, and the number of the universe''s boundary
    modes, are one question asked once: this paper does not answer it, but it can certify that the question
    requires exactly one number, that the number (on the indication of Observation \claimref{standard-model.what}(i))
    counts the modes of the universe''s own horizon, and that its explanation lies at the first event. At
    observation level, and flagged as such.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 3
    note: 'Follows the conditional dating: ''its explanation lies at the first event'' rested on standard-model.dating-descent(ii)
      unconditionally; every level now carries the Henneaux-Teitelboim condition and cites the T10 result
      that N is a parameter of the laws under the action as written. Original formal in source_formal.'
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Brought into line with the performed count (note.synthesis.what-n-is-counted; conventions.md known
      limit 5), as was done for standard-model.why-large. N is not the number of the universe''s boundary modes:
      the horizon entropy is exactly pi N^2 (synthesis.de-sitter-entropy-pi-n-squared) and, under the black hole''s
      counting rule, the mode count is pi N^2/ln 2, about 4.8e122, of which N, about 1.03e61, is the square
      root up to sqrt(pi/ln 2) (synthesis.de-sitter-mode-count). The question becomes why the universe''s horizon
      mode space is so large, of order 1e122 modes; its unification with the smallness problems and the dating
      question, and the Henneaux-Teitelboim condition, are unchanged. Title changed to match. Numbers: H0 = 67.4
      km/s/Mpc, Omega_Lambda = 0.685, M_P = 1.221e19 GeV give H = 1.19e-42 GeV and N = 1.03e61 (computed twice
      independently). The entropy is qualified as the Einstein-Hilbert area law''s: under the series''
      MacDowell-Mansouri action as written, the Gauss-Bonnet term contributes -pi N^2 to the Wald (Jacobson-Myers)
      entropy of the horizon, so the total is zero; equivalently the on-shell Euclidean action of the S^4
      saddle vanishes, since the Cartan curvature is zero there. The mode-count lineage is recorded under
      context_refs rather than motivated_by, since synthesis.de-sitter-mode-count is itself motivated by
      this observation.'
  open_problem: op.t12-n-after-the-count
---

## formal
Observations \claimref{standard-model.what} through \claimref{standard-model.dating-descent} force a unification of questions: `why is $N$ large' is `why is the universe's own horizon mode space so large', which is the dating question just registered. The size of that space is fixed by $N$ and is not $N$: the cosmological horizon's entropy is exactly $\pi N^{2}$ under the Einstein-Hilbert area law (Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared}, from Fact \claimref{synthesis.imported-gibbons-hawking-entropy}); the Gauss-Bonnet term of the MacDowell-Mansouri action as written (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}) contributes $-\pi N^{2}$, so the reading below presupposes that topological term subtracted or normalised away. Under the black hole's counting rule its boundary modes number $\pi N^{2}/\ln 2$, about $4.8 \times 10^{122}$, with $N$, about $1.0 \times 10^{61}$, the square root of that count up to $\sqrt{\pi/\ln 2}$ (Theorem \claimref{synthesis.de-sitter-mode-count}). The three smallness problems compressed into $N$ by Observation \claimref{standard-model.one-number-explain}, and the size of the universe's boundary mode space, are one question asked once: this paper does not answer it, but it can certify that the question requires exactly one number, that the number fixes the capacity $C = |J|\ln 2$ of the universe's own horizon as its square root up to $\sqrt{\pi}$, and the raw mode count $|J|$ as its square root up to $\sqrt{\pi/\ln 2}$ (exactly for the area-law entropy, under the counting rule for the mode count), and that its explanation lies at the first event if $N$ was fixed there, which Observation \claimref{standard-model.dating-descent}(ii) holds only under the Henneaux-Teitelboim promotion; under the action as written $N$ is a parameter of the laws (Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}). At observation level, and flagged as such.

## technical
At observation level, the preceding observations unify two questions: asking why $N = M_{P}/H$ is large is asking why the universe's horizon mode space is so large, which is the dating question. $N$ is not itself the number of boundary modes: under the Einstein-Hilbert area law the horizon entropy is exactly $\pi N^{2}$ (the Gauss-Bonnet term of the series' own action as written would subtract $\pi N^{2}$ and leave zero), and under the black hole's counting rule the horizon carries about $\pi N^{2}/\ln 2 \approx 4.8 \times 10^{122}$ modes, of which $N \approx 1.0 \times 10^{61}$ is roughly the square root. The three smallness problems compressed into $N$ and the size of the universe's boundary mode space are one question asked once.

The paper does not answer it, but certifies that the question requires exactly one number, that this number is the square root of the capacity of the universe's own horizon up to a factor $\sqrt{\pi}$ (and of the raw mode count up to $\sqrt{\pi/\ln 2}$), and that its explanation lies at the first event, if the dating observation's condition holds: $N$ is fixed at the origin only under the Henneaux-Teitelboim promotion, and under the action as written it is a parameter of the laws.

## lay
Several puzzles about why certain quantities in nature are so small all reduce, in this framework, to one large number, about $10^{61}$. This observation says that number also sets how much the boundary of the observable universe can hold: that boundary carries about $10^{122}$ basic modes, roughly the square of the number. If a known modification of the theory is adopted, explaining the number then becomes the same task as explaining how the universe began; with the theory as written the number is a fixed constant of the laws. The paper does not give that explanation; it only narrows the question to this one number.

## one-liner
At observation level, why $N$ is large and why the universe's horizon mode space is so large (about $\pi N^{2}/\ln 2 \approx 4.8 \times 10^{122}$ modes, $N$ roughly its square root) are one question, requiring one number whose explanation lies at the first event if, under the Henneaux-Teitelboim promotion, it was fixed there.
