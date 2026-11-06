---
id: synthesis.mass-ordered-dressing-cannot-spoil-koide
kind: claim
version: 1
title: 'Mass-ordered dressing cannot turn Koide brackets into quark masses'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, no-go, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
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
  - families.linear-conjecture-refuted-data@3
  proof: proof-main.tex
quantities:
- quantity.down-quark-mass@1
- quantity.strange-quark-mass@1
- quantity.bottom-quark-mass@1
- quantity.top-quark-mass@1
checked_by:
- kind: check
  ref: check.py::check_flavour_blind_dressing_keeps_q
- kind: check
  ref: check.py::check_raising_lighter_masses_lowers_q
- kind: check
  ref: check.py::check_quark_quotients_exceed_two_thirds
- kind: check
  ref: check.py::check_required_heavy_to_light_ratio
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.selectivity-observation-level
  - families.koide-nullity-condition-one-member-invariant
extraction:
  open_problem: op.gram-square-and-face-space
  note: 'Addresses the third part of the problem, the strong dressing that spoils the quark relation, adversarially. The selectivity account (families.selectivity-observation-level, conjectured) has leptons undressed and quarks strongly dressed, so that Koide could hold at bracket level for all three sectors while failing for physical quark masses. This result shows the strong dressing moves the quotient the wrong way. The quotient is homogeneous of degree zero, so a common factor does nothing; raising the lighter masses relative to the heaviest strictly lowers it (an exact lemma with a stated sufficient condition); and perturbative QCD dressing is of that kind (flavour-blind in MS-bar at a common scale; own-scale evaluation and the pole conversion enhance the lighter quarks), as is the constituent dressing, while the top decays before hadronising. Since the measured quotients exceed 2/3 in both quark sectors at every standard mass definition (0.731 to 0.889), the brackets exceed it by at least as much. A Koide bracket would need a dressing favouring the heavier quark by a factor of at least 1.88 (down, stored values) and 8.67 (up, own-scale values). The QCD facts (flavour-blind anomalous dimension, the sign of the scale and pole corrections, top decay before hadronisation) are argued from memory, not proved, as the title says; the u and c masses and the M_Z mass set (the 2008 running-mass table of Xing, Zhang and Zhou) are cited from memory; the down-sector and top values are the stored quantities. The exact content is the lemma and the certified numbers. Transport-absent (an inequality on the Koide quotient and standard QCD).'
---

