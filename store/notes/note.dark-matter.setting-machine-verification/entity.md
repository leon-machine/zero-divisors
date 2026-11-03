---
id: note.dark-matter.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
comments_on:
- dark-matter.towers-are-residues-single-clock-filter
- dark-matter.flag-insensitive-residue-no-flag-level
- dark-matter.population-count-one-share-half-percent
- dark-matter.asymmetry-arrow-counted-fifteenth-refutation
locators:
  paper: T14
  number: Setting
  section: Machine verification
  line: 1428
---

## formal
Every computational identity asserted in this paper at its own proof level, with the exceptions listed at the end, has been verified in exact arithmetic by the script \texttt{verify\_T14.py} \cite{ButlerVerifyT14}, which imports the series' shared library \texttt{GA.py}: exact rationals and arbitrary-precision integers, no machine floating point outside the two checks of Part N, an order-of-magnitude estimate labelled as floating point in its printed messages, the irrational constants entering only through rational brackets proved by integer inequalities. Two hundred checks, all passing, in fourteen parts keyed to statement tags; five are labelled as records rather than computations in their own printed messages (the $\theta$ no-go's degrees and homotopy table, the parity identity of Part J, the one-loop coefficient formula of Part H, and the coupling-departure illustration), and every witness the script relies on internally is counted in an aggregate check. Parts H, J and K use forty-digit decimal arithmetic for logarithms, exponentials and fixed points, the inequality chain itself being exact rational algebra. The script's printed labels give every bracket; the parts, with the statements they cover:

\emph{Part A} (Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}): the census over every signature of dimension at most ten, the reversal $r \mapsto -r$, the P3 representatives and the sterile set, and the window sensitivity (four windows, four answers).

\emph{Part B} (Proposition \claimref{dark-matter.flag-insensitive-residue-no-flag-level}): the isometry witnesses in $(1,3)$ and $(2,2)$, entry by entry, and the Jacobian of the isotropy equations.

\emph{Part C} (Proposition \claimref{dark-matter.population-count-one-share-half-percent}): the survey ratio, its uncertainty and the remainder $4.364$.

\emph{Part D} (Propositions \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, \claimref{dark-matter.orientation-arrow-seventeenth-refutation}): the $\theta$ no-go's inputs as recorded data, and on $\Cl(1,1)$ the reflection that exchanges the null pair and preserves the form.

\emph{Part E} (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}, Propositions \claimref{dark-matter.radiation-audit-what-theorem-closes-what}, \claimref{dark-matter.open-channels-their-costs}): the dilution exponents as a function of the sourcing rule for $D = 2, 3, 4$ and the single-sheet reading; the $\Neff$ coefficients, the thresholds $0.51$, $0.46$ and $0.465$, the entropy-release factor and the joint five-dimensional channels.

\emph{Part F} (Proposition \claimref{dark-matter.ceiling-valued-inherited-success}): the two valuations and the ratio of the ends.

\emph{Part G} (Theorems \claimref{dark-matter.type-residue-what-each-tower-can}, \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}, \claimref{dark-matter.mode-counts-two-modules-which-one}): for every $\Cl(p,q)$ of dimension at most five, the centre, a primitive idempotent by exhaustive search, the division algebra by exact rank, the component count and module dimension, agreeing with the classical table on all twenty signatures; the abstract agreements across residues; the module dimensions, the Witt indices and the weightings.

\emph{Part H} (Proposition \claimref{dark-matter.mirror-share-one-how-fragile}): the one-loop chain as exact rational algebra on a grid, the one-flavour factors at both ends of the ceiling range, and the coupling sensitivity with its ten-percent window.

\emph{Part I} (Theorem \claimref{dark-matter.mirror-tower-copy-one}): the even-subalgebra isomorphisms for $(2,4)$, $(4,2)$, $(1,3)$, $(3,1)$, the matching types, the pair-count witnesses and the mirror threshold $0.448$.

\emph{Part J} (Proposition \claimref{dark-matter.two-families-are-two-chiralities}, Theorem \claimref{dark-matter.flag-bit-exists-exactly-tower-dimension}, Propositions \claimref{dark-matter.population-count-one-share-half-percent}, \claimref{dark-matter.stored-asymmetry-charge-not-number}): the Fock ideals on the split forms of dimensions four, six and eight (the null-pair relations, the blade and top state, the chirality eigenvalues, the exchanging versors and their determinants), $I$ central in dimensions five and seven, the parity identity to dimension ten, the odd-dimensional Fock ideal at $m = 1, 2, 3$, the reversion form on the twistor ideal; and the mirror's cosmology at the paper's inputs: $\eta$ and $\eta^{1/3}$, the species count and the floor, the gravitational yield's shortfall, the hot deposit, the weak freeze-out, the bottleneck, the reheating, the mean-mass deficit, recombination, the cross-sections, cooling times and mean free path.

