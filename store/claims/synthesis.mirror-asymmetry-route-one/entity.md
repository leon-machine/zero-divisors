---
id: synthesis.mirror-asymmetry-route-one
kind: claim
version: 3
title: The mirror's asymmetry by the audit route, and what that route needs
status: proved
subject: dark-matter
tags: [needs-continuum]
proposed_by:
  kind: ai
  session: synthesis-gaps-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, clause (iii) and the close updated to P2 at version 2, which states the scoping route one needs (restatement)'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
derivations:
- name: main
  uses:
  - odd-extensions.two-towers-one-curved-universe@6
  - dark-matter.orientation-arrow-seventeenth-refutation@10
  - dark-matter.flag-bit-exists-exactly-tower-dimension@3
  - dark-matter.mirror-tower-copy-one@8
  - dark-tower-matter.mirrors-temperature-p2@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_reversal_keeps_flag
lineage:
  motivated_by:
  - dark-matter.mirror-tower-copy-one
about:
- obj.dark-matter.witt-flag
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Stale wording in the formal level (DECISIONS G2, R05 item 3; restatement): (iii) said that route one needs a scoping of P2 ''and no premise in the store states one'', and the close said clause (v) rests on route two; P2 at version 2 (2026-10-22) states exactly that scoping, labels not states, which reaches Q = epsilon N and not the temperature (synthesis.tower-charge-sector-label-temperature-not). (iii), the close, the technical level and proof Step 4 now say so: under P2@2 clause (v) has both routes. No assumes edge is added (route two carries (v) without P2), and Leon''s answer 2 leaves P2 unchanged, so the sentence stands.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check entries synced with check.py: +1, -1 (added check_reversal_keeps_flag; removed test_reversal_keeps_flag). Version 1 -> 2.'
  review_fixes:
    by: ai-review-fix
    date: 2026-10-21
    note: 'Referee fixes: route one needs an orientation input of route two''s kind, not already contains it; Phi cited from the theorem''s proof; lay wording; check derives LambdaPhi from Phi.'
---

## formal
Let $\Phi : (\sigma, \mu, \rho) \mapsto (\sigma, \mu, -\rho)$ be the scale-independent map from this tower's tractor fibre, metric $h$ of signature $(2,4)$, to the mirror's, metric $h'$ of signature $(4,2)$, with $h'(\Phi X, \Phi Y) = -h(X, Y)$ (the proof of Theorem \claimref{odd-extensions.two-towers-one-curved-universe}), extended to $V_{\C}$.
\begin{enumerate}
\item[(i)] $\Phi$ carries every Witt pair $(W, W')$ of $(V_{\C}, h)$ to the Witt pair $(\Phi W, \Phi W')$ of $(V_{\C}, h')$, with $\Phi W = W$ when $W$ is spanned by the $\sigma$-direction and vectors of $\mu_{\C}$. On the Fock modules, $\Lambda\Phi : \Lambda W' \to \Lambda \Phi W'$ intertwines the creation operators, intertwines the annihilation operators up to the sign $-1$ that the reversed form puts on every contraction, and intertwines every mode number operator exactly, the two signs cancelling. So $\Phi$ carries the Fock grade $k$ to grade $k$, particles to particles, and the asymmetry per mode of this tower, measured against $W$, to the mirror's measured against $\Phi W$, with sign $+1$. The composite $\Phi \circ C$ with the flag conjugate $C : v_{j} \leftrightarrow w_{j}$ of Proposition \claimref{dark-matter.orientation-arrow-seventeenth-refutation} is a second anti-isometry, carrying $W$ to $\Phi W'$, in the other family (Theorem \claimref{dark-matter.flag-bit-exists-exactly-tower-dimension}), and the asymmetry with sign $-1$.
\item[(ii)] Hence the first route of clause (v) of Theorem \claimref{dark-matter.mirror-tower-copy-one}, the audit along the reversal orbit, gives $\epsilon_{2} = +\epsilon_{6}$ exactly when the mirror is oriented by $\Phi W$, and $\epsilon_{2} = -\epsilon_{6}$ if by $\Phi W'$. Which holds is a discrete datum of the same kind as the orientation itself: conjugation of the mirror's kinematic data alone, an automorphism under the first premise of Proposition \claimref{dark-matter.orientation-arrow-seventeenth-refutation}, exchanges the two, so no kinematic or dynamical result fixes it. It is fixed by the orientation clause of Premise \claimref{dark-matter.p1-single-frozen-point} or by Premise \claimref{dark-matter.p2-indifference} applied to that discrete datum; route one therefore needs an orientation input of route two's kind: P1's orientation clause, or P2 applied to the bit.
\item[(iii)] Route one applies Premise \claimref{dark-matter.p2-indifference} to a continuous datum of the descent along the reversal orbit, the reach at which Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} obtains $\xi = 1$ and $\Delta\Neff = 7.45$, excluded. So route one stands only under a scoping of P2 that separates the asymmetry per mode from the energy deposited per unit charge. Premise \claimref{dark-matter.p2-indifference} at version 2 states one: it equates labels, not states, so it reaches the stored charge $Q = \epsilon N$ and not the temperature (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}); route one stands at that scope.
\end{enumerate}
Under P2 at version 2 clause (v) has both routes: route two by the orientation clause of P1, and route one by the audit with P2 as scoped, which equates along the orbit the labels of the descent, among them the stored asymmetry $Q = \epsilon N$ (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i)) and the orientation bit of (ii), and not the temperature ratio. The claim that the audit stands with P2 at its version-1 reach does not survive Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}.

