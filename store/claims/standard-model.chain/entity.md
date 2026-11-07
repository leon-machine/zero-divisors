---
id: standard-model.chain
kind: claim
version: 8
title: The chain
status: proved
region: standard-model
subject: standard-model
tags:
- running-and-unification
- symmetry-breaking
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.direction-demanded-content-doublet-heavy@7
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.imported-pati-salam-representation-theory-survival@1
  - standard-model.imported-proton-condition@1
  - standard-model.imported-two-loop-gauge-coefficients@1
  - standard-model.left-right-parity-what-breaks-it@8
  - standard-model.majorana-element@7
  - standard-model.matching-traces@4
  - standard-model.one-threshold-exact-criterion@3
  - standard-model.spectrum-run@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_one_and_two_loop_coefficients
- kind: check
  ref: check.py::check_one_loop_chain_solutions
- kind: check
  ref: check.py::check_real_chain_as_one_threshold_shift
locators:
  paper: T12
  number: Prop 10.10
  label: prop:pschains
  line: 1980
extraction:
  maintainer_pass_qft_full:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 7 -> 8, by Leon''s decisions of 2 November 2026: a marked note at the formal and technical levels names the tension between the chain''s one Higgs doublet below M_I and the rung field recorded as two elementary doublets (the second heavy, about 2.5 to 3.5 TeV, on the working branch with a level), and lists the recomputation of M_I and M_U with the second doublet as open. Content, status, edges, proof and check unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the one- and two-loop Pati-Salam coefficients, the exact one-loop chain solutions with certified bounds on alpha_U^-1, M_I and M_U, and the real chain as the one-threshold shift (-76/15, 0, -2/3) at f = 0.320. Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Formal level and proof have no twistor language; only the lay level's twistor slots were reworded.
  source_title: The chain
  source_formal: 'Under Hypothesis (S), take the derived content with one Higgs doublet from $M_{Z}$ to
    $M_{I}$, and above $M_{I}$ Pati-Salam with three generations, the bidoublet, the complex $(10,1,3)$
    whose vev breaks it at $M_{I}$ (Proposition \claimref{standard-model.majorana-element}) and, where
    named, the complex $(15,2,2)$; left-right parity is broken at $M_{U}$ (Proposition \claimref{standard-model.left-right-parity-what-breaks-it}),
    so the $(\overline{10},3,1)$ is not light, and nothing else is light (Fact \claimref{standard-model.imported-pati-salam-representation-theory-survival}(b)).
    Then:

    \begin{enumerate}

    \item[(1)] Fact \claimref{standard-model.imported-coefficient-sum-indices} gives $(b_{4}, b_{2L},
    b_{2R}) = (-\tfrac{23}{3}, -\tfrac{19}{6}, \tfrac72)$ with a real bidoublet, $(-\tfrac{23}{3}, -3,
    \tfrac{11}{3})$ with a complex one, and $(-\tfrac73, 2, \tfrac{26}{3})$ with a complex bidoublet and
    the $(15,2,2)$; Fact \claimref{standard-model.imported-two-loop-gauge-coefficients}''s generic formula
    gives, in the last case, the two-loop matrix $\bigl[\begin{smallmatrix} 2435/6 & 105/2 & 249/2 \\
    525/2 & 73 & 48 \\ 1245/2 & 48 & 779/3 \end{smallmatrix}\bigr]$ (rows $4$, $2L$, $2R$).

    \item[(2)] At one loop, with Lemma \claimref{standard-model.matching-traces} at $M_{I}$ and the inputs
    of Proposition \claimref{standard-model.spectrum-run}, the three couplings meet. With $x = \ln(M_{I}/M_{Z})/2\pi$
    and $y = \ln(M_{U}/M_{I})/2\pi$ the solutions are exact rationals:

    \begin{center}\small

    \begin{tabular}{@{}llllll@{}}

    \toprule

    bidoublet & $x$ & $y$ & $\alpha_{U}^{-1}$ & $M_{I}$ (GeV) & $M_{U}$ (GeV) \\

    \midrule

    real & $\tfrac{11901069}{3355625}$ & $\tfrac{5610391}{3355625}$ & $46.12$ & $4.3 \times 10^{11}$ &
    $1.6 \times 10^{16}$ \\[2pt]

    complex & $\tfrac{25548992}{7116875}$ & $\tfrac{11220782}{7116875}$ & $45.69$ & $5.7 \times 10^{11}$
    & $1.1 \times 10^{16}$ \\[2pt]

    complex, with $(15,2,2)$ & $\tfrac{22055284}{6305625}$ & $\tfrac{11220782}{6305625}$ & $37.11$ & $3.2
    \times 10^{11}$ & $2.3 \times 10^{16}$ \\

    \bottomrule

    \end{tabular}

    \end{center}

    \item[(3)] In the language of Theorem \claimref{standard-model.one-threshold-exact-criterion}, the
    real-bidoublet chain is the one-threshold shift $\Dl = (-\tfrac{76}{15}, 0, -\tfrac23)$ at threshold
    fraction $f = \tfrac{5610391}{17511460} = 0.320$: the extra gauge bosons contribute $(-\tfrac{154}{15},
    0, -\tfrac{11}{3})$ and the $(10,1,3)$ contributes $(\tfrac{26}{5}, 0, 3)$, the bidoublet''s light
    doublet being the Standard Model''s. It satisfies Corollary \claimref{standard-model.direction-demanded-content-doublet-heavy}.
    Negative entries, which no added matter in Proposition \claimref{standard-model.table-exact} can have,
    are what gauge bosons supply.

    \item[(4)] At two loops, from the record''s central values, at record level:

    \begin{center}\small

    \begin{tabular}{@{}llllll@{}}

    \toprule

    bidoublet & $M_{I}$ (GeV) & $M_{U}$ (GeV) & $\alpha_{U}^{-1}$ & $M_{U}$/bound & $\tau_{p}$ (yr) \\

    \midrule

    complex, with $(15,2,2)$ & $1.9 \times 10^{10}$ & $3.4 \times 10^{16}$ & $32.4$ & $6.4$ & $4 \times
    10^{37}$ \\

    complex & $1.4 \times 10^{11}$ & $7.9 \times 10^{15}$ & $45.1$ & $1.8$ & $2 \times 10^{35}$ \\

    real & $9.2 \times 10^{10}$ & $1.2 \times 10^{16}$ & $45.6$ & $2.7$ & $1 \times 10^{36}$ \\

    real, $(\overline{10},3,1)$ light & $4.4 \times 10^{13}$ & $8.9 \times 10^{14}$ & $40.7$ & $0.2$ &
    $3 \times 10^{31}$ \\

    \bottomrule

    \end{tabular}

    \end{center}

    The bound is Fact \claimref{standard-model.imported-proton-condition}''s; the last row keeps left-right
    parity down to $M_{I}$. With the $(15,2,2)$, $M_{I}$ moves between $1.8$ and $2.2 \times 10^{10}$
    GeV across $\alpha_{s} = 0.1180 \pm 0.0009$. Keeping left-right parity down to $M_{I}$ fails the proton
    condition.

    \end{enumerate}'
  env: proposition
  context_refs:
  - standard-model.imported-pati-salam-representation-theory-survival
  - standard-model.imported-proton-condition
  - standard-model.left-right-parity-what-breaks-it
  - standard-model.majorana-element
  - standard-model.matching-traces
  - standard-model.one-threshold-exact-criterion
  - standard-model.spectrum-run
  - standard-model.table-exact
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-pati-salam-representation-theory-survival
    - standard-model.imported-proton-condition
    - standard-model.left-right-parity-what-breaks-it
    - standard-model.majorana-element
    - standard-model.matching-traces
    - standard-model.one-threshold-exact-criterion
    - standard-model.spectrum-run
    - standard-model.hyp-s-slot-statistics
    note: 'Added the seven context_refs that the setup and items use as premises, and left out table-exact,
      cited only for comparison; the paper places the chains in the class of Chang-Mohapatra-Parida and
      Bertolini-Di Luzio-Malinsky, but no imported claim for that standard result is in the store, so
      no standard-route derivation was added. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay level now states Hypothesis
      (S), which it had dropped, the setup conditions (left-right parity broken at $M_U$, nothing else
      light) and the two-loop, record-level basis of the proton verdict.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.matching-traces
    - standard-model.one-threshold-exact-criterion
    - standard-model.spectrum-run
    stated_role:
    - standard-model.imported-pati-salam-representation-theory-survival
    - standard-model.imported-proton-condition
    - standard-model.left-right-parity-what-breaks-it
    - standard-model.majorana-element
    - standard-model.hyp-s-slot-statistics
    note: Proof is an exact or record-level run with no step naming (S); stated its role, the lepton doublet
      of the derived content, from Theorem hypercharge-global-form and Proposition weak-angle, which put
      the lepton doublet under (S).
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
about:
- obj.standard-model.one-threshold-spectrum-admissible
---

