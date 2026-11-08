# Run 2026-11-08-current-algebra: report

Target: op.qft-non-abelian-gauge-fields, attack item "the current algebra along generators": the Standard Model gauge
algebra inside the exact window current algebra of the sixteen channels (Weyl components) per light ray and generation.
Method: attacker pair (A constructive, B adversarial), blind referee C, one fix round, close-out.

## Accepted (three results)
- synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split (A; SOUND WITH FIXES): the
  gauge algebra acts through the bilinears of five modes on the sixteen channels inside u(16) (complex channels, unit J; no
  chirality mixing; all currents of helicity 0); tr_16(rho X rho X') = 4 tr_5(XX') + 4 trX trX' on gl(5), so su(3), su(2)
  and hypercharge at level 4 relative to the five-mode trace form (tr rho(Y)^2 = 10/3 for the store's Y); the Sugawara split
  with central values 32/7, 2, 1, 1 and remainder 52/7 on localised vectors; the Virasoro relations not derived.
- synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy (A; SOUND WITH FIXES): a window lemma for
  quadratic current forms; the level-one u(n) Sugawara form equals the half-integer energy on every window with no edge
  term; one generation's channel energy is exactly the so(10) Sugawara energy at level 4 plus the number term on every
  window (c = 15 + 1 = 16). Prior art: Goddard, Nahm and Olive (the operator form); new here the exact finite-window form.
- synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation (B; OVERSTATED, restated; Leon
  accepted): title "Light-ray gauge currents of a generation see the linear anomaly condition, not cubic ones"; all 32
  gauge-commuting halvings have the same gauge currents with energy and sea up to the hypercharge constant; that constant and
  the Y-N term equal tr Y, the mixed gravitational coefficient (24 of 32 fail it); no quadratic trace sees the cubic
  conditions (2 of the remaining 8 are anomaly-free).

## Leon's decisions (8 November)
Accept the restated anomaly result; levels stated relative to the five-mode trace form (conventions); the slot module's I4
matched to +J on the channels, stated once in the conventions; recorded on op.qft-non-abelian-gauge-fields: the so(10)
energy, linear not cubic, and an attack item to derive the Virasoro relations.

## Maintainer pass
Cross-references between the three added to the extraction notes after acceptance (E201 forbade them in proposals).

## Checks
Baseline 0 errors 0 warnings. Gate after fixes: all three check4 exit 0 with no warnings, validate ok. Final check 0 errors 0
warnings; build 0 errors; layout, site, lock; 393 tests OK.

## Costs (approximate subagent tokens)
Attacker A 871k (with fixes), attacker B 626k (with fixes), referee C 249k: about 1.75M.
