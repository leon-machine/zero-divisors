# GA issues from reader R06 (quantum-fields and singularity) for the GA rewriters

Entities below are GA-owned (GA_OWNED.txt); R06 did not edit them. Each item: id, what, proposed fix.

1. synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points (tensor). The formal level writes
   the metric as $-dt^2 + t^{2p_1}dx^2 + \dots$, signature (-,+,+,+), without declaring it, while the frame,
   the duals $I_4\,e_0\wedge e_i$ and the store conventions are (+,-,-,-); the proof says $C_{0i0i}$ is minus
   $C_{0i}{}^{0i}$ "since $g_{00} = -1$". Dictionary C7: declare the signature or restate in (+,-,-,-), and say
   in which curvature sign $\lambda_i$ and $Rt^2 = -\tfrac23$ are given (checked: the store-sign scalar in
   (+,-,-,-) equals the round-sphere-positive scalar in (-,+,+,+), so $-\tfrac23$ survives; the sign of
   $\lambda_i$ should be stated in the store sign). $E_1$, $E_2$, $\lambda_i$ and the Weyl-flat points verified by
   hand.
2. synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state (tensor).
   Same mixing: $G_{a,b} = \mathrm{diag}(-t^a, t^b, 1, 1)$, $g_{1,0} = -d\tau^2 + \dots$ and $R = \tfrac32 t^{-2}$ are in
   (-,+,+,+) (the proof names the check's Riemann convention), while (ii) uses the Hestenes equation with
   $\gamma_0^2 = 1$. Declare the signature (C7) and the curvature sign of $R$ and $R_{ab}R^{ab}$. Values checked
   ($R = \tfrac32t^{-2}$, $R_{ab}R^{ab} = \tfrac34t^{-4}$).
3. synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity
   (matrices). Formal (1): "the sums over the two spin states of an outgoing particle and an incoming
   antiparticle are $p + m$ and $p - m$" is narrower than what the tree trace uses (incoming electron $p_1 + m_e$,
   outgoing antimuon $p_4 - m_\mu$); the proof's Step 1 has the full rule. Proposed: "the spin sums of a particle,
   incoming or outgoing, and of an antiparticle are the multivectors $p + m$ and $p - m$". All numbers verified
   (tree formula, $\beta(3-\beta^2)/2$, $\mathrm{Im}\,\hat\Pi = -\tfrac{\alpha}{3}\beta(3-\beta^2)/2$, $-\tfrac53$).
4. synthesis.one-loop-qed-in-the-spacetime-algebra (bridge) proof (1): "The Dirac matrices over $\mathbb{Q}(i)$";
   synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces proof (3): "hermitian generators
   ... over $\mathbb{Q}(i)$". Bare unit inside $\mathbb{Q}(i)$, which the detector skips (it reads "(i)" as a
   clause label). Proposed: $\mathrm{span}_{\mathbb{Q}}\{1, I_5\}$ for the matrix reading (as the triangle result
   writes it) and $\mathrm{span}_{\mathbb{Q}}\{1, I_4\}$ for the gauge generators.
5. synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport
   (extraction note). The note quotes Sahlmann and Verch's regularisation as $s - 2i\epsilon(t(x) - t(y)) +
   \epsilon^2$ with $s$ positive for spacelike separation. With $s = -2\sigma$ this is
   $-2(\sigma + i\epsilon\Delta t - \epsilon^2/2)$, the opposite sign of the $\epsilon$ term to the store's flat form
   $\tfrac12 Q(x - x' - \epsilon I_5e_0) = \sigma - \epsilon I_5\xi_0 - \epsilon^2/2$ (computed) and to Kay and Wald's
   $\sigma_{KW} + 2i\epsilon\Delta T + \epsilon^2$, which equals $-(t - i\epsilon)^2 + r^2$. Worth rechecking the
   quoted sign against the source (an ordering or signature convention may explain it). The $\epsilon^2$ term is
   $-\epsilon^2/2$ in $\sigma$ units and $+\epsilon^2$ in $s$ units: both forms agree on it.
6. synthesis.two-loop-qed-in-the-spacetime-algebra-continued-in-dimension-gives-the-second-beta-coefficient
   proof Step 3(a): "by Feynman parameters and Step 0's integrals": there is no Step 0; the integrals are those of
   the Conventions paragraph. Typo.
7. synthesis.attachment-transport-is-flat-only-where-weyl-vanishes is not GA-owned; R06 added the which-unit
   sentence. Its proof still builds the Weyl maps from a complex symmetric traceless $3\times3$ matrix and uses a
   labelled two-spinor reading $\Psi_{ABCD}$; both are labelled readings beside the GA computation (kernel of the
   field strengths in $\Cl(2,4)$). Listed for completeness; no change asked of the rewriters.
8. singularity.connection-bivector-computed (forms), note.singularity.setting-curvature-operator-cartan-structure-equations
   (forms): no error found. For the rewriters' restatement: the dictionary (C6, C10) records $\sigma_r = e_re_t$ and
   the definition's sign for $\Omega$; R06 used that orientation to clarify the curvature-sign sentences of
   singularity.solution-where-divergence-lies and singularity.curvature-gauge-field-exact-shape-decoupling
   (checked with lib/GA.py: $\sigma_r = -(e_t\wedge e_r)$, background $R(e_t\wedge e_r) = (2M/r^3)\sigma_r$, store
   $\mathcal{R}(\sigma_r) = +(2M/r^3)\sigma_r$). Keep $\sigma_r$'s orientation stated when the forms become GA.
