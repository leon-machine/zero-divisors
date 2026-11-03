---
id: synthesis.majorana-element-is-null-blade-no-frozen-point-condition
kind: claim
version: 2
title: The Majorana element is a null five-blade of nonzero $B - L$ weight, so the Clifford norm of the frozen-point kind vanishes on it and on the whole self-dual $126$, and every invariant polynomial, holomorphic or of the real form, vanishes on it and its orbit; only the Fock norm, which needs the Hermitian structure, survives, so no condition of the frozen-point kind fixes the Majorana scale
status: proved
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, representation-theory, no-go, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
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
  - standard-model.majorana-element@7
  - mass.imported-frozen-point-tractor-connection@6
  - synthesis.majorana-scale-free-on-pati-salam-route@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_majorana_element_is_a_null_blade
- kind: check
  ref: check.py::check_clifford_norm_vanishes_on_the_self_dual_half
- kind: check
  ref: check.py::check_orbit_norm_and_the_adjoint
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.majorana-scale-free-input
  - synthesis.majorana-scale-free-on-pati-salam-route
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)). The classification that puts the Majorana scale with the rung unit v/H (a datum of the sesquilinear kind) does not depend on whether v/H is a law or initial data, so the register decision of 2026-11-01 (synthesis.rung-unit-second-free-number version 3) leaves it unchanged. Nothing else is changed.'
  open_problem: op.majorana-scale
  note: >-
    The problem's third line of attack, decided in the negative: no invariant condition of the
    frozen-point kind can fix the vev of the Majorana element. The frozen point is a real tractor
    with Clifford norm Lambda/3, and that norm is the scale. The Majorana element T is a product of
    five anticommuting nilpotents, so T^2 = 0 and its Clifford norm is zero; more than that, the
    norm vanishes on the whole self-dual half of the five-vectors, the 126, because the pseudoscalar
    of the ten is an anti-isometry of the form; and more than that again, T carries B - L = -2, so
    every holomorphic invariant polynomial of any degree vanishes on T and its orbit. What survives
    is the Fock norm <T T^dag>_0 = 1/32, a sesquilinear quantity that needs the module's Hermitian
    structure (the adjoint negates the five negative-square generators: it is not a Clifford
    anti-automorphism of the ten). This is the general statement that a vev carrying a U(1) charge
    lies in the null cone and has no invariant norm except a sesquilinear one (it applies to the
    Higgs doublet in the same way), applied to the series' own element. In the series' own
    classification it puts the Majorana scale with the rung unit v/H, seen only by the sesquilinear
    structure, and not with Lambda, fixed by a bilinear norm: structural support for registering it
    as an input beside N and v/H, and a closed route for deriving it. Companion result, filed
    alongside: synthesis.two-loop-running-cannot-fix-majorana-coupling (no relation from the
    two-loop running of the gauge couplings fixes the 126 coupling); together with the stored
    scaling symmetry the three lines of attack on the scale are closed. Transport-absent: the
    content is Clifford-algebraic and representation-theoretic, about the series' own element in
    the series' own module; the pseudoscalar anti-isometry argument is standard (self-dual forms are
    isotropic for the wedge pairing, cited from memory).
