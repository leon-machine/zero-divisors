---
id: synthesis.hypothesis-u-readings-on-the-rung-coupling-line
kind: claim
version: 4
title: On one family structure the top reading of Hypothesis (U) holds at the pure-ten point and the bottom reading at M_I at no distinguished point
status: proved
region: synthesis
subject: neutrinos
tags: [hypothesis-u, mass-generation, neutrino-premises]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - standard-model.equal-weight-module@5
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.bidoublet-complex@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_species_entries
- kind: check
  ref: check.py::check_ratio_line_and_bottom_point
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.hyp-u-equal-rank-one-eigenvalues
  - standard-model.premise-ew-equal-weight
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Its up-type readings assume the c reading of the rung vector; under the c* reading adopted on 2026-10-23 they need recomputing (equal up-type and down-type entries from one coupling). Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  open_problem: pr.u-equal-rank-one
  note: Constructive route on pr.u-equal-rank-one. The result neither assumes (U) nor (EW); it locates both on the two-parameter line of rung couplings with one family structure. The numbers m_b = 1.3651 GeV and m_t = 92.45 GeV at the intermediate scale are the fit targets of T12's stored coupling sets (verify_T12.py, Part M, obs:anglefits). The two-structure case is treated in two companion proposals filed alongside, synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition ((EW) with independent family matrices) and synthesis.stored-fits-are-models-of-not-u (the stored coupling sets); it is not claimed here.
---

## formal
Under Hypothesis (S), let the rung coupling be $c = a\,v_{4} + a'\,T^{u}_{\mathrm{GJ}} + b\,w_{4} + b'\,T_{\mathrm{GJ}}$ (the $10$ and the $126$ doublet on both rungs, no $120$), with $T^{u}_{\mathrm{GJ}} = v_{4}(B - L)\chi$ and $T_{\mathrm{GJ}} = w_{4}(B - L)\chi$ as in Propositions \claimref{standard-model.equal-weight-module} and \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}, and let one family matrix $F$ carry the three families, so that each sector's mass matrix is its one-family entry times $F$.
\begin{enumerate}
\item[(i)] On the sixteen the entries of $c$ have moduli $|a - a'|$ on $(L, \nu^{c})$, $|a + a'/3|$ on $(Q, u^{c})$, $|b - b'|$ on $(L, e^{c})$ and $|b + b'/3|$ on $(Q, d^{c})$. Hence, for every $F$, the neutrino Dirac matrix has the singular values of $M_{u}$ times $\kappa = |a - a'|/|a + a'/3|$, and likewise $M_{e}$ those of $M_{d}$ times $|b - b'|/|b + b'/3|$.
\item[(ii)] $\kappa = 1$ exactly on the Apollonius circle $|a - a'| = |a + a'/3|$, whose real points are $a' = 0$ and $a' = 3a$; on it the neutrino's rank-one eigenvalue is the top's, the top reading of Hypothesis (U) (Postulate \claimref{dark-matter.hyp-u-equal-rank-one-eigenvalues}) for the neutrino and the up quark, and its distinguished point is the pure-ten coupling $a' = 0$. $\kappa = 0$ exactly at $a' = a$, the point at which the up-type coupling commutes with the condensate projector; with one family structure this is Premise (EW) (Postulate \claimref{standard-model.premise-ew-equal-weight}) in every family direction, the case that premise's statement excludes; so with one family structure the whole line lies outside (EW).
\item[(iii)] At $a' = b' = 0$ all four rank-one eigenvalues coincide, the full content of (U) at leading order, exactly when $|a| = |b|$, the real rung vector of Proposition \claimref{standard-model.bidoublet-complex}.
\item[(iv)] The bottom reading at $M_{I}$, $\kappa = m_{b}/m_{t}$, with the intermediate-scale values $m_{b} = 1.3651$ GeV and $m_{t} = 92.45$ GeV of the Standard-Model paper's fits ($\kappa \in (0.01476, 0.01477)$), needs on the real same-sign branch $a'/a = (1 - \kappa)/(1 + \kappa/3) \in (0.9804, 0.9805)$: a departure of about two percent from the condensate-commuting point, which is neither of the two points that (ii) singles out.
\end{enumerate}
So on one family structure the top reading of (U) holds on the circle $\kappa = 1$, whose distinguished point is the pure-ten coupling (with the full (U) there at a real rung vector), the condensate-commuting coupling gives the neutrino no Dirac mass at all, and the bottom reading at $M_{I}$ is a tuned interior point of the line (running to the ceiling is not evaluated). This obtains the top reading from a stated structural choice, the pure-ten coupling, and excludes the bottom reading at both distinguished points; it does not decide between the pure-ten and the condensate-commuting coupling, and with separate family matrices for the $10$ and the $126$ (Proposition \claimref{standard-model.neutrino-dirac-matrix-charged-fermions}) the bottom-like size can come from the $126$'s entries off the heavy direction, which this clause does not address.

## technical
Hypothesis (U) says the neutrino's Dirac eigenvalue at the ceiling is the common rank-one value of all sectors, which the top keeps; the series has used it in two readings, top-like and bottom-like. This result places both readings on the line of couplings the module allows for one family structure: the $10$ and the $126$ doublet on each rung, with weights $a, a'$ (up-type) and $b, b'$ (down-type).

On the module the entries are $|a - a'|$ for the neutrino and $|a + a'/3|$ for the up quark (the $126$'s lepton-to-quark ratio $-3$, Georgi-Jarlskog's on the down side), so the neutrino Dirac matrix is the up-type matrix scaled by $\kappa = |a - a'|/|a + a'/3|$ whatever the family matrix. The top reading holds on the circle $\kappa = 1$. Two points of the line are distinguished by stored propositions: the pure $10$ ($a' = 0$), which lies on that circle (with the full hypothesis when the rung vector is real), and the condensate-commuting coupling ($a' = a$), where $\kappa = 0$, the equal-weight premise imposed in every direction, which that premise itself excludes, so the whole line lies outside it.

The bottom reading needs $\kappa = m_{b}/m_{t} \approx 0.0148$ at the intermediate scale $M_{I}$ (running to the ceiling not evaluated), that is $a'/a \approx 0.980$: two percent away from the condensate-commuting point and fixed by neither distinguished point. So with one family structure the top reading follows from the pure-ten choice (one point of the circle on which it holds) and the bottom reading has no structural home on the line; the question of which coupling the ceiling realises remains, and the two-structure case (the stored coupling sets) is separate.

## lay
The series needs to know how heavy the neutrino's ordinary (Dirac) mass is at the highest energy scale, and an assumption called Hypothesis (U) sets it equal either to the top quark's mass or to the bottom quark's. This result looks at the family of ways the theory's building blocks can couple to the Higgs-like field. Along that family the neutrino's mass is always the top quark's mass times one factor. That factor is exactly one when only the simplest coupling is present (and on a circle of other mixtures), so the top-quark reading follows from that choice, and it is exactly zero for the coupling that the series' equal-weight rule picks. The bottom-quark reading, with the masses taken at the intermediate scale of the series' fits, needs the factor to be about one and a half percent, which happens only for a finely chosen mixture two percent away from the equal-weight coupling, with no principle behind it.

## one-liner
For one family structure the rung coupling $a v_{4} + a' T^{u}_{\mathrm{GJ}}$ gives $M_{\nu}^{D}$ the up-type spectrum times $|a - a'|/|a + a'/3|$: equal to the top's on a circle through the pure ten (top reading of (U)), zero at the condensate-commuting point, and bottom-like at $M_{I}$ only at $a'/a \approx 0.980$, no distinguished point.
