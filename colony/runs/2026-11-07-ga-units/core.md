# Core results for the unit principle (maintainer pass 2026-11-07)

Neither result was already in the store. I searched with search_claims (8 queries) and find_text (I_5, I_7, e_2 e_3, span{1, J}). The nearest entities each state only part of a result:
- std-algebra.complexification@2 and odd-extensions.doubling-or-complexification@5 state Cl(V) (x) C abstractly, with a bare i. Doubling-or-complexification complexifies the even subalgebra Cl^0, not Cl(V).
- odd-extensions.mirror-inside-complexified-extension-absent-doubled@4 uses the central omega of Cl(2,3) but does not state the complexification of Cl(1,3) or the relation to I_4.
- singularity.euclidean-rotor-where-it-lies@4 (clause 3 and its note) names e_2 e_3 = I_4 sigma only as the angular rotation plane, never as a scalar of the atom.
- synthesis.phase-flow-is-time-rotor-flow-kms-continuation@2 (v) states the continuation and KMS with a bare i.

Both new entities are proved claims filed directly in store/claims/ (version 1, review: draft, session maintainer-2026-11-07). Each has entity.md, proof-main.tex, check.py and coverage.yaml, and no bare i, \mathbb{C} or sqrt(-1) in any of its four levels or its proof. Both the galang scan and the sweep's bare_i detector report none.

## 1. std-algebra.complexification-is-the-odd-extension
programme standard, subject standard-algebra.
Uses: odd-extensions.volume-element-odd-dimension@3, primer.centre@2, odd-extensions.doubling-or-complexification@5, std-algebra.complexification@2. It holds given no postulate.

Statement: for V of even dimension n, adjoin e orthogonal to V with Q(e) = -I_V^2. Then:
- I_W = I_V e is central with square -1, and the centre is span{1, I_W}.
- Cl(V + Re) = Cl(V) + Cl(V) I_W is the complexification of Cl(V) with unit I_W.
- (a + I_W b)^2 = Q(a) - Q(b) + 2<a,b> I_W.
- Through P_+- = (1 +- e)/2, I_W acts as the right unit +-x I_V.

Instances: I_5 = I_4 e in Cl(2,3), and I_7 = I_6 e in Cl(3,4).

Exact signs:
- **Q(e) = -I_V^2 is forced.** The other sign gives I_W^2 = +1, which is the doubling case. For both Cl(1,3) and Cl(2,4), I_V^2 = -1, so Q(e) = +1. The extensions are Cl(2,3) and Cl(3,4), and each has one more positive square.
- **Complex vectors.** (a + I_W b)^2 = Q(a) - Q(b) + 2<a,b> I_W.
  - e_2 + I_5 e_3 is null.
  - (y + eps I_5 e_0)^2 = Q(y) - eps^2 + 2 eps y_0 I_5, with y_0 = <y, e_0>. This is a number of the field span{1, I_5}.
  - Contrast: (e_2 + I_4 e_3)^2 = -2 + 2 e_0 e_1. Left I_4 does not complexify vectors.
- **Relation to the old unit.** For x in Cl(V), (x P_+-) I_W = +-(x I_V) P_+-.
  - On even x this is +-(I_V x) P_+-.
  - On a vector x it is -+(I_V x) P_+-.

  So through P_+, I_5 is the right unit x I_4, which is I_4 on even values, and I_7 is right multiplication by I_6. Through P_- both signs flip. The relation is fixed only by the choice of idempotent, so I_5 is never identified with I_4, nor I_7 with I_6.

## 2. synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom
subject descent.
Uses: singularity.modular-structure-completed-pair@5, singularity.pseudo-inverse-identities-hyperbolic-atom@4, std-algebra.bivector-exponential@2, tower.structure-tower-c-norms@8, singularity.kms-uniqueness-factor@5. It holds given no postulate.

Statement: for the completed pair v = (e_0 + e_1)/2, v* = (e_0 - e_1)/2, with sigma = e_0 e_1, the transverse bivector J = e_2 e_3 is the complex unit of the atom.
- J^2 = -1, J sigma = +I_4, and J* = -J under the frame star x* = e_0 rev(x) e_0.
- J commutes with the atom, and A = Cl(1,1) + Cl(1,1) J is the one-mode CAR algebra over span{1, J}.
- Ad(e^{J t sigma/2}) sends v -> e^{-Jt} v and v* -> e^{+Jt} v*.
- The rotor flow is the phase flow at t = -J lambda.
- The Gibbs state is KMS for tau_{J beta} = Ad(e^{-beta K}).
- Left I_4 is not a scalar of the atom: (I_4 v)(I_4 w) = +vw.