## formal
Under Hypothesis (S), take the derived content with one Higgs doublet from $M_{Z}$ to $M_{I}$, and above $M_{I}$ Pati-Salam with three generations, the bidoublet, the complex $(10,1,3)$ whose vev breaks it at $M_{I}$ (Proposition \claimref{standard-model.majorana-element}) and, where named, the complex $(15,2,2)$; left-right parity is broken at $M_{U}$ (Proposition \claimref{standard-model.left-right-parity-what-breaks-it}), so the $(\overline{10},3,1)$ is not light, and nothing else is light (Fact \claimref{standard-model.imported-pati-salam-representation-theory-survival}(b)). Then:
\begin{enumerate}
\item[(1)] Fact \claimref{standard-model.imported-coefficient-sum-indices} gives $(b_{4}, b_{2L}, b_{2R}) = (-\tfrac{23}{3}, -\tfrac{19}{6}, \tfrac72)$ with a real bidoublet, $(-\tfrac{23}{3}, -3, \tfrac{11}{3})$ with a complex one, and $(-\tfrac73, 2, \tfrac{26}{3})$ with a complex bidoublet and the $(15,2,2)$; Fact \claimref{standard-model.imported-two-loop-gauge-coefficients}'s generic formula gives, in the last case, the two-loop matrix $\bigl[\begin{smallmatrix} 2435/6 & 105/2 & 249/2 \\ 525/2 & 73 & 48 \\ 1245/2 & 48 & 779/3 \end{smallmatrix}\bigr]$ (rows $4$, $2L$, $2R$).
\item[(2)] At one loop, with Lemma \claimref{standard-model.matching-traces} at $M_{I}$ and the inputs of Proposition \claimref{standard-model.spectrum-run}, the three couplings meet. With $x = \ln(M_{I}/M_{Z})/2\pi$ and $y = \ln(M_{U}/M_{I})/2\pi$ the solutions are exact rationals:
\begin{center}\small
\begin{tabular}{@{}llllll@{}}
\toprule
bidoublet & $x$ & $y$ & $\alpha_{U}^{-1}$ & $M_{I}$ (GeV) & $M_{U}$ (GeV) \\
\midrule
real & $\tfrac{11901069}{3355625}$ & $\tfrac{5610391}{3355625}$ & $46.12$ & $4.3 \times 10^{11}$ & $1.6 \times 10^{16}$ \\[2pt]
complex & $\tfrac{25548992}{7116875}$ & $\tfrac{11220782}{7116875}$ & $45.69$ & $5.7 \times 10^{11}$ & $1.1 \times 10^{16}$ \\[2pt]
complex, with $(15,2,2)$ & $\tfrac{22055284}{6305625}$ & $\tfrac{11220782}{6305625}$ & $37.11$ & $3.2 \times 10^{11}$ & $2.3 \times 10^{16}$ \\
\bottomrule
\end{tabular}
\end{center}
\item[(3)] In the language of Theorem \claimref{standard-model.one-threshold-exact-criterion}, the real-bidoublet chain is the one-threshold shift $\Dl = (-\tfrac{76}{15}, 0, -\tfrac23)$ at threshold fraction $f = \tfrac{5610391}{17511460} = 0.320$: the extra gauge bosons contribute $(-\tfrac{154}{15}, 0, -\tfrac{11}{3})$ and the $(10,1,3)$ contributes $(\tfrac{26}{5}, 0, 3)$, the bidoublet's light doublet being the Standard Model's. It satisfies Corollary \claimref{standard-model.direction-demanded-content-doublet-heavy}. Negative entries, which no added matter in Proposition \claimref{standard-model.table-exact} can have, are what gauge bosons supply.
\item[(4)] At two loops, from the record's central values, at record level:
\begin{center}\small
\begin{tabular}{@{}llllll@{}}
\toprule
bidoublet & $M_{I}$ (GeV) & $M_{U}$ (GeV) & $\alpha_{U}^{-1}$ & $M_{U}$/bound & $\tau_{p}$ (yr) \\
\midrule
complex, with $(15,2,2)$ & $1.9 \times 10^{10}$ & $3.4 \times 10^{16}$ & $32.4$ & $6.4$ & $4 \times 10^{37}$ \\
complex & $1.4 \times 10^{11}$ & $7.9 \times 10^{15}$ & $45.1$ & $1.8$ & $2 \times 10^{35}$ \\
real & $9.2 \times 10^{10}$ & $1.2 \times 10^{16}$ & $45.6$ & $2.7$ & $1 \times 10^{36}$ \\
real, $(\overline{10},3,1)$ light & $4.4 \times 10^{13}$ & $8.9 \times 10^{14}$ & $40.7$ & $0.2$ & $3 \times 10^{31}$ \\
\bottomrule
\end{tabular}
\end{center}
The bound is Fact \claimref{standard-model.imported-proton-condition}'s; the last row keeps left-right parity down to $M_{I}$. With the $(15,2,2)$, $M_{I}$ moves between $1.8$ and $2.2 \times 10^{10}$ GeV across $\alpha_{s} = 0.1180 \pm 0.0009$. Keeping left-right parity down to $M_{I}$ fails the proton condition.
\end{enumerate}

