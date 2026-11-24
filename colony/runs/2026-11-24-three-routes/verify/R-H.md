# Referee R-H, run 2026-11-24-three-routes

Proposals refereed:
1. `synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall`
2. `synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none`

Scratch: `colony/runs/2026-11-24-three-routes/verify/work-R-H/` (exploration and perturbed checks only).

---

## 1. synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall

**Verdict: SOUND WITH FIXES.** Every number and identity I recomputed by my own route agrees, including the
sign of the Euler term, which I confirmed against a published source. The conditional structure is stated:
(A) and (E) are named in the one-liner, every clause that needs them says so, and nothing claims a stored
result is contradicted. Fixes concern the lay level (the "ends before the wall" conclusion is the b = 0
branch only), crediting standard results in the formal text, identifying C with the thermal density in (vi),
and import housekeeping.

### Sign and normalisation of the anomaly (settled first)

Independent routes:

- **Published value (web, checked).** Mottola and Vaulin, arXiv:gr-qc/0604051, Eq. (3.4) and (3.6b):
  `<T_a^a> = b F + b'(E - (2/3) box R) + ...`, `b' = -(N_S + 11 N_F + 62 N_V)/(360 (4 pi)^2)`, with N_F counting
  Dirac fermions, signature (-,+,+,+) (line element -dt^2 + dx^2). Their Eq. (4.12): in de Sitter,
  `T_ab = 6 b' H^4 g_ab = -(H^4/(960 pi^2)) g_ab (N_S + 11 N_F + 62 N_V)`. In (-,+,+,+) a vacuum stress is
  `T_ab = -rho g_ab`, so rho = +N H^4/(960 pi^2) > 0, and the mostly-plus trace is -rho + 3P = b' E, i.e.
  **rho - 3P = |b'| E = +alpha E** with alpha = (sum of weights)/(360 (4 pi)^2) = (...)/(5760 pi^2). This is
  exactly the proposal's sign and normalisation; the -2/3 box R piece is absorbed in the free b. The
  proposal's remembered anchor (conformal scalar on de Sitter, rho = H^4/(960 pi^2)) is right.
- **From memory (flagged).** Duff's "a" coefficient a = (n_s + 11 n_D + 62 n_v)/360 is positive (a-theorem
  sign); Starobinsky's self-consistent de Sitter solution H^2 = 360 pi/(G N) exists only with rho > 0 on de
  Sitter. From (v) with C = 0: H^2 = Mbar^2/(2 alpha) = 5760 pi^2/(2 N 8 pi G) = 360 pi/(G N). Consistent.
- **From the store.** The stored a_4 (Fact `synthesis.imported-heat-kernel-coefficients-and-background-field-gauge`
  @2 (i)) has the Euler term with coefficient -a (a > 0) for every spin; the trace is minus the a_4 density
  in the B&D-type convention, giving +a E. The store fixes the magnitude and the relative signs of the three
  spins; the overall sign of the trace relative to a_4 is not in the store and is genuinely an input of (A).
  The proof says so. Recommend citing the source above (or Duff 1994) in place of "from memory".

Recomputed by hand (independently of check.py):

