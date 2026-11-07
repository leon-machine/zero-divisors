# Apply round 2, agent D3: answer 8 (the deferred H5 renames)

All changes are notation only; no statement, status, edge or check changed. Each bumped entity is at its
locked version + 1, with a credit entry for that version and `extraction.maintainer_pass_decisions_2`
(by maintainer-2026-11-07, 2026-11-07, what was renamed, why, and that the new letter was unused in the entity).
Every new letter was checked against the entity's formal, technical, lay, one-liner and proof text.

## Items

### kappa -> mu (R02 item 8)
| entity | version | what |
|---|---|---|
| synthesis.n-plus-null-ground-state | 11 -> 12 | formal (1): the Fermi seas chi(P - mu), "mu != 0 a constant Hermitian operator on K (the cited Theorem's kappa; here kappa is the surface gravity)", flat connection mu du. kappa stays the surface gravity (beta = 2 pi/kappa, kappa/2 pi). |

Users checked (all 32 files citing the postulate, the 23 users among them): none writes the operator except
synthesis.modular-data-on-a-generator-..., the source theorem. It keeps kappa: mu is already its constant phase
e^{I_4 mu} in (v), and kappa has no other meaning there. open_problems.yaml quotes modular-data's kappa; left.

### R02 item 10 (double letters)
| entity | version | what |
|---|---|---|
| synthesis.positive-null-energy-gives-r-premises | 8 -> 9 | proof (iii)(c), (v): boost rotor B -> G, dilation rotor D -> S (D stays the covariant derivative); also d Omega^2 written out (below). |
| synthesis.stationary-generator-states-and-the-edge-scaling | 1 -> 2 | formal (i) and proof: boost rotor B -> G. |
| synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit | 5 -> 6 | formal (i) and proof: boost rotor B -> G (same letter as the result it restates). |
| synthesis.state-selection-r-and-le-against-t05 | 4 -> 5 | Boltzmann factor Q_k = e^{omega_k p} (and Q for one mode) -> z_k, z; premise labels (Q) unchanged. |
| synthesis.field-strength-cancels-...-on-null-hypersurfaces | 5 -> 6 | smooth kernel R of (iii) -> S, remainder R_omega of (iv), (b) -> S_omega; R stays the spinor transport rotor of (ii). |
| synthesis.imported-buchholz-florig-summers-...-modular-stability | 3 -> 4 | inner items (a)-(d) of clause (a) numbered (1)-(4) ("the source's items (a) to (d)"); source_formal untouched; dependants cite outer clauses only. |

### R01 item 5
| entity | version | what |
|---|---|---|
| synthesis.dirac-causal-propagator-...-null-hypersurface | 4 -> 5 | the region U of the formal -> \mathcal{O}; U stays the Hadamard coefficient Delta^{1/2} R. |
| synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature | 2 -> 3 | rho = r - 2M -> zeta (formal, proof), so rho means r/2M only across the pair; Kruskal U kept (each entity defines its own, and the companion states the different normalisation). Companion's quotation: item for D2 (applied in its v4). |

"Up to a phase" in cosmological-horizon-completed-pair was already done by the GTG prover (span{1, hat-I}).

### R04 items 3, 4
| entity | version | what |
|---|---|---|
| synthesis.covariant-rung-coupling-...-transmutation-branch | 4 -> 5 | coupling matrix A = V^dagger M_u V^* -> \mathcal{A} (formal, proof, one-liner, the nonsymmetric-Yukawa remark); pseudoscalar A, m_A, K_A kept; and the norm N -> \mathsf{N}. |

