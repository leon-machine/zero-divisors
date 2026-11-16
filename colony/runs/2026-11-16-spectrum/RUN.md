# Run 2026-11-16-spectrum: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-16-spectrum, from main at 87351bd). Run folder:
colony/runs/2026-11-16-spectrum/ (findings/, work/<name>/, verify/). Read colony/BRIEF.md and colony/POLICIES.md;
this file overrides them. Baseline: baseline.log. Session name for proposals: 2026-11-16-spectrum. Model for credit
entries: Claude Fable 5.2 (attackers), as the session runs on it.

## Goal
One problem: op.descent-state-and-spectrum ("The state of the descent and the primordial spectrum"). Read it in
full (`python3 colony/labcli.py get_open_problem '{"id":"op.descent-state-and-spectrum"}'`, about 30 KB) and its
eight linked entities in store/claims/<id>/ (entity.md, proof-main.tex, check.py). Earlier work: about two dozen
stored negative results; colony/runs/2026-11-10-phase3/findings/attack-SA.md and attack-SB.md hold the index ledger
(24 rows) and Leon's decision of 10 November: "no mechanism" kept, the spectrum is the deposit's free infrared
datum, and a future index match counts only with a second number (amplitude or running) from the same structure
with no further chosen number. Do not redo the ledger.

Leon's steer for this run: browse the graph for ideas, and think of your own. The success clause stands: a
mechanism with a computed n_s to set against the measured value, or a proof that the series cannot supply it.
Progress short of that is welcome if it is new: a stored result corrected, an escape closed with a proof over a
class, a hidden hypothesis named.

## Seeds from the orchestrator (ideas not in the store; test them, do not assume them)
Each is a lead, written before any check against the store. Kill it if it fails and say so.