\emph{Note (one doublet or two, 2 November 2026).} The chain runs with one Higgs doublet from $M_{Z}$ to $M_{I}$, while the rung field is recorded as the elementary linear field with two doublets of hypercharge $\tfrac12$ (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}); above $M_{I}$ a complex bidoublet already carries two. On the branch with a level, now the working branch of the weak scale, the second doublet is heavy, about $2.5$ to $3.5$ TeV, so the content is one doublet up to those masses and two from there to $M_{I}$. The scales $M_{I}$, $M_{U}$ and the tables above are computed with one doublet below $M_{I}$ and are not recomputed with the second doublet between a few TeV and $M_{I}$; that recomputation is open. The two doublets are themselves a reading, following only from the exact null-lift constraint, the Higgs taken exactly as the rung unit and a linear field (\claimref{synthesis.one-doublet-field-is-pure-gauge-on-the-null-lift-locus-so-two-doublets-need-the-exact-constraint}). The content of this result is unchanged.
## technical
Under (S), take the derived content with one Higgs doublet from $M_{Z}$ to the intermediate scale $M_{I}$, and above $M_{I}$ Pati-Salam with three generations, the bidoublet, the complex $(10,1,3)$ whose vev breaks it at $M_{I}$ and, where named, the complex $(15,2,2)$, with left-right parity broken at $M_{U}$ and nothing else light. The index formula gives the one-loop coefficients $(b_{4}, b_{2L}, b_{2R})$, and with the trace matching at $M_{I}$ the three couplings meet, with $x = \ln(M_{I}/M_{Z})/2\pi$ and $y = \ln(M_{U}/M_{I})/2\pi$ exact rationals; with a real bidoublet, for instance, $M_{I} \approx 4.3 \times 10^{11}$ GeV and $M_{U} \approx 1.6 \times 10^{16}$ GeV.

