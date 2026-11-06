# Run 2026-11-06-edge-normality: report

Target: op.r-premises-external, the ground-state clause of premise (N+) without stationarity (with
op.null-positivity-curved-horizons item (ii)). Second strand: results of Leon's 6 November working document
"Scalars and the Continuum" filed into the store. Method: attacker and referee (two attackers, one filer, two
blind referees, one fix round); no bridge-hunter (one cluster).

## Outcome on op.r-premises-external: proved-partial (reformulated, not settled)
- synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state (attacker A; referee P: SOUND
  WITH FIXES; fixes applied). Within gauge-invariant quasi-free states on one generator, field-level geometric
  modular action (the modular conjugation of each half-line algebra acts on the fields as the charge-conjugating
  reflection about its cut, sign eta) at cuts whose doubled differences generate a dense subgroup gives the null
  vacuum of (N+) for eta = -1 and its time reverse (the filled positive-energy sea) for eta = +1. One cut gives
  purity (every mixed state, all half-thermal and affine-KMS states included, fails at every cut); the dense cuts
  give stationarity and charge symmetry as outputs; natural-cone positivity of J gives the Hardy polarisation via
  Loewner. The hypothesis names J only: no modular group, KMS condition, temperature or stationarity. It is the
  first stationarity-free form that reaches the ground-state clause. It is spectral, not thermal, input, and the
  converse rests on literature cited from memory; recorded as an equivalent form of (N+), not a derivation.
- synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i (attacker B; referee P:
  OVERSTATED, restated to the net level; Leon accepted the restatement). Every net-level principle (Buchholz-Summers
  geometric modular action, modular stability, Haag duality, positive net translations) is shared by the vacuum's
  local gauge transforms, including pure translation-invariant Fermi seas that are locally normal and
  generator-Hadamard but not ground states, and complex conjugation maps the vacuum to the filled sea. So no
  net-level principle gives the ground-state clause, and any derivation must supply two data: the lift of the affine
  translations to the fields (a flat connection along the generator) and the orientation of the imaginary unit
  relative to time.
- Literature verified this run: Buchholz, Florig, Summers, Lett. Math. Phys. 49 (1999) (math-ph/9909003): CGMA
  alone gives translations (Prop. 3.5), with modular stability the spectrum condition up to sign (Prop. 3.6), and
  not a ground state on its own. Yafaev arXiv:1303.4040 (abstract).
- What remains open: derive field-level geometric modular action, or the ground-state clause, from a principle of
  the series; and the sign datum.

## Leon's decisions (DECISIONS.md)
(N+) stays the postulate, with field-level geometric modular action recorded as an equivalent stationarity-free
form; (N+) reworded so the null translations act by parallel transport (zero connection); the orientation of i is
NOT fixed by convention and is named as a datum (N+) assumes; all four flagged proposals accepted.

## Scalars-session strand (filer S; referee G)
- synthesis.blade-square-signs-f2-quadratic-form: SOUND WITH FIXES. Blade square signs form an F2 quadratic form
  whose Arf invariant and radical give the type of Cl(p,q); classical (Ovsienko 2016; Elduque and Rodrigo-Escudero
  2018, verified, now cited), with a transport-convenient corollary on the (1,1) and (0,2) increments.
- synthesis.nilpotent-steps-derivative-exponential-and-boost (filed as limits-as-null-steps; OVERSTATED, restated,
  renamed): dual-number derivative, any generalised inverse of a null step extracts the derivative (the Witt
  partner is the self-adjoint one), prod(1 + b_i) = exp(sum b_i) realised in Cl(N,N), the nilpotent boost. States
  that no limit is removed.
- note.one-relation.two-presentations-differ-over-the-integers: the Witt and orthonormal presentations of the (1,1)
  plane differ over Z (M_2(Z) versus an index-4 suborder; lattices II_{1,1} and I_{1,1}).
- Not filed as duplicates of stored results: the Morita/quaternionic tower (std-algebra.periodicity and others), the
  pseudo-inverse identities (singularity.pseudo-inverse-identities-hyperbolic-atom), I_4 B = J
  (synthesis.wedge-reflections-compose-to-the-two-pi-rotor-...).
- Corrections fed back to the working document: the F2 classification is published; Cl(N,N) suffices for the
  null-step products.

## Cross-links
The field-level condition is where the scalars document's identity I_4 B = J enters: the Bisognano-Wichmann wedge
reflection is I_4 composed with the transverse pi-rotation, an element of the algebra, and the residual sign datum
is the orientation of I_4 (equivalently of the transverse kernel bivector).

## Costs (approximate subagent tokens)
Attacker A 392k, attacker B 387k, filer S 350k, referee P 251k, referee G 207k: about 1.6M.