S1. The slicing gap (the main lead). The stored finite-range result
    (synthesis.finite-range-descent-deposit-cannot-seed-cmb) is a statement about a covariance of zeta of finite
    range. The stored quasi-free result (synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise, clause (iv)) bounds
    the contrast delta of the energy the modes carry and then reads its spectrum as the primordial one ("index 3,
    below 1e-77 at the pivot"). But the stored holographic result
    (synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window) converts energy fluctuations by
    the Poisson relation, P_Phi = 8 G^2 k^-4 <delta rho^2>. These are two different conversions. The gravitational
    gauge field on the descent slice is not free data: it satisfies the constraint part of the field equations given
    the deposit. Two pure readings:
      (A) uniform expansion (one simultaneous descent: the slice has uniform Hubble rate, matter at rest, no shear).
          The energy constraint then gives the relativistic Poisson relation on all scales,
          k^2 psi = 4 pi G a^2 rho delta (sign by convention), so the comoving curvature perturbation is
          R = (3/2) (a_d H_d / k)^2 delta up to sign, and
          Delta_R^2(k) = (9/4) (a_d H_d / k)^4 Delta_delta^2(k).
          A matter deposit of finite range (white, uncompensated) then has zeta of infinite range (the Newtonian
          potential of its mass excess), index -1 ("n_s = 0", the textbook white-noise case), and an amplitude
          larger than the stored shot term by (a_d H_d / k_*)^4, that is 1e21 to 1e82 over the window.
          Orchestrator's rough number, to be recomputed exactly: for a thermal deposit
          Delta_R^2(k) = (135 / (pi^4 g)) (H/T)^3 (a_d H_d / k), which reaches A_s at the pivot for T_d of order
          4e9 GeV and is of order one at 1e12 GeV. If right, under (A) the I-state deposit is excluded above about
          1e9 GeV by the wrong (red, index -1) spectrum it would produce, and the store's window is cut.
      (B) flat slice with a locally matched Hubble rate (each region a flat Friedmann solution with its own start
          time: the "field of delays" of synthesis.adiabatic-deposit-modulation-is-a-time-shift). Then zeta ~ delta/4
          locally, the stored reading, index 3; in comoving gauge the matter contrast is then compensated,
          P_delta ~ k^4.
    Questions: (a) is the gap real, i.e. does any stored premise or result select (B) (candidates: the time-shift
    result, the radical-normal tame wall, the Weyl-flat/Hadamard collar premises, the field-space premise (FS), P1's
    common count, the dating)? (b) if nothing selects it, state the dichotomy as a theorem with the hypothesis
    named, and give the index ledger under (A): n_s - 1 = s - 1 where the deposit's energy structure factor goes as
    k^s at small k. (c) What a generic mix of (A) and (B) gives (the (A) part dominates by (a_d H_d/k)^2). (d) Tod's
    theorem on isotropic (conformally regular) initial singularities, if you can cite it reliably: the free data are
    the conformal 3-metric only, so the matter contrast is slaved to the geometry; say what that does to "deposit".
    Literature from memory here (flag it): white noise in the density is "n_s = 0"; Zel'dovich's k^4 law for causal
    compensated perturbations; Magueijo and Pogosian 2003 on thermal fluctuations; Nayeri, Brandenberger and Vafa
    2006; Gabrielli, Joyce and Sylos Labini 2002 on the Harrison-Zel'dovich spectrum as "super-homogeneous";
    Torquato on hyperuniformity (the free-fermion ground state and the Harrison-Zel'dovich spectrum are both class
    II, S ~ k).

S2. The pure fermion deposit is Harrison-Zel'dovich under (A). For a homogeneous gauge-invariant quasi-free CAR
    state with occupation n_p, the number structure factor is S(k) = 1 - (1/nbar) int n_p n_{p+k}, so
    S(0) = <n(1-n)>/<n>: zero exactly when n_p is the indicator of a set (a pure state, zero entropy), and then
    S(k) = vol(Omega minus (Omega + k))/vol(Omega), linear in k for a smooth Fermi surface; for a ball
    S(k) = 3k/(4 k_F) - k^3/(16 k_F^3) exactly (a rational polynomial: checkable in exact arithmetic). So under (A):
    a pure gauge-invariant quasi-free deposit gives n_s = 1 exactly (index 0, no chosen number), 8 sigma from the
    measured value, with corrections of relative order (k/k_F)^2 only; any mixed (thermal) deposit gives index -1;
    a paired (BCS-type, non-gauge-invariant) pure state has S(0) > 0. Orchestrator's rough amplitude for a
    relativistic degenerate deposit carrying the density: Delta_R^2 = (9 g / 16 pi^2) (k_F / M_P)^4 (unreduced
    Planck mass), which needs k_F near 1e17 GeV / g^(1/4), far above the stored window. Check the energy structure
    factor, not only the number one. The number variance in a ball then goes as R^2 log R (an area law with a
    logarithm): relate this to the stored area-law reading of result (vii) of the problem. Is the tilt reachable
    without a chosen number (finite temperature gives S = S(0) + c k, whose running is +0.034 at the measured tilt,
    excluded: check)? Does the store's deposit (the I-state, occupations conserved under (L_E), entropy conserved,
    the charge Q = epsilon N) allow a pure deposit at all?

