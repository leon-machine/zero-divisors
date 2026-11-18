# Findings, cluster H (heating, couplings, scrambling), run 2026-11-18-leads

One attacker, both angles. Work files: colony/runs/2026-11-18-leads/work/H/. Labels: proved / computed / argued /
conjectured. The floor's entities are being restated by another agent in this run (energy per creation event);
every floor figure quoted below is the stored one at the time of reading (convention 3T per event) and is quoted,
not corrected. Quantities that count quanta (yields, the Pati-Salam and untuned-fit thresholds) do not depend on
that restatement.

## Kill conditions (written before the computations they govern)

Candour note: before writing these I had read the stored formula of clause (v) and done a rough mental estimate of
the tau-term for the mirror (it is 80/225 of about 316 at tau = 1, and near 5 times the rest at tau near 67). The
registrations below were written after that estimate and before any exact computation or any script.

### Lead 1 (curvature coupling in the heating)
- K1a. The tau-dependence of the scalar channel is recomputed by a route independent of the stored check
  (the helicity decomposition of lead 2, and a direct evaluation in the algebra with two different couplings
  xi_1, xi_2 at exact angles). KILL: if the weight of scalars to scalars is not (pi/180)(1 + 5 tau_1 tau_2) for
  unequal couplings, the stored clause (iv) is wrong off the diagonal and the lead stops at that report.
- K1b. Claim under test: "at the stored readings of the couplings (0 for the doublets, 1/6 for an attachment
  module) no stored conclusion that uses the rate moves by more than its stated margin". KILL: if at xi = 0 or
  xi = 1/6, for the bath's scalars or the produced scalars or both, any of (the mirror's floor at two figures, the
  Pati-Salam margins 2.2 and 1.5, the untuned fit's 1400-fold and 1100-fold, c <= 1 for one Standard-Model
  content) changes in a stated figure.
- K1c. Claim under test: "with the tilt window's coupling on the doublets (the one-field reading, which the store
  excludes on other grounds) a stored conclusion is lost". Test: the Pati-Salam clause (i) needs c < c* = 13.49
  for four Standard-Model contents. KILL (of the claim): if c stays below c* over the whole window
  [1.5225, 1.5481]. If c crosses c* inside the window, say where; if c is above c* over the whole window, say so.
- K1d. Claim under test: "the heating constrains the open datum" (the identity of the tilt fit's scalar, or the
  doublets' coupling beyond tree level). It counts as a constraint only if a stored observable bound (the dark
  radiation threshold of pred.no-dark-radiation, or an exclusion that the store asserts) excludes a value among
  the stored candidates 0, 1/6, the tilt window. KILL: if the interval of xi allowed by every stored bound that
  uses the rate contains all three, the heating does not constrain the datum and that is the result.

### Lead 2 (trace part of the fermion channel)
- K2a. Claim: the source of a particle and antiparticle of one massless chiral fermion has rotation weight
  plus or minus one about the pair's axis and no weight-zero part, so it is trace-free by a selection rule and
  not by the tree-level form of the stress. KILL: if the source computed in the algebra has a component of
  weight zero (then a trace at next order is not excluded and has to be computed).
- K2b. Claim: the spin-two norms of the three pair sources, through one orthogonality relation on the
  five-dimensional trace-free space, give the stored weights c = 1, 3, 12 with no angular integration. KILL: if
  12 x (identical-quanta factor) x (summed norm)/s^2 is not (1, 3, 12), the helicity account and the stored
  computation disagree and one of them is wrong.
- K2c. Claim: a term in the first-order field equation built from the scalar curvature (the form the stored
  anomaly statement takes at first order in the field) changes the interaction of two conserved sources only by
  a factor on the product of their traces. KILL: if the exact solution of the modified equation at a non-null
  momentum changes the bilinear on a pair one of whose sources is trace-free.

