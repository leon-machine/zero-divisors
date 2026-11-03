---
id: synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays
kind: claim
version: 2
title: On a horizon's null plane the canonical part of a spacetime-algebra spinor is the image of Lambda(m), two complex channels, one per chirality, with helicity about the generators equal to minus the chirality; so, given one (Q) version 3 array per complex channel, one massless Dirac species supplies two arrays per light ray (ln 2 at the Hawking temperature) and one Weyl field one
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, counting-rules]
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
  - field-theory.second-quantisation@5
  - field-theory.where-each-lives@3
  - synthesis.positive-null-energy-gives-r-premises@4
  - synthesis.half-integer-weight-array-carries-half-ln2@4
  - synthesis.residue-from-mode-entropy@4
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_canonical_part_is_lambda_m
- kind: check
  ref: check.py::check_boost_weight_of_canonical_part
- kind: check
  ref: check.py::check_chirality_splits_canonical_part
- kind: check
  ref: check.py::check_helicity_on_canonical_part
- kind: check
  ref: check.py::check_vector_channels_have_integer_weight
- kind: check
  ref: check.py::check_count_per_species
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.array-ln2-is-zero-mode-doublet-one-tower
  - synthesis.capacity-per-mode-independent-of-helicity
  - synthesis.n-plus-null-ground-state
extraction:
  open_problem: op.residue-killing-weights
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Note added to (vii): the slot module excludes a fifteen-component generation (its light-ray arrays are its Weyl components, sixteen per generation, synthesis.slot-module-light-ray-arrays-are-weyl-components), so the half unit of a Weyl-only neutrino does not occur in the series'' matter. Cited in the text, not a uses edge (that result uses this one). Statement of (i) to (vii) unchanged. Version 1 -> 2.'
  note: >-
    The problem's first line of attack: follow the arrays of a counted unit to the field theory's
    spinor fields on the light rays, the reading behind (Q) version 3. On the horizon's null plane
    N_k (generators along k, second null direction m) the Dirac current's flux J.k is twice the
    squared norm of Lambda(m) psi: the canonical part of the spinor on N_k is the image of
    Lambda(m) = m gamma_0/2, real dimension 4, as in the result filed alongside,
    synthesis.boost-evolution-on-generators-is-one-unitary-group, clause (i); the image of
    Lambda(k), the spinor of plane waves of momentum k, carries no flux through N_k. On the canonical
    part the covariant boost scales values by the square root of the inverse of its factor on the
    generator, so with the transport of the affine parameter it is the unitary dilation of weight
    1/2, the carrier's boost. The chirality splits the canonical part into two complex channels;
    helicity about the generator direction is minus the chirality there. Hence one massless species
    with both chiralities (a Dirac field) gives two arrays per light ray, ln 2 exactly at the Hawking
    temperature, and a Weyl field one. Under the count per light ray, with the counted unit a
    bookkeeping total over all horizon fields, the registered unit of ln 2 is two arrays of that
    total. (Q) version 3 is read in clause (vi) but is not a derivation premise here; it enters
    through the cited array entropy. Transport-absent apart from the rotor action. Literature cited
    from memory: light-front quantisation (Kogut and Soper 1970), as orientation only.
---