Exact signs (K = sigma/2, P_+ = v* v, P_- = v v*):
- **The unit.** J sigma = sigma J = +I_4, so J = I_4 sigma. J commutes with e_0, e_1, v, v* and sigma, and J* = -J.
- **The generator is I_4 / 2.** J K = I_4 / 2 and (2JK)^2 = -1. So e^{JtK} = cos(t/2) + I_4 sin(t/2): the phase flow is conjugation by e^{I_4 t/2}. This is not a rotor, and it maps no nonzero vector to a vector.
- **Phase flow.** tau_t = Ad(e^{JtK}) gives tau_t(v) = e^{-Jt} v and tau_t(v*) = e^{+Jt} v*. Infinitesimally, [JK, v] = -Jv and [JK, v*] = +Jv*. It is a group of *-automorphisms, since (e^{JtK})* = e^{-JtK}.
- **Continuation.** For z in span{1, J}, tau_z(v) = e^{-Jz} v. At z = -J lambda, e^{JzK} = e^{lambda K} = R_lambda, so v -> e^{-lambda} v and v* -> e^{+lambda} v*. Hence lambda = J t: the source's "lambda = it" with i read as J.
- **KMS.** Trace T(x) = 2<x>_0 - 2J<Jx>_0, state omega_beta = T(e^{-beta K} .)/T(e^{-beta K}).
  - omega_beta(x tau_{J beta}(y)) = omega_beta(y x), with tau_{J beta} = Ad(e^{-beta K}). It fails for Ad(e^{+beta K}).
  - omega_beta(v* v) = 1/(1 + e^beta).
  - omega_beta is faithful, and it is the unique KMS state (the KMS densities form the J-line of rho).
- **Modular flow.** Ad(rho^{Jt}) = tau_{-beta t}, so v -> e^{+J beta t} v.
- **The two units.** I_4 anticommutes with e_0, e_1, v, v*. (I_4 a)(I_4 b) = +ab, while (J a)(J b) = -ab. I_4 P_+- = +-J P_+-: I_4 equals J on the image of v* v and -J on that of v v*. They are never identified.

## Gates
- `colony/runcheck.py`: 4/4 functions pass for the first entity and 5/5 for the second. Each premise is touched by a premise() call.
- `colony/check4.py`, run on copies in proposals/<id>: 0 errors and 0 other findings for both entities. The copies are deleted, and proposals/ did not exist before.
  - The first run of entity 1 gave W413 (5 of 8 perturbations survived in check_complex_vectors_and_shifted_squares). I fixed it by pinning every sample to its hand-computed square: (6, 2), (-443/36, 2/3), (0, 0), (-190/9, 2), (-3299/196, -2/7).
- `tp check --layers 1,2,3 --keep-going --author leon`: 0 errors and 0 warnings store-wide, with no finding on either id.
  - An earlier run gave I213 on entity 2 with subject thermality: all 5 of its logical neighbours are in descent. I changed the subject to descent, which covers modular theory and KMS states.
- `tests/test_mcp.py -k conventions` passes after the conventions edit.

## Conventions
In store/conventions.md, under "The imaginary units", I replaced the "No bare imaginary unit where a pseudoscalar does the work" bullet with one bullet, "The unit principle". It states U1 to U6 as in RESOLVE.md:
- U2 cites the second id and carries its signs.
- U3 cites the first id, with I_5 and I_7 and the sign through (1 +- e)/2.
- It keeps the old bullet's plane-phase rule e^{B theta} and the imaginary-rapidity rule I_4 B under U1.
- It ends with the rule never to identify I_4, I_5, I_6, I_7 or J, and with the E609/W222 sentence.

I also changed the bullet just before it. It said V_C, Cl(p,q)_C and the Dirac module "keep their plain complexification"; it now says they are complexified by I_5 or I_7 (U3). U3 contradicts the old wording, and RESOLVE.md supersedes the conventions' "what stays" list.

## What differed from RESOLVE.md
1. **Subject.** The second entity's subject is descent, not thermality (the I213 finding above).
2. **Citations for entity 2.** It does not cite synthesis.wedge-reflections-compose-to-the-two-pi-rotor-... (the stored I_4 B = J) or synthesis.phase-flow-is-time-rotor-flow-kms-continuation. The first holds given six postulates and the second three (c1, c2, R), which would have broken "holds given no postulate". So J sigma = +I_4 is proved directly, and KMS is proved directly from the trace, with singularity.kms-uniqueness-factor for uniqueness. The frame star comes from tower.structure-tower-c-norms.
3. **J K = I_4 / 2.** This was not anticipated in RESOLVE. The source's i sigma, with i read as J, is I_4. The note on euclidean-rotor-where-it-lies reads i as I_4 on values, which gives i sigma = J. Both identities hold (I_4 sigma = J and J sigma = I_4). Sweepers must keep track of which unit an entity's i was read as: on this atom it is J, and the generator is then I_4 / 2.
4. **I_5 against I_4.** I_5 is related to I_4 only through x -> x(1 +- e)/2, with a sign, and it is the RIGHT unit. Left I_4 on a vector has the opposite sign. For scalar computations (the field span{1, I_5}) no relation is needed.
5. **The shift clause** is stated for functions of the square of the shifted vector: polynomials, quotients and power series over span{1, I_W}.
6. **Not changed, for Leon.**
   - The section's opening ("Two units, deliberately distinct") now undercounts the units.
   - Known limit 1 (I_4 anticommutes with the atom's modes) is now answered by U2 and could cite the second id.
   - Known limit 2 still says the boundary-mode algebra is "defined over C".
   - Known limit 4 still writes lambda = it and e^{-i omega t}. On the atom these are lambda = Jt and e^{-J omega t}.

   The sweep will touch the entities behind these limits, so I left the text for Leon to rule on.
7. **Literature.** Both extraction notes flag literature cited from memory, as orientation only: Porteous 1995 and Lounesto 2001 for the first entity, and Takesaki 2003 for the modular group of a matrix factor in the second. Neither result uses them as a premise.

## Fixes after review (referee-core.md, both SOUND WITH FIXES)
Every fix is folded into version 1 and recorded in each entity's extraction.maintainer_pass_ga_units note. Both ids are unchanged. No specialises or supports links were added (Leon's decision).