Hermitian norm N (no target letter given): renamed \mathsf{N}, chosen free in every entity and in both subjects
(standard-model, quantum-fields). R04's example \mathcal{N} was not used: it is the store macro \Ncone (the null
cone) and the number operator of synthesis.floor-regulator-... in quantum-fields. Kept: N = M_P/H, N_R, N_c, N_nu.
Renamed in the whole rung-field family (14 entities; four more than R04 listed, so the family stays uniform):
constant-d-term-level-fixes-... 2 -> 3 (used both N's), majorana-scale-not-carried-... 3 -> 4 (used both),
rung-field-on-the-lift-locus 4 -> 5, rung-field-d-term-action-... 5 -> 6, rung-field-level-needed-... 4 -> 5,
rung-field-charged-pair-decouples-... 4 -> 5, rung-field-charged-scalar-sum-rule 2 -> 3,
rung-field-coupling-to-its-conjugate-... 3 -> 4, scale-free-rung-potentials-... 2 -> 3,
linear-rung-field-has-a-neutral-normal-pair-... 4 -> 5, one-doublet-field-is-pure-gauge-... 3 -> 4,
rung-field-is-odd-in-the-tower-... 2 -> 3, transmutation-of-the-rung-field-... 5 -> 6, covariant-rung-coupling (above).
Products such as aN^2, eNm, dN, 2sN^*, NW'' and dN/dm were renamed by hand-checked rules.

### d Omega^2 where it clashes (R03 C)
Replaced by the explicit round metric where the entity also writes the gauge field Omega:
interior.kasner-form-interior 6 -> 7, pairing.imported-schwarzschild-connection-curvature 6 -> 7 (vartheta, the
coframe being theta^i; its technical level's theta-angle also -> vartheta), scrambling.slice-volume-exactly-per-unit-killing
4 -> 5, sheaf.weighted-limit 6 -> 7, singularity.imported-interior-collar-kasner-form 6 -> 7,
singularity.stretched-singularity-count 7 -> 8 (area element sin theta dt d theta d varphi),
synthesis.loc-independent-of-clausius-and-killing-data 4 -> 5 (three-sphere, d chi^2 + sin^2 chi(...)),
positive-null-energy (above, vartheta and phi). collapsing-hole-flux: item for D2 (applied in its v4).
Not changed (no other Omega in the entity, so no clash): sheaf.gauge-field-cometric, singularity.euclidean-section-period,
singularity.imported-induced-geometry-interior-slice, synthesis.c1-c2-forms-forced-one-number,
synthesis.exceptional-boundary-measure-one-calibration, the two singularity setting notes, and the solid angle of the
e+e- -> mu+mu- cross-section. d\Omega in kerr-ring, frozen-point-integrand and frozen-point-reduces is the exterior
derivative of the connection, and in neutral-singlet-bit a coefficient d times the state Omega: correct, kept.

## Pins reviewed
102 pins on the 30 bumped entities, all class N: 99 repinned in place (edge lists and one equivalent_to; three
history notes that the substitution touched were restored to their original text). Three are on entities others
claim and were passed: pairing.static-frame-only-expansion-survives and synthesis.clausius-on-the-action-shell-...
(items-for-D1.md; D1 had already reported, so the orchestrator may need to apply them), collapsing-hole-flux
(items-for-D2.md). No dependant quotes the old notation (the rung family's mutual quotations were renamed together).
From items-for-D3.md: loc-independent repinned black-hole-data@7 -> @8 (class N per D2).

## Not applied exactly, or for Leon
- modular-data keeps kappa for the operator (mu taken there); the postulate names the correspondence.
- The rung N rename covers 14 entities, not the four R04 named, and uses \mathsf{N}, not R04's \mathcal{N} (reasons above).
- Same pattern, not in the readers' lists, left: synthesis.boost-evolution-on-generators-is-one-unitary-group names
  its rotor B_lambda (the boost-bivector letter); synthesis.hadamard-scaling-limit-premise names its region U.
- check.py variable names (B, Q, R, N) were left; they are code, not store text.

Validation: tp check --store store --layers 1,2,3 --keep-going --author leon, run twice (before and after the
items-for-D3 repin): 0 errors, 0 warnings both times (only pre-existing I213/I305 infos).
Open at the end: collapsing-hole-flux v4 (D2) still pins positive-null-energy@8; item 3 in items-for-D2.md asks
for @9 (it was added after D2 applied items 1 and 2).