## formal
Work in the spacetime algebra $\Cl(1,3)$, $\gamma_{0}^{2} = 1$, $\gamma_{i}^{2} = -1$, with $I = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$ and $\sigma_{3} = \gamma_{3}\gamma_{0}$, at a point of a horizon generator in a gauge with $\hb(x_{0}) = 1$, $\Omega(x_{0}) = 0$ there. Let the generators of the null plane $N_{k} = \{x : \ip{x}{k} = 0\}$ run along $k = \gamma_{0} + \gamma_{3}$ (any future null direction is carried to this one by a rotor), let $m = \gamma_{0} - \gamma_{3}$ be the second null direction of the plane of $k$ and $\gamma_{0}$, and let $\Lambda(a) = a\gamma_{0}/(2a_{0})$ (Theorem \claimref{field-theory.second-quantisation}(1)), so $\Lambda(k) = (1 + B)/2$ and $\Lambda(m) = (1 - B)/2$ with $B = \gamma_{3}\gamma_{0}$ the boost bivector of the generator ($B^{2} = 1$, $e^{B\lambda/2}k\,e^{-B\lambda/2} = e^{\lambda}k$). Spinors are even multivectors $\psi \in \Cl^{+}(1,3)$ (real dimension $8$), on which a rotor $R$ acts by $\psi \mapsto R\psi$. Let $J = \gamma_{1}\gamma_{2} = -IB$ be the bivector of the transverse plane, $L_{X}\psi = X\psi$, $i_{H} = R_{I\sigma_{3}}$ Hestenes' unit, and $\Gamma\psi = I\psi I\sigma_{3}$ the chirality. Then:
\begin{enumerate}
\item[(i)] (the canonical part on $N_{k}$) the flux of the Dirac current $J_{\psi} = \psi\gamma_{0}\tilde{\psi}$ through $N_{k}$ is $J_{\psi}\cdot k = 2\,|\Lambda(m)\psi|^{2}$, the squared Euclidean norm in the blade basis: it vanishes identically on the image of $\Lambda(k)$ and is positive definite on the image of $\Lambda(m)$, which is $\ker L_{m}$, the $(-1)$-eigenspace of $L_{B}$, of real dimension $4$. Symmetrically the flux through $N_{m}$ is $2|\Lambda(k)\psi|^{2}$. So the canonical part of a spinor field on $N_{k}$ is $\Lambda(m)\psi$; $\Lambda(k)$ is the spinor of plane waves of momentum $k$ (Theorem \claimref{field-theory.second-quantisation}(1), (2)), which are constant along the generators;
\item[(ii)] (its boost weight) the covariant boost $B_{\lambda} = \cosh\tfrac{\lambda}{2} + B\sinh\tfrac{\lambda}{2}$ acts on the values of $\Lambda(m)\psi$ by $e^{-\lambda/2}$ and on those of $\Lambda(k)\psi$ by $e^{+\lambda/2}$, while the transport $u \mapsto e^{-\lambda}u$ of the generators' affine parameter multiplies the delta kernel by $e^{\lambda}$. The anticommutator is therefore preserved on the canonical part, the unitary dilation $\psi_{m}(u) \mapsto e^{-\lambda/2}\psi_{m}(e^{-\lambda}u)$, which at $\lambda = -\kappa t$ is the boost $\beta_{t}(\psi(u)) = e^{\kappa t/2}\psi(e^{\kappa t}u)$ of the continuum carrier (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}), of weight $\tfrac12$; on $\Lambda(k)\psi$ it is scaled by $e^{2\lambda}$;
\item[(iii)] (two chirality channels) $\Gamma^{2} = 1$, $\Gamma$ commutes with every $L_{X}$, $X \in \Cl^{+}(1,3)$ (so it is Lorentz invariant), with $i_{H}$ and with the central unit $I$ of Theorem \claimref{field-theory.where-each-lives}; its eigenspaces $W_{\pm}$ (the Weyl spinors) have real dimension $4$ and meet the canonical part in real dimension $2$ each: the canonical part is one complex channel of each chirality, under either unit;
\item[(iv)] (helicity) on the canonical part $L_{J} = -\Gamma\,i_{H}$ and $L_{J} = L_{I}$; the transverse rotation $e^{-J\phi/2}$ acts on the channel of chirality $\epsilon$ as $e^{+\epsilon i_{H}\phi/2}$: helicity about the generator direction $k$ is minus the chirality, equivalently the chirality about $m$. On the image of $\Lambda(k)$ the opposite signs hold, and neither identity holds on all of $\Cl^{+}(1,3)$. With the central unit both canonical channels are complex-linear for $L_{J} = L_{I}$, the other chirality's particle content entering conjugated, the split of Theorem \claimref{field-theory.second-quantisation}(4);
\item[(v)] (Weyl against Dirac) a Weyl spinor field has one complex canonical channel on each light ray of $N_{k}$, a Hestenes (Dirac) spinor field two, one of each chirality and so of opposite helicities;
\item[(vi)] (contrast) vector and bivector fields carry the boost by conjugation $X \mapsto RX\tilde{R}$ with integer weights ($\gamma_{1}, \gamma_{2}$ weight $0$; $k$, $k\wedge\gamma_{1}$, $k\wedge\gamma_{2}$ weight $1$; $m$ weight $-1$); only the one-sided spinor action gives the square root, and on spinors a full turn in the transverse plane is the rotor $J^{2} = -1$;
\item[(vii)] (the count) read with one array of version 3 of Premise (Q), weights $\kappa(k + \tfrac12)$, per complex canonical channel on a light ray, a massless Dirac species carries two arrays and a Weyl field one, each $\tfrac12\ln 2$ at the Hawking temperature (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(i)). With the count per light ray and the counted unit a bookkeeping total over all horizon fields, a light ray carrying $n_{D}$ Dirac species and $n_{W}$ further Weyl fields carries $2n_{D} + n_{W}$ arrays, $(n_{D} + \tfrac12 n_{W})\ln 2$, and a registered unit of $\ln 2$ is two arrays of this total; one Dirac species is exactly one such unit. Under the hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy} the residue per unit of two arrays is the registered $1/(4\ln 2)$. \emph{Note.} For the series' matter the slot module excludes a fifteen-component generation: its light-ray arrays are its Weyl components, sixteen per generation for every CPT halving and every mass term, eight registered units (Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}), so the half unit of a Weyl-only neutrino, a species with no right-handed partner, does not occur there.
\end{enumerate}
So the spinor reading that fixes the offset of (Q) version 3 also fixes the channel count: each complex canonical channel on a light ray is one chirality of one spinor field, and two arrays, the registered unit, are the light-ray content of one massless Dirac species, with helicity about the generators equal to minus the chirality. (i) to (vi) are identities in $\Cl(1,3)$ and use neither the area law nor any thermal premise; the area law enters (vii) only to state the residue.

