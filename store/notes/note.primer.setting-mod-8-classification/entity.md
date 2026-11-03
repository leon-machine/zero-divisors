---
id: note.primer.setting-mod-8-classification
kind: note
version: 1
title: The mod-8 classification
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Setting
  section: The mod-8 classification
  line: 396
---

## formal
Every real Clifford algebra is a matrix algebra, or a pair of matrix algebras, over $\R$, $\C$ or $\HH$, and which one depends only on $p - q$ modulo 8 \cite{ABS1964, Porteous1995, Lounesto2001}:

\begin{center}
\begin{tabular}{cl@{\qquad}cl}
\toprule
$p-q \bmod 8$ & type & $p-q \bmod 8$ & type \\
\midrule
$0$ & $\Mat_k(\R)$              & $4$ & $\Mat_k(\HH)$ \\
$1$ & $\Mat_k(\R) \oplus \Mat_k(\R)$ & $5$ & $\Mat_k(\HH) \oplus \Mat_k(\HH)$ \\
$2$ & $\Mat_k(\R)$              & $6$ & $\Mat_k(\HH)$ \\
$3$ & $\Mat_k(\C)$              & $7$ & $\Mat_k(\C)$ \\
\bottomrule
\end{tabular}
\end{center}

\noindent In each case the matrix size $k$ is fixed by the dimension count $2^{n}$. The small algebras are worth knowing by name: $\Cl(1,0) \cong \R \oplus \R$ (residue 1, split), $\Cl(0,1) \cong \C$ (residue 7), $\Cl(2,0) \cong \Cl(1,1) \cong \Mat_2(\R)$ (residues 2 and 0), $\Cl(0,2) \cong \HH$ (residue 6), $\Cl(0,3) \cong \HH \oplus \HH$ (residue 5), and the spacetime algebra $\Cl(1,3) \cong \Mat_2(\HH)$ (residue 6). The doubled rows, residues 1 and 5, are the \emph{split} algebras, the ones that decompose into two ideals; what that means for division is T1's type-C case.

The table repeats with period 8, and the repetition has a mechanism: adding one $(+1)$ and one $(-1)$ direction at once leaves $p - q$ unchanged and doubles the matrix size,
\[
\Cl(p{+}1,\, q{+}1) \;\cong\; \Mat_2\bigl(\Cl(p,q)\bigr),
\]
the $(1,1)$-periodicity theorem. This matters here, because the added $(+1,-1)$ pair spans exactly a hyperbolic plane: the unit of Example \claimref{note.primer.hyperbolic-plane} is also the unit of the classification's own periodicity.

## technical
pending

## lay
pending

## one-liner
pending
