# Consistency pass, reader R06 (quantum-fields and singularity), 7 November 2026

What I read in full: all 143 entities of read_R06.txt, every formal, technical, lay and one-liner level, every
proof (main and standard-route), the derivations, pins and extraction notes. Formal levels and proofs of every
claim were read line by line; long setting notes were read in full (some first in truncated views, then their
remainders). Check scripts were consulted only where a level depended on what a check computes (composite
scalars, massive Dirac).

## Fixed (old -> new version, what)

- synthesis.imported-adler-bell-jackiw-axial-anomaly 1 -> 2: bare unit in the mass term $2im\,j^5$ (formal,
  one-liner; the detector misses `i` followed by a letter) restated by U4 as $2I_4m\,j^5$, with the unit sentence;
  source form moved to extraction.source_formal.
- synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard 3 -> 4: every cross product
  (formal $s' = 2h\times s$, the proof's recursion) written as the dual of the outer product, $a\times b = -I(a\wedge b)$
  in $\Cl(3,0)$; all identities verified with lib/GA.py (scratch verify/check_fixes.py).
- synthesis.attachment-transport-is-flat-only-where-weyl-vanishes 2 -> 3: sentence saying which unit acts where
  ($I_4$ on spacetime bivectors, complex dimensions on $\CS$ over right $I_6$).
- field-theory.composite-scalars-mean-field-level 4 -> 5: undefined $B$ in "$\mu = mB$" defined (the mass pairing
  $B_N(f(k), f(-k))$ of field-theory.mass, $|B| = 1$, as the check computes).
- field-theory.where-each-lives 3 -> 4: the unit $\pm I_6$ of $\CS$ said to act by right multiplication.
- singularity.solution-where-divergence-lies 3 -> 4: clause (1) writes the store's macro $\mathcal{R}$ for the
  background field strength in LDG sign (dictionary C5); sentence added giving both radial eigenvalues, $-2M/r^3$
  (LDG) and $+2M/r^3$ (store), on $\sigma_r = e_re_t = -\partial_t\wedge\partial_r$.
- singularity.curvature-gauge-field-exact-shape-decoupling 4 -> 5: the formal said its sign convention was that of
  solution-where-divergence-lies(1) and of the Cartan appendix, "which agree"; (1) is LDG sign, the statement
  ($\mathcal{R} = -(M/r^3)S$, $\mathcal{R}(\sigma_r) = +2M/r^3\sigma_r$) is the store sign. Citation of the sign
  corrected at the formal level and in the proof's assembly step; formula unchanged. Computation (GA.py):
  $\sigma_r = -(e_t\wedge e_r)$, $\hb(e_t)\wedge\hb(e_r) = e_t\wedge e_r$, background $R(e_t\wedge e_r) = (2M/r^3)\sigma_r$,
  hence $\mathcal{R}(\sigma_r) = -R(\hb(\sigma_r)) = +(2M/r^3)\sigma_r$.
- interior.gauge-trajectory-unipotent-ray 8 -> 9: clause (4) "single null direction of the kernel" corrected to
  "kernel direction $e_r$, null for the rescaled limit form" ($g(e_r,e_r) = -1$ at every $r > 0$); garbled proof
  expression $1 - \beta^2 - 2\lambda\beta - \lambda^2\cdot1\cdot(-1)(-1)$ written as $1 - (\lambda+\beta)^2$.
- sheaf.gauge-field-cometric 3 -> 4: "fails at $r = 0$ through a null kernel" (every level, proof) said precisely, in
  line with dictionary C8: $\beta$ diverges and $\beta^{-1}\hb \to -P$, whose kernel contains $e_r$, null for the
  limit form.
- note.singularity.setting-machine-verification 1 -> 2: bare unit in a subscript, $R_{2\pi i} = -1$, $R_{4\pi i} = +1$,
  written $R_{2\pi J}$, $R_{4\pi J}$, $J = e_2e_3$, as the cited singularity.euclidean-rotor-where-it-lies states it.

tp check (layers 1-3, one run after all edits): no error or warning on any R06 entity; only the seven I213
infos of the baseline.

## For Leon (each with evidence and proposed fix)

