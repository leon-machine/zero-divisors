---
id: synthesis.de-sitter-mode-count
kind: claim
version: 3
title: The cosmological horizon's mode count under the black hole's rule
status: proved
region: synthesis
subject: entropy
tags: [the-number-n, mode-counting, horizons, boundary-modes, needs-continuum]
proposed_by:
  kind: ai
  session: de-sitter-count-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.cosmological-horizon-boundary-modes
derivations:
- name: main
  uses:
  - synthesis.de-sitter-entropy-pi-n-squared@5
  - scrambling.residue-each-convention@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_de_sitter_count
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.what
  - standard-model.largeness-number-universes-boundary-modes
  - pred.boundary-mode-density
  - synthesis.de-sitter-temperature-frozen-point-norm
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  note: Performs the application T12's Observation 'What N is' (i) records as not performed by any paper, the boundary-mode count at the cosmological horizon, on the algebra built on 21 October. Part (i) is exact and unconditional given the imported area law; part (ii) is conditional on the counting rule of T08's residue proposition carrying over to the cosmological horizon, a hypothesis stated in the antecedent, not a store postulate.
---

## formal
Let $\Lambda = 3H^{2} > 0$, in units $\hbar = c = 1$ with $G = M_{P}^{-2}$, and let $N := M_{P}/H$ be the number of Fact \claimref{standard-model.imported-frozen-point-dictionary}, which in the series' terms is $N^{2} = M_{P}^{2}/Q(I_{\Lambda})$.
\begin{enumerate}
\item[(i)] By Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared} the horizon has area $A_{\Lambda} = 4\pi N^{2}$ Planck areas and entropy $S_{\Lambda} = \pi N^{2}$.
\item[(ii)] If the cosmological horizon's boundary modes (Definition \claimref{obj.synthesis.cosmological-horizon-boundary-modes}) obey the counting rule of Proposition \claimref{scrambling.residue-each-convention}, one tick per modular period and $\kappa_{c}$ modes per Planck area of horizon, then the number registered per modular period is
\[
|J| \;=\; \kappa_{c}\,A_{\Lambda} \;=\; 4\pi\kappa_{c}\,N^{2} ,
\]
so the count scales as $N^{2}$ whatever the residue. With the black hole's residue it is $|J| = \pi N^{2}/\ln 2$ in the capacity convention ($\kappa_{c} = 1/(4\ln 2)$, the capacity $|J|\ln 2$ then equal to $S_{\Lambda}$) and $|J| = \pi N^{2}$ in the 1-nat convention ($\kappa_{c} = \tfrac14$).
\item[(iii)] Hence, under (ii) in the capacity convention, $N = \sqrt{C/\pi}$ with $C = |J|\ln 2$ the capacity of the horizon's boundary-mode space: the indication of Observation \claimref{standard-model.what}(i), entropy of order $N^{2}$ and $N$ the square root of the capacity, holds exactly for the entropy and up to the factor $\sqrt{\pi}$ for the capacity.
\end{enumerate}

## technical
The series' number $N$ is the Planck mass over the Hubble rate of the cosmological constant, $N = M_{P}/H$, about $10^{61}$. The cosmological horizon is a sphere of radius $1/H$, so its area is $4\pi N^{2}$ Planck areas and its Gibbons-Hawking entropy, a quarter of that, is exactly $\pi N^{2}$; in the series' language, $\pi M_{P}^{2}$ divided by the frozen point's norm. If the imaginary part of the Planck mass's weight is used for $N$ instead, the entropy is $\pi(N^{2} + 9/4)$.

The count of the horizon's boundary modes needs one hypothesis: that they are counted as the black hole's are, $\kappa_{c}$ modes per Planck area of horizon in each modular period. Then the count is $4\pi\kappa_{c}N^{2}$, proportional to $N^{2}$ whatever the residue is. With the black hole's own residue the count is $\pi N^{2}/\ln 2$ modes, whose capacity at $\ln 2$ each equals the entropy, so $N$ is the square root of the capacity divided by $\pi$. The T12 observation that the entropy is of order $N^{2}$ is therefore exact, and its reading of $N$ as the square root of the capacity holds up to $\sqrt{\pi}$. That last step adds nothing beyond the area law: the black hole's residue was calibrated so that the capacity is a quarter of the area, which is also what the Gibbons-Hawking entropy is. The count itself is about $4.8 \times 10^{122}$ modes, so $N$ is roughly its square root, not the number of modes.

## lay
The series condenses the smallness of the cosmological constant into one large number, $N$, about $10^{61}$. An earlier paper guessed that $N$ counts the universe's own horizon modes, roughly as the square root of their number, but never did the count. With the horizon's modes now built, the count can be done. The horizon's entropy comes out as exactly $\pi$ times $N$ squared, about $3 \times 10^{122}$. If the horizon's modes are counted the way the series counts a black hole's, their number is $\pi N^{2}/\ln 2$. So the guess was right in form: $N$ is, up to a factor of about $1.8$, the square root of the horizon's information capacity. What fixes the counting rule's coefficient is still open, as it is for black holes.

## one-liner
The cosmological horizon's entropy is exactly $\pi N^{2} = \pi M_{P}^{2}/Q(I)$, and under the black hole's counting rule its mode count is $4\pi\kappa_{c}N^{2}$, so in the capacity convention $N = \sqrt{C/\pi}$ for its capacity $C$.
