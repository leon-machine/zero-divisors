---
id: synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off
kind: claim
version: 2
title: 'In the Feynman gauge with a proper-time cut-off $\Lambda$ the series'' content induces $1/G = [B\Lambda^{2} - \sum w m^{2}\ln(\Lambda^{2}/m^{2})]/(12\pi) + O(m^{2})$, with $B = -36$ plus the scalars'' weights for the chain''s Pati-Salam content under Hypothesis (S); the logarithmic remainder is repulsive if the content below $\Lambda$ is the weak-scale content alone with $B = 0$, its sign is not fixed by the store for a cut-off above $M_{I}$ under (S), and it stays far below $1/G$; where $B > 0$ matching $G$ fixes $\Lambda$, so the route gives $G$ only by choosing the cut-off'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, mode-counting, no-go, undetermined-input, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
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
  - synthesis.imported-sakharov-induced-gravity-coefficients@1
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@2
  - standard-model.connection-forced@4
  - standard-model.chain@8
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@3
  - synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike@2
  proof: proof-main.tex
quantities:
- quantity.top-quark-mass@1
- quantity.w-boson-mass@1
- quantity.z-boson-mass@2
- quantity.planck-mass@1
- quantity.fermi-scale@1
checked_by:
- kind: check
  ref: check.py::check_proper_time_integral_gives_the_universal_logarithm
- kind: check
  ref: check.py::check_content_at_the_cut_off
- kind: check
  ref: check.py::check_logarithmic_remainder_sign_and_size
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations
  - programme.n-parameter-of-the-laws
  - synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2 November 2026: a uses edge to synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike@2, whose weak-scale coefficient B = 8(1 - 6 xi_R) and its regulator and gauge dependence this result takes as an input (cited by claimref in the proof''s Gauge paragraph, replacing the text citation); the proof now cites standard-model.connection-forced by claimref where the twelve vectors enter; the extraction note names the two results cited there by id. Pins of synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum (@3, dated note on the transmutation branch, its spectrum unchanged) and standard-model.chain (@8, note on one versus two doublets, content unchanged) moved. Statement and check unchanged.'
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Whether any route yields a Newton constant without a fit, beyond the cancelling three-generation content.
    The proper-time form 1/G = (B Lambda^2 - sum w m^2 ln(Lambda^2/m^2) - (1 - gamma) sum w m^2)/(12 pi) is
    standard (Sakharov; the weights of the imported Fact). New here is its evaluation on the series' content, in
    the Feynman gauge (alpha = 1, the Gupta-Bleuler form of clause (K1) of the Krein premise): the chain's
    Pati-Salam content between M_I and M_U (under Hypothesis (S)) gives B = -36 plus the scalars' weights (-36
    conformal; 28, 32, 152 minimal). The weak-scale coefficient B = 8(1 - 6 xi_R) and its dependence on the
    regulator and the gauge (12(alpha - 1) + 8(1 - 6 xi_R) under a covariant cut-off) are owned by
    synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike,
    and are used here as an input;
    synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form
    derives the one-particle form of (K1), which fixes alpha = 1. The logarithmic remainder: for the weak-scale
    content alone with B = 0 it is repulsive (the top outweighs the W and Z) and the doublets' tree term at
    xi_R = 1/6 has the same sign; under (S) the nine vectors at M_I (attractive), the scalars that B = 0 needs and
    the Majorana neutrinos under (M) enter with both signs, so the sign is not fixed by the store; the size stays
    below 1e-12 of 1/G at the Planck scale for the fields at M_I, and the content above M_U is not stored. The
    massive-vector logarithm is regulator independent but gauge dependent at xi_R != 0 (weight -(3 + 6 xi_R alpha);
    the Nielsen identity, the Higgs being off shell at order R). The weak-scale content here has two elementary
    doublets, while standard-model.chain runs with one doublet from M_Z to M_I: a tension between stored results,
    named and not resolved here. If B > 0, the cut-off is fixed by G (Lambda^2 = (3 pi/2) M_P^2 for B = 8): a fit.
    The survey of the store's scales (N initial data, the rung unit a free constant, the descent duration unfixed and
    a state datum, floors frame dependent, Pauli-Villars masses free, the locally covariant scheme with a free m^2
    coefficient) is argued. Restated from an earlier draft whose title claimed the repulsive sign without the
    condition on the content (draft id
    synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off-and-repulsively-at-logarithmic-order).
    Transport-absent.
