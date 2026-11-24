---
id: synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane
kind: claim
version: 1
title: 'Helicity-two composites of light-ray fermions: on a generator and off the null plane'
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, quantum-gravity, no-go]
proposed_by:
  kind: ai
  session: 2026-11-24-three-routes
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-three-routes
review: draft
outside_ga:
  kind: other
  why: the sea values on windows larger than two levels are computed in the Fock representation of the tower planes on occupation patterns (integers), tied to the algebra on the smallest window; the statements themselves are about elements of the tower and of the spacetime algebra
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.orthogonal-anticommute@1
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins@1
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  - synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation@1
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_no_pair_mode_has_helicity_two_and_the_quartic_turns_twice
- kind: check
  ref: check.py::check_sea_values_of_the_helicity_two_modes
- kind: check
  ref: check.py::check_commutator_of_the_composite_is_not_a_number
- kind: check
  ref: check.py::check_sum_of_two_null_momenta_is_null_only_when_parallel
- kind: check
  ref: check.py::check_causal_medium_commutes_exactly_and_its_response_depends_on_the_state
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
  - field-theory.no-canonical-commutation-relations-tower
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators
extraction:
  maintainer_pass_2026_11_24_three_routes:
    by: maintainer-2026-11-24
    date: '2026-11-24'
    note: >-
      Maintainer edits before first storage on main (the version stays 1), on Leon's decision of 24 November 2026 (the canonical pair on the two free directions adopted
      as Premise (TT), at first order: synthesis.premise-canonical-pair-on-the-two-null-directions). The Reading and
      the technical level now cite the lattice model of the first-order field
      (synthesis.lattice-model-of-first-order-gravity-slaved-field-dressed-pair-and-the-dipole-obstruction) by claim
      reference, where they cited it in words as filed alongside. The Reading says that the first of the two ways it
      names is the adopted premise and that the second stays named with no stored result; the closing sentence that
      nothing here decides whether the two directions carry states is dated. No clause, proof, check or number is
      changed, and no assumes edge is added: clauses (i) to (v) hold without the premise. The note below is kept as
      filed.
  open_problem: op.gravitational-field-at-null-momentum
  note: >-
    Adversarial side of the problem: can the free part that the stored lattice result uses be a composite of the
    light-ray fermions (bosons made of fermions, which the statistics result does not exclude), so that the
    requirement of no signal outside the light cone is met with no canonical pair on the two directions at null
    momentum. Answer in three exact parts and one reading. On one generator the helicity-two channel has no pair
    mode at all for channel weights +1/2 and -1/2; its four-fermion modes have sea values (q^3 - q)/6 (two
    flavours) and C(q+3, 7) (one species) where a current has q; for the two-flavour modes at q = 2, 3 the
    commutator is not a number on the edge-clean vectors (as for every composite of free fields) and there is
    no second quantum. Only these two families are treated; the general statement is argued. Off the plane a vector of two light-ray
    quanta has null total momentum only when the two momenta are parallel. And for a coupling at a point with no constraint, commutation with the detection at spacelike separation
    needs no canonical pair: it holds exactly for any medium whose own elements commute with the unit J and
    with one another outside the cone; what the canonical pair of the stored clause (4) supplies is a response that is a fixed
    function, independent of the medium's state and linear in the source. Stored and cited, not refiled: the
    helicity-one case and the rule [W, M] = hM (helicity-one-pair-modes), the density-wave bosons and their
    domain (fluctuation-forms (vi)), the window identity (density-modes-bosonise-only-along-one-null-direction,
    a mention), the null data of the photon (null-plane-photon-data, a mention), the first-order field at null
    momentum (a mention in the reading, not a premise, so the result does not hold given that result's
    premises). Ledger: transport-absent in content (the current-algebra facts and the kinematics are standard);
    the window forms and the reading against the stored lattice model are the store's. Prior art, cited from
    memory and not re-read in this run: the neutrino theory of light (de Broglie 1932 to 1934; Jordan 1935) and Pryce's
    theorem against it (Pryce 1938), of which clause (iii) of the helicity-one result and clause (i) here are
    the window forms; Weinberg and Witten 1980; the operator products of level-one current algebras (the
    square of the raising current of one species vanishes, the first helicity-two field has weight four);
    Sakharov's induced gravity (1967) for the alternative named in the reading. The constrained case and the
    single-mass obstruction are in the lattice model of the first-order field filed alongside
    (synthesis.lattice-model-of-first-order-gravity-slaved-field-dressed-pair-and-the-dipole-obstruction), cited
    in text only. Decisions for the maintainer: whether
    to record on the open problem that the lowest helicity-two four-fermion modes on a generator are not a free
    part in the sense of clause (4) (argued for composites in general), and that the alternative named to a
    canonical pair is the field as the response of the stored quantum fields (op.einstein-from-the-field-theory),
    a list not shown to be complete; whether to add Pryce 1938 as prior art on the helicity-one
    result.