std-algebra.complexification-is-the-odd-extension:
- **Duplicate named.** extraction.note now says the spacetime instance of (ii) is already stored as odd-extensions.four-extensions-oriented-pair (row this world + time) and odd-extensions.mirror-inside-complexified-extension-absent-doubled (iii). This entity is the general even-dimensional form, and adds (iii), (iv), the conformal instance and (vi).
- **Formal (ii) wording.** The splitting Cl(W) = Cl(V) + Cl(V) I_W is now said to hold "as real vector spaces, with Cl(V) a real subalgebra commuting with I_W".
- **New clause (vi), odd dimension.** For odd dim V, complexify through V' = V + Rf. The multiplication map Cl(V) (x) span{1, I_W'} -> Cl(W') is an injective homomorphism, so the complexification is the subalgebra Cl(V) + Cl(V) I_W'. This is the step rule2 uses. The proof is added, and the check now covers Cl(1,2) in Cl(2,3) (all 16 x 16 basis pairs, rank 16).

synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom:
- **J is a choice, now stated in (i).** The centraliser of e_0, e_1 in Cl(1,3) is the quaternion algebra span{1, J, e_0e_1e_2, e_0e_1e_3}.
  - +-J are its only units of square -1 in the even subalgebra, which is the same as being fixed by the transverse rotations.
  - The sign of J is fixed by J sigma = +I_4.
  - Odd units such as sigma e_2 (u^2 = -1, u* = -u, anticommuting with J) also commute with the atom and are not identified with J.
- **Wording across the levels.**
  - Title: "The transverse bivector is the even complex unit of the radial atom". The id is kept.
  - Lay: "the only one built from the even part of the algebra".
  - Technical and one-liner now say "even".
- **(iv)** names the source's phase flow: T05 Thm 7.16 and T07 Def 2.7, and the flow of singularity.kms-uniqueness-factor. The sign agrees: v -> e^{-Jt} v.
- **(v)** adds one sentence: the continued boost on the modes, e^{theta I_4/2}, and the dual-plane rotor on values, e^{theta J/2}, are different objects. The rotor is central in A and acts trivially on it.
- **(vi)** now says "the only span{1, J}-linear state" and "for beta != 0, not at -beta". The proof shows why field-linearity is needed: the real parts of (1 + bJ) omega_beta are KMS for every b. In the proof and the check, e^beta is renamed q.
- **extraction.note.**
  - The ledger label is now transport-absent.
  - It records that (iv) to (vi) restate singularity.euclidean-rotor-where-it-lies (1)-(2), singularity.kms-uniqueness-factor, singularity.two-kms-functionals-sign (1) and synthesis.phase-flow-is-time-rotor-flow-kms-continuation (v) with J. The new content is (i) to (iii), JK = I_4/2, and that the unit lies in Cl(1,3).
- **Premises.** primer.centre@2 is added to uses and is touched by the check.
- **Check.** It now computes the centraliser (dimension 4 and its blades), and tests tau_z at a mixed z = t + J theta: tau_z(v) = e^theta e^{-Jt} v and tau_z(v*) = e^-theta e^{Jt} v*.

No sign changed. The conventions bullet U2 gains one parenthesis: J is the even unit of the atom's quaternionic centraliser, and odd units such as sigma e_2 are not identified with it.

Gates after the fixes:
- runcheck: 4/4 and 5/5 pass.
- check4 on proposals/ copies: 0 errors and 0 other findings for both. The copies are deleted.
- tp check layers 1,2,3, filtered to the two ids: no finding on either. Store-wide it currently reports 171 errors and 2 warnings, all on entities the sweep agents are editing.
- No bare unit in any level or proof of either entity.

Decisions for Leon, from the review:
1. **Two units for the atom's phase flow.** The store now gives it two units: J here (U2), and the odd-extension unit hat I = I_V e in synthesis.phase-flow-is-time-rotor-flow-kms-continuation (v) (U3, which for the atom window with e = e_2 is sigma e_2). They anticommute in Cl(1,3) and agree as abstract flows. One of the two entities should state how they relate.
2. **Citations without uses.** rule2.odd-lorentzian-dimension-exactly-one-real and synthesis.phase-flow-is-time-rotor-flow-kms-continuation \claimref the first id without it in their uses.
3. **Links.** Whether to add pinned specialises or supports links from the stored instances to the two core results.
