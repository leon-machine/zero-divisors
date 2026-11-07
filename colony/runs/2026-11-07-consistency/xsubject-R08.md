# Cross-subject items found by R08 (entropy, generations)

1. Normalisation of the frozen point's norm.
   - Mine: synthesis.sds-clausius-fixes-area-constant (iv), synthesis.de-sitter-entropy-pi-n-squared,
     synthesis.de-sitter-mode-count (all use $N^2 = M_P^2/Q(I_\Lambda)$, $Q(I_\Lambda) = H^2 = \Lambda/3$).
   - Other subject: standard-model.imported-frozen-point-dictionary states $H^2 = Q(I_\Lambda)$ with
     $I_\Lambda = n_\infty + (\Lambda/6)n_0$ and does not say which null-pair normalisation it uses.
   - Evidence: $Q(n_\infty + (\Lambda/6)n_0) = (\Lambda/3)\,n_0\cdot n_\infty$, so $+\Lambda/3$ needs
     $n_0\cdot n_\infty = +1$ (the sds check uses $n_0 = \tfrac12(e_+ + e_-)$, $n_\infty = e_+ - e_-$); in
     T01's normalisation ($n_0\cdot n_\infty = -1$, conventions.md) it is $-\Lambda/3$.
   - Done on my side: the sds proof now names the normalisation. Proposed for the dictionary's owner:
     add "in the normalisation $n_0\cdot n_\infty = +1$" to its statement.
