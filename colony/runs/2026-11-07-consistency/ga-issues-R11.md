# GA issues found by reader R11 (completion, clifford-structure, standard-algebra, zero-divisors)

## On entities owned by the GA rewriters (not edited by R11)
1. std-algebra.sta-matrix: one symbol, two meanings. In (ii) sigma_k are the Pauli matrices inside the
   Dirac blocks; in (iii) sigma_k = gamma_k gamma_0 are the relative vectors. Proposed: write the Pauli
   blocks of the labelled reading as sigma^P_k (or drop them in favour of the GA expansion already
   given), keep sigma_k for the relative vectors. Also (iii) and the one-liner write the pseudoscalar
   as I (sigma_1 sigma_2 sigma_3 = I); the store's name for gamma_0gamma_1gamma_2gamma_3 is I_4.
2. obj.std-algebra.spacetime-algebra: the pseudoscalar is written I; the unit principle names it I_4.
   Proposed: "Its pseudoscalar is I_4 = gamma_0 gamma_1 gamma_2 gamma_3 (written I in the standard-algebra
   objects, obj.std-algebra.pseudoscalar)".

## On entities owned by nobody (not on the GA lists; for Leon)
3. singularity.transport-schwarzschild-fibre: formal clause (4) and the proof use differential forms
   (k = sqrt r dr + sqrt(2M) dt_PG, the weighted Painleve-Gullstrand coframe, dt_s) and cometric
   components ((g_p^{-1})^{tt} = 1/f, (g_p^{-1})^{rr} = -f, g^{tr} = -beta) as the working language;
   the detector did not list it. In GTG the covector k is a vector field (its dual hb^T(k)), and
   Q*_p(k) = Q(hb^T(k)) = -r is already the stated GA reading; the component computation could become
   a labelled reading. Its definition obj.singularity.fibrewise-conformal-lift was brought into GTG
   wording by R11 (version 3) to match.
4. Undeclared stand-ins (galang unexcused; W222 only once changed): rule2.imported-gamma-matrices-odd-dimension
   and rule2.imported-graphenes-two-valleys-doubling (imported physics, propose outside_ga kind imported);
   note.rule2.what-planar-obstruction-physically, note.rule2.setting-machine-verification,
   note.rule2.setting-setting-what-imported, note.rule2.three-dimensions-matter-below,
   note.transport.three-dimensions (remarks naming the gamma matrices of the physics compared; propose
   outside_ga kind bridge). rule2.rule-2-plane was declared bridge by R11 when it was changed.
