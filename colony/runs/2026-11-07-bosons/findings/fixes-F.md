# Fixes, filer F (run 2026-11-07-bosons)

Proposal: proposals/synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
Referee: verify/R.md, verdict SOUND WITH FIXES. Every fix applied in place; no rebuttals.

| R.md fix | Where applied |
|---|---|
| 1. Attribution of the infinite-band relation | Extraction note: the claim that the band modes "satisfy the canonical relations on the infinite band" is no longer listed as new. The note now says the relations are stored in singularity.bosonisation-bridge-s-wave-sector (1) (s-wave boundary modes) and follow from hawking.current-commutator-exactly-edge-split. What stays new: the restriction of omega_0, and of any symbol phi(P) tensor id_K, to band modes; the explicit domain D; and their combination. "Without normal ordering" dropped as a contrast in the formal, proof and note. Formal (vi) and the proof now cite Theorem singularity.bosonisation-bridge-s-wave-sector(1) via claimref, with no uses edge (as store precedent allows). |
| 2. Scope of (N+) | "Every horizon generator" replaced by "each generator of a horizon that Premise (N+) covers" in the Reading, technical and extraction note. Lay now says "the horizon lines it covers". Formal (vi) now reads "the state Premise (N+) assigns to the generator, by the uniqueness in Theorem ...null-vacuum-on-a-horizon-generator(ii)". No assumes edge. |
| 3. Technical, mean square | The referee's sentence was inserted verbatim, with the qualifier that convergence of the fluctuation states is not claimed. |
| 4. Reading, technical and lay wording | Reading: "they arise here as ...", and (N+) scoped. Technical: "on the generators (N+) covers, the filled sea carries bosons, its chiral density waves, one band at a time; this is not a construction of the photon or other gauge bosons". Lay: "once the band of levels along the line is taken to be infinite", plus "These ripples are not the photon or the other force carriers." |
| 5. (vii) hypothesis | Formal: "For a state omega of the block's even algebra A_e (for instance the product state of (iv)), with omega^{tensor N} the product state on the even algebras of N blocks". Last sentence: "For a gauge-invariant product state, where omega(b) = 0, the hopping mode is F_N(b) = B". Proof: one sentence on why the product of even states is a state, and why a non-even block state need not give one. |
| 6. "Pure" in (vi) | "Pure" dropped. Added the GNS line: norm^2 of w_k Omega = omega_0(v_k w_k) = 0 for k >= 0, and norm^2 of v_k Omega = omega_0(w_k v_k) = 0 for k < 0. |
| 6'. Self-adjoint pairs (coordinator item 6) | Added to formal (vii), technical and proof: for a real state the form vanishes on pairs of self-adjoint even elements. So the canonical pairs are (a, a*) and no unit is needed. A Weyl form with self-adjoint fields would need a central unit, which A_e lacks: its centre is span{1, pseudoscalar}, and the pseudoscalar squares to +1. The proof gives the two-line argument. The check now verifies the vanishing for three real product states, sigma(b, b*) = p1 - p2, pseudoscalar^2 = +1, and centre = span{1, e1f1e2f2}. |
| 7. One-liner | Changed to "density forms vanish in product states with balanced edges" and "canonical bosons on the finite excitations of the infinite band". |
| 8. Minor | (v) filled sea is now "(M even, the lowest M/2 modes filled)". Check docstring (4) count changed from 25 to 26. |
| Literature | Cushen-Hudson and Holstein-Primakoff are now marked as verified (the referee verified them). Holstein-Primakoff is no longer "from memory". The volume and pages of Goderis-Verbeure-Vets and Goderis-Vets are flagged as not independently verified. |

runcheck: all 9 check functions PASS (`python3 colony/runcheck.py .../check.py`).
check4: pending (orchestrator). validate_draft: pending (orchestrator).
