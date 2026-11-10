# bridges: run 2026-11-10-phase1 (bridge-hunter)

Read: attack-KA.md and attack-KB.md (complete), attack-EA.md (E1 filed, E2 to E4 in progress), attack-EB.md
(pre-registration only in the file; EA's midway note reports EB's two filed proposals). Store entities read directly
under store/. Scratch: work/bridge/window_entropy_check.py (60-digit decimals, a recomputation, not evidence for the
store). Labels: stored / computed / argued.

## Job 1. KB's "unexpected link 1" (array (1/2) ln 2 against continuum pi/6)

### Verdict
Not a contradiction between stored claims, and not already recorded. It is a real, unrecorded LIMIT OF SCOPE of the
adopted window reading: the two numbers are entropies of two different objects, and the store never equates them,
but the same pair of objects is the pair the window reading equates for energy, and nothing in the store says that
the identification stops at the mean energy. KB's arithmetic is right. KB's consequence ("3/(4 pi) units per Planck
area in place of 1/(4 ln 2)") follows only from an extension of the reading to entropy that no stored entity makes.
So: no kill condition is met; a scope sentence and one attack item are missing.

### (a) Does the store already state or resolve it? No, but it holds every piece.
- stored: synthesis.window-reading-array-killing-energy is worded for energy only. Formal: the array "is read as one
  chiral complex component of the continuum of that light ray on a window", "and its Killing energy, in every state,
  is the Killing energy of the continuum over that window"; the cost paragraph says it applies the discretisation
  reading "to energy" and that it "identifies the spectrum of an array, of spacing kappa, with a twisted
  identification of real Killing time over one window, which the continuum does not supply". Its three refutation
  conditions are all about energy, offset and the mass ledger. Entropy is not mentioned.
- stored: the counted entropy is the array's own Gibbs entropy under (Q) version 3:
  synthesis.half-integer-weight-array-carries-half-ln2 (i), S = sum_k s(2 pi (k + 1/2)) = (1/2) ln 2;
  synthesis.counted-unit-energy-at-half-offset (ii), one unit of two arrays has Z = 2, E = 0, S = ln 2 in the
  symmetric ordering. synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping and
  scrambling.residue-each-convention use that entropy and no other. The two-array unit does NOT resolve the
  comparison: two arrays give ln 2, two continuum components give pi/3, the ratio is unchanged.
- stored: the continuum has no window entropy to compare with.
  synthesis.clausius-is-window-first-law-plus-boost-charge-conservation: "h has purely continuous spectrum, so the
  continuum carrier has no Gibbs windows", and the first law there is the relative-entropy form "on the type III
  algebra of the half-generator" (entropy differences only). synthesis.positive-null-energy-gives-r-premises (iv):
  the boost has no eigenvectors on the continuum and the ladder values are recovered "only for modes of vanishing
  Mellin width". hawking.i-state-continuum has no entropy statement at all (0 occurrences of the word).
- stored, and the nearest thing to KB's number: synthesis.counted-unit-energy-at-half-offset (iii) records
  E/(TS) = pi/(6 ln 2) per counted unit (beta E = pi/6 above the sea, S = ln 2). KB's ratio pi/(3 ln 2) is exactly
  twice this, because the extensive continuum has S = 2 beta E (beta E = pi/12, S = pi/6 per component) while the
  array has beta E = pi/12 and S = (1/2) ln 2. So the stored number already encodes the mismatch; it is read there
  as "below one, as clause (v) requires", never as a comparison with the continuum.
- Text search (find by grep over entity.md, proofs and yaml for pi/6 as an entropy, entropy density, window with
  entropy): no entity states the continuum's entropy per window or compares it with (1/2) ln 2. Not an audit of the
  full cone.

### (b) Same object or different objects? Different.
- Array: CAR algebra over l^2(Z), weights kappa(k + 1/2), Gibbs state at beta = 2 pi/kappa. Type I. It is a chiral
  complex fermion on a circle of Killing time of length L = 2 pi/kappa with the antiperiodic condition, at L = beta:
  the square torus (stored remark in counted-unit-energy-at-half-offset: "the self-dual point", recurrence period
  equal to thermal period).
- Continuum: CAR algebra over the Mellin continuum of the half-generator in the I-state. Type III; no density
  matrix on a window. "pi/6" is the extensive coefficient: the mean entropy rate kappa/12 per unit Killing time per
  complex component, times the window length. It is not the von Neumann entropy of any state on any window
  algebra. (From memory, classical: the entropy of an interval of length L of a chiral component, vacuum
  subtracted, is (c/6) ln(sinh(pi L T)/(pi L T)), which at L T = 1, c = 1 is about 0.217, a third number.)
- Why energy agrees and entropy does not (computed): in the symmetric ordering ln Z of the circle at ratio
  r = L/beta is pi r/12 + ln prod_k (1 + e^{-2 pi r (k + 1/2)})^2 (modular S-invariance, the stored imported theta
  identities). The first term is the continuum's extensive value, the second the dual-channel correction. The
  energy is the beta-derivative, which vanishes at the fixed point r = 1 whatever the corrections are; so the
  energy match of synthesis.null-ordering-of-counted-units-is-zeta-symmetric is a fixed-point identity, not
  extensivity. The entropy at r = 1 is ln Z itself, (1/2) ln 2, and the correction is of order one:
  S_circle - pi r/6 = -0.1770 (r = 1), -0.0197 (r = 2), -8.1e-5 (r = 4), -5.9e-10 (r = 8). The array is the
  continuum's thermodynamics only for windows of many thermal lengths; the stored window is one.
- The mean energy is the only matched quantity (computed): free energy differs (array ln Z above the sea
  (1/2) ln 2 - pi/12 = 0.0848, continuum pi/12 = 0.2618); energy variance differs (stored: beta^2 Var(E) in
  (1.5964, 1.5965) per unit, 0.798 per array; continuum beta^2 Var(E) = pi/6 = 0.524 per component per window).

### (c) Is pi/6 the right continuum value? Yes, for one chiral COMPLEX component.
Own derivation: modes of one complex chiral component on a Killing-time length L have density L d omega/(2 pi) on
the whole real line of omega (holes below zero). With x = beta omega, S = (L/(2 pi beta)) Int s(x) dx,
s(x) = ln(1 + e^{-x}) + x/(e^{x} + 1). Int_0^inf ln(1 + e^{-x}) dx = Int_0^inf x/(e^{x} + 1) dx = pi^2/12, so
Int over the line = pi^2/3 and S = (pi/6)(L/beta) = (pi c/6) L T with c = 1.
- Window L = 2 pi/kappa, T = kappa/(2 pi): L T = 1 (NOT 1/(2 pi)). Complex chiral component (c = 1): pi/6.
- Majorana-Weyl (c = 1/2): pi/12. Both chiralities of a complex field: pi/3 (KB's "two-component unit").
- With L = 1/kappa (L T = 1/(2 pi)) one would get 1/12; that is not the stored window.
The stored energy density kappa^2/(48 pi) per complex component (null-ordering (i)) is (pi c/12) T^2 at c = 1, so
the store's "complex component" is c = 1 and pi/6 is the matching entropy. Recomputed array values (60 digits):
S = (1/2) ln 2, beta E = pi/12, to the precision carried. Exact reason for (1/2) ln 2: Z_sym = theta_3/eta at
tau = I_4, equal to sqrt 2, and E_sym = 0 there.

### What would decide it
1. A construction of the arrays out of the continuum modes of a light ray (already named in refutation condition (a)
   of the window reading, for energy): compute the entropy of the constructed object. If the counted object is the
   twisted circle, (1/2) ln 2 stands and the cost sentence of the reading ("which the continuum does not supply") is
   the whole content. If the counted object is the continuum per unit Killing time, the light rays per Planck area
   per period of the-residue-requires... (iii) change from 1/(2 c ln 2) to 3/(2 pi c) and the capacity convention of
   scrambling.residue-each-convention (units of ln 2 per fermionic mode) no longer applies, since a window of the
   continuum is not a finite set of modes.
2. Whether the area law's S is an absolute entropy or only its differences. The Clausius route
   (synthesis.einstein-equations-from-c-loc-and-clausius, clausius-is-window-first-law...) uses only differences,
   which both objects satisfy (first law); only the count uses the absolute value.
Decisions for Leon (suggested, maintainer-only): (i) a scope sentence on
synthesis.window-reading-array-killing-energy: the reading equates the mean Killing energy only; entropy, free
energy and energy variance of the array differ from the continuum's extensive window values ((1/2) ln 2 against
pi/6; 0.798 against pi/6); (ii) an attack item on op.residue-killing-weights: which object's entropy the count
compares with A/4. pred.boundary-mode-density's kill condition (a derivation of the residue from the boundary modes
returning another value) is not met: the continuum number is a reading, not a derivation, and returns no mode count.

