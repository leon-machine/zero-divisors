---
id: dark-matter.thickness-not-gravitational-quantity
kind: claim
version: 6
title: The thickness is not a gravitational quantity
status: proved
region: dark-matter
subject: dark-matter
tags: [counting-rules, confronted-with-data]
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
  role: restated with H as the rational datum
  version: 6
  source: run 2026-11-08-frozen-point-datum
amendments:
- version: 6
  kind: restatement
  defect: 'Wording only: the formal and technical levels wrote the de Sitter radius as sqrt(3/Lambda), a square root of a multiple of Lambda, which over the series'' rational scalars exists only for special Lambda; written now with H as the datum, Lambda = 3H^2. The content, over R, is unchanged.'
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-inverse-square-law-short-range@1
  - dark-matter.sourcing-rule-forced-not-chosen@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_inverse_cube_below_extent
- kind: check
  ref: check.py::check_the_two_extents
- kind: check
  ref: check.py::check_both_exceed_the_short_range_bound
locators:
  paper: T14
  number: Cor 7.26
  label: cor:cavendish
  line: 1163
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: 'Version 5 -> 6. Leon''s decision of 8 November 2026 (op.frozen-point-rational-datum): wording only, with H as the datum (Lambda = 3H^2); the content, over R, is unchanged. The de Sitter radius ell = sqrt(3/Lambda) written ell = 1/H, Lambda = 3H^2, in the formal display and the technical level. The measured value 10^26 m, the proof, the check and coverage unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the inverse cube of a four-dimensional potential, the two extents d_b and l from the record, and their excess over the short-range bound. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 4 -> 5. Argued note added at the formal and technical levels, from synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst under the interface premise: with a massless five-dimensional species an open fifth direction makes every hole''s emission infinite, so black-hole lifetimes exclude the branch with matter localised within L on an open direction; under the static deposit reading the burst break E_b ~ 1/L_f makes the thickness observable through evaporation. The statement about gravity, the check and the numbers are unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 3 -> 4 (maintainer decision of 26 October that R2 and R3 are deposit clauses). Note added at the formal and technical levels: the comparison of the baryon spacing d_b = 0.98 m with the short-range bound takes today''s spacing as the extent, which assumes that the hidden direction co-expands; with R2 and R3 as deposit clauses and a static hidden direction the counted thickness today is the deposit-epoch cell radius, below 2.4e-10 m for a descent above 1 MeV, under the bound (synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands, clause (iv)). The check, the numbers and the statement for the co-expanding reading are unchanged.'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.imported-inverse-square-law-short-range
    - dark-matter.sourcing-rule-forced-not-chosen
    note: "E107 fix: the corollary has no proof environment and the source presents it as following from the sourcing proposition it is a corollary of and the short-range inverse-square bound it cites, so both were made its premises with a cites-only proof file; the reductions proposition is described as excluded, not used, and was not added."
  env: corollary
  context_refs:
  - dark-matter.imported-inverse-square-law-short-range
  - dark-matter.two-reductions
  flags:
  - no proof environment found
---