| quantity | my route | result |
|---|---|---|
| scalar, xi = 1/6 | 5R^2-2Ric^2+2Riem^2 + 60R(-R/6) + 180 R^2/36 = (2,-2,0) | 3W^2 - E: Euler weight 1 |
| Dirac (4-comp., sigma = -1) | 4(5,-2,2) + 60R(-R/4)4 + 180(R^2/16)4 + 30(-Riem^2/2) = (-7,-8,5), times -1 | (7,8,-5) = 18W^2 - 11E: 11/2 per Weyl field |
| vector + 2 ghosts | 4(2,-2,5) + 60R(-R) + 180 Ric^2 + 30(-Riem^2) = (-22,172,-40); minus 2(2,-2,5) | (-26,176,-50) = 36W^2 - 62E |
| content | 48(11/2) + 12(62) = 264 + 744 | 1008 = 28 x 36; +8 = 1016 |
| alpha | 1016/5760 pi^2 | 127/(720 pi^2); 1008: 7/(40 pi^2) |
| Euler density RW | E = Riem^2 - 4Ric^2 + R^2 with A = addot/a on 3 planes, B = H^2 on 3 | 24 A B = 24 H^2 addot/a |
| radiation a = t^(1/2) | A = -1/(4t^2), B = 1/(4t^2) | E = -3/(2t^4); Ric^2 = 9/16+3/16 = 3/4 t^-4; E = -2Ric^2 |
| rho_A | d/dt(a^4 rho) = a^4 H alpha E, rho = 6 alpha H^4 solves it | rho_A = (3/8) alpha t^-4 |
| P_A | (rho - alpha E)/3 = (3/8 + 3/2)alpha/3 | (5/8) alpha t^-4 |
| rho_b on t^p | H Rdot - R^2/12 + H^2 R = p^2(2p-1)(-12 - 3(2p-1) + 6p) | -9 b p^2 (2p-1) t^-4 |
| t^-4 balance | 6 alpha p^4 - 9 b p^2(2p-1) = 3p^2(2 alpha p^2 - 3b(2p-1)) | 2 alpha p^2 = 3b(2p-1): confirmed |
| Hdot on branch | differentiate 3Mbar^2 H^2 (1-x) = C/a^4 | 6 Mbar^2 H Hdot (1-2x) = -4HC/a^4: confirmed |
| T_max^4 | 90 x 720/(8 x 127 x 116) | 2025/3683 = 0.5498; T_max = 0.8611 Mbar = 2.097e18 GeV |
| t_eq/t_P | sqrt(16 pi alpha) = sqrt(127/(45 pi)) | 0.9478 |
| share at 6e14 GeV | r = (T/T_max)^4 = 6.70e-15, x = (1 - sqrt(1-r))/2 | 1.665e-15 (< 1.7e-15) |

All weights (1, 11/2, 62), totals 1008/1016, alpha = 127/(720 pi^2), the stress components 3 alpha/(8 t^4) and
5 alpha/(8 t^4), and the Euler density -3/(2 t^4) are right. The Weyl weights 3, 9, 36 (c coefficients
1/120, 6/120 per Dirac, 12/120) and the Boyle-Turok cancellation weights (-28, -8) also agree with my memory
of the published values.

### Statement and proof