## technical
The mirror tower is this tower's tractor geometry with the metric's sign reversed, and the two are related by one canonical map that flips the sign of the form. That map keeps every maximal isotropic subspace isotropic, so it carries this tower's Witt flag to a flag of the mirror; on the Fock modules it keeps creation operators, flips the sign of annihilation operators, and so keeps every number operator and the Fock grade. Particles go to particles, and the asymmetry per mode is carried with its sign. Composing with the flag conjugate gives a second sign-reversing map that exchanges particles and antiparticles. The audit route to the equality of the two towers' asymmetries therefore needs the mirror to be oriented by the image of this tower's flag, a discrete datum that no structure fixes, as in the seventeenth refutation; it is supplied by the single-flag clause of P1 or by P2 applied to that bit. The audit route also applies P2 to a continuous datum of the descent along the reversal orbit, exactly the reach that a later note shows forces the mirror to the photon temperature and is excluded by the effective number of neutrino species. P2 at version 2 is scoped in exactly that way, to labels such as the stored charge and not to states such as the temperature, so the clause has both routes: P1's orientation clause, and the audit with P2 as scoped.

## lay
The dark-matter paper argues that the mirror world has the same small excess of matter over antimatter as ours, by two routes. One route says nature would not make an unexplained difference between the two worlds. This result checks the step that route skipped: the natural map between the two worlds does send matter to matter, not to antimatter, so if the worlds are matched by it an excess equal in size is also equal in sign. But whether the mirror is matched to us that way is itself a choice nothing fixes, the same kind of choice as which of matter and antimatter we call matter, so the route needs an assumption about orientation after all. And the same reasoning, applied to the mirror's temperature, gives a hot mirror that observations exclude, so the route also needs a reason to apply the rule to the excess and not to the heat. The rule as the framework now states it supplies that reason: it applies to labels, such as the excess, and not to states, such as the heat.

## one-liner
The canonical reversal carries this tower's flag and Fock grading to the mirror's with sign $+1$, so the audit route to $\epsilon_{2} = \epsilon_{6}$ needs P1's orientation clause or P2 applied to the orientation bit, and at its first reach it is the reach that the cold mirror refutes; P2 at version 2, scoped to labels, keeps the route.
