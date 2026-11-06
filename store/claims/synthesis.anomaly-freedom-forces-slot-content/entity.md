---
id: synthesis.anomaly-freedom-forces-slot-content
kind: claim
version: 3
title: 'Anomaly freedom forces odd slots and the slot content of (S)'
status: proved
region: synthesis
subject: standard-model
tags: [hypercharge-and-anomalies, hypotheses-s-r-c, classification]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
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
  - standard-model.imported-anomaly-coefficients@1
  - standard-model.global-form-quotient-determined@3
  - standard-model.imported-pair-systems-two-chirality-halves@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_anomaly_freedom_forces_slot_content
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.hyp-s-slot-statistics
  - standard-model.quarks-leptons-two-level-fermion-content
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The slot-module hypothesis was restated on 2026-10-23 (version 2: clauses (c), (d), (e) replaced by the generation clause (G) and chirality as a CPT halving); the clauses this result bears on are those of version 1, and its mathematics stands. Version 1 -> 2. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 2 -> 3.'
  open_problem: op.hypothesis-s
  note: Replaces Hypothesis (S) by a weaker structural assumption, that the composite's state space is a slot module tensored with the pair system, with chirality the tower grading (-1)^(pi n + k) for a slot parity pi and hypercharge the centre of S(U(2) x U(3)), and shows that the four imported anomaly conditions on the particle half then force pi = 1 (odd slots) and the slot module to be m copies of the two-mode fermionic Fock space as a graded U(2)-module, with the exclusion principle for any equivariant slot creation map. No premise holds given (S). What (S) adds beyond this is m = 1, and the declaration that the five modes form one Clifford system; neither is derived. The assumption excludes the tensor state space of standard-model.quarks-leptons-two-level-fermion-content(2), which has no single pair system, so this does not contradict that clause. Transport-convenient (the pair system is the series' Fock module; the classification is representation theory). Imported from memory, used in the proof only for clause (3) and the parafermion remark - Pieri's rule and Schur's lemma for U(2); H. S. Green, Phys. Rev. 90 (1953) 270 for the parafermion ansatz, used only as a construction that the script carries out. Mixed sums are in the normalisation of the imported Fact (doublets and triplets weighted by multiplicity), extended to higher SU(2) representations by twice the Dynkin index. The SU(2) global anomaly is also checked by the script and vanishes for the solutions; it is not part of the statement. A suggested decision for Leon (not a store change) - whether T12's outcome "adopt the weaker constituent hypothesis" is to be stated as this assumption plus anomaly freedom.
---