- (A) and (E) are named in the one-liner ("Given the trace anomaly (A) ... and the expected stress as the
  source (E)"); the title names the anomaly but not (E). The brief's rule (title or one-liner) is met.
- "No exact radiation field" is stated only given (A) and (E): clause (iv) is headed "proved given (A) and
  (E)", and the trace equation R = 8 pi G(alpha E + b box R) with left side 0 and right side
  -12 pi G alpha t^-4 is correct (3/2 x 8 = 12).
- Power-law clause holds; the reason the t^-4 order must vanish (3 Mbar^2 H^2 is O(t^-2), C/a^4 is
  O(t^-4p), p < 1) is right. Minor: "b outside [0, 2 alpha/3)" gives at b = 2 alpha/3 the double root p = 1,
  which the clause excludes (p != 0, 1); harmless, but say "b < 0 or b > 2 alpha/3".
- Smoothness values p = n/(n+1), b = 2 alpha n^2/(3(n^2 - 1)): recomputed, correct.
- (v) bounded branch: correct and standard (Fischetti, Hartle and Hu 1979; Anderson 1983, from memory).
  The end point is a finite-H, unbounded-Hdot (Ricci) singularity at positive a, as stated.
- Stored window: the anomalous share is computed from the stored reduced Planck mass (read via
  `quantity`) and the ceiling 6e14 GeV, transcribed from the prose of
  `dark-matter.ceiling-valued-inherited-success`@5 (hard-coded in check.py, since the stored result is prose).
  Two qualifications not in the text: that ceiling is the rung scale M_R (a mass), conditional on Hypothesis
  (U) of that result, and the proposal reads it as a radiation temperature; and C/a^4 is identified with the
  thermal density (pi^2/30) g T^4.
- No sentence claims a stored result is contradicted. The Reading says the radiation-type descent (a stated
  hypothesis of the deposit results) "cannot hold exactly" together with a Hadamard state and (E), and
  that the collar uses of the deposit results "stand". Correctly worded as qualifying a hypothesis.
- Over the levels: the **lay** text says "the radiation-filled universe cannot be traced back to the wall
  with these equations: it ends earlier, at a temperature just under the Planck scale". The ending at
  T_max is the b = 0 branch only; with b != 0 the field has power-law origins with p != 1/2. The technical
  level states this correctly.

### Check

`runcheck` 5/5 PASS. Perturbations (all in scratch, each made the targeted function fail, others pass):
ghost count 2 -> 1 (weights fail); spinor connection trace -1/2 -> -1/4 (weights fail); ceiling 6e14 ->
6e15 GeV (numbers fail); rho_A coefficient 3/8 -> 3/7 (stress fails). The check tests the algebra as stated;
it does not (cannot) test the overall sign of the trace relative to a_4, which is an input (stated in
coverage.yaml). check4 log (read after it appeared): 0 errors, 0 other findings, check result pass, no W413.

### Fixes

1. Lay: replace "it ends earlier, at a temperature just under the Planck scale" by "with the one free
   coefficient set to zero it ends earlier, at a temperature just under the Planck scale; with it nonzero
   it starts from an origin of a different kind, which is not the tame wall". Also add to the lay text that
   the result assumes the averaged quantum stress is what curves spacetime (E).
2. Formal (v): credit the bounded branch and the C = 0 de Sitter roots as standard ("the branch of
   Fischetti, Hartle and Hu and of Anderson; the de Sitter root is Starobinsky's"), cited from memory, so
   the clause is not read as new.
3. Formal (vi): state the identification "C/a^4 = (pi^2/30) g T^4, the thermal density of the content" and
   that 6e14 GeV is the upper end of the stored rung-scale range (a mass, conditional on (U) of the cited
   result) used as a temperature.
4. Formal (iv): "b outside [0, 2 alpha/3)" -> "b < 0 or b > 2 alpha/3".
5. Formal (i): define "the square of the field strength" (4 Tr(R^2) over bivectors, = Riem^2) where E is
   introduced; the proof uses it but the statement only names it.
6. Provenance of (A): replace "cited from memory" for the sign anchor by Mottola and Vaulin,
   arXiv:gr-qc/0604051, Eqs. (3.6b), (4.12) (checked by this referee on the arXiv text), or import (A) as a
   Fact with that locator; until then the derivation's "holds given" will not show (A) and (E), which are
   internal hypotheses. The maintainer should decide between importing (A) and keeping it named.
7. Housekeeping: `credit.source: run 2026-11-24-three-routes` names a run; normalise as for other entries.

---

## 2. synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none

**Verdict: SOUND WITH FIXES.** The core is right and I confirmed it independently: the two reflections,
the disk of invariant states (so "selects none" is proved, a continuum exhibited), q = exp(-pi k^2/(m a')),
the energy-reversing reflection's Fock states at (1 -+ exp(-pi k^2/(2 m a')))/2, the floor
n0 = (1 - sqrt(1 - q))/2, and the elementary all-orders bound. Fixes: (a) the class of states must be
isotropic (or the conjugation taken in its sector-preserving sense) for the per-sector statements (ii),
(iv)(b), (vi) and (i)(c), because the antilinear theta pairs k with -k; (b) the one-liner must name the
class; (c) two "not Hadamard" statements for mu > 0 (tracial state, energy-reversing Fock states) are argued
and not proved; (d) the number density is per two helicities, not per sector; (e) lay level drops the
"given the adiabatic Fact" qualifier and states the equal-temperature Reading as fact; (f) prior art should
be credited in the formal text, with the locators I confirmed.

### Which conjugation

The proposal uses theta = cW (W: chi(eta, x) -> gamma0 chi(-eta, x) gamma0, c: right multiplication by
sigma_1, antilinear), acting as an automorphism, inducing O_A (reflection along sigma_3) on Bloch vectors;
equivalently W followed by the particle-hole exchange. W as a plain automorphism induces O_B (half turn
about sigma_3, energy reversing). The stored conjugation (`dark-matter.premise-cpt-covariance`@4,
C = Ad(I6) o kappa) is, by the premise's own text, point-fixing, antilinear and energy-reversing ("it fixes
... every translation, and it is antilinear, so ... it reverses their generator and with it the energy").
The proposal quotes this type correctly and does not use it. Its reason it cannot serve is right: it does
not exchange the two sides of the wall at all, so it is not a conjugation across the wall, and a
point-fixing map that intertwines h(eta) at every eta and reverses energy is O' = -1 on Bloch vectors,
whose only fixed vector is 0 (the tracial state). Caveat (fix a): an antilinear map that commutes with
translations sends momentum k to -k, so invariance relates v_{-k} to -v_k; "only the tracial state" holds
for isotropic states (v depending on |k| only). Without isotropy the invariant states include
"vacuum on one half-space of momenta, filled sea on the other", which is not Hadamard either, so the
conclusion "cannot serve for (HD)" stands. theta is, for homogeneous states, the CPT of Boyle, Finn and
Turok (their Eq. (3.48) pairs u0(p, h) with v0(-p, h)).

### "Selects none": proved, for which class

(ii) is proved: O v(-eta) and v(eta) solve the same linear equation, so invariance is O v(0) = v(0), giving
the disk v(0).sigma_3 = 0 (O_A) and the segment v(0) = t sigma_3 (O_B); with (v)(b) a continuum of
Hadamard invariant states t(k) e_chi(k) is exhibited (given the Fact). The class (gauge-invariant,
quasi-free, homogeneous, helicity-diagonal, charge-symmetric) is in the formal statement, not in the title
or one-liner. Non-uniqueness extends to any larger class, as the note says. But the per-sector floor and
the per-sector minimum are class-dependent: in the theta-sense with non-isotropic states, v_k(0) = s_out(0)
with v_{-k}(0) = s_in(0) is invariant and has occupation 0 at k (q at -k), below n0. What survives in
general is the pair bound n_k + n_{-k} = 1 - v_k.(s_in + s_out)/2 >= 1 - sqrt(1 - q) = 2 n0, with equality
only at m-hat (my derivation), so (vi)'s s0 still minimises the total number. Fix: add "isotropic"
(and equal in the helicities paired by c) to the class, or state (ii), (iv)(b) for the pair (k, -k).

### The exponents (independent derivation and numerics)

- Landau-Zener, from memory: for H = mu eta sigma_3 + k sigma_1 the diabatic energies differ by 2 mu eta,
  coupling k, so P = exp(-2 pi k^2/(2 mu)) = exp(-pi k^2/mu). q = (1 - s_in.s_out)/2 is the probability that
  the state adiabatic at -infinity is not adiabatic at +infinity: q = P. Agrees.
- O_B Fock states +-sigma_3 have occupation (1 -+ x)/2 over s_out with x = s_out(0).sigma_3, and q = x^2
  (proof (iv)(b), checked), so |x| = sqrt(q) = exp(-pi k^2/(2 mu)). The two exponents are consistent.
- Numerical integration (scipy DOP853, rtol 1e-12, from eta = 40 with the first-order adiabatic start,
  `work-R-H/lz.py`, exploration only), (k, mu) = (0.3,1), (0.6,1), (1,1), (1.3,1), (1,2.5), (2,1): q matches
  exp(-pi k^2/mu) to 7 digits (e.g. 4.321392e-02 vs 4.321392e-02 at k = mu = 1) and |x| matches
  exp(-pi k^2/(2 mu)) to 7 digits; the wall-instant vacuum's occupation over s_out tends to mu^2/(16 k^4)
  (4.35e-3 vs 3.91e-3 at k = 2, the difference being the next order).
- n0 = (1 - sqrt(1 - q))/2: from (iv)(b) geometry (max of v.s_out on the disk is sqrt(1 - q), at m-hat);
  4 n0 (1 - n0) = q. Agrees.
- Number density: I compute (1/(2 pi^2)) int x^2 (1 - sqrt(1 - e^{-x^2})) dx = 0.0127597, which is twice
  int x^2 n0 dx/(2 pi^2). So 0.012760 (mu/pi)^{3/2} is the density summed over the two helicities (as in
  Boyle-Finn-Turok Eq. (5.15), sum over h = 1, 2), not "per sector"; per sector it is 0.006380 (mu/pi)^{3/2}.
  (Proof only; fix d.)

### Other points

- (iv)(c) rests on Weber-function facts (asymptotic form, connection formula, Gamma reflection), labelled
  "(Classical; Weber functions, cited from memory.)" and declared `outside_ga: complex-analysis`. Correct
  labelling; the check's Weber function is bookkeeping only (exponent arithmetic), which coverage should say.
  Recommend citing DLMF section 12 with equation numbers, or importing.
- (iv)(a) elementary bound: checked step by step (residual omega delta^{N+1} P_N, rotation flow, integral
  of (1 + x^2)^{-N-1/2}); the O_A covariance d_n(c, -sigma) via uniqueness of the unit-norm formal solution
  is valid. So q = O((mu/k^2)^{2N}) for every N is proved without special functions. Sound.
- Sufficiency criterion (v)(a), the massive one: proved in the proof (dominated convergence with
  derivative bounds C_j (1 + k)^j on compact eta-sets; Cauchy-Schwarz for Fock states). It is relative to a
  reference state and sufficient only; it is stated as an implication, correctly. It cannot by itself give
  "not Hadamard", and two places use it as if it could (next item).
- Hadamard wording: s_out Hadamard rests on Fact
  `synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard`@3 (c), which is posed
  for homogeneous isotropic states, plus the identification of all-order agreement with the Fact's "adiabatic
  of infinite order", made as the stored massive result makes it. Formal (v)(b), technical and one-liner say
  "given the Fact"; the lay level says "is well behaved" without qualification. The floor state s0 follows
  from (v)(a) relative to s_out (Gaussian difference): proved given the Fact. "The tracial state is invariant
  and not Hadamard": proved for mu = 0 by the stored moment criterion; for mu > 0 the proof offers only
  |v - s_out| = 1, which is not a proof (no necessity criterion is stored for massive fields). A one-line
  proof is available: its two-point function is one half of the anticommutator distribution, whose wave
  front set contains both C+ and C-. The technical's "[the energy-reversing reflection] cannot give a
  Hadamard state" is likewise argued (occupation tending to 1/2), not proved.
- "(CW) neither implies (HD) nor is implied by it": proved given the Fact (wall-instant vacuum invariant
  and not Hadamard by stored clause (ii), which itself holds given the Fact; s_out Hadamard and not
  invariant for mu > 0).
- Prior art: credited in the technical level and extraction note; I confirmed on the arXiv text of
  arXiv:1803.08930 (Boyle, Finn and Turok, "The Big Bang, CPT, and neutrino dark matter"): the free function
  eta(p) of CPT-invariant vacua (Eq. (3.48)), occupation (1 - cos 2eta cos lambda)/2 (Eq. (3.49)), fixing by
  least particle number and energy, mass gamma tau (Eq. (5.9)), |beta| = exp(-pi p^2/(2 gamma)) (Eq. (5.13),
  derived via parabolic cylinder functions in their Appendix A), number density (gamma/pi)^{3/2} 0.01276
  summed over helicities (Eqs. (5.15), (5.16)). So (iv)(b) in its pure-state part, (iv)(c) and (vi) are
  theirs, as the note says. The PRL is, from my memory, arXiv:1803.08928 ("CPT-symmetric universe"); to be
  checked.
- Reading (cold mirror): argued and labelled; it records a tension, not a contradiction, and says why
  hypothesis (B) of `synthesis.cold-mirror-needs-non-equilibrium-descent`@3 fails or is untouched. Fine. The
  lay level states "The demand also makes the two sides equally hot" as fact.
- Title names (CW) and the radiation-type descent, not (DF); one-liner names all three. Meets the rule.
- House style: no violations found (Pauli pseudoscalar I and right unit I sigma_3 used, no imaginary unit;
  macros from notation.yaml). `credit.source` names the run.

### Check

`runcheck` 6/6 PASS; check4 log: 0 errors, 0 other findings, pass. Perturbations in scratch: mass made even
across the wall in the reflection classification (fails: the good set changes); s_in replaced by the O_B
image (fails); wall value -1/8 of the second-order coefficient changed to -1/16 (fails). The check tests the
algebra as stated; the Weber clause is bookkeeping only, and the class question (k vs -k pairing) is not
tested (the checks work in one sector).

### Fixes

1. Class: add "isotropic, with equal vectors in the helicities that c pairs" to the class of states in the
   formal, or restate (i)(c), (ii), (iv)(b), (vi) for the pair (k, -k) in the theta-sense (the sector-wise
   statements are exact in the sense "W followed by the particle-hole exchange"). With non-isotropic states
   in the theta-sense the per-sector floor fails and only n_k + n_{-k} >= 2 n0 holds.
2. One-liner: after "the invariant quasi-free Dirac states" insert "(homogeneous, isotropic, diagonal in
   helicity, charge-symmetric)".