The real-bidoublet chain is the one-threshold shift $\Dl = (-\tfrac{76}{15}, 0, -\tfrac23)$ at threshold fraction $f \approx 0.320$, which satisfies the doublet-heavy direction; its negative entries are supplied by gauge bosons. At two loops, at record level, the chain with the $(15,2,2)$ meets the proton condition with $M_{U}$ a factor $6.4$ above the bound, while keeping left-right parity down to $M_{I}$ fails it. (Note, 2 November 2026: the chain uses one doublet below $M_{I}$, while the rung field is recorded as two doublets, the second heavy, about $2.5$ to $3.5$ TeV, on the working branch; the scales are not recomputed with the second doublet between a few TeV and $M_{I}$, an open item.)
## lay
This result tests whether the three force strengths of the Standard Model can meet at a single high energy when the symmetry first enlarges to the Pati-Salam group at an intermediate scale. Assuming the slots of the composite's basic spinor states behave like the pairs (Hypothesis (S)), and with the particle content the framework then supplies, left-right symmetry broken only at the unification scale and nothing else light, they do meet, with the intermediate scale roughly between $10^{10}$ and $10^{12}$ GeV and the unification scale near $10^{16}$ GeV. At two loops, from the measured couplings' central values, the most favourable version passes the proton-decay limit comfortably, while a version that keeps left-right symmetry down to the intermediate scale does not.

## one-liner
Under (S), the Pati-Salam chain with the framework's content unifies the three couplings at one loop with exact rational scales, and at two loops the version with a complex bidoublet and the $(15,2,2)$ passes the proton condition by a factor of six in $M_{U}$.
