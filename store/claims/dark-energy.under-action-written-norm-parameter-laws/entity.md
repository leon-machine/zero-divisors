---
id: dark-energy.under-action-written-norm-parameter-laws
kind: claim
version: 4
title: Under the action as written, the norm is a parameter of the laws
status: proved
region: dark-energy
subject: dark-energy
tags: [the-number-n, undetermined-input, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
derivations:
- name: main
  uses:
  - dark-energy.four-alternatives-are-exhaustive-three-are@2
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - dark-energy.imported-frozen-point-geometry@6
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  - standard-model.trichotomy-what-kind-number@10
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:parameter
- kind: check
  ref: check.py::check_fixed_lambda_nine_and_de_sitter_scale
- kind: check
  ref: check.py::check_n_varies_with_lambda
- kind: check
  ref: check.py::check_varying_lambda_single_norm_mode
locators:
  paper: T10
  number: Prop 5.8
  label: prop:parameter
  line: 1033
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: dimension 9 at fixed Lambda, H^2 = Q(I) on the de Sitter field, d(N^2)/dLambda, and with Lambda free dimension 10 with one norm mode outside the 9-dimensional orbit. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Kept all five premises, each used in the proof; the E204 here comes from the trichotomy fact,
      a premise outside this list. Levels pass: conditions already kept.'
  env: proposition
---

## formal
In the three-argument functional of Proposition \claimref{dark-energy.point-infinity-has-no-physical-fluctuation}, $\Lambda$ enters as the value of the Stelle-West constraints $Q(I) = \Lambda/3$, $Q(V) = -3/\Lambda$, a number fixed before variation: it is the index $\mu$ of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape}. Consequently:
\begin{enumerate}
\item[(i)] with $\Lambda$ fixed, the constrained fluctuation space of $(I, V)$ has dimension nine and the nine broken generators act onto it bijectively (Proposition \claimref{dark-energy.point-infinity-has-no-physical-fluctuation}): no fluctuation of the norm exists, every solution with parameter $\Lambda$ has $H^2 = Q(I) = \Lambda/3$ on its de Sitter region, and $N = M_P\sqrt{3/\Lambda}$ is constant on each $\mathcal{S}_\Lambda$;
\item[(ii)] $N$ varies with $\Lambda$ across the family, $d(N^2)/d\Lambda = -3M_P^2/\Lambda^2 \neq 0$, so it is not (D); and it is not (K), by the rescaling argument of Fact \claimref{standard-model.trichotomy-what-kind-number};
\item[(iii)] therefore $N$ is (P), a parameter of the laws, and not (I): clause (3) of the Standard-Model paper's classification, ``$N$ is initial data'', is false for the action as written.
\end{enumerate}
If instead $\Lambda$ is allowed to vary, the linearised constraints become three independent conditions on the thirteen components $(\delta I, \delta V, \delta\Lambda)$, the constrained space has dimension ten, the gauge orbit is still nine-dimensional (bivectors do not change a norm), and exactly one non-gauge direction appears: the norm mode
\[
(\delta I, \delta V, \delta\Lambda) \;\propto\; \Bigl(\frac{I}{2\Lambda},\ -\frac{V}{2\Lambda},\ 1\Bigr),
\]
which is the tangent at $s = 1$ of the rescaling family $(sI, V/s, s^2\Lambda)$ and which needs an equation of motion the action does not supply.

## technical
In the three-argument functional, $\Lambda$ enters as the value of the Stelle-West constraints $Q(I) = \Lambda/3$, $Q(V) = -3/\Lambda$, a number fixed before variation, so it is the index $\mu$ of the four-way classification. With $\Lambda$ fixed, the pure-gauge count leaves no fluctuation of the norm, and $N = M_P\sqrt{3/\Lambda}$ is constant on each solution space $\mathcal{S}_\Lambda$. It varies across the family, $d(N^2)/d\Lambda = -3M_P^2/\Lambda^2\neq 0$, so it is not dynamically fixed, and by the rescaling argument it is not kinematic; by exhaustiveness it is a parameter of the laws and not initial data, for the action as written.

If $\Lambda$ is allowed to vary, the constrained space of $(\delta I,\delta V,\delta\Lambda)$ has dimension ten against a nine-dimensional gauge orbit, leaving one non-gauge norm mode, $(\delta I,\delta V,\delta\Lambda) \propto (I/2\Lambda, -V/2\Lambda, 1)$, the tangent of the rescaling family $(sI, V/s, s^2\Lambda)$; it needs an equation of motion that the action does not supply.

## lay
The cosmological constant fixes the length of the frozen point. Under the action exactly as written, this length cannot fluctuate within any one solution, yet it differs between theories with different cosmological constants. That makes it a setting of the laws rather than initial data chosen for each universe. Making it initial data would need an extra equation of motion that the action does not provide.

## one-liner
Under the action as written, $N = M_P\sqrt{3/\Lambda}$ is constant on each solution space and varies with $\Lambda$, so it is a parameter of the laws and not initial data.
