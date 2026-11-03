---
id: singularity.envelope-endpoint-why-boundary-mode-locality
kind: claim
version: 7
title: The envelope and the endpoint, and why boundary-mode locality is needed for them
status: proved
region: singularity
subject: entropy
tags: [entropy-premises, radiation-spectrum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  assumes:
  - singularity.rate-models-kinematic-inputs-l-u@2
  - singularity.l-boundary-mode-locality@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:11.6
- kind: check
  ref: check.py::check_envelope_and_endpoint_under_diagonal_dynamics
- kind: check
  ref: check.py::check_locality_premise_is_necessary
locators:
  paper: T05
  number: Cor 11.6
  label: cor:envelope
  line: 2286
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the envelope and endpoint on two diagonal runs, and the (L_E) witness rho_L2 = diag(5968/15625, 9657/15625) with S_R > S_th by rigorous bounds. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check strengthened: envelope attained (S_L = S_th) before any eviction and the per-qubit capacity ln 2 pinned; size constants moved to module level. Version 6 -> 7.'
  env: corollary
  unresolved_refs:
  - rem:hopresidual
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    - singularity.class-relative-no-go-no-supplied
    added:
    - singularity.rate-models-kinematic-inputs-l-u
    - singularity.l-boundary-mode-locality
    note: 'Kept the eviction theorem (the bound and endpoint are its clause 2); removed the class-relative
      no-go, cited only to explain why the counterexample lies outside the proved class, and the transport-algorithm
      repair edge; added the rate-model and (L_E) postulates the statement names. Levels pass: the lay
      now names the rate model''s four inputs and (L_E), all in this entry''s assumes.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.rate-models-kinematic-inputs-l-u
---

## formal
From (L), (U), (C), (I) and (L$_E$), with no typicality and no assumption about the placement of correlations:
\[
S_R(t) \;\leq\; \min\bigl(\Sth(t),\, C(t)\bigr) \qquad \text{and} \qquad S_R(\text{complete evaporation}) = 0 .
\]
The premise (L$_E$) cannot be dropped: a window unitary that is not number diagonal can leave the remaining window qubit far more mixed than its thermal marginal, and then $S_R$ exceeds $\Sth$. Two pairs with $(c, s) = (\tfrac{24}{25}, \tfrac{7}{25})$, the window rotation $|00\rangle \mapsto \tfrac35|00\rangle + \tfrac45|11\rangle$, $|11\rangle \mapsto -\tfrac45|00\rangle + \tfrac35|11\rangle$ on $(L_1, L_2)$, and then the eviction of $L_1$ leave $\rho_{L_2} = \operatorname{diag}(\tfrac{5968}{15625}, \tfrac{9657}{15625})$, so $S_R = S_L \approx 0.96$ bits against $\Sth = 2H(\tfrac{576}{625}) \approx 0.55$ nats, that is $0.79$ bits.

## technical
From the rate-model inputs (L), (U), (C), (I) and boundary-mode locality (L$_E$), with no typicality and no assumption about where correlations sit, the radiation entropy obeys $S_R(t) \leq \min(\Sth(t), C(t))$ at every stage, and $S_R = 0$ at complete evaporation.

(L$_E$) cannot be dropped: in an explicit two-pair example a window unitary that is not number diagonal leaves the remaining window qubit more mixed than its thermal marginal, giving $S_R \approx 0.96$ bits against $\Sth \approx 0.79$ bits.

## lay
In the framework's model of black-hole evaporation, which assumes two sectors, overall purity, a window of the stated size and fresh thermal pairs injected at each step (the rate model's inputs (L), (U), (C), (I)), the entropy of the emitted radiation never exceeds either its thermal value or the black hole's remaining capacity, and it returns to zero once the hole has fully evaporated. This needs no assumption that the state is typical. It does need the assumption that the internal dynamics never shifts occupation numbers (boundary-mode locality, (L$_E$)): a small explicit example shows that without it the bound fails.

## one-liner
Under (L), (U), (C), (I) and (L$_E$), $S_R(t) \leq \min(\Sth(t), C(t))$ with $S_R = 0$ at complete evaporation, and the bound can fail without (L$_E$).
