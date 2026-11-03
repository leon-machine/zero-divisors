---
id: sheaf.tame-wall-induction
kind: claim
version: 5
title: Tame wall induction
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras, tameness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.determinant-identity-blow-up-expansion@3
  - sheaf.invariant-form-t3@2
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_shadow_wall_is_a_simple_regular_level_set
- kind: check
  ref: check.py::check_radical_line_is_an_adjugate_column
- kind: check
  ref: check.py::check_jacobi_formula_gives_transversality
locators:
  paper: T04
  number: Lem 5.3
  label: lem:wallinduction
  line: 700
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in two collar models, the determinant identity, the shadow wall as a simple regular zero, the radical line as an adjugate column, and Jacobi formula giving a nonzero transversality datum. Version 4 -> 5.'
  env: lemma
  unresolved_refs:
  - rem:bundlesetup
  typing:
    by: ai-typing-pass
    added:
    - sheaf.tameness
    note: 'Both edges are real premises; the proof uses the transversality condition of the original wall
      to bound the derivative, so the tameness postulate was added to assumes. Levels pass: lay now keeps
      compactness and tameness of the original wall; one-liner phrased as an assumption.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.tameness
---

## formal
Assume $\Sig$ compact, and fix the collar. Near the wall, on the far side, $s$ is strictly monotone along transversals: $s = 1/\lambda + O(1)$ with derivative $s' = -\lambda'/\lambda^2\,(1 + o(1)) \neq 0$, since the singular term dominates the bounded derivative of the smooth remainder; call the (relatively compact) region where this monotonicity holds the \emph{monotone zone}, and let
\[
S \;:=\; \sup\,|s| \quad\text{over the far-side part of the collar \emph{outside} the monotone zone}
\]
(finite: that region has compact closure avoiding $\Sig$). Call the coupling \emph{good} if $|\mu\nu| < 1/(2S)$. For good couplings:
\begin{enumerate}
\item every far-side zero of $F$ lies in the monotone zone with $\beta \equiv 1$ there, so the shadow wall $\Sig'$ is the regular level set $\{F = 0\}$ with $dF = 2\mu\nu\,ds \neq 0$ transversally: a smooth closed hypersurface, and the zero of $\det h$ across it is simple;
\item at each point of $\Sig'$ exactly one $h$-eigenvalue (with respect to an auxiliary frame metric) vanishes, to first order, and the radical line of $h|_{\Sig'}$ is a smooth line subbundle: it is the column space of the adjugate $\operatorname{adj}(h)$, which has rank one along $\Sig'$;
\item the invariant transversality datum of Lemma \claimref{sheaf.invariant-form-t3} (which makes sense verbatim for any bundle with symmetric form) is nowhere zero on $\Sig'$: by Jacobi's formula the simplicity of the zero of $\det h$ \emph{is} the transversality of the degeneration.
\end{enumerate}
Hence $(T, h)$ is itself a tame corank-one degeneration along $\Sig'$, in the bundle-valued sense of Remark \ref{rem:bundlesetup}. The completion therefore iterates: each wall's ambient form is a tame degeneration with its own shadow wall, and the infinite wall sequence exists unconditionally for good couplings, not merely generically.

## technical
Take $\Sig$ compact with a fixed collar. Near the wall on the far side, $s = 1/\lambda + O(1)$ is strictly monotone along transversals; outside this monotone zone, on the far part of the collar, $|s|$ is bounded by a finite $S$. Call the coupling good if $|\mu\nu| < 1/(2S)$. Then every far-side zero of $F = 1 + 2\mu\nu\beta^2 s$ lies in the monotone zone, and the shadow wall $\Sig' = \{F = 0\}$ is a smooth closed hypersurface across which $\det h$ has a simple zero.

Along $\Sig'$ exactly one eigenvalue of $h$ vanishes, to first order, and the radical line is a smooth line bundle, spanned locally by a column of $\operatorname{adj}(h)$. By Jacobi's formula the simplicity of the zero of $\det h$ is the nonvanishing of the transversality datum. So $(T,h)$ is again a tame corank-one degeneration along $\Sig'$, and the completion iterates for every good coupling, not merely generically.

## lay
Repairing a degenerate wall on one side creates a new shadow wall on the other. This result shows that, for a compact original wall that degenerates in the well-behaved (tame) way, if the repair is done gently enough, the shadow wall is just as well behaved as the original. So the same repair can be applied to it, and the process can be repeated.

## one-liner
Assuming a compact tame wall and a good coupling, the shadow wall is a smooth closed hypersurface along which the ambient form is again a tame corank-one degeneration, so the completion iterates.
