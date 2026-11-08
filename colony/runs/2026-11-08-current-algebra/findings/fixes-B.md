# Fixes B: synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation

Referee C: OVERSTATED. Accepted in full: the hypercharge zero-mode constant L tr_C rho(Y) is the difference of
the seas' hypercharges (L/2) tr_{V+} Y, and tr_{V+} Y is also the Y-N mixed central term in u(16); it is the
mixed gravitational (linear) anomaly coefficient, nonzero for 24 of the 32 sign patterns. Only the cubic
conditions go unseen: among the 8 patterns with tr Y = 0, phi_C is an exact isomorphism of currents, energy and
sea, and 2 of them are anomaly-free. Verified independently before editing (component contributions 1, 1, -1, 1, 2;
tr Y in {0, +-2, +-4, +-6}; zero exactly when the sign of the 2 is opposite to three of the four +-1).

Restated, every level (id kept):
- Title: "Light-ray gauge currents of a generation see the linear anomaly condition, not cubic ones" (89 chars).
- Formal (iii): sea's hypercharge (L/2) tr Y J and the Y-N central term q tr Y J, both the linear coefficient;
  values 0, +-2, +-4, +-6, zero on 8 of 32; the 2 anomaly-free among the 8; six anomalous not distinguished;
  "each anomaly coefficient is a weighted trace, linear for the mixed gravitational condition and cubic for the
  others"; "32 sign patterns and any neutral line" (also in the preamble).
- Reading: one linear condition, seen as the sea's hypercharge and the Y-N central term, and cubic conditions
  that need the channel weights.
- Technical, one-liner ("levels carry no anomaly information" removed), lay ("cannot tell apart the eight
  arrangements whose total hypercharge is zero, six of them inconsistent"; "It knows only the simplest part of it").
- Extraction note (b): "the gauge currents with energy and sea, up to the hypercharge constant"; no relation
  between the levels of g and the cubic conditions; the linear one is the Y-N mixed level and the sea's
  hypercharge. Prior art: a representation and its conjugate have equal quadratic indices and opposite anomaly
  coefficients (classical).
- Proof (iii): the sea's hypercharge, the constant as the difference of the seas' hypercharges, the Y-N term from
  the stored matrix identity with M' = 1, the 8 / 24 / 2 count.
- New check check_hypercharge_constant_is_the_linear_anomaly_coefficient: tr Y values and the 24 / 8 / 2 counts,
  the 2 anomaly-free inside the 8, the constant as the difference of seas' hypercharges for all 32 x 5
  one-component reversals, and on a GA window (L = 2, channels of V_{1,0} and V_{2,0}) the sea's hypercharge and
  [rho_1(JY), rho_1(1)*] on the sea, both tr Y J. Coverage entry added.
- Not done (per instruction): no citation of the sibling proposals (E201).

Gate: runcheck 5 of 5 pass; check4 exit 0, 0 errors, 0 other findings (no W413); validate_one ok, no codes;
re-registered with propose_claim (moved aside, entity.md, proof-main.tex, check.py identical, coverage.yaml copied
back, check4 rerun clean).