---

## formal
Let each field carry its weight $w$ in units of one minimally coupled real scalar (Fact \claimref{synthesis.imported-sakharov-induced-gravity-coefficients}(a), (b): $1 - 6\xi_{R}$ for a real scalar of curvature coupling $\xi_{R}$, $1$ for a Weyl fermion, $-4$ for a gauge vector with its ghosts in the Feynman (Gupta-Bleuler) gauge, as in \claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}) and its mass $m$, and regulate the one-loop effective action by a proper-time cut-off $t \ge \Lambda^{-2}$, in the Feynman gauge.
\begin{enumerate}
\item[(i)] \emph{(The form; proved, given the Fact.)} $1/G_{\mathrm{ind}} = \tfrac{1}{12\pi}\bigl[B\Lambda^{2} - \sum_{j}w_{j}m_{j}^{2}\ln(\Lambda^{2}/m_{j}^{2}) - (1 - \gamma)\sum_{j}w_{j}m_{j}^{2} + O(m^{4}/\Lambda^{2})\bigr]$, $B = \sum_{j}w_{j}$ over the fields lighter than $\Lambda$; the coefficient of $\ln\Lambda^{2}$ is the $m^{2}$-part of the $t^{2}$ heat-kernel coefficient and does not depend on the regulator, while $B\Lambda^{2}$ and the constant do. For a massive vector at $\xi_{R} \neq 0$ that coefficient depends on the gauge parameter: its weight is $-(3 + 6\xi_{R}\alpha)$, $-4$ at $\xi_{R} = \tfrac16$ and $\alpha = 1$.
\item[(ii)] \emph{(The content at the cut-off; computed.)} Under Hypothesis (S), for a cut-off between $M_{I}$ and $M_{U}$ of the chain (Theorem \claimref{standard-model.chain}: twenty-one vectors, forty-eight Weyl fields, the bidoublet, the complex $(10,1,3)$ and optionally the complex $(15,2,2)$), $B = -36 + \sum_{j}(1 - 6\xi_{R,j})$ over the chain's real scalars: $-36$ if all are conformally coupled, $28$, $32$ or $152$ if all are minimally coupled. The content above $M_{U}$ is not stored.
\item[(iii)] \emph{(The logarithmic remainder; computed.)} (a) If the content below $\Lambda$ is the weak-scale content alone (twelve vectors, forty-eight Weyl fields, the two elementary doublets of \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}) and $B = 0$ ($\xi_{R} = \tfrac16$), then for every cut-off $\Lambda \ge 10\,m_{t}$ the remainder $\sum_{j}w_{j}m_{j}^{2}\ln(\Lambda^{2}/m_{j}^{2})$ is positive, the top quark outweighing the $W$ and $Z$, so $1/G_{\mathrm{ind}} < 0$ at this order; the doublets' tree term $-8\pi\xi_{R}v^{2} = -\tfrac{4\pi}{3}v^{2}$ has the same sign; both are below $10^{-31}M_{P}^{2}$ at $\Lambda = M_{P}$. (b) Under (S), for a cut-off above $M_{I}$, the nine vectors at $M_{I}$ (weight $-4$ each), the chain's scalars and, under Premise (M) (\claimref{neutrino.m-framework-realises-majorana-term-scale}), the Majorana neutrinos enter with both signs, so the sign of the remainder is not fixed by the store; for masses up to $6 \times 10^{11}$ GeV and scalar weights of size at most $1$ these fields contribute below $10^{-12}M_{P}^{2}$ at $\Lambda = M_{P}$.
\item[(iv)] \emph{(Matching; computed.)} If $B > 0$, the observed $G$ is reproduced at leading order exactly when $\Lambda^{2} = 12\pi M_{P}^{2}/B$ (for $B = 8$, $\Lambda^{2} = \tfrac{3\pi}{2}M_{P}^{2}$).
\end{enumerate}
\emph{Reading (argued).} The store supplies no cut-off scale in Planck units: $N$ is initial data (\claimref{programme.n-parameter-of-the-laws}), the weak scale's constant is a second free number (\claimref{synthesis.rung-unit-second-free-number}), the descent's duration, which would set the deposit's ultraviolet end, is not fixed and is a datum of the state, which enters the stress tensor only through smooth state-dependent terms (\claimref{synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands}), the floors are frame dependent, the Krein premise's Pauli-Villars masses are free, and the locally covariant scheme leaves a free coefficient times $m^{2}$ (Fact (d)). So the induced-gravity route reaches $G$ only by choosing one dimensionful regulator datum, and $G$ stays an input. Transport-absent.