## Links to relay

### L1. Horizon pair states are the E-cluster's two-party states, and their CHSH value is fixed by the weight
Entities: synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product (v);
singularity.eviction-window-thermal-product-radiation-entropy; singularity.q-joint-quasi-freeness-s-wave.
Attackers: EA, EB (and KA's unchecked "mode pairs across the horizon").
stored: clause (v) of the mode split already writes the cross-horizon pair in GA,
rho = (1/4)(1 + p_k p_k')(1 + r p_k) + cs (w_k w_k' + v_k' v_k), a pure even state, and reads the eviction theorem's
pairs as these. computed (by hand in the algebra, not run through GA.py; to be tested): w_k w_k' + v_k' v_k =
-(1/2)(e_k f_k' + f_k e_k') and e_k (e_k' p_k) = -f_k e_k', so with EA's parties (A: x e_1 + z p_1; B: x e_2 p_1 +
z p_2) the correlation matrix is diag(2cs, 1), cross terms zero by evenness, and the maximum CHSH value of the pair
is 2 sqrt(1 + 4 c^2 s^2) = 2 sqrt(2 - r^2), r = tanh(x/2). It is 2 sqrt 2 only at zero weight (the version 2
zero mode, the eviction theorem's maximally entangled idealisation); at (Q) version 3 every pair has |x| >= pi, so
the largest per-pair value is 2 sqrt(1 + sech^2(pi/2)) = 2.1530, and 2.0003 at the next weight. So the E setting
applies to the two sides of a window with the Klein twist and real coefficients, the state is even, and the
observables must mix parity (x e_1 is odd, z p_1 even): this is where EB's parity-even statement bites. With
parity-even observables and one mode per side the value is at most 2 (EB-1); EB's two-modes-per-party result is
the form a superselected observer on one side would need. Why relay: it gives E1 an exact stored state to evaluate
(a one-parameter family with rational r available), and it says the offset decision of 23 October lowers the
per-pair Bell value from 2 sqrt 2 to at most 2.153.

Added after the final re-read of attack-EB.md (11:32): EB has independently found half of this ("the stored
eviction pair state at equal weights is a CHSH-saturating state", and that the twisted one-mode split reaches its
value only through e1 and e2 p1, which the stored parity average sends to 0). What L1 adds is the weight
dependence. DISCREPANCY TO SETTLE: EB writes the value on the stored even pair state as 2(c + s) (14/5, 82/29,
478/169); my hand value for pair amplitudes c, s is 2 sqrt(1 + 4 c^2 s^2), the standard maximum for a pure
two-level pair (Horodecki criterion, from memory), which is SMALLER than 2(c + s) whenever c != s (at 3/5, 4/5:
2.772 against 2.8). The two agree at c = s. Either EB's c, s are not the pair's amplitudes (for example setting
angles, or a different normalisation of the directions), or one of the two is wrong; EB's check or a GA.py run of
the correlation matrix diag(2cs, 1) decides. The weight statement (value below 2 sqrt 2 at every nonzero weight,
tending to 2 as the weight grows) holds on either formula.

### L2. Monogamy: the stored note uses it in words only; E3 would give it numbers
Entities: note.singularity.monogamy-firewalls-small-corrections-theorem; singularity.what-event-returns-radiation.
Attackers: EA (E3), EB (E3 test).
stored: the note cites monogamy in the firewall sense ("at no stage does one quantum carry both entanglements")
with no inequality; its technical, lay and one-liner levels are "pending". No CHSH, Bell or Tsirelson statement
exists in the store (grep: the two notes naming monogamy are the only hits). argued: if E3's quadratic trade-off
w(C_AB)^2 + w(C_AC)^2 <= 8 is proved in the algebra, then for a window mode A with partner B in the pair state of
L1, any third party C (the early radiation, with a second Klein twist) has w(C_AC)^2 <= 8 - 4(2 - r^2) = 4 r^2,
that is |w(C_AC)| <= 2r < 2: the note's sentence becomes an exact statement with the stored weights. This needs
E3 to hold with two twists and with the party C possibly many modes; EB's kill test for E3 is the relevant check.
Not a result until E3 is. (Final re-read: EB argues that three parties with odd observables need nested twists,
B by Gamma_A and C by Gamma_A Gamma_B, which the stored twist theorem covers only for two parts; with even
observables and two modes each the ordinary proof applies. The horizon application needs the odd case for one
mode pair, or the even case with two modes per party, so it inherits that gap.)

### L3. The Klein twist element of an array is its one-window Killing flow
Entities: mode-split (ii) (uniqueness: K = +-Gamma_A);
synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays; (Q) version 3 ("the Killing
flow at one modular period is the parity automorphism").
Attackers: EB (role of the twist), KB (for the record on op.counted-mode-energy).
stored + argued: on a finite window an array's one-window flow is its grading Gamma, which is the element the Klein
twist multiplies the other party's generators by, and mode-split (ii) proves the twist is unique up to sign. Under
the window reading the one-window evolution of n arrays is e^{2 pi J n/24} Gamma, which is +-Gamma exactly when
12 | n (the stored test "with the grading's sign left free"). So "the other party's observables are its generators
carried once round the modular period of the first party" is a physical reading of the twist, and the stored
recurrence test is the condition for the evolution operator to be an admissible twist. Argued only: (ii) is for
finite l, and nothing in E needs it. Relay as a remark, not a lead for a proposal.

### L4. The Smarr rate is "one S per thermal time"; the label's ledger on Kerr
Entities: synthesis.counted-unit-energy-at-half-offset (iii) ("the Smarr relation reads beta M = 2 N ln 2");
op.counted-mode-energy (attack item 1); synthesis.hole-mass-is-ground-energy-label; KA's clause (v).
Attackers: KA, KB.
computed (one line from KA's identity and stored inputs): the count rate times ln 2 is T S, so K4's
8 pi nu (M - 2 Omega_H J) is N ln 2 = beta (M - 2 Omega_H J)/2, the Kerr form of the stored Schwarzschild sentence
beta M = 2 N ln 2. argued: under the window reading the counted units carry zero mean Killing energy and the label
carries all of M; on Kerr the same bookkeeping makes the label carry M with the co-rotating combination
M - 2 Omega_H J = 2 T S as what the count sees, so the label's energy function there is Smarr with its work term.
This bears on op.counted-mode-energy attack item 1 (label as a Smarr-Komar charge), not on Einstein's equations.
It stays argued while Kerr is outside (N+).

### L5. (SH) and the stored double-count warning
Entities: synthesis.c-loc-is-a-second-placement-of-the-count; synthesis.einstein-equations-from-c-loc-and-clausius.
Attacker: KA (proposal text), KB.
stored: the Clausius route needs only delta S = eta delta A with G_cl = 1/(4 eta), on a local patch, so it holds on
Kerr horizon patches with no new input; and the second-placement entity records that a horizon placement counted
in addition to the cutoff placement gives G_cl = 2G. KA's (SH) is eta = 2 pi nu rho_0 (KA says so). Relay: the
proposal should say that (SH) is the (Loc) placement written as a volume count, identified with it and not added
to the cutoff count, or the stored factor of two applies.

## Links rejected

- Smarr heat term against the Clausius route as a new bridge. Rejected. The Clausius relation of the store is
  about changes (delta Q of matter crossing a patch, delta S = eta delta A); the Smarr term 2 T S is the Euler
  integral of the first law by homogeneity and, in K4, a steady accrual rate at fixed area with no heat flux.
  They share eta and nothing else; "heat term" is a name. What survives is L4 and L5.
- Rational Kerr holes and the rational rotors (KB's link 3). A parametrisation, with one arithmetic coincidence
  worth a line and no more. computed: a/M and s/M are the sine and cosine of the rotor angle, t = a/r_+ the
  half-angle parameter of synthesis.the-sign-is-the-rotor-at-infinity; t -> 1/t exchanges r_+ and r_- (the inner
  horizon is the reciprocal parameter); Omega_H/kappa_+ = a/s is the tangent, so the generators wind a/s turns per
  modular period. Integer winding n needs 1 + n^2 a square, impossible for n >= 1: no rational Kerr hole has
  integer winding, and winding one is t = sqrt 2 - 1 = tan(pi/8), the same irrational that E2's Pell approximants
  approach. It is the one fact "the eighth turn is not a rational rotor" read twice. No stored entity uses
  Omega_H/kappa, the extremal hole is t = 1 (the quarter turn), not R_infinity, and nothing in E depends on Kerr.
  Not relayed as a lead.
- The Klein twist against the two-array unit's entropy. Rejected. stored: mode-split (v), "for even states the
  tensor product is the product in the algebra, with no twist"; thermal states of arrays are even, so
  (1/2) ln 2 + (1/2) ln 2 = ln 2 and every count in cluster K is blind to the twist. The twist matters only for
  parity-odd observables (L1).
- EB's two-modes-per-party result as a derivation of the two-array unit. Rejected. Two modes per party is what
  parity-even CHSH observables need; two arrays per unit is what the area law needs at (1/2) ln 2 per array. The
  first counts modes on one side of a cut, the second groups whole arrays (each infinitely many modes) on one
  light ray; the-residue-requires... (i) proves no premise fixes the grouping. A coincidence of the number two.
- The mode count per light ray against the CHSH setting (RUN.md's example). Nothing found beyond L1: the count
  uses entropies of even product states, the CHSH setting uses one pair and odd observables.
- The two-array unit as the resolution of Job 1. Rejected, see (a): the ratio pi/(3 ln 2) is per component.
- KA's "Euclidean volume, as in Rindler wedge entanglement at a cutoff". Not tested by lookup beyond L1 and
  Job 1 (c): the wedge's entropy in the store is relative-entropy differences on a type III algebra, which is
  the reason the continuum has no absolute number to set against the count.