### Lead 3 (scrambling)
- K3a. Claim: the spreading half of the spreading law is proved by synthesis.affine-cell-boost-spreads-without-
  scrambling. KILL: if (a) that result's past cone contains the spreading law (circular), or (b) its clause (i)
  is not the statement t = kappa^{-1} ln N for the object the law names, or (c) the law's own growth step
  (amplitude e^{kappa t} against a suppression 1/N under a generic quadratic coupling) is a different mechanism
  from the proved one in a way that changes the statement and not only the scope. Each of (a), (b), (c) is
  answered separately; (b) or (c) firing means the correction restates the law, with the unproved part named.
- K3b. Claim: the return delay has no proved core beyond the first. KILL: if a stored proved result gives the
  doubling count or the round structure, then part of the second can also be restated as proved.

## Outcomes of the kill conditions
- K1a: not fired. Scalars to scalars at seven pairs of unequal couplings, by direct evaluation in the algebra and
  exact integration: (pi/180)(1 + 5 tau_1 tau_2) each time (work/H/lead1.py). Second route (lead 2): the weight
  is 4 sigma sigma (N N/5 + theta theta/36)/s^4 from one norm and one trace per source.
- K1b: not fired. At 0 or 1/6 on either side the mirror's coefficient changes by 5120/4557741 = 0.112 percent
  (0.56793 to 0.56729), the floor by 0.028 percent; no stated figure moves.
- K1c: fired in part. With the tilt coupling on the four real scalars of the bath and of each copy, four
  Standard-Model contents have c from 13.448 to 14.313 over the window, against the stored c* = 13.4949 (inputs
  at their weakening ends): the inequality reverses at xi = 1.52399, 5.5 percent of the way into the window. At
  central inputs c* = 14.44 and c stays below it (margins 1.018 to 1.002). So the stored margin 1.5 is used up
  and the clause is not decided over the window; "lost" would overstate it.
- K1d: fired. Every stored bound that uses the rate allows 0, 1/6 and the tilt window alike on the Standard
  Model's four scalars; a visible radiation value at the floor would need |1 - 6 xi| above about 1500. The
  heating does not constrain the open datum.
- Not registered, found while answering "which scalar of the bath": the stored coefficients take the bath to be
  the Standard Model's content (4, 45, 12), which the stored texts say. On the chain under (S) the content
  between M_I and M_U is (64, 68 or 188; 48; 21), and both the ceiling 6e14 GeV and the seeding temperatures of
  the Pati-Salam clause (i) (above 5e11 GeV) lie in that interval. See lead 1 below; this is where a stored
  margin does move.
- K2a: not fired. The chiral pair's two real source components satisfy L T_1 = T_2, L T_2 = -T_1 under the
  rotation generator about the pair's axis: weight one only, trace-free, orthogonal to the trace line.
- K2b: not fired. Norms s^2/6, s^2/4, 2 s^2; 12 sigma N/s^2 = 1, 3, 12. Found on the way: the two vector
  combinations of weight zero (equal helicities) carry no source at all, so the vector pair is weight two only.
- K2c: not fired. With mu ((a.k) k - Q a) R[h] in the field equation the bilinear is
  <T1_tf, T2_tf> - tr T1 tr T2/(6 (1 + 3 mu Q)); unchanged when one source is trace-free (four values of mu).
- K3a: (a) not fired: the past cone of the affine-cell result (74 entities) does not contain the spreading law,
  nor do the cones of the phase-flow, one-unitary-group and (N+)-to-(R) results. (b) fired: clause (i) is about
  affine cells of one horizon generator, not the window's counted modes; and only the cell at the edge covers
  "the first N cells". (c) fired: the law's growth step is the rotor flow's (stored, phase-flow theorem), and
  under (L_E) has no real-time reading (stored, number-diagonal theorem); the proved real-time count has
  amplitudes falling as e^(-kappa t/2). So the correction restates the law; it does not only change its status.
- K3b: fired in a narrow sense: the doubling count has a proved reading (m = 2 in clause (i) of the affine-cell
  result: n doublings cover 2^n cells, each lasting kappa^-1 ln 2, so kappa^-1 ln N exactly). The delay as a
  statement about the return of information has no proved core.