3. (v)(b), "the tracial state is invariant and not Hadamard": for mu > 0 either add the wave-front argument
   (its two-point function is half the anticommutator, whose wave front set contains C+ and C-) or mark it
   argued. Technical: "so it cannot give a Hadamard state" -> "so, as the tracial state, it gives no
   Hadamard state (argued: its occupation tends to one half)".
4. Proof (iv)(c): "per sector" -> "summed over the two helicities" for 0.012760 (mu/pi)^{3/2} (per sector
   0.006380).
5. Lay: "The state that sits exactly on the minimum is well behaved" -> "... is well behaved, given a
   standard theorem on such states"; "The demand also makes the two sides equally hot" -> "The demand would
   also make the two sides equally hot (argued), which sits badly with the series' cold mirror".
6. Formal (iv)(b) to (vi): credit inline "(the pure-state profile, the transition probability and the
   least-number choice are those of Boyle, Finn and Turok, arXiv:1803.08930, Eqs. (3.48), (3.49), (5.13))";
   replace "read in part, through a summarising fetch" by these locators; confirm the PRL's arXiv number.
7. coverage / check docstring: say that the Weber function checks exponent bookkeeping only.
8. Cross-reference to proposal 1 (see below).

---

## Overlaps and conflicts

**No duplication.** Proposal 1 is about the background (whether the exact radiation field reaches the wall
when the quantum stress sources gravity); proposal 2 is about a test Dirac field on a prescribed background.