## technical
In Sakharov's induced gravity with a proper-time cut-off $\Lambda$, in the Feynman gauge, each field contributes to $1/G$ its weight times $\Lambda^{2}$, minus its weight times $m^{2}\ln(\Lambda^{2}/m^{2})$, over $12\pi$. The weights are $1 - 6\xi_{R}$ per real scalar of curvature coupling $\xi_{R}$, $1$ per Weyl fermion and $-4$ per gauge vector. The logarithmic coefficient is fixed by the heat-kernel coefficient and does not depend on the regulator, though for massive vectors at $\xi_{R} \neq 0$ it depends on the gauge; the quadratic one depends on both.

The quadratic coefficient $B$ counts every field lighter than the cut-off. If the cut-off lies above the chain's intermediate scale, under Hypothesis (S) the Pati-Salam content has twenty-one vectors, and $B = -36$ plus the scalars' weights: negative if the scalars are conformally coupled, $28$ to $152$ if they are minimally coupled. Nothing in the store fixes these couplings or the content above the unification scale.

Where $B = 0$ and only the weak-scale content lies below the cut-off, the remainder is logarithmic and has the wrong sign: the top quark outweighs the $W$ and $Z$ bosons, and the Higgs doublets' classical curvature coupling adds a term of the same sign, so the induced $1/G$ is negative and far too small. Under (S), with a cut-off above the intermediate scale, the heavy vectors there pull the other way and the sign is not fixed by the store; the size stays far below $1/G$. Where $B > 0$, the observed $G$ fixes the cut-off, for instance $\Lambda^{2} = \tfrac{3\pi}{2}M_{P}^{2}$ at $B = 8$: a fit. Reading, argued: no stored datum supplies the cut-off in Planck units, so $G$ stays an input. Transport-absent.

## lay
Sakharov's idea is that gravity's strength could be produced by the quantum jitter of all other fields, up to some shortest length where the jitter is cut off. The result is the cut-off energy squared times a count of the fields, plus a much smaller term from the particle masses. If the series' larger unified symmetry is real at high energies, the count depends on how its many extra Higgs fields couple to curvature, which nothing in the series decides. If only the everyday particles lie below the cut-off and their count is zero, the small mass term is left, and it has the wrong sign: it would make gravity repulsive, and it is far too weak. With the series' unified symmetry, heavy force carriers pull the other way and the sign is undecided, but the term is still far too weak. Where the count is positive, gravity's observed strength can be matched, but only by choosing the cut-off to match it, a little above the Planck energy. The series has no number that would set that cut-off, so on this route the strength of gravity remains an input.

## one-liner
In the Feynman gauge with a proper-time cut-off the series' content induces $1/G = [B\Lambda^{2} - \sum w m^{2}\ln(\Lambda^{2}/m^{2})]/(12\pi)$, with $B = -36$ plus the scalars' weights for the chain's Pati-Salam content under Hypothesis (S); the remainder is repulsive if only the weak-scale content lies below the cut-off and $B = 0$, of sign not fixed by the store under (S) above $M_{I}$, and far below $1/G$; where $B > 0$ matching $G$ fixes the cut-off, a fit.