---

## formal
\emph{Setting.} As in \claimref{synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins}: the modes on one null generator carry a generator momentum $k$ in the window $I = \{-N, \dots, N - 1\}$ and a channel; each mode is a tower plane, $a^{*} = v$, $a = w$ (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), with the adjoint $*$ and numbers in $\mathrm{span}\{1, J\}$, $J$ the kernel bivector. A channel is a pair $(\epsilon, f)$ of a helicity sign $\epsilon = \pm$ and a flavour $f$; the rotation by $\theta$ about the generator acts by $a_{k,\alpha} \mapsto e^{-\theta w_{\alpha}J}a_{k,\alpha}$ with $w = \pm\tfrac12$ for $\epsilon = \pm$ (Theorem \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv)), and an element has helicity $h$ if the rotation multiplies it by $e^{h\theta J}$. The chiral sea $\Omega$ has every channel filled for $k < 0$ and empty for $k \ge 0$, and $\omega_{\Omega}$ is its state. Write $\rho_{a}(E^{f}_{+-}) = \sum_{k, k+a \in I}a^{*}_{k,(+,f)}a_{k+a,(-,f)}$ for the helicity-one pair mode of flavour $f$.
\begin{enumerate}
\item[(i)] \emph{(No pair mode of helicity two; proved.)} The rotation multiplies $a^{*}_{k,\alpha}a_{l,\beta}$ by $e^{\theta(w_{\alpha} - w_{\beta})J}$. With every weight $\pm\tfrac12$ the helicity of a pair mode is $-1$, $0$ or $1$: $[W, M] = hM$ with $|h| \ge 2$ forces $M = 0$, for any number of channels. A product of $n$ pair modes of helicity one has helicity $n$, so the helicity-two channel of one generator begins with four fermions.
\item[(ii)] \emph{(Sea values; proved.)} Two flavours: $X_{q} = \sum_{a=1}^{q-1}\rho_{a}(E^{1}_{+-})\,\rho_{q-a}(E^{2}_{+-})$, $q \ge 2$, $N \ge q$, has helicity $2$, annihilates $\Omega$, and
\[
\omega_{\Omega}([X_{q}, X_{q}^{*}]) = \binom{q+1}{3} = \frac{q^{3} - q}{6} .
\]
One species: $V_{q} = \sum (k_{2} - k_{1})(l_{2} - l_{1})\,a^{*}_{k_{1},+}a^{*}_{k_{2},+}a_{l_{2},-}a_{l_{1},-}$, the sum over $k_{1} < k_{2}$, $l_{1} < l_{2}$ in $I$ with $l_{1} + l_{2} - k_{1} - k_{2} = q$, $N \ge \max(2, q - 2)$, has helicity $2$, annihilates $\Omega$, and
\[
\omega_{\Omega}([V_{q}, V_{q}^{*}]) = \binom{q+3}{7} ,
\]
which vanishes for $q \le 3$. The least generator momentum above the sea of a vector with the same number of fermions and two units of helicity relative to the sea is $2$ with two flavours and $4$ with one species. For comparison a pair mode $\rho_{q}(E^{f}_{+-})$ has the value $q$, the value of a current.
\item[(iii)] \emph{(The commutator is not a number; computed exactly.)} On the window $N = q + 2$, with $\psi_{1} = \rho_{2}(E^{2}_{+-})^{*}\Omega$ and $\psi_{2} = \rho_{1}(E^{2}_{-+})^{*}\Omega$ (edge-clean vectors of one pair), the normalised expectation $\langle\psi, [X_{q}, X_{q}^{*}]\psi\rangle/\langle\psi, \psi\rangle$ in $\Omega$, $\psi_{1}$, $\psi_{2}$ is $1, 0, 3$ at $q = 2$ and $4, 2, 10$ at $q = 3$ ($\psi_{1}$ has squared norm $2$), while the commutator of the total density mode $\rho_{q}(\id)$ of the four channels with its adjoint has normalised expectation $4q$ in all three. And $(X_{q}^{*})^{2}\Omega = 0$ at $q = 2, 3$: these modes hold no second quantum there. At $q = 4$ the square is not zero: $|(X_{4}^{*})^{2}\Omega|^{2} = 36$, where a canonical mode with the same sea value $10$ would have $200$. A commutator that is not a number is what every composite of free fields has, the square of a free boson field included, so this clause shows little by itself; it is recorded with the absence of a second quantum at the lowest momenta.
\item[(iv)] \emph{(Two null momenta; proved.)} In $\Cl(1,3)$ with $n = \gamma_{0} + \gamma_{3}$, $\bar n = \gamma_{0} - \gamma_{3}$ and transverse vectors in the span of $\gamma_{1}, \gamma_{2}$, a null vector with $\alpha > 0$ is $p = \alpha\,\bar n + p_{\perp} + \beta\,n$ with $\beta = |p_{\perp}|^{2}/4\alpha$, $|p_{\perp}|^{2} = -Q(p_{\perp})$. For two such vectors
\[
Q(p_{1} + p_{2}) = \frac{|\alpha_{2}p_{1\perp} - \alpha_{1}p_{2\perp}|^{2}}{\alpha_{1}\alpha_{2}} \ge 0 ,
\]
zero exactly when $p_{1}$ and $p_{2}$ are parallel.
\item[(v)] \emph{(A causal medium needs no canonical pair; proved, with a model computed.)} Take the matter factor of \claimref{synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation} ($P_{1}$, $P_{2}$, $J_{\mathrm{s}} = c_{1}P_{1} + c_{2}P_{2}$, detection $O = U^{-1}P_{1}U$) and let $\phi^{0}_{n}(t)$ be self-adjoint elements of any algebra that commute with the matter factor and with a unit $J$, where $J^{2} = -1$, $J^{*} = -J$ and $J$ commutes with the matter factor (in the model below the kernel bivector); no assumption is made on the commutators of the $\phi^{0}$ with one another. The coupling is at a point and no constraint ties the field to the source. Let the source act at site $0$ at the times $t'$ of a finite set by the kicks $K_{t'} = \exp(-g\,J\,J_{\mathrm{s}}\,\phi^{0}_{0}(t'))$, let $W_{<t}$ and $W_{\ge t}$ be the ordered products of the kicks before $t$ and from $t$ on, $\phi_{n}(t) = W_{<t}^{-1}\phi^{0}_{n}(t)W_{<t}$ the field and $O_{H}$ the detection after all kicks. Then exactly
\[
[\phi_{n}(t), O_{H}] = W_{<t}^{-1}\,[\phi^{0}_{n}(t),\ W_{\ge t}^{-1}\,O\,W_{\ge t}]\,W_{<t} ,
\]
which vanishes whenever $\phi^{0}_{n}(t)$ commutes with $\phi^{0}_{0}(t')$ for every source time $t' \ge t$, and to first order in $g$ equals $g\,J\,[J_{\mathrm{s}}, O]\sum_{t' \ge t}[\phi^{0}_{n}(t), \phi^{0}_{0}(t')]$. \emph{Model.} Five tower modes $b_{x}$ on a ring, $\phi^{0}_{n}(t) = h_{n-t}$ with $h_{x} = b_{x}^{*}b_{x+1} + b_{x+1}^{*}b_{x}$ (a shift dynamics; $h_{x}$ and $h_{y}$ commute unless $y = x \pm 1$), source times $0, 1$, kick angles with $(\cos, \sin) = (\tfrac35, \tfrac45)$ and $(\tfrac{5}{13}, \tfrac{12}{13})$ on the two paths, $U = \tfrac35 + \tfrac45 e_{2}$: of the $20$ events $(n, t)$, $0 \le t \le 3$, the commutator is nonzero at the six $(0,0), (1,0), (3,0), (4,0), (1,1), (4,1)$ and zero at the other fourteen, in agreement with the rule. The response of the medium is an element, not a function: after one kick of angle $a$ ($\cos a = \tfrac35$) the mean of $h_{1}$ is $0$ in the empty medium and $-\sin a = -\tfrac45$ in the vector $(b_{0}^{*} + J b_{2}^{*})$ applied to it: it depends on the medium's state and is not proportional to the kick angle.
\end{enumerate}
\emph{Reading (argued throughout; nothing in it is proved here).} The free part of clause (4) of the stored lattice result has a commutator that is a number, the commutator function of the field equation. (a) On one generator the pair modes of helicity zero are such fields on their domain (\claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi)) and those of helicity one are quasi-spins (the stored result). At helicity two there is no pair mode (proved, (i)), and what (ii) and (iii) show concerns two families only, $X_{q}$ and $V_{q}$, the lowest four-fermion modes: sea values of degree three or seven in $q$, and for $X_{q}$ at $q = 2, 3$ a commutator that is not a number and no second quantum. Linear combinations of four-fermion modes, other flavour structures and six or more fermions are not treated, so the statement that no helicity-two composite on a generator is a canonical field is argued from these examples and not proved. The general tool is the theorem of Weinberg and Witten (1980, cited from memory, not used in any proof here): no massless particle of helicity two in a theory with a Lorentz-covariant conserved stress, a hypothesis that free fermion fields satisfy. The curvature datum of a free helicity-two field on a null plane, one further derivative of a datum with the value $q$, would have $q^{3}$: the two-flavour mode matches that form at large $q$ in the sea's expectation only. (b) A pair mode at one transverse point superposes all relative transverse momenta, so by (iv) its vectors lie at $Q(P) > 0$ apart from the parallel ones; the first-order field has directions that the source does not fix only at $Q(k) = 0$ (\claimref{synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints}). This is standard kinematics, and the parallel sector that remains is the sector on one generator, so (b) rests on (a) and has its scope. (c) By (v), for a coupling at a point with no constraint, commutation at spacelike separation does not single out a canonical pair: a medium with causal commutators gives it exactly. What the canonical pair of clause (4) supplies is the response as a fixed function, the same in every state of the field and linear in the source, which is what makes the mean field obey the classical first-order equation. The lowest helicity-two four-fermion modes on a generator do not supply that response, so they are not a free part in the sense of clause (4); as part of a causal medium they would still meet commutation by (v). Two ways of meeting the requirement of no signal outside the light cone are thereby named, and the list is not shown to be complete: a canonical pair for the two directions, or the gravitational field as the response of the stored quantum fields (open problem op.einstein-from-the-field-theory), to which a causal medium of composites would belong. The first is the hypothesis (TT) of the lattice model of the first-order field, adopted by Leon's decision of 24 November 2026 as a premise of the series at first order (Premise \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}); the second stays named, and the store holds no result for it. Clauses (i) to (v) do not depend on the premise. For the second way: the spin-two response of the stored free content is a continuum with no pole at null momentum, and a pole needs the induced term of Einstein and Hilbert, whose coefficient the store holds to depend on the cut-off (\claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off}); so that way is narrowed by a stored result. \emph{Constraints.} Clause (v) has no constraint. For the gravitational field the constrained part of the field is a matter element at equal time, which fails to commute at a distance by itself and has to be cancelled by a dressing that shifts the field; that case is treated in the lattice model of the first-order field (\claimref{synthesis.lattice-model-of-first-order-gravity-slaved-field-dressed-pair-and-the-dipole-obstruction}), and whether a medium without canonical variables can carry such a dressing is shown neither there nor here. The obstruction found there for a single mass on two sites, which changes the centre of mass, a charge of the constraints, does not depend on what the free part is made of: it holds for a canonical pair, for a composite and for a medium alike. In one space dimension there is no transverse momentum and the density waves are canonical on their domain: the reduction of a horizon's channels under joint J3 (\claimref{hawking.joint-j3-s-wave-reduction}) is of that kind and is not touched by this result. Nothing here decides whether the two directions carry states of their own; that was decided by adoption on 24 November 2026 (the premise cited above), and this result shows neither that the premise is necessary nor that the pair can be derived.

