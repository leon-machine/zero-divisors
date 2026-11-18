# Maintainer pass: the energy per creation event (Leon's decision of 18 November 2026, 14:04)

LAB = /home/claude/phys-graph (branch run/2026-11-18-leads, from main after pull request 45). Leon decided: adopt the
computed mean energy per creation event in the gravitational floor, in place of the stored convention (3T per event,
energy fraction 4Y). Read first: colony/runs/2026-11-18-navigate/verify/R3.md, section "The energy convention", and
colony/runs/2026-11-18-navigate/maintainer-M1.md (the previous pass, same entities), and
colony/runs/2026-11-18-navigate/MAINTAINER.md for the bookkeeping, style and check rules, which apply here unchanged
(source string for credit entries: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'; extraction key
maintainer_pass_2026_11_18_energy).

## The computation to store
In the rate integral of Theorem synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, clause
(v), the angular weight of every channel is s^2 = 4 E1^2 E2^2 (1 - cos)^2 times a constant, so each incoming leg is
weighted by E^3 f(E). The mean energy of a leg is therefore
  Bose:  Gamma(5) zeta(5) / (Gamma(4) zeta(4)) T = 4 zeta(5)/zeta(4) T      (about 3.832 T)
  Fermi: (15/16) 24 zeta(5) / ((7/8) 6 zeta(4)) T = (30/7) zeta(5)/zeta(4) T (about 4.106 T)
and an event deposits E1 + E2: 8 zeta(5)/zeta(4) T from a Bose pair, (60/7) zeta(5)/zeta(4) T from a Fermi pair. For a
produced species j the mean over the bath's channels weights these by the Bose and Fermi parts of alpha_j in clause (v):
  Bose part  proportional to (c_j (N_s + 12 N_v) + 5 tau_j sum_i tau_i)/225,   Fermi part proportional to 49 c_j N_w/4800.
With s/rho = 4/(3T) the energy fraction at production is (4/3)(E_event/T) Y, with Y the yield of events. Referee's
values for (4, 45, 12): 7.873 T (real scalar), 7.890 T (chiral fermion, vector), 7.889 T (the Standard Model's content,
and nine vectors); energy fraction about 10.52 Y; floors 1.273 times those on the 4Y convention. Recompute all of this
yourself; zeta(4) = pi^4/90, and zeta(5) is to be bracketed by rationals in the checks (1.0369277 < zeta(5) < 1.0369278;
verify the bracket by a partial sum with an exact tail bound, in the check).

## What to change
1. dark-matter.seeding-gravity-floor-dark-towers-temperature: the floor is defined with the mean energy per event. State
   and prove the mean (the computation above, citing clause (v) of the theorem for the weights), give the energy fraction
   (4/3)(E_event/T) Y and the new prefactor of xi_floor (about 1.23e-3 c^(1/4) (16/g_d)^(1/4) at the ceiling, with the
   small dependence of E_event on the produced content stated), and remove the "3T per event" and "8Y" counts and the
   sentence I added that says the mean was "computed in the review ... not by this proposition's check": it is now
   proved and checked here. Keep "this is a floor".
2. Every entity that quotes a number built from the floor (M1's report lists them, and R3 lists what each becomes):
   dark-matter.coefficients-floors-they-give-what-gravity (floors, eta', the crossover coefficient, Delta N_eff values and
   their round bounds, the floor at the rescue temperature if it depends on the energy), dark-matter.stored-asymmetry-
   charge-not-number, dark-matter.radiation-audit-what-theorem-closes-what, simulations.imported-mirror,
   synthesis.mirror-temperature-measures-deposit-under-r (clauses (i) and (iii), with (R) and without),
   synthesis.adiabatic-deposit-modulation-is-a-time-shift, dark-tower-matter.mirrors-composition,
   dark-matter.mirror-share-one-how-fragile, simulations.s3-mirror-cluster (the quoted present floor),
   pred.no-dark-radiation (its sentence quoting the floor; kill condition, threshold and status untouched), and the
   quoted numbers in store/open_problems.yaml (op.pre-descent-theory "below 2.5e-5", and any other quote of 5.2e-4,
   6.4e-4, 4.4, 2.5e-5, 3.0e-5: grep the whole store, notes excluded, and list what you find). Remove the
   "on the stored convention" qualifiers and the "computed in the review" sentences that were added on 18 November in
   coefficients (iv) and mirror-temperature (i): the numbers are now the stored ones.
3. Quantities that count quanta and not energy (the yield, the shortfall against the baryon number, c*, the Pati-Salam
   and untuned-fit results) do not change; do not touch them. If you find one that does depend on the energy, report it.
4. If any qualitative conclusion changes at the new floors (eta' crossing one, a bound that fails, a margin that
   closes, "the floor drops out" under (R)), stop on that clause, restate it truthfully, and list it.
5. Bookkeeping as in the previous brief: version + 1 on each changed entity, amendments entry (kind restatement),
   credit entry, extraction note, all four levels consistent, checks updated in exact arithmetic with rational brackets.

## Checks you may run, and the report
`python3 colony/runcheck.py store/claims/<id>/check.py` per changed check; `python -m tp check --store store --layers 1-3
--keep-going --author leon` once at the end. No layer 4, no check4, no validate_draft. Do not commit or push, do not
spawn agents, do not touch anything outside the entities named here and the quoted numbers you find.
Write colony/runs/2026-11-18-leads/maintainer-energy.md: each entity old -> new version, every number old -> new with the
computation, conclusions that changed (or none), stale quotes found and what you did, layer 1 to 3 result.
