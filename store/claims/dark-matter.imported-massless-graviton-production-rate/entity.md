---
id: dark-matter.imported-massless-graviton-production-rate
kind: claim
version: 5
title: 'Imported: the massless-graviton production rate'
status: imported
region: dark-matter
subject: dark-matter
tags: [quantum-gravity, matter-asymmetry]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, reduced Planck mass letter at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'flag at every level: the Fact imports a process of a quantised gravitational field, which the series does not hold; rate and coefficients unchanged'
  version: 3
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'restatement: the later published value and its normalisation added beside the stored one, which is one sixteenth of it; the fermion weight; the flag replaced by a citation of the derived rate'
  version: 4
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate), at Leon''s decision'
- name: Claude Fable 5.2
  role: 'dated note: the rate is at non-null momentum and does not depend on the canonical pair adopted on 24 November 2026; rate, coefficients and provenance unchanged'
  version: 5
  source: 'maintainer pass of 2026-11-24 (run 2026-11-24-three-routes)'
amendments:
- version: 5
  kind: restatement
  defect: 'the Fact names a graviton and says that the derived rate needs no quantum of the gravitational field, written when the series held none; since 24 November 2026 the series posits a canonical pair on the two free directions at null momentum, and the text did not say that this rate, at non-null momentum, is independent of it'
  evidence: 'synthesis.gravitational-pair-production-from-the-operator-source-at-first-order: check.py::check_first_order_field_at_non_null_momentum_is_fixed_by_the_source'
- version: 4
  kind: restatement
  defect: 'the stored coefficient, from the 2018 source, is one sixteenth of the value the same group prints in 2022 with the canonically normalised coupling (the 2018 source couples the field with half that coupling), and both sources weight each of the 45 chiral fermions as a Dirac fermion; the Fact stated the 2018 value alone, with a flag that the process was not held by the series'
review: typed
imported_from:
- citation: N. Bernal, M. Dutra, Y. Mambrini, K. Olive, M. Peloso, and M. Pierre, Spin-2 portal dark matter,
    Phys. Rev. D 97 (2018), 115020.
  key: Bernal2018
- citation: 'S. Clery, Y. Mambrini, K. A. Olive, and S. Verner, Gravitational portals in the early Universe, arXiv:2112.15214.'
  key: CleryEtAl2022
locators:
  paper: T14
  number: Fact A.1
  label: fact:alpha
  line: 1467
extraction:
  maintainer_pass_2026_11_24_three_routes:
    by: maintainer-2026-11-24
    date: '2026-11-24'
    note: 'Version 4 -> 5, on Leon''s decision of 24 November 2026 (the canonical pair on the two free directions adopted as Premise (TT), at first order: synthesis.premise-canonical-pair-on-the-two-null-directions). The flag paragraph of 10 November had already been replaced on 18 November by the citation of the derived rate, so no flag is left to restate. One dated note is added at the formal and technical levels: the rate is at non-null momentum, where the first-order field is fixed by its source, uses no state of the adopted pair and does not depend on the premise. The rate, both published coefficients, the coefficients the store uses and the provenance are unchanged; results that use the Fact use the same statement.'
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 3 -> 4, at Leon''s decision of 18 November 2026 (correct the stored numbers now). The Fact now states both published values, what each source''s coupling is, and that the two differ by sixteen; both sources were read on the web on 18 November 2026 (arXiv:1803.01866 on ar5iv: equations (3), (8), (15), appendix (17), (25) to (27), (31), Table I; arXiv:2112.15214: equations (2), (11), (79), (83) to (90)). The flag of 10 November is replaced by a citation of synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, which derives the rate with no quantum of the field and gives the coefficients the store uses. The four direct users are restated in the same pass.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3, by Leon''s decision of 10 November 2026 (flag now, derive later). A flag paragraph is added at every level: the rate is computed in its source from the exchange of a quantum of a spin-2 field, the series holds no quantum of the gravitational field (conventions, section "Gravity and the graviton"), and the results that use the Fact rest on it conditionally. The rate, its coefficients and the provenance are unchanged, and no dependant is edited in this pass except the three predictions that carry a pointing sentence. The open problem op.graviton-rate-as-classical-field-process asks for the rate as a process of the classical gauge field sourced by matter, or a proof that it vanishes, and lists what rests on the Fact.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item F14 (routine): the reduced Planck mass 2.435e18 GeV is written bar M_P = M_P/sqrt(8 pi) (quantity.reduced-planck-mass), not M_P, the letter of the non-reduced quantity.planck-mass (1.22e19 GeV), at every level; the provenance keeps Bernal et al.''s M_P with a note that the source writes it for the reduced mass. Notation; values unchanged.'
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported; levels only.
---