## technical
On one light ray the fermion modes are tower planes labelled by a momentum in a finite window and a channel with helicity weight $+\tfrac12$ or $-\tfrac12$. A pair of them can turn by one unit about the ray or by none, never by two, so the helicity-two channel starts with four fermions. For two flavours the lowest such mode is the product of the two helicity-one pair modes summed over the split of the momentum; its commutator has the sea value $(q^{3} - q)/6$. For one species the exclusion principle removes that product and the first mode has $\binom{q+3}{7}$, zero below $q = 4$. A current has $q$.

The commutator of the two-flavour mode is not a number: on two edge-clean vectors with one pair its normalised expectation is $0$ and $3$ at $q = 2$ against $1$ on the sea, and the mode cannot be applied twice at $q = 2, 3$. Every composite of free fields has a commutator that is not a number, so this alone shows little.

Off the null plane, two null momenta sum to a null one only when parallel: $Q(p_{1} + p_{2}) = |\alpha_{2}p_{1\perp} - \alpha_{1}p_{2\perp}|^{2}/\alpha_{1}\alpha_{2}$.

Last, an exact identity for any medium coupled at a point, with no constraint, to the stored two-path matter factor, the medium's elements commuting with the unit $J$: the field's commutator with the later detection is the commutator of the free element with the detection evolved through the later kicks only. It vanishes wherever the medium's own elements commute, with no canonical commutator used; a five-mode fermion ring shows it at $14$ of $20$ events and fails at the six the rule names. The medium's response is $-\sin a$ in one state and $0$ in another, not a fixed function proportional to the source.

