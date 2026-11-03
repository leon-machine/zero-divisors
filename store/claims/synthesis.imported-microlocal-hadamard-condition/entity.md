---
id: synthesis.imported-microlocal-hadamard-condition
kind: claim
version: 2
title: 'Imported: the microlocal form of the Hadamard condition (Radzikowski 1996), and for the Dirac field on both orderings of the two-point function (Hollands 2001), under which Hadamard states differ by smooth kernels'
status: imported
region: synthesis
subject: thermality
tags: [horizons, car-algebra, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'M. J. Radzikowski, Micro-local approach to the Hadamard condition in quantum field theory on curved space-time, Commun. Math. Phys. 179 (1996), 529--553.'
  key: Radzikowski1996
  doi: 10.1007/BF02100096
- citation: 'S. Hollands, The Hadamard condition for Dirac fields and adiabatic states on Robertson-Walker spacetimes, Commun. Math. Phys. 216 (2001), 635--661; arXiv:gr-qc/9906076.'
  key: Hollands2001
  locator: 'Def. IV.1; Thm. IV.2'
  doi: 10.1007/s002200000350
- citation: 'C. J. Fewster, Lectures on quantum energy inequalities, arXiv:1208.5399.'
  key: Fewster2012
  locator: 'Secs. 2.3, 3.2'
extraction:
  note: >-
    Imported so that the result on the microlocal condition on a horizon generator can pin the bulk
    condition whose generator analogue it poses, instead of citing it from memory. Checked on 2026-11-01:
    Radzikowski 1996 against the publisher's record of DOI 10.1007/BF02100096 (title, author, journal,
    volume 179, pages 529-553, year) and its abstract (for the two-point distribution of a quasi-free
    neutral Klein-Gordon field, the global Hadamard condition of Kay and Wald, the Feynman propagator being
    a distinguished parametrix, and the wave front set spectral condition are equivalent; a micro-local
    proof that Cauchy evolution preserves the Hadamard form, by propagation of singularities). Hollands
    against the arXiv text of gr-qc/9906076: Definition IV.1 (a quasi-free Dirac state is Hadamard if the
    primed wave front sets of the two two-point functions are the sets of null-related covectors with
    future-directed, respectively past-directed, first covector), the sentences that the condition "needs
    to be imposed separately for the positive and negative frequency twopoint functions" and that the
    conditions on the two are "in general independent", and "all Hadamard states differ by a smooth piece
    only" (proof of Thm. IV.1, citing Thm. IV.2); the DOI against the arXiv record. Cited from memory, not
    checked: the journal volume and pages of Hollands (Commun. Math. Phys. 216 (2001) 635-661), and the
    explicit form of the set C^+ in Radzikowski's own sign convention (the form stated is that of Hollands'
    Definition IV.1). For
    the scalar field, that two Hadamard two-point functions differ by a smooth function (now stated in (a),
    version 2) was checked on 2026-11-01 against C. J. Fewster, Lectures on quantum energy inequalities,
    arXiv:1208.5399, Sec. 2.3 ("the difference of two Hadamard 2-point functions is smooth") and Sec. 3.2;
    that it follows from the Feynman propagator being a distinguished parametrix, unique up to smooth
    kernels, is cited from memory. No restriction
    of a four-dimensional Hadamard state to the algebra of one null generator is part of this Fact.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decision of 2026-11-01 approving Radzikowski 1996 and Hollands 2001 as routine imports, so that synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state cites them as Facts; partly verified (see note).'
  maintainer_pass_deposit_state:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (deposit-state imports): clause (a) now states the smooth-difference property of scalar Hadamard two-point functions, which the deposit-state results use and the note had cited from memory; checked against Fewster''s lectures (see note). Clause (b) and the Dirac statement unchanged.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric $g$ is globally hyperbolic, read on several charts where its global structure needs them. For nonzero covectors write $(x_{1}, \xi_{1}) \sim (x_{2}, \xi_{2})$ if $x_{1} \neq x_{2}$ lie on a null geodesic $\gamma$ of $g$, $\xi_{1}$ is cotangent to $\gamma$ at $x_{1}$ and $\xi_{2}$ is its parallel transport along $\gamma$, or if $x_{1} = x_{2}$ and $\xi_{1} = \xi_{2}$ is null. For a distribution $D$ on $M \times M$ write $\mathrm{WF}'(D) = \{(x_{1}, \xi_{1}; x_{2}, \xi_{2}) : (x_{1}, \xi_{1}; x_{2}, -\xi_{2}) \in \mathrm{WF}(D)\}$, and let $C^{\pm} = \{(x_{1}, \xi_{1}; x_{2}, \xi_{2}) : (x_{1}, \xi_{1}) \sim (x_{2}, \xi_{2}),\ \xi_{1}\ \text{future-directed (}+\text{), past-directed (}-\text{)}\}$, in the Fourier convention of the sources.
