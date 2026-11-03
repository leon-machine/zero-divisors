---
id: note.programme.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: standard-model
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T17, deposited version
comments_on:
- programme.n-parameter-of-the-laws
locators:
  paper: T17
  number: Setting
  section: Machine verification
  line: 676
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
A survey proves little and quotes much, so its script has a different task from the companion scripts': it is a \emph{consistency audit}. The script \texttt{verify\_T17.py} \cite{ButlerVerifyT17} imports the series' shared exact-arithmetic library \texttt{GA.py}; exact rationals, integers, and certified interval brackets throughout, no floating point anywhere; seventy-five checks when every companion file is present, all passing, in six parts. What it audits is stated exactly. For each of the seventeen companion papers T0 to T16 it opens the companion's compiled PDF and reads the page count from the file's own page tree, and it reads the companion's check count from the count the companion paper records in the version block of its source (or, when invoked with \texttt{--run-siblings}, from a fresh run of the companion script, counting the PASS lines it prints), and compares both with the status table and with the script's own recorded values; a companion file that is absent is reported as skipped, never as passing. It parses this paper's four tables from the source and counts their rows. It recomputes the physical numbers the paper quotes. Because this paper is kept current, the audit is also its refresh mechanism: when a review round changes a companion's page or check count, the corresponding check fails until this survey is regenerated, so a stale quotation is a reported error rather than a silent one.

\emph{Part A: the series' counts} (forty-seven checks). The paper inventory (eighteen papers, numbered consecutively, the identifiers 0 through 17 read from the file stems); the status table parsed and compared with the recorded page and check counts; the series total of 1762 computed from the recorded counts and compared with every place the body prints it; seventeen page counts read from the companion PDFs; seventeen check counts read from the companion papers' records or scripts; the version column read against the version printed on the title page of each of the twenty papers in the table; the refutation table's rows covering the ordinals 1 to 17 exactly once, each row naming its carrying paper; the stance table's six-plus-six, numbered in order; the ten open directions, each assigned; the measure's cardinality, two numbers and one bit, at each site the paper states it; and this paper's own compile log, which must carry no float-overflow warning (every table here is a breakable longtable) and no undefined reference.

\emph{Part B: the black-hole numbers}, as exact monomials in $\pi$ and $M$: $\beta = 8\pi M$ with $\beta/2\pi = 4M$; the epoch volume $V = \beta^{2} = 64\pi^{2}M^{2}$; the equivalence $\nu = 1/16\pi \iff N_{\mathrm{epoch}} = \nu V = 4\pi M^{2} = S_{\mathrm{BH}}$; and the naive count's overshoot by exactly $16\pi$, the horizon-area coefficient.

\emph{Part C: the dark count.} The sterile residues computed as the fixed points of $r \mapsto -r$ mod 8 (exactly $\{0, 4\}$); the count of five dark causal residues; and the ratio arithmetic T14 states, with five entering none of it: the symmetric remainder $4.364 = 5.364 - 1$ once the mirror's one share is removed; that remainder as $\Omega h^{2} = 4.364 \times 0.02237$, inside $0.0976 \pm 0.0012$; and the mirror's share of the dark density, $1/5.364$, between $18.6$ and $18.7$ percent.

\emph{Part D: the matter numbers.} The two exact one-loop rationals ($78761/379488$ and $6539/28320$) bracketed to four decimals, with the over-twenty-times-closer inequality against the measured angle; the integer bracket $2^{398} < 10^{120} < 2^{399}$; the hypercharge quadratic's roots, sum, and product; $3/8$ as the exact trace ratio; the frozen-point norm $Q(I) = \Lambda/3$ as a rational-function identity in formal $\Lambda$, and the dictionary's sign, $m^{2} = -w(w+3)\Lambda/3$, positive at the midpoint $w = -\tfrac32$ of the real interval $[-3, 0]$ and negative at $w = 1$ outside it, with the principal-series form $m^{2} = (\nu^{2} + \tfrac94)\Lambda/3$ at $w = -\tfrac32 + i\nu$ as a polynomial identity in formal $\nu$; and the compression identity $G\Lambda N^{2} = 3$.

\emph{Part E: the neutrino numbers}, by certified interval arithmetic (integer-square-root brackets on the mass-squared splittings): the normal-ordering floor confined to $(0.057, 0.061)$ eV and containing the predicted $0.059$; the $0.052$ eV zero-extending-prior bound strictly below the floor; the $0.092$ eV physical-prior bound above it; the inverted-ordering requirement above $0.097$ eV; the two $m_{\beta\beta}$ values recomputed from the splittings and the mixing brackets under the hierarchy premise and real breaking, bracketing $1.5$ and $3.7$ meV inside the hull $1.3$ to $3.9$ meV and below next-generation sensitivity; the quoted Koide value inside $2/3 \pm 10^{-5}$; and the Cabibbo bracket containing $0.225$.

\emph{Part F: the capacity identities.} The Witt index of Lorentzian signature (one); the increment identity on an exhaustive grid; and the ascended capacity three, equal on both sides of the chart.

What the audit does not and cannot check is what no script can: whether the source papers' proofs are correct (their own scripts and Leon's review carry that), whether the tiers are correctly assigned, whether the payload and remainder cells describe their papers faithfully, and whether the method section's claims about method are true of the practice. The audit guarantees a weaker and more useful thing: that the page and check counts this survey quotes are the companions' own, that its tables agree with one another, and that the physical numbers it repeats recompute.

## technical
pending

## lay
pending

## one-liner
pending