## formal
Matter that couples to the Standard-Model plasma through gravity alone is produced from it, at tree level, at a rate per volume
\[
R(T) \;=\; \frac{\alpha\,T^{8}}{\bar{M}_{P}^{4}}, \qquad \bar{M}_{P} = 2.435 \times 10^{18}\ \mathrm{GeV},
\]
with $\bar{M}_{P} = M_{P}/\sqrt{8\pi}$ the reduced Planck mass, the sum over the Standard-Model bath being inside the coefficient, weighted as $4|\mathcal{M}^{0}|^{2} + 45|\mathcal{M}^{1/2}|^{2} + 12|\mathcal{M}^{1}|^{2}$ over its scalar, fermion and vector degrees. Two published values of the coefficient for a produced real scalar are imported, with what each source states.
\begin{enumerate}
\item[(a)] \cite{Bernal2018}, equation (31) and Table I: $\alpha = 3997\pi^{3}/663552000 \approx 1.9 \times 10^{-4}$ for a scalar, and $1.1 \times 10^{-3}$, $2.3 \times 10^{-3}$ for a Dirac fermion and a vector, as the massless limit of that paper's massive spin-2 mediator. Its coupling is $h_{\mu\nu}T^{\mu\nu}/(2\bar{M}_{P})$ (its equation (3); the source writes $M_{P}$ for the reduced mass), its propagator that of a canonically normalised field (appendix, equation (17)), and its squared amplitudes (appendix, equations (25) to (27)) are one sixteenth of the canonically normalised ones (both without symmetry factors).
\item[(b)] \cite{CleryEtAl2022}, equations (86) and (90): $\alpha = 3997\pi^{3}/41472000 \approx 3.0 \times 10^{-3}$ for a scalar and $11351\pi^{3}/20736000 \approx 1.7 \times 10^{-2}$ for a Dirac fermion, with the coupling $-h_{\mu\nu}T^{\mu\nu}/\bar{M}_{P}$ of a canonically normalised field (its equation (2)) and the same rate integral. This is sixteen times (a).
\item[(c)] Both sources sum the fermion amplitude over both helicities and multiply by $45$, which weights each chiral fermion of the Standard Model as a Dirac fermion.
\end{enumerate}
The normalisation of (b) is the one that reproduces Newton's law, and the coefficients the store uses are those of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v), which derives the rate with the chiral fermions weighted once: $5789\pi^{3}/82944000 \approx 2.16 \times 10^{-3}$ for a real scalar, $16087\pi^{3}/82944000 \approx 6.01 \times 10^{-3}$ for a chiral fermion, $16087\pi^{3}/20736000 \approx 2.41 \times 10^{-2}$ for a real massless vector, counting creation events of two quanta each. The value (a), which the store used until 18 November 2026, is low by $46312/3997 \approx 11.6$ for the scalar. In its sources the rate is computed from the exchange of a quantum of a spin-2 field; the cited theorem obtains the same rate from the operator source with no state of the gauge field, and the two accounts agree at this order. \emph{Note (24 November 2026).} By Leon's decision of that date the series posits, at first order, a canonical pair on the two free directions of the gravitational gauge field at null momentum (Premise \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}). The rate here is at non-null momentum, $Q(k) = s > 0$, where the first-order field is fixed by its source: it uses no state of that pair and does not depend on the premise.

## technical
The rate per volume at which the Standard-Model plasma produces a species coupled to it through gravity alone is $R(T) = \alpha\,T^{8}/\bar{M}_{P}^{4}$, with $\bar{M}_{P} = 2.435 \times 10^{18}$ GeV the reduced Planck mass. Two published values for a produced scalar are imported: $3997\pi^{3}/663552000$ (Bernal et al. 2018, with the coupling $h_{\mu\nu}T^{\mu\nu}/(2\bar{M}_{P})$) and $3997\pi^{3}/41472000$ (Clery et al., arXiv:2112.15214, with the canonical coupling $-h_{\mu\nu}T^{\mu\nu}/\bar{M}_{P}$), the second sixteen times the first. Both weight each of the $45$ chiral fermions as a Dirac fermion.

The later normalisation is the one that reproduces Newton's law. The coefficients the store uses are those derived in the store with the chiral fermions weighted once: $2.16 \times 10^{-3}$ for a real scalar, $6.01 \times 10^{-3}$ for a chiral fermion, $2.41 \times 10^{-2}$ for a real massless vector, per creation event of two quanta. The first published value is low by about $11.6$ for the scalar. Under the operator-source hypothesis of that derivation, the derived rate needs no quantum of the gravitational field. (Note of 24 November 2026: the series now posits, at first order, states on the two free directions of the field at null momentum, \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}; this rate is at non-null momentum and does not depend on that premise.)

## lay
Even matter that feels no force but gravity is produced in a hot early universe, because ordinary particles colliding can occasionally create it through gravity. This imported result gives the rate, which rises very steeply with temperature. It is the input that fixes how warm gravity alone can make the hidden worlds.

Two published numbers for it exist, from overlapping authors, and they differ by a factor of sixteen: the earlier paper used half the correct strength of the coupling between gravity and matter. The later number is the correctly normalised one. Both papers also count each of the Standard Model's fermions twice. The collection used the earlier number until 18 November 2026; it now uses values derived inside the collection, which are about eleven times larger for a hidden scalar. That derivation also shows that, if gravity's field is fixed by the matter that sources it, the rate does not need gravity to be carried by particles.

## one-liner
The plasma produces a gravitationally coupled species at $\alpha T^{8}/\bar{M}_{P}^{4}$; two published scalar coefficients are imported, $3997\pi^{3}/663552000$ (2018, with half the canonical coupling) and sixteen times that (2022, canonical), both weighting chiral fermions as Dirac; the store uses the coefficients derived in it ($2.16 \times 10^{-3}$ scalar, $6.01 \times 10^{-3}$ chiral fermion, $2.41 \times 10^{-2}$ massless vector), which, under the operator-source hypothesis of that derivation, need no quantum of the gravitational field.