## formal
If the fifth direction carried the metric, gravity would fall as the inverse cube on scales below its extent $L$. The two extents the series has are the baryon spacing and the de Sitter radius ($\Lambda = 3H^{2}$),
\[
d_{b} \;=\; \left(\frac{3}{4\pi n_{b}}\right)^{1/3} \;\approx\; 0.98\ \mathrm{m}, \qquad \ell \;=\; \frac{1}{H} \;\approx\; 10^{26}\ \mathrm{m},
\]
with $n_{b} = 0.25\ \mathrm{m}^{-3}$ from $\Omega_{b}h^{2} = 0.02237$ (script: $d_{b}$ bracketed in $(0.95, 1.02)$ m). Both exceed the bound of Fact \claimref{dark-matter.imported-inverse-square-law-short-range} by more than four orders of magnitude. So the four-dimensional reading of P1 is forced by experiment, not chosen; the reductions of Proposition \claimref{dark-matter.two-reductions}, which needed a metric fifth direction to be well posed, describe a setting that is itself excluded; and the thickness in R3 can never be measured or computed gravitationally, since gravity does not see the direction it lives in. Only the tower's own dynamics, its cell size, can set it, so R3 is correctly a statement counted in the tower's own cells; and for the projected density $\rho_{5}L$ to be finite the fifth direction must be compact or the matter localised within $L$ by those dynamics, which the series does not supply. That the count is one radius is R3; the contact mechanism of Section \ref{subsec:free} returns it, and gravity cannot. The comparison with $d_{b}$ takes today's baryon spacing as the extent, which assumes that the hidden direction co-expands with the shared ones. With R2 and R3 read as deposit clauses and a static hidden direction, the counted thickness today is the deposit-epoch cell radius, below $2.4 \times 10^{-10}$ m for any descent above $1$ MeV, more than $10^{5}$ times under the bound (Proposition \claimref{synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands}(iv)); for that length the comparison above gives no exclusion, and the experimental argument rests on the co-expanding reading and on $\ell$.

\emph{Note (evaporation, argued).} Black holes reach where gravity does not. Under the interface premise a populated five-dimensional tower radiates through its Kaluza-Klein levels, whose number below a hole's temperature grows linearly with the extent $L_{f}$ of the fifth direction (\claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}(i)). If a massless five-dimensional species exists, an open fifth direction therefore makes every hole's emission infinite, so observed black-hole lifetimes exclude the branch above in which the direction is open and the matter is localised within $L$ by its dynamics, for any species free to move along the whole direction; the compact branch remains. And under the static deposit reading the extent is finite and small, and the break $E_{b} \propto 1/L_{f}$ of the burst's primary high-energy tail (\claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}(iii), (iv)) measures it, so the thickness, which gravity cannot see, is in principle observable through evaporation ($L_{f}$ is at least the counted thickness, and equal to it when the matter fills the fifth direction).

## technical
If the fifth direction carried the metric, gravity would fall as the inverse cube on scales below its extent $L$. The two extents the series has are the baryon spacing $d_{b} = (3/4\pi n_{b})^{1/3} \approx 0.98$ m and the de Sitter radius $\ell = 1/H \approx 10^{26}$ m ($\Lambda = 3H^{2}$), and both exceed the experimental short-range bound of about $40$ micrometres by more than four orders of magnitude.

So the four-dimensional reading of P1 is forced by experiment, the reductions that needed a metric fifth direction describe an excluded setting, and the thickness in R3 cannot be measured or computed gravitationally. Only the tower's own dynamics can set it, and for $\rho_{5}L$ to be finite the fifth direction must be compact or the matter localised within $L$, which the series does not supply. The comparison with $d_{b}$ assumes that the hidden direction co-expands: if R2 and R3 are deposit clauses and the hidden direction is static, today's counted thickness is the deposit-epoch cell radius, below $2.4 \times 10^{-10}$ m, which lies under the short-range bound, so for that length the comparison does not exclude a metric fifth direction.

Evaporation does see the fifth direction (argued, under the interface premise, from \claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}): a populated five-dimensional tower radiates through Kaluza-Klein levels whose number grows with the extent, so with a massless five-dimensional species an open fifth direction would make every hole's emission infinite, and black-hole lifetimes exclude the branch in which the matter is localised within $L$ on an open direction; under the static deposit reading the break energy $E_{b} \propto 1/L_{f}$ of the burst's high-energy tail measures the extent, so the thickness is observable through evaporation.

## lay
If gravity itself spread into the hidden fifth dimension, it would strengthen unusually quickly at short distances, and laboratory tests rule that out for any size the framework could offer. So gravity lives in our four dimensions only, and the depth of hidden matter that counts towards gravity cannot be found from gravity. It has to be set by the hidden sector's own physics.

## one-liner
Short-range tests of Newton's law exclude a metric fifth direction of either available extent, so the thickness in R3 is not a gravitational quantity.
