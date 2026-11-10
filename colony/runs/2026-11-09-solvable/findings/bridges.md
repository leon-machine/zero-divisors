# Bridges, run 2026-11-09-solvable

Read: every findings/attack-*.md as of 14:42 (C1B, C2B, C3A, C3B done; C1A, C2A, C4A, C4B in progress), the
entity.md of the six proposals in proposals/ (not their checks), and the one-liners of C4A's three drafts in
work/C4A/ (to check overlap). Every link below was tested by direct store lookups (get_claim, cone, find_text,
search_claims); nothing was derived at length. Labels: "stored" = what the store says at the version read;
"argued" = my reading, for the attacker to test.

## Links sent

### L1. J3 and the helicity lift answer part of "which fields form the sea" (to C3A, C3B; cc C1A)
Entities: hawking.joint-j3-s-wave-reduction (postulate v1) and hawking.helicity-lift-joints-itemised (proved v5),
against synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays and
synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content; with
synthesis.array-ln2-is-zero-mode-doublet-one-tower (proved v5) clause (iv).
Why. Stored: J3 lies in the past cone of synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4, which C3A's
clause (ii) uses, and neither C3 proposal cites it. J3 says the current boson of the s-wave theory (the bosonised
current of (Q)'s arrays, hawking.imported-s-wave-bosonic-sector v6) is the reduction of each four-dimensional massless
field. The helicity lift explicitly includes the photon (s = 1) and the graviton (s = 2) through J1. array-ln2 (iv):
one array's current sector is one oscillator tower, so one array registers at most one helicity channel. So the store
already has a reading in which integer-weight fields are neither outside the sea nor extra arrays. They are the arrays'
current bosons. Consequences to test. (a) C3A: K3 ("killed if the store places integer-weight fields in (Q)'s arrays")
needs re-examining against J3. The bosonisation reading supports counting c = number of arrays with no double count,
but the proposal should cite J3 and say that its scope (CAR arrays only) follows J3's reading, not a separate choice.
(b) C3B: under J3 the additive table c = 16 n_g + 2 n_V + n_s + 2 eps double counts. If the bosons are counted
separately, eps = 1 is the store's helicity-lift reading (the graviton's homogeneities -6, +2 are in J1). That
contradicts the findings' "eps = 0 is the store's own reading". (c) Argued: if every massless helicity channel on a
light ray must be registered by its own array (J3 read per light ray, plus (iv)), then 2 n_V + n_s + 2 eps <= 16 n_g.
On the store's content (12 vectors, the 8 real components of the linear rung field, graviton) that is 34 <= 16 n_g,
so n_g >= 3. This lower bound does not depend on the recurrence choice. The stored tension is
synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (helicity-one pair currents are not exact
bosons), so the two stored readings need reconciling before anything is filed. (d) C1A: a J3 proof at the horizon
becomes the premise for C3's sea question. State it per boost-weight-zero channel (C1B's Teukolsky remark) and say
whether it reaches s = 2.

### L2. Premise U is a non-periodic selector for residues 1 and 7 (to C4A; cc C1A, C1B)
Entities: dark-tower-matter.u-transposition-rule (postulate v2, clause U3) and dark-tower-matter.pairs (proved v3),
against C4A's draft synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free. Context:
synthesis.gauge-algebra-by-tower and dark-tower-matter.constituents-field.
Why. Stored: gauge-algebra-by-tower takes b = complex Witt index floor((n+2)/2) of the conformal space, notes that the
real Witt index is 2 in every causal tower, and builds the extra pairs with a unit u taken from the constituents'
field F. U3: every complex unit used to build a ladder pair lies in F, and no external unit is adjoined. The
constituents' field is per residue: R for residues 1 and 7, H for 3 and 5. Argued: at (10,1), the conformal space
(11,2) has b = 6 and real Witt index 2. Four pairs need a unit, and F = R supplies none, so U cannot be met on the
literal tower. At (2,1), b = 2 = real Witt index and no unit is needed. At (12,1), F = H supplies u. So U selects the
lowest member for residues {1,7} and not for {3,5}. U is not in the cone union C4A used (checked: absent from the
cones of lowest-causal-residues-zero-four-content, towers-are-residues and oriented-causal-towers), while H1 and pairs
are. The draft says H1 and the constituent definitions are "transported through (i)". That move must be justified,
because applying the stored definitions to the factor A rather than to Cl(beta sigma) is what keeps U true. If it
cannot be justified, this is a partial derivation of the window for {1,7}. For C1: op.odd-towers item 1 (answered in
store at dimensions 3 and 5) is conditional on P3's lowest-causal clause. The field type survives the shift; the
ladder-pair construction does not, for F = R.

### L3. C4's independence method closes C3A's "new choice" verdict (to C3A; cc C4A, C4B)
Entities: synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free (proved
v2), against synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays.
Why. C3A shows that (Q), KMS and the window reading hold for every n, and greps the 196-entity cone. In C4's form, an
independence proof needs two models of the full premise set. The stored generation-free result supplies the content
side. Checked: its 173-entity cone contains none of (Q), (N+), the window reading or the null ordering, so models with
n_g = 1 (where U differs from Gamma) and n_g = 3 (where U = Gamma) exist, provided no light-ray premise constrains
n_g. C3A's grep is the evidence for that proviso. C3A names this result in its text but not in `uses`; adding it, and
listing the joint cone the way C4A's coneunion.py does, turns "argued: a choice" into the two-model proof. The
symmetry form also applies: central rephasing of the implementer fixes every automorphism-level premise and KMS, and
only the window reading pins the phase.