## formal
Let $F = \bigoplus_{n \ge 0} F_{n}$ be a finite-dimensional polynomial representation of $U(2)$, graded by the slot number $n$ (the scalar $\mu I_{2}$ acting on $F_{n}$ as $\mu^{n}$), and let $W$ be the pair space of Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}. On the composite space $F \otimes \Lambda^{\bullet}W$ let $(A, B) \in S(U(2) \times U(3))$ act as $A \otimes \Lambda^{\bullet}B$, so that the abelian factor of Theorem \claimref{standard-model.global-form-quotient-determined} acts on $F_{n} \otimes \Lambda^{k}W$ by $\lambda^{3n - 2k}$ and $Y = (3n - 2k)/6$. Fix a slot parity $\pi \in \{0, 1\}$, let the chirality be the grading $(-1)^{\pi n + k}$, and let the particle half be its $+1$ part. The anomaly sums are those of Fact \claimref{standard-model.imported-anomaly-coefficients}, the $[SU(2)]^{2}U(1)$ sum weighting a weak representation of spin $j$ by $\tau_{j} = \tfrac23 j(j+1)(2j+1)$ (twice its Dynkin index, so a doublet counts once, as in the Fact). For a $U(2)$ irreducible $F_{\lambda}$, $\lambda = (\lambda_{1} \ge \lambda_{2} \ge 0)$, write $n = \lambda_{1} + \lambda_{2}$, $d = \lambda_{1} - \lambda_{2} + 1$ and $\tau = \tau_{(\lambda_{1} - \lambda_{2})/2}$.
\begin{enumerate}
\item \emph{(Per-irreducible coefficients.)} The particle half of $F_{\lambda} \otimes \Lambda^{\bullet}W$ contributes, for either $\pi$, $2d(n - 1)$ to the gravitational sum $\sum Y$ and $2\tau(n - 1)$ to the $[SU(2)]^{2}U(1)$ sum; to the $[SU(3)]^{2}U(1)$ sum it contributes $\tfrac{d}{6}\bigl(3(n - 1) - (-1)^{n}\bigr)$ for $\pi = 1$ and $\tfrac{d}{6}(3n - 4)$ for $\pi = 0$; for $\pi = 1$ and $\lambda = (a, a)$ it contributes $a^{3} + 3(a - \tfrac23)^{3}$ to the $U(1)^{3}$ sum.
\item \emph{(Classification.)} The particle half satisfies the four anomaly conditions of the Fact if and only if $\pi = 1$ and $F \cong (\Lambda^{\bullet}\C^{2})^{\oplus m}$ as a graded $U(2)$-module for some $m \ge 0$. At $\pi = 0$ no nonzero $F$ qualifies. For $\pi = 1$ the particle half is then $m$ copies of
\[
(1,1)_{0} \oplus (1,\bar{3})_{-2/3} \oplus (2,3)_{1/6} \oplus (2,1)_{-1/2} \oplus (1,1)_{1} \oplus (1,\bar{3})_{1/3},
\]
which also has vanishing $[SU(3)]^{3}$ coefficient.
\item \emph{(Exclusion.)} For such $F$, every $U(2)$-equivariant slot creation map $a^{\dagger} : \C^{2} \otimes F_{n} \to F_{n+1}$ satisfies $a^{\dagger}(u)a^{\dagger}(u') = -a^{\dagger}(u')a^{\dagger}(u)$ for all $u, u' \in \C^{2}$; in particular $a^{\dagger}(u)^{2} = 0$.
\item \emph{(Parafermionic slots.)} The order-$p$ parafermionic Fock space on two slot modes (Green's ansatz with $p$ components) is, for $p = 1, 2, 3, 4$, the sum of the $F_{\lambda}$ with $\lambda_{1} \le p$, each once; for $p \ge 2$ it contains $F_{(2,0)}$, so its particle half fails the $[SU(2)]^{2}U(1)$ condition at either parity. At $p = 2$ and $\pi = 1$ the four sums are $20$, $12$, $\tfrac{14}{3}$ and $\tfrac{254}{9}$.
\end{enumerate}

## technical
Keep everything in Hypothesis (S) except the slot statistics and the slot parity: let the slots carry any finite graded representation $F$ of the slot mixing $U(2)$, with slot number counted by its centre, tensor it with the pair system $\Lambda^{\bullet}W$, take hypercharge from the centre of $S(U(2) \times U(3))$, and take as particles the $+1$ part of the tower grading $(-1)^{\pi n + k}$, $\pi$ the parity of a slot quantum. Each irreducible $F_{\lambda}$ contributes to the four anomaly sums by closed formulas in its slot number $n$ and dimension. The $[SU(2)]^{2}U(1)$ sum is a sum of nonnegative terms that vanish only for weak singlets and for $n \le 1$, which removes every weak multiplet with two or more slot quanta, at either parity. The gravitational and $[SU(3)]^{2}U(1)$ sums then fix the multiplicities of the vacuum and the doublet in terms of the singlets $\det^{a}$: at even slot parity the doublet's multiplicity would be $-\sum_{a} a\,m_{(a,a)}$, so everything vanishes; at odd slot parity the cubic sum reduces to $\sum_{a} 2a(2a - 1)(a - 1)\,m_{(a,a)} = 0$, which removes every $\det^{a}$ with $a \ge 2$. What survives is odd slots carrying exactly $m$ copies of the two-mode fermionic Fock space, and the exclusion principle follows for any equivariant creation map because $\mathrm{Sym}^{2}\C^{2}$ does not occur in $\Lambda^{2}\C^{2}$. Parafermionic slots of order two or more carry a weak triplet with two quanta and are anomalous.

## lay
The series' Standard-Model paper needs a premise, called (S), saying that the two places a composite's twistors occupy behave like fermions. This result keeps the rest of that setting but lets those places behave in any way compatible with the symmetry, and lets their contribution to handedness be either odd or even. Requiring that the resulting particles be free of gauge anomalies, the consistency condition every chiral gauge theory must meet, forces the places to count as odd for handedness and to have exactly the fermionic pattern, possibly repeated several times, and forces the exclusion principle. More exotic behaviour, such as parafermions, and even places, give anomalous particle content.

## one-liner
With the composite space a $U(2)$ slot module tensored with the pair system, hypercharge from the centre and chirality the tower grading $(-1)^{\pi n + k}$, the particle half is anomaly-free if and only if the slots are odd ($\pi = 1$) and the slot module is $m$ copies of $\Lambda^{\bullet}\C^{2}$, and then equivariant slot creation obeys exclusion; parafermionic slots of order $p \ge 2$ are anomalous.