Reading (argued): the lowest helicity-two four-fermion modes on a generator are not a free part in the sense of clause (4) of the stored lattice result; that no helicity-two composite on a generator is canonical is argued from these two families, not proved. Without a constraint, commutation alone does not force a canonical pair; a response that is state-independent and linear in the source does. With the gravitational constraints the detection has to be dressed, which is the subject of the lattice model of the first-order field (\claimref{synthesis.lattice-model-of-first-order-gravity-slaved-field-dressed-pair-and-the-dipole-obstruction}), and its obstruction for a single mass does not depend on what the free part is made of. The canonical pair, the first of the two ways named, was adopted as a premise of the series at first order on 24 November 2026 (\claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}); nothing proved here depends on it.

## lay
The graph holds a requirement, that gravity carry no signal faster than light, and a model showing that a gravitational field with nothing of its own breaks it while a field with its own wave-like variables keeps it. Could those variables be made from particles the graph already has, pairs of fermions travelling along a light ray, instead of being added? Gravity's kind of wave turns twice about its direction of travel. Along one light ray pairs of fermions turn once or not at all, never twice; that much is proved. The simplest combinations of four fermions that do turn twice were computed and do not behave as independent quanta, which argues, without proving it for every combination, that the answer is no. Away from the ray two such fermions only travel together as a massless object when they are exactly parallel. A further exact calculation shows what the added variables are really for. In a model where matter is coupled to a medium at a point, any ordinary quantum medium with a speed limit already prevents faster-than-light signals; what the wave-like variables add is a response that is the same whatever state the medium is in, which is what makes the field obey the classical equation. Gravity adds constraints that this model leaves out. Since 24 November 2026 the series assumes such variables for weak gravity, as an assumption and not as something built from the fermions; this result does not show that assuming them is the only way.

## one-liner
On one null generator with channel weights $\pm\tfrac12$ no pair mode has helicity two; the four-fermion helicity-two modes have sea values $(q^{3} - q)/6$ (two flavours) and $\binom{q+3}{7}$ (one species) against $q$ for a current, and the two-flavour mode has a commutator that is not a number (normalised expectations $1, 0, 3$ on three edge-clean vectors at $q = 2$) and no second quantum at $q = 2, 3$; two null momenta sum to a null one only when parallel; and in the stored two-path model any medium coupled at a point with no constraint, whose elements commute with the unit $J$ and with one another outside the cone, commutes exactly with the detection at spacelike events (computed for a five-mode ring, $14$ of $20$ events), its response depending on its state ($0$ or $-\tfrac45$): argued from these, the lowest helicity-two four-fermion modes on a generator are not a free part in the sense of the stored lattice result's clause (4), and without a constraint commutation alone does not force a canonical pair.