\begin{enumerate}
\item[(a)] (Radzikowski.) For the two-point distribution $\Lambda$ of a quasi-free state of the neutral Klein-Gordon field, the global Hadamard condition of Kay and Wald holds if and only if $\Lambda$ satisfies the wave front set spectral condition, $\mathrm{WF}'(\Lambda) = C^{+}$ (equivalently, the associated Feynman propagator is a distinguished parametrix). The Hadamard form is preserved by Cauchy evolution, by propagation of singularities. Any two such Hadamard two-point distributions differ by a smooth function on $M \times M$ (added in version 2).
\item[(b)] (Hollands; the Dirac field.) For a quasi-free state $\omega$ of the Dirac field with the two two-point functions $\mathcal{G}^{(+)}(h, f) = \omega(\Psi(f)\bar\Psi(h))$ and $\mathcal{G}^{(-)}(h, f) = \omega(\bar\Psi(h)\Psi(f))$, $\omega$ is Hadamard if $\mathrm{WF}'(\mathcal{G}^{(\pm)}) = C^{(\pm)}$. The conditions on $\mathcal{G}^{(+)}$ and $\mathcal{G}^{(-)}$ are in general independent and are imposed separately. Any two Hadamard states differ by a smooth piece: the differences of their two-point functions are smooth kernels.
\end{enumerate}
\emph{Provenance:} \cite{Radzikowski1996}; \cite[Def.~IV.1, Thm.~IV.2]{Hollands2001}; for the scalar smooth-difference statement \cite[Secs.~2.3, 3.2]{Fewster2012}. Not part of this Fact: a restriction of a Hadamard state of a four-dimensional field to the algebra of one null generator; the store's generator condition is an analogue posed directly on that algebra.

## technical
The Hadamard condition is the standard requirement on physical states of a free quantum field in a gravitational background: at short distances the two-point function has the same singularity as the vacuum's, so that the energy density can be renormalised by point splitting. Radzikowski showed that, for the scalar field, it is equivalent to a condition on the wave front set of the two-point function: its singularities lie only on pairs of points joined by light rays, with the frequency positive along the ray. Hollands gave the corresponding condition for the Dirac field, which has two two-point functions, one for each ordering of the field and its adjoint; the condition is imposed on each separately, the two being independent. In both cases two Hadamard states differ by a smooth kernel, and the condition is preserved by the field equation's evolution from a Cauchy surface. Applying the condition to the algebra of one horizon generator is an analogue adopted in the result that cites this Fact, not part of the Fact.

## lay
Physicists require that a reasonable quantum state of a field, looked at closely enough, resembles empty space. Radzikowski found a precise way to say this in terms of where the state's correlations are infinitely sharp and in which direction their energy flows, and Hollands extended it to electrons and other particles of spin one half. Any two states meeting the requirement differ only by something smooth. These are taken from the literature.

## one-liner
A quasi-free Klein-Gordon state is Hadamard exactly when its two-point function satisfies the wave front set spectral condition $\mathrm{WF}'(\Lambda) = C^{+}$ (Radzikowski 1996); a quasi-free Dirac state is Hadamard when $\mathrm{WF}'(\mathcal{G}^{(\pm)}) = C^{(\pm)}$ on both orderings, imposed separately (Hollands 2001); Hadamard states differ by smooth kernels.