## Lead 1. The curvature coupling in the heating

Routes considered. (1) The problem's own: put the stored values of xi into clause (v) of the rate theorem and
follow each stored user of the rate. (2) From another subject: the Sakharov coefficient's scalar count (eight
real components on the content, 64 to 188 on the chain above M_I) against the heating's bath (four), that is,
ask which scalars are in the bath before asking their couplings. (3) Own: decompose the pair sources by
rotation weight (lead 2), which gives the tau-dependence without integration and says which species can carry
a trace at all. Chosen: (1) for the registered claims, checked by (3); (2) because (1) came out null on the
Standard Model's scalars and the lead asks which scalar is which.

Established.
- proved (summation of clause (v); the unequal-coupling weight verified directly): the summed coefficient of a
  produced content D from a bath is (pi^3/17280)[(C_D (N_s + 12 N_v) + 5 tau_D tau_B)/225 + 49 C_D N_w/4800],
  C_D = n_s + 3 n_w + 12 n_v. Couplings enter only through tau_D tau_B. Vectors' and fermions' coefficients
  see no coupling (so the nine-vector and 22-vector figures are independent of the datum).
- computed, Standard Model's bath (4, 45, 12), a copy as content:
  | case | c | ratio | c^(1/4) ratio |
  |---|---|---|---|
  | stored reading, all doublets at 0 | 0.567928 | 1 | 1 |
  | either side or both at 1/6 | 0.567290 | 0.998877 (lower by 5120/4557741) | 0.99972 |
  | tilt window on bath and copy | 3.362 to 3.578 | 5.920 to 6.301 | 1.560 to 1.584 |
  | tilt window on the bath only | 0.6095 to 0.6111 | 1.073 to 1.076 | 1.018 |
  | one more real scalar at the tilt coupling, bath only | 0.5807 to 0.5811 | 1.023 | |
  | the same in bath and copy | 0.768 to 0.782 | 1.352 to 1.377 | 1.078 to 1.083 |
  One produced real scalar: 2.1641e-3 at 0, 2.0046e-3 conformal (0.926), 1.256e-2 to 1.296e-2 at the tilt
  coupling (5.80 to 5.99; about half a vector's 2.4055e-2).
- computed, which stored conclusion moves on the Standard Model's four scalars: none at 0 or 1/6. At the tilt
  window on all doublets: the Pati-Salam clause (i) at four contents (c* = 13.4949) is reached at xi = 1.52399
  (c = 13.448 at the window's lower end, 14.313 at its upper end); at central inputs c* = 14.44 is not
  reached. The clause at the odd towers' 22 vectors does not depend on the datum. The untuned fit's margin at
  four contents would go from 1145 to about 730-fold: no change of conclusion. The floors would rise by 1.56
  to 1.58, and the crossover eta' = 1 that the floors' entity places at c between 1.539 and 1.54 (being
  restated; quoted) would be passed for |1 - 6 xi| above 6.25, xi above 1.208 or below -0.875: so at the tilt
  coupling the mirror at its floor would no longer be charge-dominated. All of this is on the one-field
  reading that the stored result excludes on other grounds and that contradicts the stored tree-level value.
- argued, which coupling is whose: the heating's scalars are fields of the content with an action; the stored
  reading for them is 0, which is what the stored coefficients assume. The conformal value belongs to the
  attachment's helicity-zero module. The tilt fit's scalar is no stored field. The heating does not constrain
  the open datum on the Standard Model's scalars (K1d): to bring the mirror's radiation at its floor to 0.01
  would need |1 - 6 xi| near 1600 on all doublets.
- computed, not registered, the bath on the chain. Stored content between M_I and M_U under (S): 21 vectors, 48
  Weyl fields, N_s = 64, 68 or 188 real scalars. The ceiling 6e14 GeV and the temperatures of the Pati-Salam
  clause (up to 5.34e11 GeV, 28 times the chain's two-loop M_I) lie in that interval.
  | N_s | per vector (ratio) | 22 vectors c, margin | four SM contents, margin | four copies of the chain's content: xi = 0 | conformal |
  |---|---|---|---|---|---|
  | 64 | 0.04079 (1.696) | 0.897, 1.969 | 3.889, 1.365 | 6.908, 1.182 | 6.255, 1.212 |
  | 68 | 0.04117 (1.712) | 0.906, 1.965 | 3.928, 1.362 | 7.106, 1.174 | 6.368, 1.207 |
  | 188 | 0.05266 (2.189) | 1.158, 1.847 | 5.087, 1.276 | 15.888, 0.960 | 10.251, 1.071 |
  Stored margins: 2.2 and 1.5. For N_s = 188 and one coupling for all scalars, four copies of the chain's
  content are below c* only for xi between 0.0215 and 0.3118: the clause fails at the tree-level value and
  holds at the conformal one. c* at N_s = 188 is 256 vector species or 10 Standard-Model contents (stored: 560
  and 23). With the chain's bath at the ceiling the floors of vector towers rise by 1.14 to 1.22, and a mirror
  that is a copy of the chain's content has c = 1.73 to 3.97 at xi = 0 (3.0 to 7.0 times the stored 0.568).
  Not computed: the mirror's floor, eta' and composition with that content (g_d and the energy per event
  change with it, and those entities are being restated).
- computed, the working branch's second doublet and the heavy neutrinos, for the record: bath and copy
  (8, 45, 12): c = 0.5870 (1.034, floor 1.008); with three right-handed neutrinos (8, 48, 12): 0.6216
  (1.095, floor 1.023); 22 vectors from those baths: 0.5376 and 0.5521 (1.016, 1.043). No stated figure of the
  Pati-Salam clause changes in its stated digits from these alone (margins 2.22 and 1.53).
Proposal: synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath (validate_draft ok,
check4 exit 0, no findings). Ledger: transport-absent.
Next step: restate synthesis.seeding-remainder-excludes-perturbative-pati-salam clause (i) with the chain's
bath (its margins and counts), a maintainer edit or a correction in a later run; decide the bath for the
floors' entities (see Decisions).

## Lead 2. The trace part of the fermion channel at next order

Routes. (1) The problem's own: take the stored anomaly statement (a term in the quantum trace proportional to
the d'Alembertian of the scalar curvature) and compute its contribution to the pair-to-pair amplitude.
(2) From another subject: the stored first-order theorem's decomposition of conserved sources into a trace
line and five trace-free components, with the rotation group at a timelike momentum; a selection rule.
(3) Own: test whether any term of the field equation built from the scalar curvature can reach a trace-free
source. Chosen: (2) and (3), because they answer the question for every order at once and (1) is a special
case of (3).

Established.
- proved: conserved sources at timelike k are a trace line (P_k) plus five trace-free components;
  B = <T1_tf, T2_tf> - tr T1 tr T2/6.
- proved (computed at one configuration, general by covariance): rotation weights about the pair's axis are 0
  for a scalar pair (norm s^2/6, trace (1 - 6 xi) s), 1 for a chiral fermion pair (norm s^2/4, trace-free),
  2 for a vector pair (norm 2 s^2, trace-free). The two vector combinations of weight zero carry no source.
- proved: the channel weights follow from these norms by one orthogonality relation (the rotation algebra has
  one line of invariants in the tensor square of the trace-free space; rank 24 of 25, exact):
  W = sigma sigma (4 pi/s^4)(N N/5 + theta theta/36) = (pi/180)(c c + 5 tau tau), c = 12 sigma N/s^2 = 1, 3, 12.
  This turns the stored clause (iv), computed at sampled angles, into a consequence; the two routes agree
  angle by angle for both relative helicities of fermion to fermion.
- proved: a source pair of nonzero weight is trace-free. So the fermion channel has no trace part for any
  conserved stress whose two-quantum element keeps weight one.
- proved: with mu ((a.k) k - Q a) R[h] in the field equation the bilinear becomes
  <T1_tf, T2_tf> - tr T1 tr T2/(6 (1 + 3 mu Q)); weights (pi/180)(c c + 5 tau tau/(1 + 3 mu s)^2).
- argued: the stored anomaly term is such a term (the trace of a free field's renormalised stress is
  state-independent, from memory; a conserved source built from the scalar curvature alone is a multiple of
  P_k R). So the correction to the chiral-fermion coefficient from the stored trace statement is zero. The
  first effect of that statement on the rate is on the scalars' trace term, relative size about 6 mu s, of
  order s/Mbar^2: third order in G in the rate (G^3 T^10), near 6e-8 times a small coefficient at the ceiling.
  The store uses the rate at order G^2 only.
- argued: where a trace could first arise for non-scalars: mixed pairs of opposite chirality through a Yukawa
  coupling, and equal-helicity vector pairs through <F1 F2>_0, both beyond tree level in the matter couplings.
  Not sized beyond that.
- not done: the common rescaling of every c_i c_j by the trace-free part of the vacuum's response, same order
  G^3; it is not a trace part.
Proposal: synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-forbid-a-fermion-trace
(validate_draft ok, check4 exit 0, no findings after one tightening of a weak check). Ledger: transport-absent.

## Lead 3. The two scrambling estimates

Routes. (1) The lead's own: restate the spreading law as proved on the scope of the stored affine-cell
theorem. (2) Adversarial: test whether that theorem is about the law's object and mechanism at all (K3a), and
read the stored phase-flow and number-diagonal theorems against the law's growth step. (3) Own: look for a
proved core of the return delay (K3b). Chosen: all three; (2) decided the form of (1).

Established.
- Is the spreading half proved by the stored synthesis result? In part. Proved there: on one generator of a
  Killing horizon, in the affine-cell basis, the boost in real time spreads one cell over N cells at
  t = kappa^-1 ln N, for every integer N, with amplitudes falling as N^(-1/2). Not the law's object: the law
  speaks of the window's N counted modes (on the stretched singularity, with N of the order of S), and only
  the cell at the edge covers "the first N cells". Not the law's mechanism: the law's growth e^(kappa t)
  against a suppression 1/N is the rotor flow's (a count in rapidity), by the stored phase-flow theorem, and
  under (L_E) has no real-time reading on the windows, by the stored number-diagonal theorem.
- What remains an estimate: (e1) the identification of the window's modes with affine cells (the count is
  absent on boost-adapted cells); (e2) N of the order of S (the area-law proposition gives equality only with
  the calibration nu Delta t = M/2); (e3) that covering cells is scrambling (Lyapunov exponent 0, stored).
- The correction is filed as a restatement of scrambling.spreading-law-chaos-bound-saturated, version 6 -> 7,
  status conjectured -> proved, with clauses (a) real-time count on a generator, (b) count in rapidity on the
  ladder, (c) the rate under (N+), (d) chaos bound met and not saturated, each proved from stored results, and
  (e) the three unproved steps, named as an estimate inside the statement. Every stored file is kept; the
  proof file now holds a proof; one check function is added; no circularity (cones checked).
- The return delay, scrambling.return-delay-scrambling-log-recovered: no proved core as a statement about the
  return of information. Its arithmetic has a proved reading (n doublings of the affine-cell flow cover 2^n
  cells, kappa^-1 ln N exactly, with no ln 2 to absorb), which belongs to the first entity's clause (a). It
  stays conjectured. It cites the spreading law at version 6 and has to be read against version 7 before its
  pin moves: its sentence "the first-principles account of the spreading exponent is Assembly ..." is then
  true of clause (b) only, which its own text already says (modular time).
- Which open problem should hold the second: op.island-dictionary (area entropy), the problem on how
  information returns (eviction against the island). The return delay is the timing half of that question:
  attack item to add, "derive the delay between deposit and eviction from the eviction theorem's window, in
  Killing time or in rapidity, and compare it with 4M ln S". If Leon prefers a separate home, the settled
  problem on the two boost flows lists "chaotic (non-quadratic) dynamics of the windows" as not covered, and
  a new problem with that title would hold both the delay and clause (e) of the restated law.
Proposal: scrambling.spreading-law-chaos-bound-saturated (correction, version 7; validate_draft ok, check4
exit 0, see the last lines of this file for its warnings). Ledger: transport-absent.

## Unexpected links
- To the energy restatement (MAINTAINER-energy): the mean energy per event depends on the trace weights through
  the Bose part of the rate; its stated bounds 7.66 < E/T < 8.22 hold for every coupling, but the quoted
  7.889 T is for couplings 0 and for the Standard Model's bath. With the chain's bath the Bose share rises
  (the Fermi part is 49 C N_w/4800 with N_w = 48 against a Bose part (N_s + 252)/225 per unit of C), so E/T
  moves toward 7.66. The crossover eta' = 1 "at c between 1.539 and 1.54" in the floors' check is exceeded by
  a mirror that copies the chain's content (c = 1.73 to 3.97), though g_d changes too.
- To cluster G (the field at null momentum, the trace-free channel of op.einstein-from-the-field-theory): the
  decomposition of lead 2 is the timelike-momentum companion of the stored null-momentum statement. At
  timelike k the stabiliser is the rotation group, the six conserved sources are 1 + 5, and pair sources have
  weights 0, 1, 2. Vector pairs of equal helicity carry no first-order source at all; the weight-two pair is
  the only one that would survive a limit to null momentum as the two transverse trace-free directions N_p of
  the stored theorem. A scalar-curvature term in the field equation, which is what the stored anomaly remark
  amounts to at first order, never touches the trace-free channel.
- To the Sakharov results of op.curvature-coupling-across-subjects: the induced coefficient counts the chain's
  scalars above M_I with weights (1 - 6 xi) and says "nothing in the store fixes these couplings"; the heating
  counts the same scalars with weights (1 - 6 xi)^2. At N_s = 188 the two readings pull in opposite senses
  for the stored conclusions: minimal coupling gives B = 152 > 0 (the matching to Newton's constant possible)
  and lets four copies of the chain's content exceed c*; conformal coupling gives B = -36 and keeps the
  exclusion. This is a second place where the chain's scalar couplings are a stored undetermined input.
- To the housekeeping row on the two scrambling estimates (row 6 of the survey): answered by lead 3.

## Decisions for Leon
1. Status of scrambling.spreading-law-chaos-bound-saturated: accept the restatement as proved on clauses (a)
   to (d) with (e) named as an estimate, or keep it conjectured and add only the scope. The case for proved:
   every clause (a) to (d) is a stored theorem or an identity checked exactly, and the unproved window reading
   is no longer asserted. The case against: the entity's title and place (the scrambling paper's Assembly)
   suggest the window law, which is not proved; a reader may take "proved" for more than it covers.
2. Home of the return delay: op.island-dictionary with one new attack item (recommended), or a new problem on
   chaotic dynamics of the windows.
3. The bath of the dark-matter results. They state the Standard Model's content. On the chain under (S) the
   content at the ceiling and at the Pati-Salam clause's temperatures is (N_s, 48, 21). Options: (a) keep the
   Standard Model's bath as a stated hypothesis and add a clause giving the chain's figures (the filed result
   supplies them); (b) restate clause (i) of the Pati-Salam exclusion with the chain's bath, since that
   clause is on the chain (margins above 1.84 and 1.27 at N_s = 188, counts 256 and 10); (c) also restate
   the floors with the chain's bath where (S) is assumed. Recommended: (b) now, (a) for the floors until the
   content above M_I is settled, since the dark-matter subject does not assume (S).
4. Whether a tower "with the mirror's content" at temperatures above M_I means a copy of the Standard Model's
   content (as stored) or of the chain's content. On the second reading the Pati-Salam exclusion at four such
   towers depends on the curvature couplings of the chain's scalars and fails at the tree-level value 0.
5. The curvature couplings of the chain's scalars (bidoublet, (10,1,3), (15,2,2)): the store fixes none. If
   the tree-level reading 0 decided for the doublets on 9 November is meant to extend to them, say so; it now
   has a consequence (item 4).

## Gate results
- synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-forbid-a-fermion-trace: validate_draft
  ok; check4 exit 0, first run one warning W413 (5 of 8 perturbations of one function passed), tightened with
  pinned values, second run 0 findings.
- synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath: validate_draft ok; check4
  exit 0, 0 findings.
- scrambling.spreading-law-chaos-bound-saturated (version 7): validate_draft ok (replaces existing); check4
  exit 0; see below.
  First run: three warnings W405 (premises declared and not touched by a check); they are premises of
  structural statements and of the unproved clause, now excused with reasons in coverage.yaml. Second run:
  exit 0, no errors and no warnings (three I405 notes for the excused premises and the note on the legacy
  script, which passes).
- Process note: twice a gate process of another agent was running when one of mine started (once check4, once
  validate_draft); the check for running processes came out as "1" and I did not wait. No process was killed.

## Files
- work/H/lead1.py, lead1b.py: the coefficient tables of lead 1 (exact rationals, floats for display only).
- work/H/P1, P2, P3: sources of the three proposals (the filed copies are under proposals/).
- work/H/dbg/run.py: a helper that turns `ok = ok and ...` lines into assertions to locate a failing line.

## Fix round (after the referee's report R-A)

### A1, heating coefficients: clause (iii) was wrong; recomputed; conclusion reversed
The referee's point: I changed the bath to the chain's content in the coefficient c and left the threshold
c* = 13.4949 at the Standard Model's bath. Verified against the store before changing anything: the stored
yield is Y = c T^3/(3 kappa_s M_P^3), kappa_s = sqrt(pi^2 g_*/90)(2 pi^2/45) g_s, 145.3 at g = 100
(dark-matter.seeding-gravity-floor-dark-towers-temperature, formal), and the stored Pati-Salam check builds
c* = A/(2 M_3^4) with A = 3 kappa_s M_P^3 (...). So c* goes as g^(3/2) of the same bath. The referee is right
and I did not see it. Recomputed (work/H/lead1c.py), bath (188, 48, 21), g = 314, c* = 75.09:

| quantity | first filing (threshold left at g = 100) | corrected |
|---|---|---|
| margin, 22 vectors (c = 1.158) | 1.84 | 2.837 |
| margin, four Standard-Model contents (c = 5.087) | 1.27 | 1.960 |
| c* in vector species / Standard-Model contents | 256 / 10 | 1425 / 59 |
| four copies of the chain's content, xi = 0 (c = 15.89) | 0.96, "fails" | 1.474, holds |
| the same, xi = 1/6 (c = 10.25) | 1.07 | 1.645 |
| interval of one coupling with c < c* | (0.0215, 0.3118) | (-0.1403, 0.4736) |

These agree with the referee's table. For N_s = 64 and 68 (g = 190, 194; chains without the (15,2,2), not the
clause's): margins 2.505 and 2.519 at 22 vectors, 1.736 and 1.746 at four Standard-Model contents, 1.504 and
1.505 for chain copies at xi = 0. Conclusions reversed: on the chain the stored margins rise (2.2 -> 2.83,
1.5 -> 1.95), they do not fall; the stored clause is conservative there; the curvature couplings of the
chain's scalars decide nothing at either stored reading. The following earlier lines of this file are
superseded and wrong as conclusions: the last column pair of the chain table under lead 1 and its sentence
"the clause fails at the tree-level value and holds at the conformal one"; the counts 256 and 10; the third
"Unexpected link" (the two readings "pull in opposite senses"); "Decisions for Leon" items 3 to 5 in the form
given (see below); and the remark in the first link that a mirror copying the chain's content exceeds the
crossover eta' = 1 (the yield at fixed c falls by 5.56 with the chain's bath, so that comparison needs
c g^(-3/2), not c). Also to be read with the same correction: the working-branch figures (bath (8, 45, 12) or
(8, 48, 12)) raise c* by 6 and 14 percent as well as c, so the margins are 2.27 and 1.57, and 2.30 and 1.58,
not 2.22 and 1.53; still no stated figure changes. Floors with the chain's bath: a vector tower's floor goes
as (c g^(-1/2))^(1/4), 1.054 times the stored one at N_s = 188, not 1.22.
What changed in the proposal: clause (iii) rewritten for N_s = 188 only, with the bath in both places; the
Reading's last paragraph replaced; technical, lay, one-liner and the extraction note rewritten; the check's
fourth function replaced (it now tests margins in eighth powers against c*(100)^2 (g/100)^3 and keeps the old
figures 1.84 and 1.27 as the inconsistent case); "the least of the stored unification scales" corrected to
8.9e14 GeV (two-loop table), with 3.4e16 for the clause's chain; the four-copies case labelled as this
result's construction; "increases with" replaced by "does not decrease"; the assignment of the tree-level
reading made even (stored only for the rung field's doublets; the bath's four scalars are such a doublet;
the copies' and the chain's scalars are not fixed by a stored statement). Title and id still describe the
result. Nothing declined.

### A2, rotation weights: all fixes applied
Clause (v) is worded as the elementary conditional it is (the trace is rotation invariant; all content is in
the hypothesis that the two-quantum element is a pair of weight one; the tree-level source satisfies it; the
interacting case is not proved). The sentence "zero, at the next order in G as well" is replaced: the part of
the correction that comes from the stored trace statement is zero; the fermion coefficient does change at
order G^3 through the trace-free vacuum response, not computed. "No order in couplings" is marked as resting
on the helicity of the state, not on (v). The anomaly remark is cited where it is stored, clause (v) of the
Weyl-flat theorem, and the note says that theorem already argues the classical decoupling. Title changed to
"Rotation weights of pair sources: the channel weights, and no trace at nonzero weight"; the id's slug
("...-forbid-a-fermion-trace") no longer matches and is the orchestrator's to rename. Nothing declined.

### A3, spreading law: status kept conjectured, as recommended
Agreed with the referee: clauses (a) to (d) are stored theorems, and "proved" on the id that the paper's
Assembly points to would be read as a proof of the window law. Version 7 is now a restatement with status
conjectured: every level says the entity records the paper's estimate together with the proved statements it
rests on, each cited as a stored theorem; clause (e) is the estimate; no proof is attached (the derivation
carries a note, proof-main.tex is a record of where each cited statement is proved). The orientation in (a)
is corrected: the lapse kappa^-1 ln N is "in the direction of time in which the flow dilates the affine
parameter", with the opposite sign conventions of the affine-cell and one-unitary-group theorems named as a
difference between the two stored theorems. The added check stays, described as restating stored clauses in
the affine-cell theorem's convention. Decision 1 for Leon is withdrawn (no status change is proposed).
Nothing declined.

### Decisions for Leon, as they now stand
1. (withdrawn) The spreading law's status stays conjectured.
2. Home of the return delay: op.island-dictionary with one attack item (recommended), or a new problem on
   chaotic dynamics of the windows. Unchanged.
3. The bath of the dark-matter results on the chain: a matter of scope wording, not of conclusions. The stored
   Pati-Salam clause is conservative with the Standard Model's bath; its text could say so, and the floors'
   scope sentence could say that the bath (in c and in g) is the Standard Model's.
4, 5. (withdrawn as decisions) The copies' content and the chain's scalar couplings decide no stored
   conclusion; they remain undetermined inputs of the Sakharov results only.

### Checks after the fixes (runcheck only; no check4, no validate_draft in this round)
All four functions pass in each of the three proposals.