S3. Geometry-blind pre-metric deposits. A deposit laid down before any metric, with no geometric information
    (its state invariant under relabelling of the N light rays, or cells, of P1's count), is exchangeable; its
    two-point function is one constant off the diagonal, so on any slice it is white noise plus a k = 0 mode
    (index 3 under (B), -1 under (A)). So the pre-metric escape hatch of the finite-range result ("initial data of
    the pre-metric sector") needs a deposit that carries a conformal structure. Prove or refute; say which stored
    structure, if any, gives the pre-metric state a group smaller than the symmetric group (the frozen point's
    stabiliser acting on the slice by conformal maps needs a weight-zero field).

S4. The tower as a cascade. Each transport step adds a plane with one direction squaring to -1 and one to +1; the
    boost of that plane is the dilatation of the conformal model one floor down. If the store ties rungs to comoving
    scales (rung unit, tower floors, tube-point scale, window reading), a state built rung by rung with one
    independent bit per rung has equal variance per logarithmic interval (index 0) with a log-periodic modulation,
    and a tilt of order 1/depth. The 10 November survey says the pair channel is one shell with no spatial mode, so
    expect this to die on "no stored map from rungs to comoving scales": check and record it in one paragraph, no
    more, unless the map exists.

S5. Attack item 3 of the problem (sparse or energetically broad quasi-free deposits). With S(k) <= 2 for every
    homogeneous quasi-free CAR state (number-conserving or paired), a spectrum flat over the observed band needs at
    most about k_1^3 / A_s quanta per unit volume at the largest observed scale k_1, so quanta each far above the
    Planck mass if they carry the density: decide whether this closes the item, under (A) and under (B).

## Attackers
SA (constructive). Aim: settle S1 as a theorem (the dichotomy with its hypothesis named; the conversion under (A)
   derived in the store's language: Gauge Theory Gravity on a flat background, the h and Omega gauge fields; other
   formalisms only as labelled readings), then S2 (the exact structure factor, the index and the amplitude under
   (A)), with the corrected wording the stored quasi-free clause (iv) needs. At most 3 proposals; prefer two strong
   ones. Add at least one route of your own from the graph.
SB (adversarial and cross-pollinating). Aim: break S1 and S2. Find the stored premise that selects (B), if there is
   one; test the (A) conversion against the superhorizon-zeta Fact and the Sachs-Wolfe Fact as stored; recompute the
   thermal amplitude by a different route; check whether (A)'s white deposit is a growing mode at all (decaying-mode
   content, shear), whether the infrared divergence of index -1 is admissible, and what the observed band then
   bounds (a ceiling on T_d under (A)?). Then S3 and S5 as proofs or refutations, and S4 in one paragraph. Look in
   other subjects for anything that fixes the deposit's small-k structure (hawking.i-state,
   synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations, the mirror's deposit law,
   synthesis.quadratic-flows-cannot-thermalise-descent, synthesis.cold-mirror-needs-non-equilibrium-descent, the
   record chain, the count N). At most 3 proposals.
Division: SA files the dichotomy/conversion result and the structure-factor result; SB files the exchangeability
result, the sparse-deposit result and any refutation or correction of a stored entity. Each reads the other's
findings file midway (findings/attack-SA.md, findings/attack-SB.md) and never files what the other filed. If SB's
attack kills S1, SA restates to what survives.

## Run-specific rules
- One cluster, so no bridge-hunter; the orchestrator relays cross-links.
- Kill conditions are pre-registered in the findings file before computing. For S1: "a stored premise or proved
  result forces the flat-slice reading (B)" kills the dichotomy as new (then record which premise does it, and
  whether the stored statements cite it). For S2: "the energy structure factor of a pure gauge-invariant deposit
  does not vanish linearly at k = 0" kills the index-0 row.
- Index matches: Leon's rule of 10 November applies. n_s = 1 exactly is a miss at about 8 sigma and is to be
  reported as a miss; do not tune anything to the measured tilt. A one-parameter family that reaches the window is
  reported as a fit with its parameter named.
- Corrections to stored entities (version+1) keep every stored file; list every new assumes edge, new postulate or
  hypothesis and every changed status as a decision for Leon; do not make them.
- Statements and proofs in geometric algebra where the algebra does the work; cosmological perturbation theory in
  GTG language (flat background, gauge fields), with the metric reading only as a labelled parenthetical.
- Checks: exact rational arithmetic, `import GA`, premise() per premise. pi is bracketed by rationals as the stored
  checks do.
- The machine has 2 CPUs and a second attacker running: one gate process at a time each.