## formal
Let $Q(m) = \sum_{k}m_{k}/(\sum_{k}\sqrt{m_{k}})^{2}$ for positive $m = (m_{1}, m_{2}, m_{3})$ with $m_{3}$ the largest, the quotient of Proposition \claimref{families.linear-conjecture-refuted-data}, and call $m' = (D_{1}m_{1}, D_{2}m_{2}, D_{3}m_{3})$ a dressing of $m$ by the factors $D_{k} > 0$.
\begin{enumerate}
\item[(i)] \emph{(Flavour-blind dressing.)} $Q(\lambda m) = Q(m)$ for every $\lambda > 0$.
\item[(ii)] \emph{(Dressing that favours the lighter flavours.)} If $D_{1}, D_{2} \ge D_{3}$ and $D_{j}m_{j} \le D_{3}m_{3}/9$ for $j = 1, 2$, then $Q(m') \le Q(m)$, with equality only when $D_{1} = D_{2} = D_{3}$. (With $s_{k} = \sqrt{m_{k}}$, $S_{1} = \sum s_{k}$, $S_{2} = \sum s_{k}^{2}$: $\partial Q/\partial s_{j} = 2(S_{1}s_{j} - S_{2})/S_{1}^{3}$, negative whenever $3s_{j} \le s_{3}$ and positive for $j = 3$.)
\item[(iii)] \emph{(The quarks.)} At the stored values ($m_{d}$, $m_{s}$ at $2$ GeV, $m_{b}(m_{b})$, $m_{t}$ direct) and at further standard definitions, $Q > \tfrac23$ in both quark sectors: down in $(0.731, 0.732)$ (stored) and $(0.745, 0.746)$ (running masses at $M_{Z}$); up in $(0.848, 0.849)$ ($m_{u}$ at $2$ GeV, $m_{c}(m_{c})$, $m_{t}$), $(0.831, 0.832)$ (charm pole mass) and $(0.888, 0.889)$ (at $M_{Z}$). So if the physical masses are a dressing of the kind in (i) or (ii) of brackets $m^{0}$, then $Q(m^{0}) \ge Q(m) > \tfrac23$: such a dressing cannot turn a Koide bracket ($Q = \tfrac23$) into the measured quark masses.
\item[(iv)] \emph{(What a Koide bracket would need.)} If $D_{3}/D_{j} \le R$ for $j = 1, 2$ and $R\,m_{j} \le m_{3}/9$, then $Q(m^{0}) \ge Q(Rm_{1}, Rm_{2}, m_{3})$, which exceeds $\tfrac23$ for $R < R^{*}$ with $R^{*} \in (1.88, 1.89)$ for the stored down sector, $(2.19, 2.20)$ for the down sector at $M_{Z}$, $(8.67, 8.68)$ for the up sector at own scales and $(17.5, 17.6)$ at $M_{Z}$. A Koide bracket needs a dressing that enhances the heaviest quark over a lighter one by at least $R^{*}$. Neither (ii) nor (iv) treats a dressing that raises the middle mass and lowers the lightest relative to the heaviest ($D_{2} > D_{3} > D_{1}$).
\end{enumerate}
Argued, not proved (standard QCD, cited from memory and not stored): perturbative strong dressing is of the kind in (i) and (ii): the mass anomalous dimension in a mass-independent scheme is the same for every flavour, so running between common scales is a common factor, and evaluating each mass at its own scale or converting to the pole mass enhances the lighter quarks, by asymptotic freedom; constituent dressing, additive and of order $\Lambda_{\mathrm{QCD}}$, favours the lighter quarks too. On that reading these dressings can only lower the quark quotients, and the quarks' failure of the relation is not produced by them from Koide brackets.

## technical
The selectivity account explains why Koide holds for the charged leptons and not for the quarks: leptons are undressed, quark masses are dressed by the strong interaction. This result tests that account and finds the dressing pushes the wrong way. The Koide quotient does not change when all three masses are multiplied by one factor, and it strictly decreases when the lighter masses are raised relative to the heaviest (as long as they stay below a ninth of it). Perturbative strong dressing is of this kind, by standard QCD (argued here, not stored): in the standard scheme all quark masses run by the same factor between common scales, and quoting each mass at its own scale, or as a pole mass, makes the lighter quarks relatively heavier. So the strong dressing can only lower the quotient. The measured quark quotients are above $\tfrac23$ in both sectors under every standard mass definition (between $0.731$ and $0.889$), so the undressed values would be further from Koide, not on it. A Koide relation at bracket level would need a dressing that favours the heaviest quark by a factor of at least $1.88$ in the down sector and $8.67$ in the up sector, which no known strong-interaction effect does.

## lay
A striking formula relates the masses of the electron, muon and tau, but it fails for the quarks. One proposed reason is that quarks feel the strong force, which changes their apparent masses, while leptons do not. This result checks the direction of that change. The formula's key number is unaffected when every mass is scaled by the same factor, and it goes down when the lighter particles get relatively heavier. The strong force does exactly that: it scales all quark masses alike, and where it differs it makes the lighter ones relatively heavier. So it can only move the quarks towards the formula from above, and the quarks sit above it already. The strong force cannot be what spoils the formula for quarks.

## one-liner
The Koide quotient is unchanged by a common dressing factor and strictly lowered by raising the lighter masses, so a strong dressing that is flavour-blind at a common scale and favours the lighter quarks at own scales, as pole masses or as constituent masses (argued from standard QCD) can only lower it; with the measured quark quotients above $\tfrac23$ in both sectors (between $0.731$ and $0.889$), a Koide bracket would need a dressing favouring the heaviest quark by at least $1.88$ (down) and $8.67$ (up).