\emph{Part K} (Appendix \ref{app:seeding}): the floor prefactor and its scalings, the Boltzmann integral between Riemann sums, the nine-vector coefficient, the $\Neff$ shares, and the mirror share $1/5.364$.

\emph{Part L} (Premise \claimref{dark-matter.p5-boundary-modes-hold-entropy-not}, Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}, Fact \claimref{dark-matter.imported-schwinger-discharge-charged-hole}): the baryon-emission mass, the burst and entropy ratios, $T_{\mathrm{H}}$ at one solar mass, and the Schwinger charge, its ratio to extremal and the crossover mass.

\emph{Part M: the unit-ball rule} (Section \ref{sec:rule}; Propositions \claimref{dark-matter.nesting}, \claimref{dark-matter.unit-ball-rule}, Remark \claimref{note.dark-matter.equivalent-forms-assignment-not}, Lemma \claimref{dark-matter.direction-nesting-adds-algebra}, Proposition \claimref{dark-matter.contact-mechanism-returns-r3}, Table \ref{tab:excludes}, Remarks \claimref{note.dark-matter.scope-mechanism}, \claimref{note.dark-matter.common-thickness-curve-if-two-differ}, Propositions \claimref{dark-matter.total-function-thickness}, \claimref{dark-matter.two-roots-are-chord-arc-quarter}, \claimref{dark-matter.two-reductions}, Remark \claimref{note.dark-matter.r1-against-series-mass-formulas}, Proposition \claimref{dark-matter.sourcing-rule-forced-not-chosen}, Corollary \claimref{dark-matter.thickness-not-gravitational-quantity}, Remark \claimref{note.dark-matter.sheet-family-linear-spectra}, Observation \claimref{dark-matter.status-rule}): one hundred and four checks, every measure an exact monomial $q\,\pi^{k}$ with $q$ rational; the measures, the hat-box identity and the Wallis integrals; the nesting relations and the four identities of Lemma \claimref{dark-matter.direction-nesting-adds-algebra} in $\Cl(1,4)$, $\Cl(1,3)$, $\Cl(4,1)$, $\Cl(3,1)$, with the reflection that exchanges the components; the closed form against the record; the equivalent forms; the arithmetic of the mechanism's stated counts (the slab as an exact Riemann sum, the downward count, O solved for the spacing, the alternatives, the section weight as a bracketed integral, the non-composition across the double nesting; the clauses themselves are postulated and not checked); $T(c)$ with its symmetry, floor, roots, windows and fractions; the de Sitter reductions; the clock reflection; the mass bound over the Gaussian rationals; the look-elsewhere count; the consistency numbers, with the stress identity, the metric feedback and the orientation average $\tfrac{2}{3}$ of Proposition \claimref{dark-matter.reduced-response-gravity-needs-supporting-stress}.

\emph{Part N: the density R2 assigns} (Section \ref{subsec:simulated}): on a sheet the number per unit area and the expansion rate fall together in radiation domination ($a^{2}H$ constant at fixed $g_{*}$), and a symmetric relic annihilating at full strength is left at about $3 \times 10^{-14}$ of R2's density; floating point, order of magnitude.

What the script does not check, imported at the cited levels: the Boltzmann computation of Remark \claimref{note.dark-matter.sheet-family-linear-spectra} (CLASS, floating point, deposited as a record with its patch and inputs); Witt's theorem (witnesses only) and Polyakov's; the wall-displacement and acoustic no-go theorems; the two-time instability import; the CPT covariance of structures later papers add; the Goldstone and deposit-energy estimates (dimensional analysis in-proof); the homotopy groups (recorded); the Fock-module identification of the tower module (T3); the Standard-Model paper's chain (its inputs' reversal invariance is checked, not the chain); Chevalley's general criterion (not used); the graviton production rate and the standard thermal history the seeding formula assumes (the integral and the coefficients are checked); the thermalisation of a pure-glue tower's produced quanta; the dimensional-analysis step of Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}; the dissipative-dark-matter bounds; the mirror's nucleosynthesis network and the settling of its gas beyond their arithmetic; the two spin-group isomorphisms of Corollary \claimref{dark-matter.which-towers-can-carry-arrow}; the Schwinger field and the discharge mechanism (the scales built from them are checked); the exhaustiveness clause; and the survey values \cite{Planck2018}, refreshed at submission.

## technical
pending

## lay
pending

## one-liner
pending
