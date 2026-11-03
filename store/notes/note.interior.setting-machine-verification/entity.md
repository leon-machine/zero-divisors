---
id: note.interior.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: singularity
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
comments_on:
- interior.gauge-trajectory-unipotent-ray
- interior.exact-scale-decoupling
- interior.stabilisers-flat-model
- interior.non-null-stabilisers-section-they-act
locators:
  paper: T06
  number: Setting
  section: Machine verification
  line: 931
---

## formal
Every computational identity of Parts one and two, and every printed constant of Part three, is verified by the deposited script \texttt{verify\_T06.py} \cite{ButlerVerifyT06}, which imports the series' shared exact-arithmetic library \texttt{GA.py} and runs in exact rational arithmetic, so every check is an identity, not an approximation, with the single exception of one CONTROL check in floating point (marked as such, on matrix exponentials, whose exact content is carried by the six identities beside it). Eighty-two checks pass: eighty-one exact checks and the CONTROL check, which needs \texttt{numpy} and \texttt{scipy}; when those cannot be imported the script prints an explicit SKIPPED line for it and the count is eighty-one, so a reader without them can still run every exact check. The coverage, by part. \emph{Part one:} the pseudoscalar algebra; the unipotent ray (Proposition \claimref{interior.gauge-trajectory-unipotent-ray}: $P^2 = 0$ on the frame, the group law, the closed-form inverse, all Painlev\'e-Gullstrand metric entries at sample rational $\beta$ inside, at, and outside the horizon ($\beta = 1$ included), and the null roots $\lambda = -\beta \pm 1$); the shape operator (Proposition \claimref{interior.exact-scale-decoupling}: the conjugation table, the spectrum $(-2,-2,1,1,1,1)$, $S^2 + S = 2$ as an operator identity on all six frame planes, the trace summed from the computed spectrum). \emph{Part two:} the flat model over $\mathbb{Q}$ (Proposition \claimref{interior.stabilisers-flat-model}: the point embedding is null with the stated pairing, the stabiliser of the vector $\nInf$ has dimension exactly ten and of the ray eleven, computed as kernel ranks of the $15 \times 6$ action matrix by exact Gaussian elimination; the grading, Levi, and nilradical actions; two-step nilpotency of $\nInf \wedge w$ with square image in $\R\nInf$, and the exact translation exponential $e^{tN}X(x) = X(x - tw)$ at rational samples); the non-null stabilisers (Proposition \claimref{interior.non-null-stabilisers-section-they-act}: dimension ten and complement signatures $(1,4)$ and $(2,3)$ by exact congruence diagonalisation); the Schouten arithmetic of Lemma \claimref{interior.metric-parallelism-trace-schouten-condition} and Theorem \claimref{interior.scale-tractor-leaves-cone} as identities of rational functions in a formal $\Lambda$; and the algebraic part of the tractor connection \eqref{eq:tractorconn} as a $6 \times 6$ matrix: metric preservation (Lemma \claimref{interior.metric-parallelism-trace-schouten-condition}(i)) with a flipped-sign control, $\nabla_a I_g = (0, -\Sch_{ab}, 0)$ and the null norm (Theorem \claimref{interior.covariant-form-vacuum-equations}), and the parallelism of $(1, 0, \Lambda/6)$ with norm $\Lambda/3$ evaluated through the tractor metric, with a non-Einstein control (Theorem \claimref{interior.scale-tractor-leaves-cone}), and the index order of the Schouten slot fixed on a non-symmetric sample. \emph{Part three, first half:} the Kasner exponent identities; for Section \ref{subsec:tangential}, the series $S(r) = 1 + \tfrac{3}{10}r + \tfrac{9}{56}r^2 + \cdots$, the expansion of $\tau\sigma_3$ with its three printed coefficients and the sign of every computed coefficient of $\delta$, the leading $\tfrac23\cot\theta\, r^{1/2}$ of the rotation coefficient $\varepsilon$ built from the $\tau$ series at a rational latitude, the rates in $\tau$ read off the leading exponents of $\delta$, $\varepsilon$ and $\tau$ against the constructed inversion $(3\tau/2)^{2/3} = r + O(r^2)$, and the Cauchy-Schwarz bound $\|H\| \le 1$ of Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} at rational unit directions, attained at the Schwarzschild exponents (Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}), plus the floating-point control that the transport distance halves per quartering of $r$ at three latitudes while a fixed coordinate segment diverges (Corollary \claimref{interior.schwarzschild-lines-exactly}); the series $\tau(\rho)$, its $\tfrac23$-power inversion, and the Hubble-normalised rates, as exact truncated power series in $\rho = \sqrt r$ (the printed constants $-\tfrac13$, $-\tfrac{4}{15}$, $\tfrac23$, $-\tfrac{2}{15}$ are all checked, via a J.C.P.\ Miller recurrence for rational powers of unit series, promoted into \texttt{GA.py} for the series' later use); the identification of the Kasner exponents with the computed boundary values of the rates, and the $R$-variable expansion extracted from those rates by exact division against $R(\rho)$, its constants matching the printed ones and its residual starting at $\rho^6$; the boost-generation lemma (Lemma \claimref{interior.boosts-generate-exactly-levi-factor}: the commutator closure of the three boosts has dimension exactly six, contains all three rotations, and annihilates both null directions); and the Schwarzschild-de Sitter comparison (Theorem \claimref{interior.schwarzschild-de-sitter-weighted-limit}: the $\tau$-coefficients agree through order $\rho^8$ at two rational values of $\Lambda$, the first discrepancy is exactly $-\Lambda\rho^9/27$ and linear in $\Lambda$, and the rate constants are unchanged). \emph{Part three, second half:} Kerr-Schild unipotency ($P_k^2 = 0$, and the inverse-metric and metric identities $\hb(a)\cdot\hb(b) = a\cdot b + 2H(a\cdot k)(b\cdot k)$ and $\hb^{-1}(a)\cdot\hb^{-1}(b) = a\cdot b - 2H(a\cdot k)(b\cdot k)$ on all sixteen frame pairs at three values of $H$); the complex subalgebra as a field with exact inverses; the disc-interior scale $M I (a\cos\theta)^{-3}$, built from an independently computed inverse cube; the reduction at $a = 0$, where the real scale $-M/r^3$ returns Fact \claimref{interior.imported-schwarzschild-curvature-spectrum}'s eigenvalues $+2M/r^3$ on the plane pair and $-M/r^3$ on the four mixed planes, with the opposite overall convention failing as a control; the complex eigenvalue table $2 : (-1)$ with the same $S$, now on complexified bivectors; and the Killing-spinor identity $\chi^3\,\mathfrak M = -M$, with $\mathfrak M$ built from an independently computed inverse cube and negative controls at exponents two and four. The script exits nonzero on any failure and prints one line per check, tagged by the statement it certifies.

## technical
pending

## lay
pending

## one-liner
pending