1. "$i = I_4$" as a naming of the unit. About fifteen field-theory entities and two titles ("Mass with $i = I_4$",
   field-theory.mass; "The unit $i = I_4$ keeps its properties only in dimension 0 mod 4") write "with $i = I_4$"
   in formal, technical and one-liner levels (also obj.field-theory.single-algebra-field, second-quantisation,
   fock-space-maxwell-modes, elementary-photon-ga, orientation-relocated, modular-period, wedge-reflections,
   linear-rung, quartet, field-level BRST, the field-theory setting notes). The detector exempts "i =", so the unit
   pass left them. Decide whether the identification counts as a bare unit; if yes, the fix is mechanical ("with
   the unit $I_4$"; titles "Mass with the unit $I_4$", "The unit $I_4$ keeps its properties only in dimension
   0 mod 4"), a level change for each entity.
2. Duplicate clause: synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator... still states clause
   (vii) (no smooth weighting of the floors keeps a boost) with proof Step 8, although the decision of 2 November
   merged it into synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off as clause (v).
   Proposed: drop (vii) from the formal and one-liner (keep a pointer "merged into ... (v)") and the proof's Step 8;
   a formal-level change.
3. Duplicate result: interior.gauge-trajectory-unipotent-ray (T06) clauses (1)-(2) are singularity.unipotent-ray,
   (3) the metric of sheaf.gauge-field-cometric and note.singularity.setting-metric-gauge-field-static-form, (4)
   singularity.cones-fold; it recomputes them and has no uses edge to singularity.unipotent-ray or
   singularity.cones-fold. Keeper: singularity.unipotent-ray and singularity.cones-fold (the originals); the T06
   entity adds only the group law. Proposed: uses edges singularity.unipotent-ray@4 and singularity.cones-fold@4
   (restatement), keeping the group law as its own content.
4. Duplicate import: field-theory.imported-standard-field-theory lists the Adler-Bell-Jackiw anomaly among its six
   imports by name only; synthesis.imported-adler-bell-jackiw-axial-anomaly imports it with checked citations.
   Proposed: a marked note in the former pointing to the latter (no edge change needed).
5. singularity.non-removability-invariant-argument: (a) the formal says $K$ "is invariant under every gauge
   transformation", but the technical level and proof say displacements pull it back (it is a scalar, not an
   invariant function); proposed wording "a scalar: unchanged by rotation-gauge transformations and carried along by
   displacements, so its unbounded range near $r = 0$ survives every gauge choice". (b) $K := R_{abcd}R^{abcd}$ is
   tensor notation in a non-GA-owned entity; the GA form is $K = 4\sum$ of the squared eigenvalues of
   $\mathcal{R}$ over the six frame planes (as the proof computes); a level change.
6. Notation clash in T05 setting notes: note.singularity.setting-machine-verification ("the radial curvature
   $\mathcal{R} = (\beta\beta')'\sigma_r$") and note.singularity.setting-introduction (table, "$R(B) = -\tfrac{M}{r^3}S(B)$")
   use the script letter or $R$ for curvatures in two signs, as dictionary C5 notes for the gauge-theory setting
   note. These are verbatim paper text; a reading sentence like the one added to the two claims would resolve it.
7. field-theory.mass formal and technical: "the epsilon pairing $\lambda^{\mathsf T}\epsilon\lambda$" is a
   two-component matrix reading beside $B_N$; label it as a reading ("in two-component form") or drop it.
8. Kasner and radical-normal walls (GA-owned) mix (-,+,+,+) metrics with the store's (+,-,-,-) algebra; sent to
   the rewriters (ga-issues-R06.md 1-2). If the rewriters do not restate them, Leon's dictionary C7 rule needs a
   signature declaration in each.

## Duplicates

- floor-regulator (v) and regulator-free (vii): same statement; keep floor-regulator (proof and check there).
- singularity.unipotent-ray / singularity.cones-fold and interior.gauge-trajectory-unipotent-ray: see For Leon 3.
- Adler-Bell-Jackiw in two imports: see For Leon 4.
- Restatements already marked as such (no action): field-theory.imported-tower-limit, imported-one-datum-massive-law,
  imported-statistics-no-go-palatial-algebra, sheaf.gauge-field-cometric, singularity.imported-one-sided-completion-singularity.

## Known open items

None of the six listed open items is an entity of R06. Bearing on two of them (details in xsubject-R06.md): the
Hadamard regulator (the parametrix import gives $-\epsilon^2/2$ in $\sigma$ units, $+\epsilon^2$ in the source's $s$
units, computed), and the sign of $I_6$ on $\CS$ (the field-theory convention: $I_6 = +I_4$ on the $E = +1$ doublet,
$J = R_{I_6} = +I_4$ on $\ker n_0$ in $T$).

## Other checks made (no defect)

Recomputed by hand or GA.py: unit-i4 parity table and $2^{D-2}$ count; chiral counterterm sums $\tfrac{10}{3}$,
$\tfrac{95}{54}$, $-\tfrac59$, $\tfrac{95}{648}$; deposit moments ($\tfrac1{30}$, $\tfrac1{20}$, $\tfrac15$, $c = \tfrac83$,
$16\pi(k+2)!T^{k+3}$); LSZ beta coefficients and $Z_3$; one-loop QED clause (5) $-N + 8m^2$; e+e- threshold and
absorptive part; floor commutant and filled-sea central term; locality bracket factor; Kasner $E_1$, $E_2$;
running coefficients and asymptotic-freedom bounds; quartet counts (27, 48, 75, sector sizes); Gribov $c(\kappa)$,
$M\widetilde M = \tfrac{64}{25}$; regulator-free $T(s^{-2})$, $T(1/s)$, $\mu\partial_\mu$; quasi-spin gap $Gn_b$, 63 and
46 GeV; triangle $1/(2\pi^2)$; Gildener-Weinberg $V'''$; linear-rung 542 and 383 GeV; spin-product slab limit
$\tfrac15$; wedge identities; one-sided completion and the global-coupling determinant $m^2$; scheme-robustness
constants; Schwarzschild Gram, radical and $g_k = -r$.

## Counts

Entities read: 143 (claims 99, about 30 of them imports or restating Facts; notes 42; objects 2). Fixed in place: 10 (9 claims, 1 note), all
with version + 1. For Leon: 8. Duplicates: 3 (plus 5 marked restatements). GA issues sent: 8 (ga-issues-R06.md).
Cross-subject: 4 (xsubject-R06.md). tp check runs used: 1.