---
## formal
Under Hypothesis (S), let $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ be the Majorana element of Proposition \claimref{standard-model.majorana-element}, a grade-five element of the Clifford algebra of the ten, represented on the five-mode module ($32$ dimensions) with the real-form generators $\gamma_{2m} = v_{m} + w_{m}$ ($\gamma^{2} = 1$) and $\gamma_{2m+1} = w_{m} - v_{m}$ ($\gamma^{2} = -1$), so the real algebra is $\Cl(5,5)$ and the scalar part is $\langle A\rangle_{0} = \tfrac{1}{32}\mathrm{tr}\,A$. Let $Q(A, B) = \langle A\tilde{B}\rangle_{0}$ be the Clifford bilinear form, the form whose value $Q(I) = \Lambda/3$ on the frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$ is the frozen-point condition (Fact \claimref{mass.imported-frozen-point-tractor-connection}), and $I_{10} = \gamma_{0}\cdots\gamma_{9}$ the pseudoscalar of the ten.
\begin{enumerate}
\item[(i)] \emph{(A null blade.)} $T^{2} = 0$: $T$ is a zero divisor, and $Q(T) = 0$ (reversion is the identity on grade five). Its Fock norm is $\langle TT^{\dagger}\rangle_{0} = \tfrac{1}{32}$, $TT^{\dagger}$ being the projector on the full state. And $[B - L, T] = -2T$ (Proposition \claimref{standard-model.majorana-element}(2)).
\item[(ii)] \emph{(The whole $126$ is isotropic.)} $I_{10}^{2} = 1$, $I_{10}$ anticommutes with every generator, and left multiplication by $I_{10}$ is an anti-isometry of $Q$ on grade five, $Q(I_{10}A, I_{10}B) = -Q(A, B)$. Hence $Q$ vanishes identically on each of the two $126$-dimensional eigenspaces of $I_{10}$ on the five-vectors and pairs them nondegenerately, $Q(A_{+}, A_{-}) = \tfrac12 Q(A)$. $T$ lies in the $+1$ eigenspace, the self-dual half (over $\C$ the $126$ of Proposition \claimref{standard-model.majorana-element}(3), whose $(10,1,3)$ is the orbit of $T$), $T^{\dagger}$ in the other, and $Q(T, T^{\dagger}) = \tfrac{1}{32}$ is the Fock norm.
\item[(iii)] \emph{(No invariant polynomial at all on $T$.)} Every polynomial $P$ on the five-vectors invariant under the compact Pati-Salam group, or under any group containing $\exp(i\theta(B - L))$, satisfies $P(T) = P(0)$: the $U(1)_{B - L}$ orbit of $T$ is $e^{-2i\theta}T$, so each homogeneous component of positive degree vanishes on $T$, and by invariance on the whole orbit $gTg^{-1}$. Since $B - L$ is a real element of the $\mathfrak{so}(5,5)$ of this module, $\exp(t(B - L))$, $t \in \R$, lies in the real spin group and scales $T$ by $e^{-2t}$, so every continuous invariant of the real form, not only the holomorphic ones, takes its value at $0$ on $T$: $T$ lies in the null cone. This is a statement about $T$ and its orbit, not about the $126$, whose invariant ring is not trivial; and the $126$ carries no invariant bilinear form at all, Clifford or other, because it is not isomorphic to its dual (checked for $Q$ on five rotors of the $21$).
\item[(iv)] \emph{(What survives, and what it needs.)} The invariants that do not vanish on $T$ involve $T^{\dagger}$, that is the module's Hermitian structure: the adjoint fixes $\gamma_{2m}$ and negates $\gamma_{2m+1}$, so it is the Clifford reversion composed with the reflection of the five negative-square generators, not an anti-automorphism of the Clifford algebra of the ten, and it depends on the split of the ten into the two fives, the choice of a maximal isotropic subspace (the particle modes). A condition $\langle TT^{\dagger}\rangle_{0} = M^{2}$ fixes the magnitude of a vev along $T$ against $M$ and nothing fixes $M$: in the classification of the series' rung-unit premise (synthesis.rung-unit-second-free-number, a postulate, not assumed here) the Majorana scale is a datum of the sesquilinear kind, like the rung unit $v/H$, not of the bilinear kind, like $\Lambda$, whose frozen-point norm is the scale.
\end{enumerate}
So a condition of the frozen-point kind, an invariant algebraic equation on the element alone, cannot fix the Majorana scale: on $T$ every such equation reads $0 = 0$. This is the general fact that a vev carrying a $U(1)$ charge lies in the null cone and has no invariant norm except a sesquilinear one, applied to the series' own element. Together with the invariance of the stored relations under the rescaling of the $126$ coupling (Proposition \claimref{synthesis.majorana-scale-free-on-pati-salam-route}) and the companion result that the two-loop running of the gauge couplings does not fix that coupling either (filed alongside, synthesis.two-loop-running-cannot-fix-majorana-coupling), this closes the three lines of attack on the derivation of the scale and supports registering it as an input.

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). No number here depends on the choice.

## technical
The cosmological constant enters the series through a norm: the frozen point of the tractor bundle is a real vector whose Clifford square is $\Lambda/3$, so the scale is written into the geometry as an invariant number attached to an invariant element. The open problem asks whether the Majorana scale could enter the same way, through an invariant condition on the Majorana element $T$. Under Hypothesis (S) it cannot, for three nested reasons. $T$ is the product of the five creation operators, five anticommuting nilpotents, so $T^{2} = 0$ and its Clifford norm is zero: it is a null blade, a zero divisor, like the null tractors of the series rather than the frozen point. The vanishing is not peculiar to $T$: the pseudoscalar of the ten squares to one and reverses the sign of the Clifford form on five-vectors, so the form is zero on each of the two halves of the five-vectors it separates, one of which is the $126$ containing $T$ and its Pati-Salam orbit. And no other invariant polynomial helps: $T$ carries $B - L = -2$, so a phase rotation multiplies it by a phase, and a real boost of the real form rescales it, while both fix every invariant, which forces every invariant of positive degree to vanish on it and on its orbit (not on the whole $126$, whose invariants are not all constant). This is the general null-cone statement for a charged vev, the Higgs doublet included, applied to $T$. The only invariant quantity that is nonzero on $T$ is its Fock norm, built with the adjoint, which is not an operation of the Clifford algebra of the ten but of the module with its Hermitian structure; a condition on it fixes the vev only against a scale supplied from elsewhere. In the series' own terms the Majorana scale sits with $v/H$, seen by the sesquilinear structure alone, not with $\Lambda$.

## lay
The series fixes the cosmological constant by attaching it to a special direction in an enlarged geometry whose length is that constant. One hope for the scale of neutrino masses was to fix it the same way, by an invariant length of the object that gives the right-handed neutrino its mass. That object has no length. It is built from five operators each of which squares to zero, so it squares to zero itself; the same is true of the whole family of objects it belongs to; and because it carries a charge under a symmetry of the model, no invariant quantity of any kind, length or otherwise, can be nonzero on it. The only size one can attach to it uses the complex structure of the particle space, and that size is just the scale one would have to put in by hand. So the neutrino mass scale cannot be fixed the way the cosmological constant is; it belongs with the other free scale of the series, the one that sets the weak scale, exactly as any charged field's size would.

## one-liner
Under Hypothesis (S), the Majorana element $T = v_{1}\cdots v_{5}$ is a null five-blade ($T^{2} = 0$, Clifford norm $0$) of $B - L$ weight $-2$, the pseudoscalar of the ten is an anti-isometry of the Clifford form on five-vectors so the form vanishes on the whole self-dual $126$, and every invariant polynomial, holomorphic or of the real form, vanishes on $T$ and its orbit (not on the whole $126$); only the Fock norm $\langle TT^{\dagger}\rangle_{0} = \tfrac{1}{32}$ survives, which needs the module's Hermitian structure and fixes a vev only against an external scale, so no condition of the frozen-point kind $Q(I) = \Lambda/3$ fixes the Majorana scale, which sits with $v/H$ rather than with $\Lambda$.