**Conflict, and how both can be stored.** Proposal 2's (RD) with (DF) uses a = a' eta exactly through
eta = 0 and on both sides, so M = m a' eta is odd: this is precisely the "mass term linear in conformal time
through [the wall]" that proposal 1's Reading places "outside what (A) and (E) allow". Under (A) and (E):
with b = 0 the branch joined to late radiation ends at a positive scale factor (T_max about 0.86 Mbar) and
there is no wall and no far side; with b != 0 a power-law origin has p != 1/2, so M is a power p/(1 - p) of
eta, not linear (smooth only at p = n/(n + 1), n >= 2, where M is eta^n: odd only for odd n, and then
the Landau-Zener form changes). So (A) + (E) + (RD) + (DF) cannot all hold, though no stored result is
contradicted. Both are worded conditionally: proposal 1 names (A) and (E) in its one-liner; proposal 2 names
(RD), (DF), (CW) in its one-liner, and its Dirac field is a test field (no (E)). They can be stored together,
with these cross-references (in text; a pinned `contradicts` is not available because none of these
hypotheses is a stored postulate, and the inconsistency is of a conjunction):

- Proposal 2, after (RD)/(DF) in the formal (or in its Reading): "(RD) and (DF) prescribe the background;
  with the expected stress of a Hadamard state of the content as its source, the exact radiation field does
  not reach the wall (\claimref{synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall},
  given its (A) and (E)), so this result holds for a prescribed background, not a self-consistent one."
  Also add that id to its `lineage.motivated_by` or as a related link. Suggestion (argued, my own estimate,
  not required): the Landau-Zener window is |eta| ~ 1/sqrt(m a'), cosmic time ~ 1/(2m), far from the Planck
  region where proposal 1's correction is of order one, so the floor is insensitive to it at order
  sqrt(m t_P); but the reflection W needs exact oddness at eta = 0, which is where proposal 1 bites.
- Proposal 1, in its Reading where it names "a mass term linear in conformal time through it or a
  continuation across it": cite
  \claimref{synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none}
  as a result that assumes these ((RD), (DF)) and is therefore not available jointly with (A) and (E).

If the maintainer stores (A), (E), (RD), (DF) as postulates, the build should flag any result resting on all
four (as E307 does for a recorded pairwise contradiction); short of that, the two text cross-references are
the record.