### L4. The Sugawara central values and the c = 0 mod 24 test (to C2A, C3A, C3B)
Entities: synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split and
synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy, against both C3 proposals.
Why. The C3 proposals call the array count the "central charge". On finite windows there is no Virasoro algebra (C2B's
A1 trace argument: [L_1, L_-1] = 2 L_0 needs tr L_0 = 0). C3A's proof uses only H, so it stands, but the word
"central charge" is earned only through C2A's band-domain result: the free bilinear L_n at c = 16 per generation
(C2A's kill condition K-a). C3 should scope the wording. For C2A, a cheap consistency clause: the vacuum constants
-c_f/24 of the split sum to -16/24 per generation, which is the window-reading constant of C3A's clause (ii). Stored:
H = H_so(10) + H_N exactly, so c = 15 + 1. Argued: posing the recurrence on the gauge-charged Sugawara part alone gives
15 n_g = 0 mod 24, so 8 | n_g, the same verdict as dropping nu_R. The 3 | n_g verdict therefore needs the
number-current sector. No single factor (32/7, 2, 1, 1, 52/7) passes on its own (C3A).

### L5. The stored quartet result makes the light-ray count independent of the breaking pattern (to C3B, C2B; cc C2A)
Entity: synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta
(proved v4: 27 physical polarisations per momentum for the two-doublet breaking), against C3B's proposal.
Why. C3B's statement "under Higgs breaking the null-data count is unchanged" is labelled argued. The stored quartet
count gives it: 27 + 5 remaining scalars = 32 = 24 + 8. C2B's charge-breaking counter-model (Goldstone rank 4) gives
16 + 12 + 4 = 32 as well. So the test cannot see the vacuum, which agrees with C2B's B2 conclusion that the BRST
complex does not select the breaking pattern. C3B should cite the quartet result. C2B can note that the light-ray count
is a second structure that is blind to the vacuum.

### L6. The two-array unit and J3's helicity channels (to C4A; cc C1A)
Entities: synthesis.array-ln2-is-zero-mode-doublet-one-tower (iv) and
synthesis.capacity-per-mode-independent-of-helicity (iii), against C4A's draft
synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping.
Why. Stored: capacity-per-mode rests on J3, so J3 is in the draft's cone, and its clause (iii) says J3 decides "one or
two helicity channels per (omega, l, m)". The draft's "no premise fixes the grouping" must therefore say why J3 (a
stored postulate) does not fix it. Argued: J3 with (iv) fixes the map from arrays to channels (one array per helicity
channel of one Weyl field's partial wave), not how channels group into units. A two-array unit would be a pair of Weyl
fields of opposite chirality, which J3 does not select. A pairing of the 16 into 8 needs the neutral singlet (15 is
odd), which links to C3A's question (5). If C1A proves J3, the draft's conclusion should still hold, but the sentence
is needed.

## Candidates rejected
- Adams' theorem on RP^n against the store's k: C1A and C1B independently showed ht = e = n + 1 there. This is
  intra-cluster and settled.
- C1B's spin-1/2 horizon rate exp(kappa r_*) against C3's half offset: different quantities. The sqrt(f) comes from
  the dW/dr_* term of a first-order operator. Vectors (integer helicity) still decay like f. The (Q) offset is the
  KMS antiperiodicity of Killing weights, not a near-horizon fall-off.
- Wall rungs (C1) against Higgs rungs (C3B's n_h, C4B's rung unit): both are adjoined hyperbolic planes, but no
  stored edge links them. The Standard Model's two rungs come from the chirality-preserving U(2)
  (rungs.two-twistor-bivector-null-invites-one), and a wall's k is a bundle count on Sigma. The chain "k fixes n_h"
  has no support.
- C1B's KO-theoretic conjecture against C4A's Bott shift: the only shared element is a classical theorem.
- 24 = 8 x 3 against the mod-8 tower clock: numerology.
- Koide (C2B) against the Georgi-Jarlskog weight (C4B). The GJ map from leptons to down quarks, D = (3, 1/3, 1), is a
  dressing in the class D1 > D3 > D2 with D3/D2 = 3, above C2B's thresholds (2.19 own scale, 2.63 at M_Z). That is
  consistent but circular: the leptons are Koide by data, so asking that the undressed down bracket be Koide
  reproduces m_s/m_mu. There is no constraint on the free weight.
- Sakharov's three against the recurrence's 3 | n_g: intra-C3, and both attackers already have it.
- C2A's sign-bit route (op.hypothesis-s) against C4A's Cl(8,0) split: no shared premise.
- C1B's per-area channel count (R4) against C3's sea: the C3 count is per light ray, with transverse labels in K.
  It is argued only; at most a footnote to L1.