## technical
The registered residue holds, at the weights $\kappa(k + \tfrac12)$ of Premise (Q) version 3, exactly when a counted unit is two s-wave arrays, and the store had no reason why arrays come in pairs. This result looks at where the arrays come from. (Q) version 3 reads its offset from the boundary modes being spinor fields of boost weight $\tfrac12$ on the horizon's light rays. In the spacetime algebra a spinor is an even multivector acted on from one side by rotors. On the horizon's null plane, with generators along $k$ and second null direction $m$, the flux of the Dirac current through the plane is twice the squared norm of $\Lambda(m)\psi$, $\Lambda(m) = m\gamma_{0}/2$: that half of the spinor, of real dimension four, is the canonical part on the plane, and the other half, the spinor of plane waves moving along $k$, carries no flux there. The boost of the generator scales the canonical values by the square root of the inverse of its factor on $k$, which together with the stretching of the affine parameter is the unitary dilation of weight $\tfrac12$, the boost of the series' continuum carrier.

The chirality splits the canonical part into two complex channels, one of each chirality. On these channels the rotation about the generators acts as minus the chirality: helicity about the generator direction is minus the chirality, an algebraic identity there and false on the whole spinor. Hence one massless species with both chiralities, a Dirac field, gives two channels on each light ray, of opposite helicities, and a Weyl field gives one. With one array per channel, two arrays carry exactly $\ln 2$ at the Hawking temperature. Counting per light ray, with the counted unit a bookkeeping total over all the horizon's fields, the registered unit of $\ln 2$ is two arrays of the total, and one Dirac species is exactly one unit. Vector fields, acted on by conjugation, carry integer weights and so would give the other offset.

## lay
The series counts quantum modes on a black hole's horizon, and it needs each counted unit to hold exactly one bit of entropy. With its current assumption about the modes' energies, one ladder of modes holds half a bit, so a counted unit must be two ladders, and nothing explained why. This result traces the ladders to the particles that would carry them. Particles of spin one half, like electrons and neutrinos, are described by spinors. On the surface swept out by the horizon's light rays only half of a spinor's components carry particles across it, and those split into two channels, the two handednesses of the particle, with the spin about the light rays fixed by the handedness. So a spin-one-half particle that has both handednesses, as the electron does, supplies exactly two ladders per light ray, one bit; a particle with one handedness only supplies half a bit. The horizon's total is then counted in bits, two ladders to a bit, over all its fields.

## one-liner
In $\Cl(1,3)$ the flux of the Dirac current through a horizon's null plane $N_{k}$ is $2|\Lambda(m)\psi|^{2}$, so the canonical part there is the image of $\Lambda(m) = m\gamma_{0}/2$, real dimension $4$, of boost weight $\tfrac12$ in the carrier's convention, split by chirality into two complex channels with helicity about $k$ minus the chirality; given one (Q) version 3 array per channel, one massless Dirac species gives two arrays per light ray, $\ln 2$ at the Hawking temperature, a Weyl field one, and the per-light-ray total over fields counts two arrays per registered unit.
