# Report, run 2026-11-16-spectrum

Target: op.descent-state-and-spectrum ("The state of the descent and the primordial spectrum"), at Leon's
direction: browse the graph for ideas and think of new ones. Two attackers (constructive, adversarial), one blind
referee (a different model, deriving the perturbation theory independently before reading the proofs), one fix
round, one maintainer agent. No bridge-hunter (one cluster).

## Gates
Every proposal: check4 0 errors and validate_draft ok after the fix round (logs in verify/final/). After the
maintainer pass: layers 1, 2, 3 and 5 at 0 errors and 0 warnings store-wide; check4 on the seven changed store
entities (the five accepted results, the time-shift result, the finite-range result) 0 errors; 445 unit tests pass;
build, layout, site and lock rebuilt. NOT done: the store-wide layer-4 run. The layer-4 cache on main is stale (the
review-service changes to tp/validate.py invalidated every record), so the run is from scratch, more than an hour
on the cloud machine; it was stopped at Leon's instruction ("push as it stands") and the stale cache is left as it
was. No stored check file changed except the quasi-free result's, which keeps its five functions and adds one.

## Outcome
The problem is not settled and keeps its status (reformulated). The series still records no mechanism for the
measured spectrum. What the run found is a datum the store had never fixed, and with it a correction to the reasons
the stored negative results give.

## The slicing gap
The gravitational gauge field on the descent slice is not free: the constraint part of the field equation ties the
slice's curvature, its expansion perturbation and the deposit's contrast, 3R = 6 H^2 (delta - 2 delta_H). The slice
data are free, and in the radiation era the conserved amplitude is an exact linear function of them. Conventional
cosmology never meets the choice, because earlier metric evolution or causal compensation fixes the growing mode. A
deposit laid down in one event with no earlier metric stage has nothing that fixes the slice's expansion datum, and
no stored premise or result does (argued, by reading of the candidates: the time-shift result, both readings of the
dating's join, the field-space premise, the tame-wall and Hadamard-deposit premises, P1's count).

One white (thermal) deposit therefore has three readings:

| Reading | Slice | Index n_s - 1 | Amplitude at the pivot |
|---|---|---|---|
| (FR) | flat, deposit at rest (the stored reading, unnamed until now) | +3 | below 1e-77 |
| (FM) | flat, with the deposit's own momentum noise | +1 | below 4e-41 (whole bath) |
| (UE) | uniform expansion | -1 | (9/4)(a_d H_d/k)^4 times the contrast spectrum |

Under (UE) the thermal deposit reaches A_s at the pivot for T_d between 3.6e9 and 3.7e9 GeV, is 3.4e-12 to 3.6e-12
at the stored ceiling 7.3e8 GeV, and is 12 to 13 at 1e12 GeV, which is not a perturbation. Index -1 exceeds one
below a finite wavenumber, so (UE) gives a bound with an infrared end, not a spectrum; the largest observed scale
puts a rough conditional ceiling near 1e9 GeV on the descent temperature (no analysis of the low multipoles made).

## Established (five accepted results)
- synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit (SOUND WITH FIXES). Proved: the
  constraint on any slice from the stored field equation (sampled with the GTG engine at generic rational jets);
  the slice-independent combinations; the growing-mode projection in the radiation field (exact series); the three
  readings and their indices. Computed: the thermal amplitudes. Argued: no stored premise selects a reading.
  Transport-absent.
- synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary (SOUND WITH FIXES). Proved: a
  homogeneous gauge-invariant quasi-free deposit has a white energy term S_E(0) that vanishes exactly for pure
  stationary states; for the Weyl field the trace identity in Cl(3,0); the filled ball's excess over the vacuum is
  (k_F^4 k / 8 pi^2)(1 - l^3/30 + l^4/96). Under (UE) the filled ball gives n_s = 1 exactly: a miss at 8.3 to 8.4
  sigma, with amplitude 3 H_d^2/(8 pi^2 M_P^2) (reduced Planck mass), short by more than 1e17 on the window.
  Argued: the stored deposit is mixed, deep in the white regime, so its row under (UE) is index -1.
- synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape (OVERSTATED, restated; id kept). Proved:
  a deposit invariant under a relabelling group transitive on unordered pairs supplies two second moments only;
  white noise plus a k = 0 term for cells that tile the slice or sit on a lattice; off a lattice the shape is the
  placement's own structure factor. Argued: a pre-metric deposit carries a spectrum only through its invariance
  group or its placement.
- synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta (SOUND
  WITH FIXES; id kept). Proved, conditional on each flat reading: reaching A_s needs some quantum far above the
  Planck mass. With Hypothesis (QP) (deposit quanta below the Planck mass) attack item 3 is closed on flat slices;
  under (UE) it stays open.
- synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise, version 4 to 5 (restatement, SOUND WITH FIXES). The
  comparison of the shot term with A_s and the words "index 3" are now stated under (FR). No inequality or number
  changed.

## Killed in the run
- The orchestrator's seed that "matter at rest, no shear" are hypotheses of the uniform-expansion reading: uniform
  expansion alone suffices.
- The stored "index 3" for a thermal deposit on a flat slice: it is +1 once the deposit's momentum noise is counted.
- (UE) as a spectrum on an unbounded slice.
- The scale-invariant row as a statement about the store's deposit: the stored state rules do not deposit a pure
  stationary state. It stands as a miss about a deposit the series does not have.
- The tower read as a scale cascade: no stored map from rungs or floors to comoving scales, and one bit per rung is
  exchangeable in rungs.
- The seed's running for a nearly degenerate deposit (+0.034): the thermal sea gives +0.069, a one-parameter fit,
  excluded.
- An area-law logarithm read as a tilt (about -0.016): a sharp-window artefact, dropped by its author.

## Leon's decisions, 16 November 2026
1. The descent slice is left free: no reading adopted; the slice's expansion datum is a free datum of the descent.
2. The (UE) ceiling on the descent temperature is a conditional remark, with an attack item for the proper analysis.
3. The four stored entries that used the flat reading without naming it are reworded (time-shift result,
   finite-range result, holographic result, the open problem's text).
4. "Deposit quanta below the Planck mass" is a hypothesis of the sparse-deposit result only.
5. The restated exchangeable-deposits result and version 5 of the quasi-free result are accepted; ids kept.

## Left open (attack items on the problem)
What fixes the slice's expansion datum (a locality premise would select the flat slice; a junction rule at the join
would fix the slice data); the low-multipole analysis under (UE); non-quasi-free and bosonic deposits; the infrared
datum of a Hadamard deposit; a red or non-Gaussian modulator. The amplitude and the index are both still free.

## Cross-links noted, not acted on
- The spatial part of the rotation-gauge field Omega(e_j) is k times the slice-independent potential.
- The (UE) temperature at A_s lies within a factor five of the stored (R) ceiling; recorded as a coincidence.
- The filled sea's amplitude has the slow-roll form at epsilon = 1/3: a coincidence of form, no meaning claimed.

## Not done, for a later pass
- The store-wide layer-4 run and a refreshed layer-4 cache (see Gates).
- synthesis.frozen-point-geometry-reads-descent-as-vacuum and synthesis.pati-salam-chain-defects-cannot-source-spectrum
  still pass from a matter deposit of finite range to "the finite-range class, index 3" without naming (FR). They are
  outside the four entries Leon approved for rewording and were left as they are.
- The time-shift result's proof sentence "below 1e-77 ... must therefore contain a classical component" rests on the
  quasi-free comparison with A_s, now stated under (FR).
- The finite-range result says "reduced Planck mass" in words and keeps the symbol M_P; the store has no macro for
  the reduced mass.
- The literature cited from memory in the new results (Zel'dovich; Magueijo and Pogosian 2003; Tod; Torquato and
  Stillinger; Gabrielli, Joyce and Sylos Labini 2002; Gioev and Klich 2006) is used in no proof step and was not
  imported or checked against the sources.
