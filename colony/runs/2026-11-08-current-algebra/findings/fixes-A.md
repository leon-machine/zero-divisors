# Fixes by attacker A (referee C: both SOUND WITH FIXES)

## synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split
- Formal (iii): on D, H is now the sea-normal-ordered H_inf of
  synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (iii) summed over the
  channels, with the zero modes J(M)_0 counted from the sea; the window statement is for the window H and window zero
  modes. Proof (iii), the band: the same, with [H_inf, j^{xy}_m] = -m j^{xy}_m on D.
- Formal (iv): added "The Virasoro relations of the L^f are not derived; c_f is defined as 2 dim f/(2 + lambda_f),
  equal to twice the level-two norm, and would be the central charge if they hold."
- Lay: "(central charges)" replaced by "(central values, the central charges if the factor energies obey the Virasoro
  algebra, which is not shown here)".
- Referee fix 3 (cite the sibling proposals) not applied: a proposal cannot cite another proposal (E201); left to the
  maintainer after acceptance (the coset remainder as a function of the so(10) currents, P2 (iv); the shared trace form
  with B's proposal).

## synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy
- Title (quoted in YAML, 87 characters): "On every window one generation's channel energy is so(10) Sugawara plus the
  number term".
- Prior art: added Goddard, Nahm and Olive, Phys. Lett. B 160 (1985) 111 (title and journal checked by the referee,
  volume and page from memory) as the operator form of the identity, its condition being in substance A_C proportional
  to Delta (symmetric space E6/(SO(10) x U(1)), from memory). "New here" now limited to the window lemma (i) with its
  u(n) case (ii) and the exact finite-window form of (iii); the tensor identity A_so = -3 A_N recognised as the
  classical symmetric-space condition, computed exactly here.
- Formal (iii): states "so(10) at level 4: lambda = 2h/k with h = 8; c = 15".
- Lay: the 45-dimensional symmetry "here is a symmetry of the currents along the light ray, not a unified gauge
  symmetry".

## Gate
Checks unchanged. Per proposal, with PYTHONDONTWRITEBYTECODE=1, one gate process at a time:
- P1 (Sugawara split): runcheck 5/5 pass; check4 exit 0, 0 errors, 0 other findings; validate_one ok, no codes.
- P2 (so(10)): runcheck 4/4 pass; check4 exit 0, 0 errors, 0 other findings; validate_one ok, no codes.
Re-registered with propose_claim (ok, accepted for review, no E/W codes) after moving the old proposal folders aside
(to the session scratchpad, aside-fix1; nothing deleted); entity.md, proof-main.tex and check.py confirmed identical to
the work folders; coverage.yaml copied back into both proposal folders.
