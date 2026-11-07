# GA issues for the GA rewriters (entities of R08 in GA_OWNED.txt)

Not edited by R08.

- synthesis.slot-module-light-ray-arrays-are-weyl-components (v2): two units without a sentence on
  which acts where. The formal reads the slot module's numbers in span{1, I_4}; proof (i) writes the
  massive equation $\nabla\psi I_4\sigma_3 = \mathcal{M}(\psi)$, i.e. Hestenes' right unit $i_H =
  R_{I_4\sigma_3}$ on the spinor values (as in synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays).
  Proposed: one sentence saying $i_H$ acts on the spinor values and span{1, I_4} on the internal index,
  and whether they are identified on $V_+$ (I did not settle this). The formal also writes
  $\Lambda^\bullet\C^5$ (fine under U1, already declared in words).
- synthesis.euler-term-horizon-entropy-shift (v4): formal (i) and proof keep $\epsilon_{abcd}F^{ab}\wedge
  F^{cd}$ and $E_4 = R_{abcd}R^{abcd} - \ldots$ in components and forms beside the GA form of $E_4$; no
  error found (all numbers rechecked: dS 3 -> 0, Nariai 2 -> -4, nucleation -1 -> -4, Euclidean actions).
- families.rigidity-pairing-sector-one-event (v5, already rewritten) and
  note.families.setting-machine-verification (v2): no remaining issue found. R08 rewrote the matching
  cross products in note.families.setting-gaussian-theorems (not owned) to the rigidity proof's
  $-I_f(p\wedge q)$ notation, so the two now agree.

Other GA-language items in R08's non-owned entities, listed for Leon in consistency-R08.md rather
than rewritten (not pure notation): synthesis.kerr-ring-count-misses-area-law (metric and coordinate
forms, unnamed unit in $z = r - Iau$); synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free
proof (5) defines the cross product as $a\wedge b = I_3(a\times b)$ and uses it once (could be stated
with the dual alone); synthesis.boundary-mode-first-law-of-entanglement (iv) works in metric
components with the sign conversion stated (consistent, kept as the import's language).
