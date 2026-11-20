# Simulating the Dark Towers: Methods, Assumptions and Tests of the Unit-Ball Composition: Companion note to T14: the mathematics, the code and the premises behind the merger, halo and Galaxy tests (regenerated from the store)

**Abstract.** The dark-matter paper T14 fixes how much matter each dark tower holds. By its unit-ball rule the mirror carries 18.6 percent of the dark matter, the three-dimensional towers 49.7 percent and the five-dimensional towers 31.6 percent. This note sets out the assumptions, equations, code and results of the tests of those amounts. Quanta confined to a sheet scatter in two dimensions; per unit of the mass gravity sees, their cross-section is a length times the sheet spacing. At composite strength the three-dimensional towers' matter is a fluid, eight to thirteen orders of magnitude above the cluster bound, whatever its confinement scale. A tree-gravity, multi-species smoothed-particle code, with the sheet fluid's pressure confined to its planes, follows a Bullet-like merger and a cluster's assembly. As T14 writes it, the composition fails both tests: 68 percent of the dark matter collides, with randomly oriented sheets the subcluster dissolves from the lensing map, and halos reach about 0.4 of the cold-dark-matter ellipticity. If the odd towers' matter is collisionless, only the mirror collides; the subcluster keeps a lensing peak on its galaxies, its gas trailing, at the cost of a puffier subcluster and halos about 0.8 as elliptical. A semi-analytic Milky Way model with helium-star feedback excludes the mirror's proton-only branch; its helium branch fits at the Sun under some normalisations, and in the bulge only if the bulge holds over twice the mirror's proportional share of its dark mass. Two films, the code and a verification script accompany the note.

## What we assume

**Postulate 1 (R1: equal mass per quantum).** The quanta of every populated tower carry the same mass $m$.

**Postulate 2 (R2: one quantum per unit ball).** A populated tower whose space has $D$ dimensions (under P3, \claimref{dark-matter.p3-nearest-dimension-representatives}, $2$, $3$ or $4$) holds one quantum per unit ball $\B^{D}$ of that space, in one unit of length common to all towers: every tower has the same Wigner-Seitz radius. The rule presupposes that all six towers are populated, which for the odd four is the inference of Observation \claimref{dark-matter.which-towers-are-populated}.

**Postulate 3 (R3: one cell per unshared direction).** In the sourcing rule, a tower's matter counts through exactly one unit of length of each direction its neighbour lacks, on one side: a five-dimensional tower's matter through one unit of its extra direction, and a three-dimensional tower's sheets stacked one unit apart along the direction it lacks. the section ``The thickness: a contact mechanism'' gives a mechanism that returns this value and costs it.

\emph{The unit.} The unit is the length $d$ of Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}): one length common to all towers, the radius of the ball in which E counts mass, and independent of how a tower's mass is divided into quanta. This is the fixed-common-length reading, adopted by the decision of 19 November 2026; it replaces the reading of 10 November 2026, in which the unit was each tower's own cell radius, the Wigner-Seitz radius of its own filling. Under R1 and R2 (\claimref{dark-matter.r1-equal-mass-per-quantum}, \claimref{dark-matter.r2-one-quantum-per-unit-ball}), E holds in R2's common length, which is then $d$ (Proposition \claimref{dark-matter.unit-ball-rule}(iv)), every tower's cell radius is $d$ and the two readings coincide; under R2 alone they coincide only if R2 is taken in the length $d$. They differ when R2 fails: with a tower's own cell radius $a_{r}$ as the unit the shares are $(m_{r}/m_{6})(V_{3}/V_{D_{r}})(a_{6}/a_{r})^{3}$, which Premise E does not fix, and with the common length they are $V_{3}/V_{D_{r}}$ under E alone (Theorem \claimref{synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball}(i)). The title keeps the word cell: the cell is the unit ball of Premise E. The premise takes its unit from E, so where E is not assumed the unit has to be supplied in another way: by R1 with R2, whose common cell radius is then E's length, or by the democracy premise (\claimref{dark-matter.d-democracy-total-mass}), whose length is the de Sitter radius.

**Postulate 4 (C: the odd towers collisionless (model specification, reading (C))).** The matter of the four odd towers (the two three-dimensional and the two five-dimensional towers) has no self-interaction of order one. For the three-dimensional towers this means an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ at cluster speeds for isotropic compression, $4 \times 10^{-6}$ for compression normal to the sheets (Corollary \claimref{simulations.confinement-scale-does-not-matter}).

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Premises C and S2 belong to two exclusive readings of the three-dimensional towers' matter in the simulations: reading (C), collisionless, under Premise \claimref{simulations.c-odd-towers-collisionless}, and reading (W), a sheet fluid at composite strength, under Premise \claimref{simulations.s2-sheet-fluid}. The two simulation results (\claimref{simulations.halo-shapes}, \claimref{simulations.merger}) list both among their conditions because each reports both readings; no result holds the two together. C is not a statement about the series' structure: it is the condition the cluster bound requires (Corollary \claimref{simulations.confinement-scale-does-not-matter}), adopted as the premise of reading (C). Whether it holds is not decided by anything stored: the radiation audit leaves the three-dimensional towers' self-interaction at composite strength if their matter is the confined charged matter its closure leaves, which the series does not establish (Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}).

**Postulate 5 (S1: one species per tower (model specification)).** The matter of each populated tower is one species. Within its tower it is either collisionless or a fluid; across towers species interact only through gravity (Theorem \claimref{dark-matter.superselected-hence-dark-exactly-stable}). Our matter is two species: galaxies, collisionless, and our gas.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Its second clause, that species of different towers interact only through gravity, is not a premise: it is the stored Theorem \claimref{dark-matter.superselected-hence-dark-exactly-stable}, under that theorem's own conditions. Its first clause is a simplification of the model: for the five-dimensional towers the stored content under (S) is four Dirac species (Proposition \claimref{dark-tower-matter.five-dimensional-content}), treated here as one fluid component.

**Postulate 6 (S2: the sheet fluid (model specification, reading (W))).** At composite strength the three-dimensional towers' matter is an ideal gas with two degrees of freedom ($\gamma = 2$) whose pressure and viscosity act only within its sheet. Along the sheet's normal it moves without pressure, since sheets cross freely \cite[Rem.~7.30]{ButlerT14}. The sheets of a given orientation form one family shared by all the matter of the tower \cite[Lem.~6.1, Prem.~7.4]{ButlerT14}, so parcels of different halos on the same sheet collide. T14 does not say how quanta on differently oriented sheets interact; between two such parcels the force and separation are contracted with the mean of the two in-plane projectors, $(P_{i} + P_{j})/2$, which is the projection onto the sheet when the normals are parallel and otherwise keeps a fraction of each normal component (Lemma \claimref{simulations.averaged-pair-operator}).

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Premises C and S2 belong to two exclusive readings of the three-dimensional towers' matter in the simulations: reading (C), collisionless, under Premise \claimref{simulations.c-odd-towers-collisionless}, and reading (W), a sheet fluid at composite strength, under Premise \claimref{simulations.s2-sheet-fluid}. The two simulation results (\claimref{simulations.halo-shapes}, \claimref{simulations.merger}) list both among their conditions because each reports both readings; no result holds the two together. S2 is conditional on the three-dimensional towers' matter interacting at composite strength, the negation of C for those towers; under C it is vacuous for them. In the merger result reading (W) holds the subcluster's sheet fluid back with its gas and, with random or line-of-sight normals, gives no separate lensing peak (\claimref{simulations.merger}).

**Postulate 7 (S3: the mirror in a cluster (model specification)).** Mirror matter in a cluster is a fully ionised helium plasma, $\gamma = 5/3$, cooling by bremsstrahlung alone (below about $10^{6}$ K He$^{+}$ line cooling would in reality dominate, so settling would come sooner; Cost K3). Gas that cools below about $7 \times 10^{4}$ K becomes collisionless (the settled phase). There is no mirror star formation and no feedback.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Its window: the helium composition is the stored decimal estimate's only for a mirror temperature ratio $\xi = T'/T$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ (Computation \claimref{dark-tower-matter.mirrors-composition}); at $\xi = 2.8$ to $3.2 \times 10^{-4}$ (the gravitational floor's value with the production coefficients first imported) and at the present floor, $6.6 \times 10^{-4}$, that estimate gives a neutron-rich mirror for a copied lepton number $L \leq 0$ ($96$ to $100$ and $83$ to $96$ percent neutrons) and towards the $\Neff$ cap a hydrogen-rich one, and outside the window S3 is not the stored composition. Nothing stored fixes $\xi$.

**Postulate 8 (S4: our matter (model specification)).** Our gas is adiabatic, $\gamma = 5/3$, without cooling. Galaxies are collisionless particles carrying $2$ percent of each halo's mass. They are stellar-mass tracers on galaxy scales (each carries $10^{10}$ to $4 \times 10^{10}\ \Msun$), not galaxies with internal structure.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. It is a numerical approximation of this tower's matter and is not true of it as a statement about nature (our gas cools).

**Postulate 9 (S5: halos (model specification)).** Each halo is a Hernquist sphere matched to a Navarro-Frenk-White halo of the same mass and concentration, in equilibrium, with every species sharing the profile in proportion to its mass fraction.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. It is the numerical set-up of the initial conditions; nothing in the series bears on it.

## Introduction



**setting  (Introduction).** The dark-matter paper T14 \cite{ButlerT14} derives eight towers of the Clifford clock, proves that matter in the five populated dark towers gravitates on our metric and does nothing else, and by one geometric rule, the unit-ball rule, returns the ratio of dark to visible matter as $(11\pi + 16)/(3\pi) = 5.364$. The Clifford clock is the mod-$8$ periodicity of the real Clifford algebras, read as a ladder of spacetimes of different dimension, ours among them. The rule was found by fitting one length, so the total is not a test of it. What the rule also fixes, and what can be tested, is the composition: which towers hold how much, and therefore what that matter does when halos collide, when clusters assemble and when gas settles into a galaxy.

Tower dimensions count time. A three-dimensional tower has two space dimensions, so its matter lives on sheets, one direction short of ours; a five-dimensional tower has four, one more. There are two of each, and these four are the odd towers; with the mirror, a copy of ours, they are the five populated dark towers. The share of a tower is the ratio of unit-ball volumes, $V_{3}/V_{D}$ for a tower whose space has $D$ dimensions, which gives $V_{3}/V_{2} = 4/3$ for each three-dimensional tower (Fact \claimref{simulations.imported-unit-ball-rule-family}).

This note collects everything that was done to test the composition. It is a methods note: each section states its premises, the equations it uses, how the code implements them, and what came out. Nothing here changes a derived result of T14. Where the tests disagree with a physical statement of T14, the note says which statement and what was found, and T14 records the outcome in its Section 7.7.

**setting  (Introduction).** \textbf{What is tested.} Two readings of the same amounts:
\begin{enumerate}
\item[(W)] \emph{As written.} T14's discussion of its radiation audit fixes the three-dimensional towers' self-interaction at composite strength \cite[Prop.~6.2]{ButlerT14}: an in-sheet cross-section of nuclear size, $0.21$ to $2$ fm, since the audit closes these towers by confinement. The mirror is collisional and dissipative, the five-dimensional towers are left undetermined.
\item[(C)] \emph{Odd towers collisionless.} The same amounts, with the matter of all four odd towers collisionless (Premise \claimref{simulations.c-odd-towers-collisionless}). Only the mirror collides.
\end{enumerate}

**setting  (Introduction).** \textbf{What the note finds.}
\begin{itemize}
\item At composite strength the three-dimensional towers' matter is a fluid within its sheets, and its effective cross-section per mass in a cluster is $10^{8}$ to $10^{13}\ \cmg$ (Proposition \claimref{simulations.effective-cross-section-sheet-matter}, the table accompanying \claimref{simulations.effective-cross-section-sheet-matter}). The confinement scale does not matter (Corollary \claimref{simulations.confinement-scale-does-not-matter}); the series does not supply it, since no coupling rule for the odd towers follows from the algebra \cite[Prop.~A.4]{ButlerT14}.
\item In a Bullet-like merger, reading (W) loses the subcluster from the lensing map (unless every sheet's normal lies along the merger axis); reading (C) keeps it, with its mass peak on its galaxies and its gas behind (the section ``Results: mergers and halos''). T14's mixed count, which exchanges the two odd shares, is run alongside as a comparison and behaves as (W).
\item In an assembled cluster, (W) gives about $0.4$ of the cold-dark-matter (CDM) ellipticity, below CDM in both seeds, and (C) about $0.8$, overlapping it.
\item In the Milky Way, the mirror's proton-only branch is excluded; its helium branch, with helium-star feedback, fits the room at the Sun under some normalisations of the mirror's gas and survives in the bulge only if the bulge holds over twice the mirror's proportional share of its dark mass (the section ``The mirror in the Galaxy'').
\end{itemize}

**setting  (Introduction).** \textbf{Levels.} Proposition \claimref{simulations.effective-cross-section-sheet-matter}, Corollary \claimref{simulations.confinement-scale-does-not-matter} and Lemma \claimref{simulations.averaged-pair-operator} are proved here; Computation \claimref{simulations.cluster-bound-two-dimensions} is a numerical evaluation of an imported result. Everything that rests on simulation or on a galaxy-formation model is at observation level: it compares models with one another and with published measurements, and its costs are listed in the section ``What the tests decide, and what they cost''. The runs are idealised (about $80{,}000$ particles per merger and $32{,}000$ per assembled cluster, one merger geometry run once per composition, no cosmological surroundings), and they are suited to comparing compositions, not to precision prediction.

**setting  (Introduction).** \textbf{Films.} Two films accompany the note \cite{ButlerSuppT14b}. \file{merger\_three\_ways.mp4} shows the merger in three compositions side by side (a figure of the original); \file{bullet\_moment.mp4} builds up the Bullet-like moment of reading (C) layer by layer against the observed numbers (a figure of the original). Both are also on YouTube, as ``Galaxy clusters in collision'' and ``The Bullet moment''. the section ``The films'' describes what each shows and how it was made.

## Setting, imports and premises





**Theorem 10 (Imported: the unit-ball rule and its family).** Under Premises R1 (equal mass per quantum), R2 (one quantum per unit ball of each tower's space, with a common Wigner-Seitz radius $d_{b}$) and R3 (one cell radius per unshared direction), the share of a tower whose space has $D$ dimensions is $V_{3}/V_{D}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; 1 + 2\cdot\frac{4}{3} + 2\cdot\frac{8}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.364 .
\]
With the thickness of the unshared direction left as $c\,d_{b}$ the total is
\[
T(c) \;=\; 1 + \frac{8}{3c} + \frac{16c}{3\pi},
\]
which equals $5.364$ at $c = 1$ and $c = \pi/2$ and has its floor $5.255$ at $c = \sqrt{\pi/2}$. The three-dimensional towers' sheets are stacked one cell radius apart along the direction they lack, and they move with the matter. \emph{Provenance:} \cite[Prems.~7.2 to 7.4, Props.~7.6, 7.15 and 7.28]{ButlerT14}.

*Proof.* Under Premises R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) (equal mass per quantum), R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}) (one quantum per unit ball of each tower's space, with a common Wigner-Seitz radius $d_{b}$) and R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}) (one cell radius per unshared direction), the share of a tower whose space has $D$ dimensions is $V_{3}/V_{D}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; 1 + 2\cdot\frac{4}{3} + 2\cdot\frac{8}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.364 .
\]
With the thickness of the unshared direction left as $c\,d_{b}$ the total is
\[
T(c) \;=\; 1 + \frac{8}{3c} + \frac{16c}{3\pi},
\]
which equals $5.364$ at $c = 1$ and $c = \pi/2$ and has its floor $5.255$ at $c = \sqrt{\pi/2}$. The three-dimensional towers' sheets are stacked one cell radius apart along the direction they lack, and they move with the matter. \emph{Provenance:} \cite[Prems.~7.2 to 7.4, Props.~7.6, 7.15 and 7.28]{ButlerT14} (\claimref{dark-matter.reduced-response-gravity-needs-supporting-stress}, \claimref{dark-matter.total-function-thickness}, \claimref{dark-matter.unit-ball-rule}).




**Theorem 11 (Imported: the mirror).** The mirror tower is a copy of ours, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$ where its matter is helium or protons. Its temperature ratio $\xi = T'/T$ lies between the gravitational floor, $6.6 \times 10^{-4}$ (at the production coefficients and the mean energy per creation event since derived in the store; T14 printed $2.8$ to $3.2 \times 10^{-4}$), and the hot-deposit estimate, about $4 \times 10^{-3}$, a free datum of the descent that is an exception to P2 at its version-1 reach (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}; P2 as scoped leaves $\xi$ free, Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}, and the cold mirror then needs a non-equilibrium descent, Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}); its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$. T14 takes it to be helium on the expected (burning) branch and protons on the alternative; T14c finds it helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate, and at $\xi = 2.8$ to $3.2 \times 10^{-4}$, T14's printed floor, degenerate and, for a copied lepton number $L \leq 0$, $96$ to $100$ percent neutrons; at the present floor, $6.6 \times 10^{-4}$, it is still neutron-rich for $L \leq 0$, $83$ to $96$ percent neutrons, and only moderately degenerate (Computation \claimref{dark-tower-matter.mirrors-composition}). As neutral atoms its elastic cross-section per mass is of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\cmg$, and inside a halo it is a plasma, collisional and dissipative like our gas. \emph{Provenance:} \cite[Thm.~4.3, Props.~4.6 and 4.7, Prop.~6.2]{ButlerT14}.

*Proof.* The mirror tower is a copy of ours, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$. Its temperature ratio $\xi = T'/T$ lies between the gravitational floor, $6.6 \times 10^{-4}$ (the source prints $2.8$ to $3.2 \times 10^{-4}$, the value at the production coefficients first imported and at energy $3T$ per creation event; the present value is that of \claimref{dark-matter.stored-asymmetry-charge-not-number}(iii)), and the hot-deposit estimate, about $4 \times 10^{-3}$; its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$; on the expected (burning) branch it is helium, on the alternative it is protons. As neutral atoms its elastic cross-section per mass is of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\cmg$, and inside a halo it is a plasma, collisional and dissipative like our gas. \emph{Provenance:} \cite[Thm.~4.3, Props.~4.6 and 4.7, Prop.~6.2]{ButlerT14} (\claimref{dark-matter.stored-asymmetry-charge-not-number}, \claimref{dark-matter.mirror-share-one-how-fragile}, \claimref{dark-matter.mirror-tower-copy-one}, \claimref{dark-matter.radiation-audit-what-theorem-closes-what}).


**setting  (Imported from the dark-matter paper).** Throughout, the dark composition at $c = 1$ is
\begin{equation}
f_{\mathrm{mirror}} = \frac{3\pi}{11\pi + 16} = 0.1864,\qquad
f_{3\mathrm{D}} = \frac{8\pi}{11\pi + 16} = 0.4971,\qquad
f_{5\mathrm{D}} = \frac{16}{11\pi + 16} = 0.3165,
\end{equation}
and the baryon fraction of every halo is $1/(1 + T) = 0.1571$. Each tower's matter makes up these fractions of the dark matter in every halo; the cosmic baryon fraction is taken as the rule's $1/(1 + T) = 0.1571$ in the simulations and as Planck's $\Omega_{b}/\Omega_{m} = 0.1565$ in the Galaxy model (whose $H_{0}$ is $67.4$ km/s/Mpc; the simulations use $70$ in $r_{200}$). The mixed count of T14 \cite[Rem.~7.10]{ButlerT14} exchanges $f_{3\mathrm{D}}$ and $f_{5\mathrm{D}}$ and has the same total, since $T(\pi/2) = T(1)$. T14 records it as an assignment that is not consistent; it is run alongside as a comparison.



**Fact (imported) 12 (Imported: the Bullet Cluster).** In 1E0657-558 the two galaxy concentrations are $0.72$ Mpc apart on the sky; the lensing peaks lie $9.6''$ ($42$ kpc, subcluster) and $11.8''$ ($52$ kpc, main cluster) from the brightest cluster galaxies, within $1\sigma$ of the galaxy luminosity centroids, and the centres of total mass are offset from the plasma at $8\sigma$ \cite{Clowe2006}. The mass-to-light ratios give $(M/L)_{\mathrm{sub}}/(M/L)_{\mathrm{main}} = 0.84 \pm 0.07$, from which the subcluster has lost no more than about $23$ percent of its mass (a bound on mass loss inferred from the ratio, not on the mass inside a fixed aperture). The self-interaction cross-section per mass is below $1.25\ \cmg$ ($68$ percent) from the absence of an offset between mass and galaxies, whose centroids are known to about $5''$ ($22$ kpc), and below $0.7\ \cmg$ from the mass-to-light ratios \cite{Randall2008}. From $72$ cluster collisions $\sigma/m < 0.47\ \cmg$ at $95$ percent \cite{Harvey2015}, relaxed to about $2\ \cmg$ when that sample's offsets are corrected \cite{Wittman2018}.

*Provenance:* D. Clowe, M. Bradac, A. H. Gonzalez, M. Markevitch, S. W. Randall, C. Jones and D. Zaritsky, A direct empirical proof of the existence of dark matter, Astrophys. J. 648 (2006) L109.; S. W. Randall, M. Markevitch, D. Clowe, A. H. Gonzalez and M. Bradac, Constraints on the self-interaction cross section of dark matter from numerical simulations of the merging galaxy cluster 1E 0657-56, Astrophys. J. 679 (2008) 1173.; D. Harvey, R. Massey, T. Kitching, A. Taylor and E. Tittley, The nongravitational interactions of dark matter in colliding galaxy clusters, Science 347 (2015) 1462.; D. Wittman, N. Golovich and W. A. Dawson, The mismeasure of mergers: revised limits on self-interacting dark matter in merging galaxy clusters, Astrophys. J. 869 (2018) 104..



**Fact (imported) 13 (Imported: cluster shapes).** The mean projected ellipticity $\langle 1 - b/a\rangle$ of massive clusters from weak-lensing shear maps is $0.46 \pm 0.04$, in agreement with cold dark matter \cite{Oguri2010}.

*Provenance:* M. Oguri, M. Takada, N. Okabe and G. P. Smith, Direct measurement of dark matter halo ellipticity from two-dimensional lensing shear maps of 25 massive clusters, Mon. Not. R. Astron. Soc. 405 (2010) 2215..



**Fact (imported) 14 (Imported: the Milky Way's mass budget).** At the Sun the total surface density within $1.1$ kpc of the plane is $68 \pm 4\ \Msun\,\mathrm{pc^{-2}}$, of which stars and stellar remnants contribute $38 \pm 4$ dynamically \cite{BovyRix2013}; counted, stars and remnants are $33.4 \pm 3$ and gas $13.7 \pm 1.6$, a total of $47.1 \pm 3.4$ \cite{McKee2015}. A thin dark disk is bounded at $95$ percent by $4.56$ ($h \le 50$ pc) and $5.59\ \Msun\,\mathrm{pc^{-2}}$ ($h = 100$ pc), with $68$ percent bounds $2.17$ and $2.71$ \cite{Widmark2021}. The bulge region holds a dynamical mass of $(1.85 \pm 0.05) \times 10^{10}\ \Msun$ with a dark fraction of $17 \pm 2$ percent \cite{Portail2017}. A mirror analysis bounds the excess bulge mass, dynamical minus photometric, by $0.83 \times 10^{10}\ \Msun$ at $2\sigma$, and finds $\Omega_{b'} \lesssim 0.8\,\Omega_{b}$ at low mirror temperature \cite{RouxCline2020}.

*Provenance:* J. Bovy and H.-W. Rix, A direct dynamical measurement of the Milky Way's disk surface density profile, disk scale length, and dark matter profile at 4 kpc $lesssim R lesssim$ 9 kpc, Astrophys. J. 779 (2013) 115.; C. F. McKee, A. Parravano and D. J. Hollenbach, Stars, gas, and dark matter in the solar neighborhood, Astrophys. J. 814 (2015) 13.; A. Widmark, C. F. P. Laporte, P. F. de Salas and G. Monari, Weighing the Galactic disk using phase-space spirals. II. Most stringent constraints on a thin dark disk using Gaia EDR3, Astron. Astrophys. 653 (2021) A86.; M. Portail, O. Gerhard, C. Wegg and M. Ness, Dynamical modelling of the galactic bulge and bar: the Milky Way's pattern speed, stellar and dark matter mass distribution, Mon. Not. R. Astron. Soc. 465 (2017) 1621.; J.-S. Roux and J. M. Cline, Constraining galactic structures of mirror dark matter, Phys. Rev. D 102 (2020) 063518..

**setting  (The premises of this note).** The simulations need a model of each tower's matter that T14 does not supply. These are the premises, stated once and used throughout.

## Self-interaction within a sheet



**setting  (The effective cross-section).** A quantum of a three-dimensional tower lives in a two-dimensional sheet. It collides only with quanta of its own sheet, and its cross-section is a length $\lambda$. Gravity sees the tower's matter per unit of shared three-volume \cite[Lem.~6.1]{ButlerT14}.



**Theorem 15 (The effective cross-section of sheet matter).** Let the sheets carry $n_{2}$ quanta per unit area, be stacked a distance $s$ apart, and let each quantum have in-sheet cross-section $\lambda$. Then the collision rate of a quantum moving at speed $v$ equals that of a three-dimensional gas of number density $n_{3} = n_{2}/s$ with cross-section
\[
\sigma_{\mathrm{eff}} \;=\; \lambda\, s ,
\qquad\text{so}\qquad
\frac{\sigma_{\mathrm{eff}}}{m} \;=\; \frac{\lambda s}{m}.
\]
In a halo region of overdensity $\Delta$ at redshift $z$ the spacing lies between $d_{b}\Delta^{-1}/(1+z)$ (all compression along the normal) and $d_{b}/(1+z)$ (all compression in the plane), and is $s = d_{b}\Delta^{-1/3}/(1+z)$ for isotropic compression. Here $d_{b}$ is the mean comoving spacing of the sheets, which R3 sets at one unit. \emph{Note (19 November 2026).} R3's unit is the length of Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}); it is this world's baryon spacing $d_{b}$ in the particle model, R1 and R2, assumed here for that value. The identity $\sigma_{\mathrm{eff}} = \lambda s$ needs neither.

*Proof.* The in-sheet collision rate is $n_{2}\lambda v$, and $n_{2}\lambda v = (n_{2}/s)(\lambda s)v = n_{3}\sigma_{\mathrm{eff}}v$. By R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}) the sheets are one unit apart in the mean, comoving \cite[Prem.~7.4]{ButlerT14}, and under R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) and R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}) that unit is the common cell radius $d_{b}$, this world's baryon spacing. A region compressed by $\Delta$ in volume has its comoving lengths reduced by $\Delta$ along one direction, by $\Delta^{1/3}$ along each for isotropic compression, or not at all along the normal if the compression is in the plane; the physical spacing carries the further factor $1/(1+z)$.


**setting  (The effective cross-section).** With R1 ($m$ the nucleon mass) and R2, Planck's $\Omega_{b}h^{2} = 0.02237$ and $h = 0.674$ give $n_{b} = 0.251\ \mathrm{m^{-3}}$ and $d_{b} = (3/4\pi n_{b})^{1/3} = 0.983$ m. In a cluster core ($\Delta = 10^{4}$, $z = 0.3$) the isotropic spacing is $3.5$ cm. the table accompanying \claimref{simulations.effective-cross-section-sheet-matter} gives the result for the range of composite sizes and compressions.

\centering \begin{tabular}{@{}lccc@{}}
\toprule
Region & normal compression & isotropic & in-plane compression \\
\midrule
outskirts, $\Delta = 200$ & $4.7\times10^{9}$ to $4.5\times10^{10}$ & $1.6\times10^{11}$ to $1.5\times10^{12}$ & $9.5\times10^{11}$ to $9.0\times10^{12}$ \\
core, $\Delta = 10^{4}$ & $9.5\times10^{7}$ to $9.0\times10^{8}$ & $4.4\times10^{10}$ to $4.2\times10^{11}$ & $9.5\times10^{11}$ to $9.0\times10^{12}$ \\
\bottomrule
\end{tabular}

\emph{The three-dimensional towers' $\sigma_{\mathrm{eff}}/m$ in $\cmg$ (Proposition \claimref{simulations.effective-cross-section-sheet-matter}), in clusters at $z = 0.3$ ($\Delta$ the overdensity), for in-sheet cross-sections $\lambda = 0.21$ fm (the nucleon's Compton length) to $2$ fm. The cluster bounds are $0.47$ to $1.25\ \cmg$ (Fact \claimref{simulations.imported-bullet-cluster}). In a core at $\lambda = 1$ fm the in-sheet mean free path $1/(n_{2}\lambda)$ is $26$ AU, so on cluster scales the matter is a fluid within its sheets.}



**Fact (imported) 16 (Imported: low-energy scattering in two dimensions).** For elastic scattering in two dimensions by a hard disk of radius $a$, the partial-wave phase shifts are $\tan\delta_{m} = J_{m}(ka)/Y_{m}(ka)$ and the total cross-section is the length $\lambda = (4/k)\sum_{m=-\infty}^{\infty}\sin^{2}\delta_{m}$. As $ka \to 0$ only $m = 0$ survives, with $\delta_{0} \to \pi/\bigl(2(\ln(ka/2) + \gamma_{E})\bigr)$; the same logarithmic form holds for any short-range interaction with two-dimensional scattering length of order $a$. \emph{Provenance:} \cite{Adhikari1986}.

*Provenance:* S. K. Adhikari, Quantum scattering in two dimensions, Am. J. Phys. 54 (1986) 362..



**Theorem 17 (The cluster bound in two dimensions).** For quanta of the nucleon mass at a relative speed of $3000$ km/s ($k = 0.0238\ \mathrm{fm^{-1}}$ in the centre-of-mass frame):
\begin{enumerate}
\item[(i)] a hard disk of radius $0.21$ fm has $\lambda = 13$ fm from the partial-wave sum and $14$ fm from the logarithmic form; of radius $10^{-11}$ fm, still $\lambda = 0.49$ fm;
\item[(ii)] the bound $\sigma_{\mathrm{eff}}/m < 1\ \cmg$ in a cluster core (isotropic spacing) requires $\lambda < 4.8 \times 10^{-12}$ fm;
\item[(iii)] by size alone that requires $a < 10^{-4.0 \times 10^{6}}$ fm; by interaction strength, an s-wave phase shift $\delta_{0} < 1.7 \times 10^{-7}$.
\end{enumerate}

*Proof.* Follows from \claimref{simulations.imported-low-energy-scattering-two-dimensions} and \claimref{simulations.effective-cross-section-sheet-matter}, as the source states.

The computation rests on \claimref{dark-matter.r1-equal-mass-per-quantum} and \claimref{dark-matter.r2-one-quantum-per-unit-ball}, which fix the common mass and the Wigner-Seitz radius $d_{b}$ (one quantum of the common mass per unit ball of the common length), and on \claimref{dark-matter.r3-one-cell-per-unshared-direction}, through \claimref{simulations.effective-cross-section-sheet-matter}, which stacks the sheets $d_{b}$ apart: together they fix the isotropic spacing of a cluster core used in (ii).


**setting  (The confinement scale drops out).** \textbf{How it is computed.} (i) is Fact \claimref{simulations.imported-low-energy-scattering-two-dimensions} evaluated at $ka = 0.0050$ and $ka = 2.4 \times 10^{-13}$, with $\mu = m/2$; the script computes the Bessel functions by their series and the partial-wave sum to $m = \pm 1$. (ii) is Proposition \claimref{simulations.effective-cross-section-sheet-matter} with $s = 3.5$ cm solved for $\lambda$. (iii) With the s-wave alone $\lambda = 4\sin^{2}\delta_{0}/k$, so $\lambda < 4.8 \times 10^{-12}$ fm gives $\delta_{0} < 1.7 \times 10^{-7}$; in the logarithmic form $\lambda \approx \pi^{2}/\bigl(k(\ln(ka/2) + \gamma_{E})^{2}\bigr)$, so the bound requires $|\ln(ka/2) + \gamma_{E}| > 9.3 \times 10^{6}$, that is $a < 10^{-4.0 \times 10^{6}}$ fm. These are floating-point evaluations, checked in the script (the section ``Machine verification''); nothing below depends on their digits beyond the first.



**Theorem 18 (The confinement scale does not matter).** Any self-interaction of composite strength makes the three-dimensional towers' matter a fluid in clusters, whatever the size of a composite. The cluster bound is met only if the quanta barely interact: an in-sheet phase shift below about $2 \times 10^{-7}$ (isotropic compression in a core; about $4 \times 10^{-6}$ for compression normal to the sheets), which is Premise C.

*Proof.* For $\lambda \ge 0.21$ fm, the table accompanying \claimref{simulations.effective-cross-section-sheet-matter} gives $\sigma_{\mathrm{eff}}/m \ge 9.5 \times 10^{7}\ \cmg$ in every cluster region and compression. Smaller composites barely lower this: a hard disk of radius $a = 10^{-30}$ fm still has $\lambda \approx \pi^{2}/\{k\,[\ln(ka/2) + \gamma_{E}]^{2}\} \approx 0.08$ fm (with $\ln(ka/2) = -73.5$; by \claimref{simulations.imported-low-energy-scattering-two-dimensions}), so $\sigma_{\mathrm{eff}}/m \ge 3 \times 10^{7}\ \cmg$ (by \claimref{simulations.effective-cross-section-sheet-matter}), and the matter remains a fluid on cluster scales. The size of a composite enters $\lambda$ only through the logarithm (Computation \claimref{simulations.cluster-bound-two-dimensions}(i) and (iii)), so no physical confinement scale reaches the bound. The phase-shift limits are Computation \claimref{simulations.cluster-bound-two-dimensions}(iii) at the isotropic spacing and, since $\lambda \propto \sin^{2}\delta_{0}$ and the bound on $\lambda$ scales as $1/s$, a factor $(4.4 \times 10^{10}/9.5 \times 10^{7})^{1/2} \approx 22$ larger at the normal-compression spacing.


**setting  (The confinement scale drops out).** \textbf{The five-dimensional towers and the mirror.} A five-dimensional tower's matter counts through one cell radius $L$ of its extra direction, so its effective cross-section is $\sigma_{4}/L$ with $\sigma_{4} \sim \lambda^{3}$; in general $\sigma_{\mathrm{eff}} = \sigma_{D}\,d_{b}^{\,3-D}$. For $\lambda = 0.21$ to $2$ fm and $L = d_{b}/(1+z)$ this is $7 \times 10^{-20}$ to $6 \times 10^{-17}\ \cmg$: collisionless by geometry. The mirror's figure is that of Fact \claimref{simulations.imported-mirror}, $5 \times 10^{7}$ to $2 \times 10^{8}\ \cmg$: a fluid like our gas. a figure of the original shows the three.

**setting  (The colliding share).** If collisional dark matter were held back in a merger as completely as the gas is, the share of the dark matter that collides would bound the subcluster's mass loss, whatever its cross-section. As a heuristic, then, by the relation displayed with \claimref{simulations.imported-mirror}:
\[
\text{(W): } f_{\mathrm{mirror}} + f_{3\mathrm{D}} = 68.3\%, \qquad
\text{(C): } f_{\mathrm{mirror}} = 18.6\%, \qquad
\text{mixed count: } 50.3\%,
\]
against a mass loss of at most $23$ percent (Fact \claimref{simulations.imported-bullet-cluster}). These are shares of the dark matter, as T14 counts them, so the bound is read as a bound on the subcluster's dark matter, its gas having been stripped in any case. Counted with the subcluster's own gas ($13.7$ percent of its mass: the baryon fraction $0.157$ less the $2$ percent in galaxies), the colliding fraction of its mass is $0.137 + 0.843\,f$, with $f$ the colliding share of the dark matter above: $71$ percent in (W), $29$ in (C) and $56$ in the mixed count, and on that count reading (C) is above the bound as well. T14 \cite[Rem.~7.10, Prop.~7.15(v)]{ButlerT14} counts the self-interacting fraction as the three-dimensional towers alone (about half) and tests the mirror's $18.6$ percent separately; for a bound on mass loss the two add. The simulations of the section ``Results: mergers and halos'' test the heuristic, and it holds only roughly in either direction: colliding matter that partly passes through is held back less than its share (\texttt{rule\_par}), while a halo that puffs loses more than its share from a fixed aperture (Observation \claimref{simulations.merger}). a figure of the original shows the comparison.

## The simulation code



**setting  (The simulation code).** The code \file{tpsim.c} \cite{ButlerSuppT14b} was written for these tests, in C with OpenMP. It solves gravity for every particle and smoothed-particle hydrodynamics separately for each fluid species, so that each fluid interacts hydrodynamically only with itself (Premise S1).

**setting  (Units and species).** Lengths are in kpc, velocities in km/s and masses in $10^{10}\ \Msun$, so that $G = 43009.1$ and the unit of time is $1\ \kpc/(\mathrm{km/s}) = 0.9778$ Gyr. Particle types are:
\begin{itemize}
\item[$0$] collisionless dark matter: the five-dimensional towers, in reading (C) the three-dimensional towers, and in the compositions with the mirror settled from the start, the mirror;
\item[$1$] galaxies;
\item[$2$] our gas;
\item[$3$] mirror gas;
\item[$4$] sheet fluid;
\item[$5$] settled mirror matter.
\end{itemize}

**setting  (Gravity).** Gravity is computed with a Barnes-Hut octree \cite{BarnesHut1986}. A node of side $\ell$ at distance $r$ from its centre of mass is opened if $\ell^{2} > \theta^{2}r^{2}$ or if the particle lies inside it, with $\theta = 0.7$. Forces use Plummer softening,
\[
\mathbf{a}_{i} \;=\; \sum_{j} G\,m_{j}\,\frac{\mathbf{r}_{j} - \mathbf{r}_{i}}{\bigl(|\mathbf{r}_{j} - \mathbf{r}_{i}|^{2} + \epsilon^{2}\bigr)^{3/2}},
\qquad \epsilon = 15\ \kpc ,
\]
with nodes standing in for the particles they contain.

**setting  (Smoothed-particle hydrodynamics).** Each fluid species has its own tree. The kernel is the cubic spline of support $2h$ \cite{MonaghanLattanzio1985},
\[
W(r, h) = \frac{1}{\pi h^{3}}
\begin{cases}
1 - \tfrac{3}{2}q^{2} + \tfrac{3}{4}q^{3}, & 0 \le q < 1,\\[2pt]
\tfrac{1}{4}(2 - q)^{3}, & 1 \le q < 2,\\[2pt]
0, & q \ge 2,
\end{cases}
\qquad q = r/h ,
\]
normalised so that $\int W\,d^{3}r = 1$. Density is gathered at each particle's own smoothing length, $\rho_{i} = \sum_{j} m_{j}W(r_{ij}, h_{i})$; pressure and sound speed are $P_{i} = (\gamma - 1)\rho_{i}u_{i}$ and $c_{i} = \sqrt{\gamma(\gamma - 1)u_{i}}$. The next smoothing length is
\[
h_{i} = \tfrac{1}{2}\Bigl(\frac{3N_{\mathrm{ngb}}m_{i}}{4\pi\rho_{i}}\Bigr)^{1/3}, \qquad N_{\mathrm{ngb}} = 40,
\]
limited to a change between $0.8$ and $1.25$ per step, floored at $h_{\min} = 10\ \kpc$, and cut to $0.7h_{i}$ if a particle's neighbour list reaches its cap of $2000$.

The equations of motion are the symmetric form \cite{Monaghan1992},
\begin{align*}
\frac{d\mathbf{v}_{i}}{dt} &= -\sum_{j} m_{j}\Bigl(\frac{P_{i}}{\rho_{i}^{2}} + \frac{P_{j}}{\rho_{j}^{2}} + \Pi_{ij}\Bigr)\,\mathbf{g}_{ij},
\\
\frac{du_{i}}{dt} &= \sum_{j} m_{j}\Bigl(\frac{P_{i}}{\rho_{i}^{2}} + \tfrac{1}{2}\Pi_{ij}\Bigr)\,\mathbf{v}_{ij}\cdot\mathbf{g}_{ij},
\end{align*}
with the kernel gradient averaged over the two smoothing lengths, $\mathbf{g}_{ij} = \tfrac{1}{2}\bigl(\nabla_{i}W(r_{ij}, h_{i}) + \nabla_{i}W(r_{ij}, h_{j})\bigr)$, and $\mathbf{v}_{ij} = \mathbf{v}_{i} - \mathbf{v}_{j}$. The artificial viscosity acts on approaching pairs \cite{MonaghanGingold1983}:
\[
\Pi_{ij} = \frac{-\alpha\,\bar{c}_{ij}\mu_{ij} + \beta\mu_{ij}^{2}}{\bar{\rho}_{ij}}, \qquad
\mu_{ij} = \frac{\bar{h}_{ij}\,\mathbf{v}_{ij}\cdot\mathbf{r}_{ij}}{r_{ij}^{2} + 0.01\bar{h}_{ij}^{2}} \quad (\mathbf{v}_{ij}\cdot\mathbf{r}_{ij} < 0),
\]
with $\alpha = 1$, $\beta = 2$ and bars denoting pair means. Internal energy is floored at $u_{\mathrm{floor}} = u(10^{4}\ \mathrm{K})$ for mean particle mass $0.6\,m_{p}$.

**setting  (The sheet fluid).** Premise S2 is implemented by contracting both the kernel gradient and the separation vector of every pair of sheet-fluid particles with an averaged pair operator before they enter the equations above. With $\mathbf{n}_{i}$ and $\mathbf{n}_{j}$ the unit normals of the two particles' sheets,
\begin{equation}
P_{ij}(\mathbf{v}) \;=\; \mathbf{v} - \tfrac{1}{2}\bigl((\mathbf{v}\cdot\mathbf{n}_{i})\mathbf{n}_{i} + (\mathbf{v}\cdot\mathbf{n}_{j})\mathbf{n}_{j}\bigr),
\qquad
\mathbf{g}_{ij} \mapsto P_{ij}\mathbf{g}_{ij}, \quad \mathbf{r}_{ij} \mapsto P_{ij}\mathbf{r}_{ij}.
\end{equation}
$P_{ij}$ is the mean of the two in-plane projectors, the rejections $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n}_{i})\,\mathbf{n}_{i}$ and $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n}_{j})\,\mathbf{n}_{j}$ (Lemma \claimref{simulations.averaged-pair-operator}(ii)). When all normals are parallel it is the projection onto the common sheet, nothing acts along the normal except gravity, and motion along it is ballistic; for differently oriented normals it is not a projection and keeps part of each normal component (Lemma \claimref{simulations.averaged-pair-operator}(iii)). Each particle's normal is fixed at its initial value, random per particle or common to all (the section ``Initial conditions'').



**Theorem 19 (The averaged pair operator).** \begin{enumerate}
\item[(i)] $P_{ij} = P_{ji}$, and the contracted pair forces conserve momentum exactly and, in the equations before time integration and with the smoothing lengths held fixed within a step, total energy.
\item[(ii)] For parallel normals $\mathbf{n}_{i} = \mathbf{n}_{j} = \mathbf{n}$, $P_{ij}$ is the projection onto the sheet: in the geometric algebra of $\mathbb{R}^{3}$ it is the rejection $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n})\,\mathbf{n}$, and it annihilates $\mathbf{n}$.
\item[(iii)] For orthogonal normals it keeps half of each normal component; its eigenvalues are then $1$, $\tfrac{1}{2}$, $\tfrac{1}{2}$, so it is idempotent only when $\mathbf{n}_{i} = \pm\mathbf{n}_{j}$.
\end{enumerate}

*Proof.* (i) $P_{ij}$ is symmetric in $i$ and $j$ and $\mathbf{g}_{ij} = -\mathbf{g}_{ji}$, so the force of $j$ on $i$, $-m_{i}m_{j}F_{ij}P_{ij}\mathbf{g}_{ij}$ with $F_{ij}$ the symmetric bracket, is minus the force of $i$ on $j$. The kinetic power of the pair is $-m_{i}m_{j}F_{ij}\,\mathbf{v}_{ij}\cdot P_{ij}\mathbf{g}_{ij}$, and the two internal-energy terms sum to $+m_{i}m_{j}F_{ij}\,\mathbf{v}_{ij}\cdot P_{ij}\mathbf{g}_{ij}$, since $\mathbf{v}_{ji}\cdot P_{ji}\mathbf{g}_{ji} = \mathbf{v}_{ij}\cdot P_{ij}\mathbf{g}_{ij}$ and the viscous term is split equally. (ii) With $Q(\mathbf{n}) = \mathbf{n}\mathbf{n} = 1$ (\claimref{std-algebra.vector-squares}) and $\mathbf{v}\mathbf{n} = \mathbf{v}\cdot\mathbf{n} + \mathbf{v}\wedge\mathbf{n}$ (\claimref{std-algebra.product-decomposition}), $(\mathbf{v}\wedge\mathbf{n})\mathbf{n} = (\mathbf{v}\mathbf{n} - \mathbf{v}\cdot\mathbf{n})\mathbf{n} = \mathbf{v} - (\mathbf{v}\cdot\mathbf{n})\mathbf{n}$, which is $P_{ij}(\mathbf{v})$ for $\mathbf{n}_{i} = \mathbf{n}_{j} = \mathbf{n}$. (iii) For $\mathbf{n}_{i}\perp\mathbf{n}_{j}$, $P_{ij}\mathbf{n}_{i} = \tfrac{1}{2}\mathbf{n}_{i}$, $P_{ij}\mathbf{n}_{j} = \tfrac{1}{2}\mathbf{n}_{j}$ and $P_{ij}$ fixes the direction dual to $\mathbf{n}_{i}\wedge\mathbf{n}_{j}$, $(\mathbf{n}_{i}\wedge\mathbf{n}_{j})I_{3}$ with $I_{3}$ the pseudoscalar of $\Cl(3,0)$, so $P_{ij}^{2} \ne P_{ij}$; in general $P_{ij}$ is idempotent only when $(\mathbf{v}\cdot\mathbf{n}_{i})\mathbf{n}_{i} = (\mathbf{v}\cdot\mathbf{n}_{j})\mathbf{n}_{j}$ for every $\mathbf{v}$, that is $\mathbf{n}_{i} = \pm\mathbf{n}_{j}$. Not covered by (i): variable smoothing lengths without correction terms, and what acts after these equations (the integrator, the energy floor and cooling). The script checks (i) on a rational instance with distinct normals and viscosity, (ii) exactly in the blade engine, and (iii) in exact rationals.


**setting  (The sheet fluid).** The averaging in the relation displayed with \claimref{simulations.confinement-scale-does-not-matter} is an approximation: it stands in for the interaction of quanta on differently oriented sheets, which T14 does not specify (Premise S2). The runs with all sheets parallel (the section ``Initial conditions'') do not use the average. With the normals along the line of sight (\texttt{rule\_perp}) the subcluster fails as with random sheets; with the normals along the merger axis (\texttt{rule\_par}) the fluid slides through along the axis and the subcluster keeps a lensing peak but half its mass (the section ``Results: mergers and halos'').

**setting  (The mirror's cooling and settling).** Bremsstrahlung from a fully ionised helium plasma, with Gaunt factor $1.2$ and $Z^{2} = 4$, gives $du/dt = -A\rho\sqrt{u}$ for a constant $A$. At fixed density this has the exact solution
\[
\sqrt{u(t + \Delta t)} \;=\; \sqrt{u(t)} - \tfrac{1}{2}A\rho\,\Delta t ,
\]
which the code applies after each step. When $u$ falls below $3u_{\mathrm{floor}}$ (for the helium plasma, $\mu = 4/3$, about $6.7 \times 10^{4}$ K) the particle becomes type $5$ and is collisionless from then on (Premise S3).

**setting  (Time integration and output).** All particles share one time step,
\[
\Delta t = \min\Bigl(\Delta t_{\max},\ \min_{i}\tfrac{1}{4}\sqrt{\epsilon/|\mathbf{a}_{i}|},\ \min_{i\in\text{fluid}}\tfrac{1}{4}h_{i}/v_{\mathrm{sig},i}\Bigr),\qquad
v_{\mathrm{sig},i} = \max\Bigl(2c_{i},\ \max_{j}\bigl(c_{i} + c_{j} - 3w_{ij}\bigr)\Bigr),
\]
with $\Delta t_{\max} = 0.002$, the inner maximum over approaching pairs, and $w_{ij} = \mathbf{v}_{ij}\cdot\mathbf{r}_{ij}/r_{ij}$, negative on approach. The integrator is kick-drift-kick leapfrog, with the step shortened to land on each output time. Snapshots record positions, velocities, masses, internal energies, densities, smoothing lengths, types and halo labels. A merger run takes $15$ to $60$ minutes on two cores.

**setting  (Time integration and output).** \textbf{Tests.} Two tests (\file{tpsim\_tests.py}, output deposited) check the sheet fluid and the code's stability. A uniform sphere of hot sheet fluid ($2000$ particles) with every normal along $z$ grows in rms extent by factors $1.49$ and $1.47$ in $x$ and $y$ over $0.1$ time units and stays at $1.00$ in $z$; with random normals it grows by $1.33$ to $1.35$ along all three axes. An isolated main-cluster halo with the unit-ball composition as written ($20{,}000$ particles, every species) keeps its $10$ and $50$ percent mass radii within $1.3$ percent over $1$ time unit ($0.98$ Gyr).

## Initial conditions



**setting  (Halos).** A halo of mass $M_{200}$ and concentration $c$ is a Hernquist sphere of the same mass inside $r_{200}$, with the scale length that matches the Navarro-Frenk-White inner profile \cite{Hernquist1990, NFW1997, SpringelDiMatteoHernquist2005}:
\[
r_{200} = \Bigl(\frac{GM_{200}}{100H_{0}^{2}}\Bigr)^{1/3},\qquad
a = \frac{r_{200}}{c}\sqrt{2\Bigl[\ln(1 + c) - \frac{c}{1 + c}\Bigr]},\qquad
M_{H} = M_{200}\Bigl(1 + \frac{a}{r_{200}}\Bigr)^{2},
\]
with $H_{0} = 70$ km/s/Mpc; the first is the radius inside which the mean density is $200$ times critical, and the last makes the Hernquist enclosed mass $M_{H}r^{2}/(r + a)^{2}$ equal $M_{200}$ at $r_{200}$. The sphere is truncated at $15a$, keeping $225/256$ of $M_{H}$. Positions are drawn from the enclosed-mass profile; each particle is then assigned a species at random in proportion to the species' mass fraction (Premise S5).

Collisionless particles take speeds from the isotropic Hernquist distribution function $f(E)$ \cite{Hernquist1990} by rejection sampling up to the escape speed, with random directions. Fluid particles start at rest with $u = \sigma_{r}^{2}/(\gamma - 1)$, so that $P = \rho\sigma_{r}^{2}$ and the gas is in hydrostatic equilibrium with the isotropic Jeans dispersion
\[
\sigma_{r}^{2}(r) = \frac{GM_{H}}{12a}\Bigl[12x(1 + x)^{3}\ln\frac{1 + x}{x} - \frac{x}{1 + x}\bigl(25 + 52x + 42x^{2} + 12x^{3}\bigr)\Bigr], \qquad x = r/a ,
\]
which solves $d(\rho\sigma_{r}^{2})/dr = -\rho\,GM(r)/r^{2}$ for the Hernquist density. The sheet fluid has no pressure along its normal, so it also carries a Gaussian velocity of dispersion $\sigma_{r}$ along the normal.

**setting  (The merger).** Modelled on the Bullet Cluster: a main cluster with $M_{200} = 1.5 \times 10^{15}\ \Msun$ and $c = 4$ ($60{,}000$ particles), and a subcluster with $1.5 \times 10^{14}\ \Msun$ and $c = 7$ ($20{,}000$ particles), separated by $2500$ kpc along $x$ with impact parameter $150$ kpc along $y$, closing at $1800$ km/s, in the centre-of-mass frame. The random-number seed is $7$ for every merger. The truncated masses are $2.29 \times 10^{15}$ and $1.97 \times 10^{14}\ \Msun$, so main-cluster particles carry $3.8 \times 10^{10}\ \Msun$ and subcluster particles $9.8 \times 10^{9}\ \Msun$. Every halo has baryons $0.1571$ of its mass (galaxies $0.020$, our gas $0.1371$) and dark matter $0.8429$, split by composition as in the table accompanying \claimref{simulations.averaged-pair-operator}. The line of sight is $z$, perpendicular to the orbit.

\centering \begin{tabular}{@{}lllll@{}}
\toprule
Code & Mirror & 3D towers & 5D towers & Reading \\
\midrule
\texttt{cdm} & collisionless & collisionless & collisionless & reference \\
\texttt{rule} & gas $0.186$ & sheet fluid $0.497$ & collisionless $0.316$ & (W) \\
\texttt{mirror} & gas $0.186$ & collisionless & collisionless & (C) \\
\texttt{mixed} & gas $0.186$ & sheet fluid $0.316$ & collisionless $0.497$ & mixed count, (W) \\
\texttt{mixednm} & collisionless & sheet fluid $0.316$ & collisionless & mixed count, mirror settled \\
\texttt{rule1} & gas $0.186$ & one tower fluid $0.249$ & collisionless & one 3D tower collides \\
\texttt{rule1nm} & collisionless & one tower fluid $0.249$ & collisionless & as \texttt{rule1}, mirror settled \\
\bottomrule
\end{tabular}

\emph{Compositions run, as shares of the dark matter (\file{merger.py}). The orientation codes describe the sheets' normals: \texttt{random} (a random normal per particle), \texttt{perp} (all normals along the line of sight, perpendicular to the merger axis, so the axis lies in the sheets) and \texttt{par} (all normals along the merger axis). A run is named \emph{model\_orientation}; \texttt{mirror\_only} is model \texttt{mirror} with random normals, reading (C). Suffix \texttt{nm}: the mirror collisionless from the start; suffix \texttt{lo}: half resolution.}

The variants isolate one effect each. \texttt{mixed} is T14's mixed count with the mirror as gas. \texttt{mixednm} and \texttt{rule1nm} make the mirror collisionless from the start, so that only the sheet fluid collides and its effect is seen apart from the mirror gas's; \texttt{rule1} and \texttt{rule1nm} let only one of the two three-dimensional towers collide, halving the sheet fluid.

**setting  (Cluster assembly).** Eight progenitors with $M_{200} = 2 \times 10^{14}\ \Msun$ and $c = 5$, $4000$ particles each, are placed at random inside $1.5$ Mpc, at least $700$ kpc apart, with random velocities of dispersion $150$ km/s, and the whole is set at rest at the origin. They collapse and merge into one cluster, $2.3 \times 10^{15}\ \Msun$ in all with $M_{200} \approx 2.0 \times 10^{15}\ \Msun$ at the end, followed to $t = 2.0$ ($1.96$ Gyr). Each composition in the table accompanying \claimref{simulations.merger} is run with two random seeds, $11$ and $23$; \texttt{rule1} is run once, with seed $11$ (projected ellipticity $0.17$, $0.72$ of CDM's with the same seed), and is not tabulated.

## Measurements



**setting  (Measurements).** \textbf{Centres.} Each cluster's centre is found by shrinking spheres on its own collisionless members (dark matter, galaxies and settled mirror matter): the centre of mass within a sphere, the sphere shrunk by $10$ percent, repeated down to $40$ kpc. The search at each snapshot starts from the previous one.

**setting  (Measurements).** \textbf{The Bullet-like moment.} The Bullet-like moment is the nearer of the two snapshots after closest approach that bracket the observed $720$ kpc separation, or the last snapshot ($t = 1.3$) if that separation is never reached.

**setting  (Measurements).** \textbf{Quantities measured.} At that moment, projected along $z$ on a $10$ kpc grid smoothed by $25$ kpc:
\begin{itemize}
\item \emph{galaxy peak}: the maximum of the subcluster's galaxies within $150$ kpc of its centre;
\item \emph{lensing contrast}: projected total mass at the galaxy peak divided by the main cluster's azimuthal median at the same radius from its own peak; a value near $1$ means the subcluster has no separate lensing peak;
\item \emph{mass-peak offset}: the signed distance along the motion from the galaxy peak to the nearest local maximum of projected mass within $300$ kpc of it and more than $250$ kpc from the main cluster's peak, positive when the mass peak leads the galaxies; offsets below $10$ kpc are within one grid cell;
\item \emph{gas offset}: the distance along the motion from the galaxy peak to the maximum of our gas weighted by $m\rho$ (an X-ray proxy) within $450$ kpc of it and more than $200$ kpc from the main cluster's peak;
\item \emph{own mass}: the subcluster's own particles within $150$ kpc of its galaxy peak, relative to the same quantity in the CDM run at CDM's Bullet-like moment ($t = 1.12$; the half-resolution runs against \texttt{cdm\_lo} at $t = 1.10$);
\item \emph{galaxy concentration}: the subcluster's galaxy mass within $150$ kpc of its galaxy peak, relative to that within $150$ kpc of its centre at $t = 0$;
\item \emph{mass-to-light change}: total over galaxy mass within $150$ kpc apertures on the subcluster's galaxy peak and the main cluster's mass peak, $(M/L)_{\mathrm{sub}}/(M/L)_{\mathrm{main}}$, divided by the same ratio at $t = 0$.
\end{itemize}
Randall et al.\ measure the mass-to-light ratio itself; the division by its value at $t = 0$ removes the sampling offset of the initial conditions. Only $94$ to $100$ (subcluster) and $81$ (main cluster) galaxy particles fall in the two apertures, among about $4900$ and $3700$ particles in all, so at $t = 0$ the ratio is $1.086$ in reading (C) and $1.146$ in CDM rather than $1$ (\file{ml\_baseline.py}, from the fixed-seed initial conditions). The ratio at either epoch carries a Poisson error of about $15$ percent from those counts; the change, a ratio of two such, carries at least that and up to about $21$ percent, about twice to two and a half times the observational error ($0.07/0.84 = 8$ percent).

**setting  (Measurements).** \textbf{Halo shapes.} The assembled cluster's centre is found by shrinking spheres on all mass. Its three-dimensional axis ratios come from the iterative reduced inertia tensor, $I_{ab} = \sum m\,x_{a}x_{b}/r_{\mathrm{ell}}^{2}$ over the ellipsoid of the current shape, inside $300$ and $1000$ kpc. The projected ellipticity $1 - b/a$ is the same construction in two dimensions inside a projected $500$ kpc, averaged over the three coordinate projections; this is the quantity of Fact \claimref{simulations.imported-cluster-shapes}.

## Results: mergers and halos



**setting  (The merger).** the table accompanying \claimref{simulations.averaged-pair-operator} gives every merger run; a figure of the original plots the three measurements that the observation constrains for the five main runs.

\centering  
\begin{tabular}{@{}lrrrrrr@{}}
\toprule
Run & sep.\ (kpc) & max sep.\ (kpc) & contrast & offset (kpc) & own / CDM & $M/L$ change \\
\midrule
\texttt{cdm} & 742 & 1083 & 7.50 & $-5$ & 1.00 & 0.87 \\
\texttt{cdm\_lo} & 723 & 1090 & 7.13 & $-45$ & 1.00 & 0.91 \\
\texttt{rule\_random} & 584 & 625 & 0.95 & $+15$ & 0.10 & dissolved \\
\texttt{rule\_random\_lo} & 514 & 526 & 0.90 & $-5$ & 0.08 & dissolved \\
\texttt{rule\_perp} & 376 & 501 & 0.81 & $+185$ & 0.12 & dissolved \\
\texttt{rule\_par} & 720 & 829 & 3.24 & $-15$ & 0.48 & 0.68 \\
\texttt{mirror\_only} & 729 & 835 & 4.74 & $-5$ & 0.57 & 0.82 \\
\texttt{mixed\_random} & 460 & 579 & 1.11 & $-15$ & 0.27 & dissolved \\
\texttt{mixed\_perp} & 542 & 600 & 1.26 & $-5$ & 0.16 & dissolved \\
\texttt{mixednm\_random} & 730 & 792 & 2.69 & $-25$ & 0.44 & 0.61 \\
\texttt{mixednm\_perp} & 711 & 759 & 1.83 & $-95$ & 0.30 & 0.67 \\
\texttt{rule1\_random} & 486 & 493 & 1.47 & $-25$ & 0.23 & dissolved \\
\texttt{rule1nm\_random} & 723 & 846 & 3.78 & $+25$ & 0.55 & 1.18 \\
\midrule
observed & 720 & & separate peak & 42\rlap{$^{\dagger}$} & & $0.84 \pm 0.07$\rlap{$^{*}$} \\
\bottomrule
\end{tabular}

\emph{The Bullet-like merger (the section ``Measurements''): separation at the Bullet-like moment, maximum separation after closest approach up to $t = 1.3$ (the CDM run was followed to $1.5$; the runs at $1083$ to $1090$ and $759$ to $846$ kpc are still separating at $1.3$), lensing contrast, signed mass-peak offset from the galaxies (positive: the mass peak leads; below $10$ kpc is within one grid cell), the subcluster's own mass within $150$ kpc of its galaxies relative to CDM's, and the mass-to-light change since $t = 0$ (sampling error $15$ to $21$ percent). The own-mass column has no observed counterpart: Randall et al.'s $23$ percent bound on mass loss is inferred from the mass-to-light ratio, not from the mass inside a fixed aperture. Where the contrast is near or below $1$ there is no separate subcluster peak, and the offset (\texttt{rule\_perp}'s $+185$) locates the nearest mass maximum, not a subcluster's. ``Dissolved'': the subcluster no longer has a galaxy concentration, so the ratio does not measure what the observation measures. Each run is one realisation. Observed values from Fact \claimref{simulations.imported-bullet-cluster}; $^{\dagger}$the subcluster's lensing peak, within $1\sigma$ of its galaxy centroid, which is known to $22$ kpc; $^{*}$the observed value is the ratio itself, not a change.}



**Conjecture 20 (The merger).** In reading (W) the subcluster's sheet fluid and mirror gas are held back with its gas, $71$ percent of its mass ($56$ percent in the mixed count). Its potential collapses, its galaxies spread, and by the end of the runs it has not separated beyond $500$ to $630$ kpc. With random normals, or with the normals along the line of sight so that the merger axis lies in the sheets, it has no separate lensing peak (contrast $0.81$ to $0.95$). With every normal along this merger's axis (\texttt{rule\_par}) the fluid slides through along the axis; the subcluster then has a lensing peak (contrast $3.24$, $15$ kpc from its galaxies) but keeps half its mass. The mixed count fails in the same way. With the mirror collisionless from the start, so that only the sheet fluid collides, the subcluster keeps a weaker peak (contrast $2.69$ in the mixed count, $3.78$ with one three-dimensional tower colliding) and $0.44$ to $0.55$ of CDM's own mass: with a quarter to a third of the dark matter as sheet fluid, the sheet fluid alone costs about half the subcluster's central mass.

In reading (C) the subcluster reaches the observed separation with its mass peak on its galaxies and its gas $355$ kpc behind. Its own mass inside $150$ kpc of its galaxies is $0.57$ of CDM's, a deficit larger than the $23$ percent bound, because its halo puffs more than it strips. Its galaxies spread with it: the galaxy mass within $150$ kpc of the galaxy peak is $0.83$ of its start, where CDM's is compressed to $1.31$. Mass and light leave the aperture together, so the ratio inside it is kept while the mass inside it falls. Per unit of its collisionless content, the subcluster's collisionless matter inside the aperture is $0.683$ as concentrated as CDM's, and $0.683 \times 0.814$ (the collisionless share of the dark matter in reading (C), $1 - 0.186$) gives $0.556$, its collisionless matter against CDM's dark matter in the aperture; with stars and settled mirror matter the own mass is $0.57$. The mass-to-light ratio, from which the bound is derived, is therefore the test: its change is $0.82$ (the ratio itself $0.89$) against the observed $0.84 \pm 0.07$; CDM's is $0.87$ (ratio $1.00$). With a sampling error of $15$ to $21$ percent this measure does not separate reading (C) from CDM; the lensing peak and the gas offset separate both from reading (W). Its contrast, $4.7$ against CDM's $7.5$, is lower, and it has lost its mirror gas and part of its outer halo (a figure of the original). Each composition is one realisation of one geometry. Computed; observation level.

**setting  (The merger).** The half-resolution runs agree with the full ones (contrast $0.90$ against $0.95$ for \texttt{rule\_random}, $7.13$ against $7.50$ for CDM). a figure of the original follows the subcluster's own mass through the merger in the three main compositions.

**setting  (Cluster assembly).** \centering  
\begin{tabular}{@{}lccccc@{}}
\toprule
Composition & seed 11 & seed 23 & mean & ratio to CDM & seed ratios \\
\midrule
CDM & 0.24 & 0.39 & 0.31 & 1.00 & \\
unit-ball, (W) & 0.13 & 0.14 & 0.13 & 0.43 & 0.56, 0.35 \\
unit-ball, (C) & 0.15 & 0.33 & 0.24 & 0.77 & 0.63, 0.85 \\
mixed count, (W) & 0.09 & 0.22 & 0.15 & 0.49 & 0.37, 0.57 \\
mixed count, mirror settled & 0.20 & 0.26 & 0.23 & 0.75 & 0.86, 0.68 \\
one 3D tower fluid, mirror settled & 0.20 & 0.29 & 0.24 & 0.78 & 0.84, 0.74 \\
\midrule
observed & & & $0.46 \pm 0.04$ & & Fact \claimref{simulations.imported-cluster-shapes} \\
\bottomrule
\end{tabular}

\emph{Projected ellipticity $1 - b/a$ inside $500$ kpc of the assembled cluster, mean of three projections, for the two seeds; the last column is each seed's ratio to the CDM run of the same seed. CDM's own two seeds differ by $0.15$.}



**Conjecture 21 (Halo shapes).** Isolated assembly from eight progenitors makes rounder halos than infall along filaments, so the measure is the ratio to the CDM run (the table accompanying \claimref{simulations.merger}), and with two seeds the criterion is whether both seeds of a composition lie below both of CDM's. In reading (W) they do: the ellipticity is $0.43$ of CDM's (seed ratios $0.56$ and $0.35$), and the sheet fluid, supported by its pressure, is cored (its density is flat within the noise inside about $75$ kpc) and rounder than the collisionless dark matter (inside $300$ kpc, $c/a$ of $0.78$ and $0.85$ against $0.59$ and $0.44$ in the two seeds). It is also less concentrated: $38$ percent of the mass within $300$ kpc, near its measured share of $0.41$ within $r_{200}$, but only $10$ to $12$ percent inside $50$ kpc, where settled mirror matter is $39$ to $43$ percent. In reading (C) the ratio is $0.77$ ($0.63$ and $0.85$), and the second seed overlaps CDM's range: rounder, not excluded. Inside $300$ kpc in seed $11$ its $c/a$ matches CDM's ($0.62$ against $0.64$) and its $b/a$ is larger ($0.93$ against $0.71$), so the halo is closer to oblate symmetry than CDM's. In reading (C), $39$ and $29$ percent of the mass inside $50$ kpc (seeds $11$ and $23$) is settled mirror matter: the over-cooling of a dissipative gas simulated without feedback (Premise S3), which also makes the inner profiles unreliable. The compositions with the mirror settled from the start sit at $0.75$ to $0.78$ of CDM; at equal sheet fluid, the mixed count with its mirror gas gives $0.49$ and without it $0.75$, and the mirror gas without sheet fluid, reading (C), gives $0.77$: the mirror gas and the sheet fluid together round the halo more than either alone. Computed; observation level.

**setting  (Cluster assembly).** A halo-model estimate of the small-scale matter power spectrum, with the simulated change of profile applied at every mass (\file{pk.py}, output deposited), gives $P(k)/P_{\mathrm{CDM}} = 1.01$ to $1.34$ at $k$ of about $3$ and $10\ h\,\mathrm{Mpc^{-1}}$ for the unit-ball, mixed and reading (C) halos. The seed-to-seed spread is as large as the effect, so the test is not used.

## The films



**setting  (The films).** Both films are rendered from simulation snapshots by \file{render\_lib.py} \cite{ButlerSuppT14b}. Each layer is a projected map along the line of sight on a grid of $300$ cells across the field, smoothed by a Gaussian of $18$ kpc (gas) or $25$ kpc (total mass), placed on a log scale, and added in its own colour onto a dark ground: galaxies as individual points, our gas weighted by $m\rho\sqrt{u}$ (a bremsstrahlung proxy for the X-ray map), mirror gas, and total projected mass as contours (what lensing measures). In Film 1 the sheet fluid is drawn as solid green contours rather than a fill, since a green fill screen-blended over the pink gas reads as white. The colour scales are fixed from one snapshot and shared by every panel, so brightness can be compared across panels.

The films use the same initial conditions as the runs of the table accompanying \claimref{simulations.averaged-pair-operator}, re-run with snapshots every $0.01$ time units ($9.8$ Myr). They reproduce the Bullet-moment measurements of the table accompanying \claimref{simulations.averaged-pair-operator} within run-to-run noise (contrast $4.48$ against $4.74$ for (C), $0.92$ against $0.95$ for (W), $7.27$ against $7.50$ for CDM; mass-to-light change $0.79$ against $0.82$ for (C)), the differences coming from the shifted time steps.

**setting  (The films).** \textbf{Film 1: the merger, three ways.} \file{merger\_three\_ways.mp4} ($16$ s, $1920 \times 1080$), titled for a general audience ``Galaxy clusters in collision: testing three ideas about dark matter'', shows CDM, reading (W) with random normals and reading (C) side by side from approach to $1.27$ Gyr, labelled ``Standard cold dark matter: none of it collides'', ``Unit-ball rule: mirror and 3D-tower matter collide'' and ``Unit-ball rule: only mirror matter collides''.

The subtitle states that collisions are within a tower's own matter and that different towers interact only through gravity (Fact \claimref{dark-matter.superselected-hence-dark-exactly-stable}). Collisionless matter appears only in the total-mass contours, so the CDM panel has no orange or green layer and the right-hand panel no green one; the film's legend calls the sheet fluid ``colliding 3D-tower matter''. A panel beside the chart explains the Bullet-like separation.

Below the maps a chart, with its own legend, follows the subcluster's own mass (a figure of the original), with a cursor at the current time. The film runs without pauses; reading (C)'s Bullet-like separation, $1.17$ Gyr, falls at $15$ s. The camera is centred between the two clusters of the CDM run and its width follows their separation; positions are interpolated linearly between snapshots at three frames per interval.

**setting  (The films).** \textbf{Film 2: the Bullet-like moment.} \file{bullet\_moment.mp4} ($20$ s, $1600 \times 900$) uses the snapshot of reading (C)'s run in the table accompanying \claimref{simulations.averaged-pair-operator} at $t = 1.20$ ($1.17$ Gyr). It adds the layers one at a time (galaxies, our gas, mirror gas, total mass) with a sentence on each, then marks the subcluster's galaxy peak, its mass peak, its gas peak and the main cluster's mass peak, and lists the simulated values beside the observed ones of Fact \claimref{simulations.imported-bullet-cluster}: separation $729$ kpc against $720$; mass peak $5$ kpc from the galaxies against about $42$ kpc, within $1\sigma$; gas $355$ kpc behind against an $8\sigma$ offset; mass-to-light $0.82 \pm 0.17$ against $0.84 \pm 0.07$ (the film shows the change since $t = 0$ with its $21$ percent sampling error, the section ``Measurements''); contrast $4.7$, with CDM's $7.5$ for reference.

## The mirror in the Galaxy



**setting  (The mirror in the Galaxy).** The mirror's share is the same in both readings, so the merger cannot separate them. Its standing test in T14 is the Galaxy \cite[\S 8, refutation item 6]{ButlerT14}: dissipative mirror matter, $18.6$ percent of the dark matter, must not settle into structures the Milky Way's dynamics excludes.

**setting  (Composition and recombination).** With $\xi$ in T14's interval the mirror's weak interactions freeze out at $T' = 274$, $117$ and $47$ MeV for $\xi = 2.8 \times 10^{-4}$, $10^{-3}$ and $4 \times 10^{-3}$ (rate normalised to our freeze-out at $0.80$ MeV, expansion set by our $g_{*} = 106.75$). T14 gives $0.43$ to $0.45$ GeV at the floor; both lie above the hadronisation temperature, so the helium fraction is the same. Near the floor the neutron-to-proton ratio is set at hadronisation, so $Y' = 0.996$, $0.995$ and $0.986$: helium, with $0.4$ to $1.4$ percent residual hydrogen. Saha recombination of helium at $\eta'$, with $\xi$ raised by T14's entropy factor of about $2.6$ after burning (and by its burning reheat, a further factor of about $3.1$, at the floor), puts it at a visible temperature of $0.08$ to $1.6$ keV, redshift $3 \times 10^{5}$ to $7 \times 10^{6}$, overlapping T14's $0.1$ to $0.8$ keV \cite[Prop.~4.6]{ButlerT14}; the ends differ by the recombination criterion and the reheating bracket, which does not affect what follows. The extra radiation is $\Delta N_{\mathrm{eff}} \le 10^{-7}$. After recombination the mirror gas has a Jeans mass of $2 \times 10^{-6}$ to $2 \times 10^{-4}\ \Msun$ at $z = 100$: for the cosmic microwave background and large-scale structure it is cold dark matter, and the Galaxy is where it can be tested.

**setting  (Cooling).** Collisional-ionisation-equilibrium cooling for hydrogen and helium uses the rates of Katz, Weinberg and Hernquist \cite{KWH1996}, plus one term they omit, which matters only without hydrogen: collisional excitation of neutral helium from its ground state, with an effective collision strength of $0.15$; varied by a factor of three either way it changes the pure-helium curve only between about $2 \times 10^{4}$ and $10^{5}$ K and leaves the floor and the cooling times at the virial temperatures used unchanged. The metal-free curve reproduces Sutherland and Dopita's \cite{SutherlandDopita1993} ($\log\Lambda_{N} = -22.26$, $-23.25$, $-23.01$ at $10^{5}$, $10^{6}$, $10^{7}$ K, normalised to $n_{H}^{2}$). Metals add the Tozzi-Norman fit for $0.3\,Z_{\odot}$ \cite{TozziNorman2001}, converted from their $n_{e}n_{i}$ normalisation to $n_{H}^{2}$ by the factor $0.704/0.578$ that \file{cooling.py} uses ($0.704 = (X + Y/2)(X + Y/6)$, which counts the helium ions as $Y/6$; $0.578 = X^{2}$ for $X = 0.76$; for a fully ionised plasma of that $X$, $n_{e}n_{i} = 0.722\,(\rho/m_{p})^{2}$, which would change the metal term by $3$ percent and no conclusion), scaled linearly in $Z$ and, for a helium plasma, by electrons per gram. At equal density and equal virial velocity:
\begin{itemize}
\item metal-free helium cools $12$ to $94$ times more slowly than our metal-enriched gas at $V = 100$ to $200$ km/s, the Milky Way's hot halo;
\item $4$ to $6$ times more slowly if the mirror has enriched itself to the same metallicity;
\item as fast as ours in small early halos ($V \approx 30$ km/s), where He$^{+}$ line cooling dominates.
\end{itemize}
The residual hydrogen holds a cooling floor near $10^{4}$ K.

**setting  (The model).** One Milky Way halo is shared by both sectors: the same growth, potential and spin. Its growth follows the Fakhouri-Ma-Boylan-Kolchin rate \cite{Fakhouri2010},
\[
\frac{dM}{dt} = A\Bigl(\frac{M}{10^{12}\Msun}\Bigr)^{1.1}(1 + bz)\sqrt{\Omega_{m}(1+z)^{3} + \Omega_{\Lambda}},
\]
with $(A, b) = (46.1\ \Msun/\mathrm{yr}, 1.11)$ (mean) or $(25.3, 1.65)$ (median). Each sector accretes its baryon share $f_{b}\,dM$ ($f_{b} = \Omega_{b}/\Omega_{m} = 0.1565$) into a hot halo, an isothermal sphere $\rho_{g}(r) = m_{\mathrm{hot}}/(4\pi Rr^{2})$ at the virial temperature $T = \mu m_{p}V^{2}/2k$ of its own composition. Following Croton et al.\ \cite{Croton2006}, with their parameter values, and with $R$ and $V$ the halo's virial radius and circular velocity, $m_{\mathrm{hot}}$ and $m_{\mathrm{cold}}$ the hot and cold gas masses, $r_{\mathrm{cool}}$ the radius at which the cooling time equals the reference time, and $\lambda$ the spin parameter:
\begin{align*}
t_{\mathrm{cool}}(r_{\mathrm{cool}}) &= t_{\mathrm{dyn}} = R/V \quad (\text{or the cosmic time}),\\
\dot m_{\mathrm{cool}} &= \tfrac{1}{2}m_{\mathrm{hot}}\frac{r_{\mathrm{cool}}}{R}\frac{V}{R} \quad (\text{all hot gas per } t_{\mathrm{dyn}} \text{ if } r_{\mathrm{cool}} > R),\\
\dot m_{*} &= \alpha\,\frac{m_{\mathrm{cold}} - m_{\mathrm{crit}}}{t_{\mathrm{disk}}}, \qquad
m_{\mathrm{crit}} = 3.8 \times 10^{9}\Msun\,\frac{V}{200\ \mathrm{km/s}}\,\frac{3R_{d}}{10\ \kpc},\\
\Delta m_{\mathrm{reheat}} &= \epsilon_{\mathrm{disk}}F\,\Delta m_{*}, \qquad
\Delta E = \tfrac{1}{2}\epsilon_{\mathrm{halo}}F\,\Delta m_{*}V_{\mathrm{SN}}^{2},\\
\Delta m_{\mathrm{eject}} &= \frac{\Delta E - \tfrac{1}{2}\Delta m_{\mathrm{reheat}}V^{2}}{\tfrac{1}{2}V^{2}}, \qquad
\dot m_{\mathrm{return}} = \gamma_{\mathrm{ej}}\,m_{\mathrm{ej}}/t_{\mathrm{dyn}},
\end{align*}
with $\alpha = 0.07$, $\epsilon_{\mathrm{disk}} = 3.5$, $\epsilon_{\mathrm{halo}} = 0.35$, $V_{\mathrm{SN}} = 630$ km/s, $\gamma_{\mathrm{ej}} = 0.5$, recycled fraction $0.43$, $R_{d} = \lambda R/\sqrt{2}$ and $t_{\mathrm{disk}} = 3R_{d}/V$. Metals are followed in each sector from a metal-free start: a yield $y = 0.03$ per unit of stars formed enters the cold gas and is carried by every flow, and each hot halo cools at its own metallicity. The feedback factor $F$ multiplies the supernova energy and mass loading per unit stellar mass; for our sector it is a calibrated number $F_{\mathrm{cal}}$, and the mirror's is $F$ times that.

**setting  (The model).** \textbf{Calibration and normalisation.} In each set-up our sector's $F_{\mathrm{cal}}$ is tuned so that its settled mass, stars plus cold gas, is the observed $6.0 \times 10^{10}\ \Msun$. The mirror, at $\Omega_{b'} = 0.995\,\Omega_{b}$, then runs in the same halo with feedback $F\,F_{\mathrm{cal}}$ and with yield $yF$ (its extra feedback comes from extra supernovae, which also make metals; the consistent choice) or, for comparison, $y$. Its surface density at the Sun is normalised to ours, either in total,
\[
\Sigma'_{x} = 47.1\ \Msun\,\mathrm{pc^{-2}}\times\frac{m'_{x}}{6.0 \times 10^{10}\ \Msun},
\]
or with gas and stars scaled separately to our observed $13.7$ and $33.4$ (component normalisation). The mass the mirror puts in the bulge volume is taken as a quarter of its settled mass, the fraction of ours the bulge volume holds. There are $24$ set-ups: $M_{200} = 1.0$, $1.2$ and $1.5 \times 10^{12}\ \Msun$; mean or median growth; $t_{\mathrm{dyn}}$ or cosmic time as cooling reference; and a star-formation-threshold disk of $5.6$ kpc ($\lambda = 0.035$) or $2.6$ kpc ($\lambda = 0.0163$, the Milky Way's). Points with $F\,F_{\mathrm{cal}}$ above $12$ are dropped as not converged.

**setting  (How much feedback a helium mirror has).** A pure-helium star is a bare helium core. Helium stars collapse to iron cores from about $2.5\ \Msun$ \cite{Woosley2019}, form black holes above final masses of about $10$ to $12\ \Msun$ \cite{Woosley2019, Ertl2020}, and explode by pair instability from $64$ to $133\ \Msun$ \cite{HegerWoosley2002}. Taking $10^{50}$ erg from $2.5$ to $3\ \Msun$, $10^{51}$ erg from $3\ \Msun$ to the black-hole cut, none above it to $64\ \Msun$, and pair-instability energies rising from $10^{51}$ to $10^{53}$ erg, the energy per unit mass formed relative to ours ($1.08 \times 10^{49}$ erg/$\Msun$ for a Chabrier IMF \cite{Chabrier2003}, one core collapse per $93\ \Msun$) is given in the table accompanying \claimref{simulations.halo-shapes}.
\centering \begin{tabular}{@{}lcccccc@{}}
\toprule
IMF shifted up in mass by & 1 & 3 & 5 & 7 & 10 & 30\\
\midrule
$F$, black holes above $12\ \Msun$ & 3.6 & 5.7 & 6.3 & 6.4 & 6.2 & 4.7\\
$F$, black holes above $30\ \Msun$ & 4.1 & 6.4 & 7.1 & 7.3 & 7.2 & 5.7\\
\bottomrule
\end{tabular}

\emph{The helium-star feedback factor $F$: supernova energy per unit stellar mass formed of a pure-helium population relative to ours, by the black-hole cut (rows) and the factor by which the IMF is shifted up in mass (columns); \file{imf\_table.py}.}

No shifted IMF exceeds $F \approx 7.3$. Our IMF's shape gives $3.6$ to $4.1$.



**Conjecture 22 (The mirror in the Galaxy).** Over the $24$ set-ups:
\begin{enumerate}
\item[(i)] The proton-only branch, at the feedback a hydrogen population has ($F = 1$), puts $47$ to $56\ \Msun\,\mathrm{pc^{-2}}$ of gas and stars at the Sun and $(15$ to $18) \times 10^{9}\ \Msun$ in the bulge volume. It fails every combination of bounds and normalisations.
\item[(ii)] The helium branch without star formation settles $48$ to $117\ \Msun\,\mathrm{pc^{-2}}$. It fails.
\item[(iii)] The helium branch with stars at $F = 1$ gives $23$ to $42\ \Msun\,\mathrm{pc^{-2}}$ and $(7$ to $13) \times 10^{9}\ \Msun$. It fails. At equal feedback it settles $49$ to $85$ percent as much as our sector, because it cools more slowly.
\item[(iv)] The helium branch at the helium-star feedback, $F = 3.6$ to $7.3$ with yield $yF$, gives $5.6$ to $20\ \Msun\,\mathrm{pc^{-2}}$ of gas and stars, $1$ to $8$ of gas, and $(1.8$ to $6.2) \times 10^{9}\ \Msun$ in the bulge volume; with yield $y$, $4.2$ to $14$, $1$ to $7$ and $(1.3$ to $4.2) \times 10^{9}\ \Msun$. Whether it passes depends on choices the data and the model do not fix. The first is how much of the bulge's dark mass, $3.1 \times 10^{9}\ \Msun$ (Fact \claimref{simulations.imported-milky-ways-mass-budget}), may be mirror: $0.6 \times 10^{9}$ if it is shared in proportion to the composition, $3.1 \times 10^{9}$ if the collisionless towers contribute nothing there, up to $8.3 \times 10^{9}$ if a mirror bar can hide within the stellar mass-to-light uncertainty. Every floor computed here exceeds $0.6 \times 10^{9}$, so on the proportional reading the bulge excludes the helium branch at every $F$ and yield; it survives in the bulge only on the other two, which require over twice the proportional share ($1.33/0.6 = 2.2$ times with yield $y$, $1.78/0.6 = 3.0$ with $yF$): held as dark mass, over $43$ percent of the bulge's dark mass with yield $y$ and $57$ percent with $yF$; otherwise hidden within the stellar mass-to-light uncertainty. The others are the normalisation of the mirror's gas, the bounds at the Sun, the yield and the IMF.

With yield $yF$, the numbers of converged set-ups that pass the lenient bounds at the Sun (thin gas below $5.59$, gas and stars below $15\ \Msun\,\mathrm{pc^{-2}}$) and each reading of the bulge room are as follows, given as ranges over the two black-hole cuts and the two disk scales (\file{verdict\_output.txt} has every count):
\begin{center}\small
\begin{tabular}{llccc}
\toprule
IMF shape & normalisation & room $8.3$ & room $3.1$ & room $0.6$ \\
\midrule
ours & total & $8$ to $9$ of $11$ or $12$ & $0$ to $4$ & $0$ \\
ours & component & $0$ to $2$ & $0$ to $1$ & $0$ \\
best shift & total & all ($9$ or $10$) & $5$ to $8$ & $0$ \\
best shift & component & $2$ to $8$ & $0$ to $7$ & $0$ \\
\bottomrule
\end{tabular}
\end{center}
\item[(v)] With yield $yF$ even the most favourable case leaves at least $5.6\ \Msun\,\mathrm{pc^{-2}}$ at the Sun and $1.78 \times 10^{9}\ \Msun$ in the bulge volume; with yield $y$, at least $4.2$ and $1.33 \times 10^{9}\ \Msun$.
\end{enumerate}
Computed; observation level.

**setting  (The result).** So with the consistent yield the Galaxy test would be decided by either of two measurements not yet made: a $2\sigma$ limit below $5\ \Msun\,\mathrm{pc^{-2}}$ on extra disk-like mass at the Sun with scale height $100$ to $500$ pc (the room is $4.6 \pm 5$, the dynamical stellar surface density less the counted one, Fact \claimref{simulations.imported-milky-ways-mass-budget}), or a limit below $1.7 \times 10^{9}\ \Msun$ on disk-like dark mass in the bulge volume, which would bound the mirror's mass there directly, whatever reading of the room is taken. Either excludes the helium branch under every choice tried with yield $yF$; with the yield held at ours the limits would need to reach $4.2\ \Msun\,\mathrm{pc^{-2}}$ and $1.3 \times 10^{9}\ \Msun$. The thin-gas bound is not used to decide, because the mirror's gas at high $F$ sits at the star-formation threshold of the model, which is its least certain part.

Roux and Cline find $\Omega_{b'} \lesssim 0.8\,\Omega_{b}$ at low mirror temperature \cite{RouxCline2020}. Their analysis includes a helium mirror with $\eta' = \eta\,\beta/x^{3}$, down to $x = T'/T = 10^{-3}$, which covers T14's hot end; what it does not include is the floor of T14's interval and the helium-star supernova factor.

## The total and the radiation



**setting  (The total and the radiation).** The two remaining charts are T14's results, shown here for completeness. a figure of the original is the total against the thickness: the observed value is met at $c = 1$ and $c = \pi/2$, where the thickness was set, and the floor $5.255$, the family's one prediction independent of $c$, sits $1.7\sigma$ below Planck's value with lensing \cite{Planck2018}. A measured value clearly below $5.255$ would exclude the whole family. a figure of the original is the radiation: with the dark sectors heated only through gravity the extra radiation is below $10^{-7}$ \cite[Props.~6.2 and 6.3]{ButlerT14}, so $N_{\mathrm{eff}}$ stays at the Standard Model's $3.044$, against the measured $2.99 \pm 0.17$.

## What the tests decide, and what they cost



**setting  (What the tests decide, and what they cost).** \centering \begin{tabular}{@{}>{ \arraybackslash}p{0.27\textwidth}>{ \arraybackslash}p{0.2\textwidth}>{ \arraybackslash}p{0.2\textwidth}>{ \arraybackslash}p{0.23\textwidth}@{}}
\toprule
Test & (W) as written & (C) odd towers collisionless & Observed \\
\midrule
$\Omega_{\mathrm{dark}}/\Omega_{b}$ & $5.364$, fitted & $5.364$, fitted & $5.364 \pm 0.065$ \\
Colliding share (the section ``Self-interaction within a sheet'') & $68\%$: fails & $19\%$ of the dark matter by composition ($29\%$ of the subcluster's mass with its gas); the $M/L$ change below is the measured check & $\le 23\%$ loss \\
$\sigma/m$ of 3D matter & $10^{8}$ to $10^{13}$: fails & $\approx 0$ by Premise C & $< 0.47$ to $1.25\ \cmg$ ($0.7$ from $M/L$) \\
Bullet: separate lensing peak & $0.8$ to $1.0$: fails ($3.2$, half the mass, with normals along the merger axis) & $4.7$: passes, puffier & separate peak \\
Bullet: $M/L$, sub over main & dissolved or $0.68$ (change) & $0.82$ change, $0.89$ ratio: consistent, as is CDM (sampling error $15$ to $21$ percent) & $0.84 \pm 0.07$ \\
Halo ellipticity, ratio to CDM & $0.43$ (seeds $0.56$, $0.35$): fails & $0.77$ ($0.63$, $0.85$): rounder & CDM-like \\
Mirror in the Galaxy & same as (C) & proton-only excluded; helium branch open at the Sun ($2\sigma$ room) under some normalisations, in the bulge only if the bulge holds over twice the mirror's proportional share of its dark mass & room $4.6 \pm 5\ \Msun\,\mathrm{pc^{-2}}$ (Sun); $3.1 \times 10^{9}\ \Msun$ dark (bulge) \\
$N_{\mathrm{eff}}$ & $3.044$ & $3.044$ & $2.99 \pm 0.17$ \\
\bottomrule
\end{tabular}

\emph{The tests at a glance.}

**setting  (What the tests decide, and what they cost).** \textbf{What the tests decide.} Read as T14 writes it, the composition fails the merger and the halo shapes, and it fails them because of the three-dimensional towers' self-interaction, not because of the amounts. Read with the odd towers collisionless, the same amounts keep a lensing peak on the subcluster's galaxies with its gas behind and a mass-to-light change consistent with the observed ratio (as CDM's is; the measure does not discriminate), and come within a quarter of CDM on halo shapes. The remaining exposure is the mirror in the Galaxy, the same in both readings: its helium branch is open at the Sun, at the $2\sigma$ room, under some normalisations of the mirror's gas and, in the bulge, only if the bulge holds over twice the mirror's proportional share of its dark mass.

**setting  (What the tests decide, and what they cost).** \textbf{Statements of T14 the tests bear on.} T14 records the outcome in its Section 7.7 and at each place cited below \cite[Fact~7.32]{ButlerT14}.
\begin{enumerate}
\item At composite strength the three-dimensional towers' self-interaction is $10^{8}$ to $10^{13}\ \cmg$ (Proposition \claimref{simulations.effective-cross-section-sheet-matter}), far above the cluster bounds \cite[Prop.~6.2]{ButlerT14}.
\item ``A halo built from collisionless sheets is a cold-dark-matter halo'' \cite[Rem.~7.30]{ButlerT14} needs the sheet matter collisionless; as a fluid it is cored, rounder and less concentrated than collisionless matter (Observation \claimref{simulations.halo-shapes}).
\item The self-interacting fraction, counted as all colliding dark matter, is $68$ percent in reading (W) and $19$ percent in reading (C); T14's Proposition 7.15(v) counts the three-dimensional towers alone (about half); for the merger bound its Section 7.7 adds the mirror, as here \cite[Prop.~7.15(v), \S7.7]{ButlerT14}. The Bullet bound on mass loss is about $23$ percent \cite{Randall2008}, inferred from the mass-to-light ratio.
\item The mirror analysis T14 cites \cite[\S 8, refutation item 6]{ButlerT14} rescales $\eta$ and includes a helium mirror down to $T'/T = 10^{-3}$ \cite{RouxCline2020}; it covers the hot end of T14's interval, not its floor.
\item For the helium branch with stars the excess over the Galaxy's room at the Sun is a factor of $1.5$ to $2.8$ over the $2\sigma$ room of $15\ \Msun\,\mathrm{pc^{-2}}$ at equal feedback, and at the helium-star feedback it falls within the $2\sigma$ room at the Sun in most set-ups in total normalisation (all of them at the best-shifted IMF) and persists in the bulge unless the bulge holds over twice the mirror's proportional share of its dark mass (Observation \claimref{simulations.mirror-galaxy}). The order-of-magnitude excess holds for the proton-only branch and for a mirror that forms no stars \cite[\S 8, refutation item 6]{ButlerT14}.
\item The current bounds on the settled phase are the thin-disk bound of Widmark et al.\ \cite{Widmark2021} and the microlensing bound of Mr\'oz et al.\ (compact objects at most $1$ percent of the halo from $1.8 \times 10^{-4}$ to $6.3\ \Msun$ and $10$ percent up to $860\ \Msun$ \cite{Mroz2024}), which T14's refutation item 6 uses. The thin-disk bound, about $5\ \Msun\,\mathrm{pc^{-2}}$ at $95$ percent, holds for scale heights of $50$ pc or less; it does not reach the $5\ \Msun\,\mathrm{pc^{-2}}$ at $100$ to $500$ pc that would decide the helium branch, and the bulge models \cite{Portail2017} do not separate a disk-like part of the bulge's dark mass, so the Galaxy test is not yet decidable.
\end{enumerate}

**setting  (What the tests decide, and what they cost).** \textbf{Costs.}
\begin{enumerate}
\item[(K1)] Premise C is not derived and is not T14's reading. It is a statement about the three-dimensional towers' couplings, which the series does not fix (Remark \claimref{note.simulations.what-premise-c-needs}).
\item[(K2)] The model of the sheet fluid (Premise S2) takes each orientation's sheets as one family shared by both clusters, so that the clusters' sheet matter collides, and averages the force between differently oriented sheets the relation displayed with \claimref{simulations.confinement-scale-does-not-matter}; T14 implies the first \cite[Lem.~6.1, Prem.~7.4]{ButlerT14} but does not specify the second. Of the parallel-sheet runs, which do not use the average, the one with the merger axis in the sheets fails in the same way and the one with the normals along the axis keeps a lensing peak at half the mass.
\item[(K3)] The mirror in the clusters cools by bremsstrahlung alone, without line cooling, star formation or feedback (Premise S3). Its settled phase over-concentrates in halo centres, and the reading-(C) subcluster loses more of its mirror gas than a model with feedback would.
\item[(K4)] The simulations are idealised: one merger geometry run once per composition, $80{,}000$ particles per merger and $32{,}000$ per assembled cluster, $15$ kpc softening, isolated assembly, two seeds per halo composition. They compare compositions; their absolute numbers are not predictions.
\item[(K5)] The Galaxy model is semi-analytic with one smooth growth history per halo, prescriptions calibrated on our sector, and a star-formation threshold that sets the mirror's gas floor. The room for extra disk-like mass at the Sun is the difference of two measurements, not a published bound.
\end{enumerate}

## Position in the series



**setting  (Position in the series).** This paper is T14b of the series, a companion to the dark-matter paper T14 \cite{ButlerT14}. It is downstream of T14's Proposition 4.1 (superselection), Theorem 4.3 and Proposition 4.6 (the mirror), Proposition 6.2 (the radiation audit and its self-interaction statement) and Section 7 (the unit-ball rule, its premises R1 to R3, the thickness family and the moving sheets), and it tests the composition T14's Section 7 fixes against the record. Remark \claimref{note.simulations.what-premise-c-needs} refers to the Standard-Model paper T12 \cite{ButlerT12} for the gauge charges of the four-dimensional minimal massive composite. It proves nothing about the series' algebra and changes no derived result of T14; it says which of T14's physical statements the simulations and the Galaxy model support and which they do not (the section ``What the tests decide, and what they cost''). The capstone T17 \cite{ButlerT17} should carry the table accompanying \claimref{simulations.mirror-galaxy} beside T14's ledger entry, Premise C as the condition under which the rule's composition meets the cluster record, and the two measurements of the section ``The mirror in the Galaxy'' that would decide the mirror's helium branch.

## Machine verification



**setting  (Machine verification).** \textbf{The script.} \file{verify\_T14b.py} \cite{ButlerVerifyT14b} imports the series' shared library \file{GA.py} and checks the note's computational identities and derived numbers: $60$ checks, all passing, in eight parts. A few are arithmetic restatements of a quoted number rather than tests of a claim (D4, F3, R4, R7). Algebraic identities are checked in exact rational arithmetic; evaluations with physical constants, transcendental functions and integrals in double precision, with the tolerance stated beside each check.

\emph{Part A: composition.} $T(1) = (11\pi + 16)/(3\pi)$ between rational bounds; $T(\pi/2) = T(1)$; the three shares and their sum; the baryon, galaxy and gas fractions of every halo; the three colliding shares and their order against the bounds.

\emph{Part B: self-interaction.} Proposition \claimref{simulations.effective-cross-section-sheet-matter} as an exact identity; $n_{b}$ and $d_{b}$; the ratio $V_{3}/V_{2} = 4/3$ from the unit-ball volumes; the range of the table accompanying \claimref{simulations.effective-cross-section-sheet-matter}; the bound on $\lambda$; Computation \claimref{simulations.cluster-bound-two-dimensions}, with Bessel functions by their series; the five-dimensional range; the mean free path.

\emph{Part C: the code's algebra.} The kernel's normalisation, derivative and continuity, exactly; Lemma \claimref{simulations.averaged-pair-operator}(ii) in the blade engine of $\Cl(3,0)$, (iii) in exact rationals, including $P_{ij}^{2} \ne P_{ij}$ for orthogonal normals, and (i) on a rational instance with distinct normals and viscosity; the cooling update as a polynomial identity; the units; the settling threshold at $\mu = 0.6$ and its temperature for the helium plasma, from the code's $u(T)$ formula and constants; the algebra of the bremsstrahlung coefficient (the electron and ion densities and $T(u)$ for He$^{++}$) against $du/dt = -\varepsilon/\rho$, with the code's constants.

\emph{Part D: initial conditions.} The Hernquist matching and $r_{200}$, exactly; the Jeans equation for $\sigma_{r}^{2}$ at three radii; the truncation fraction; the merger geometry, exactly.

\emph{Part E: the mirror's composition.} Freeze-out temperatures, $Y'$, $\eta'$, the recombination temperature and $\Delta N_{\mathrm{eff}}$.

\emph{Part F: cooling.} The metal-free $\Lambda_{N}$ at three temperatures; the cooling-time ratios of helium to our gas; the Tozzi-Norman conversion.

\emph{Part G: supernova energy.} The continuity of the IMF; our energy per unit mass; $F$ for our IMF's shape and the best shifted IMF.

\emph{Part R: recorded outputs.} Selected simulation and model outputs, carried as constants from the run summaries, and the comparisons the text draws from them: the mass-to-light change, ratio and sampling error; the merger separations; the halo ratios, with their seed-paired values; the Galaxy floors against the decisive limits and the three readings of the bulge room. The outputs themselves are reproduced by the deposited scripts, not by this one: Part R does not read \file{outputs/}, so a change to a deposited output would not fail the script.

\emph{What the script does not check:} the simulations and the Galaxy model themselves, which the section ``Running the code'' shows how to rerun, and the imported Facts and published bounds.

## Running the code



**setting  (Running the code).** The supplement \cite{ButlerSuppT14b} holds everything needed to rerun the simulations, the Galaxy model, the films and the figures. This section says which files produce which result, how to lay them out, and how to run them. Everything in the note was run on Linux (Ubuntu 24.04) on two cores, with gcc 13.3, Python 3.11, numpy 2.4, scipy 1.17, matplotlib 3.10 and ffmpeg 6.1.

**setting  (What is needed).** \begin{itemize}
\item Python 3.10 or later with numpy, scipy and matplotlib (\file{requirements.txt}).
\item A C compiler with OpenMP, to build \file{tpsim.c}: gcc on Linux. On macOS the system compiler does not accept \texttt{-fopenmp}; gcc from Homebrew should work, but this has not been tested.
\item ffmpeg with the libx264 encoder on the command path, for the two films only.
\item On Windows, the Windows Subsystem for Linux (WSL 2) with Ubuntu. The scripts call the compiled code as \texttt{./tpsim} and write a temporary file under \texttt{/tmp}, which native Windows does not provide.
\item For the full runs, about $7$ GB of disk (the merger snapshots $6$ GB, the film frames $1$ GB) and half a day to a day on two cores (the table accompanying \claimref{simulations.mirror-galaxy}).
\end{itemize}

**setting  (Which files do what).** the table accompanying \claimref{simulations.mirror-galaxy} lists every file in the supplement's \file{code/} folder against the result it produces. Five files are libraries, imported by the others and not run on their own: \file{ics.py} (initial conditions and snapshot input and output, used by every simulation script), \file{render\_lib.py} (the films' maps), and \file{cooling.py}, \file{fastcool2.py} and \file{sam2.py} (the Galaxy model). \file{merger.py}, \file{analyze3.py} and \file{halo\_measure.py} are run and also imported. The verification script \file{verify\_T14b.py} sits at the suite's top level beside \file{GA.py}, which it imports.

\centering \begin{tabular}{@{}>{ \arraybackslash}p{0.3\textwidth}>{ \arraybackslash}p{0.36\textwidth}>{ \arraybackslash}p{0.26\textwidth}@{}}
\toprule
Result in the note & Files & Writes \\
\midrule
Self-interaction (the section ``Self-interaction within a sheet'', the table accompanying \claimref{simulations.effective-cross-section-sheet-matter}, a figure of the original) & \file{sheet\_sidm.py}, \file{scatter2d.py} & printed tables \\
The simulation code (the section ``The simulation code'') & \file{tpsim.c}; \file{ics.py}; \file{tpsim\_tests.py} for the two code tests & snapshots, test output \\
The merger (the table accompanying \claimref{simulations.averaged-pair-operator}, a figure of the original) & \file{merger.py} (runs \file{tpsim}), \file{analyze3.py}; \file{ml\_baseline.py} for the mass-to-light ratio at $t = 0$ & \file{runs/<tag>/}, \file{summary3.json}, \file{ml\_baseline.json} \\
Cluster assembly (the table accompanying \claimref{simulations.merger}, a figure of the original) & \file{halo.py} (runs \file{tpsim}), \file{halo\_measure.py}, \file{proj\_ell.py}; \file{pk.py} for the power spectrum & \file{halos/<tag>/}, \file{proj\_ell.json}, \file{pk\_output.txt}, \file{pk\_ratio.json} \\
The films and a figure of the original & \file{compact.py}, \file{remeasure.py}, \file{merger\_movie.py}, \file{bullet\_moment.py}; \file{render\_lib.py} & frames, \file{track.json}, the two films \\
Mirror composition (the section ``The mirror in the Galaxy'') & \file{mirror\_cosmo.py} & printed table \\
Galaxy model (Observation \claimref{simulations.mirror-galaxy}, a figure of the original) & \file{chem\_test2.py}, \file{verdict.py}; \file{sam2.py}, \file{cooling.py}, \file{fastcool2.py} & \file{chem2\_*.json}, pass counts \\
The factor $F$ (the section ``The mirror in the Galaxy'') & \file{imf\_table.py}; \file{imf\_feedback.py} for the energy brackets & printed tables \\
All figures & \file{make\_figs.py} & \file{T14b\_fig\_*.pdf} \\
All of the above, in order & \file{reproduce.py} & \file{work/} \\
\bottomrule
\end{tabular}

\emph{The files in \file{code/} and what each produces.}

**setting  (Laying out the files).** Open the supplement's top folder, \file{T14b\_supplement}, as the project in the IDE and keep its layout:
{ \begin{verbatim}
T14b_supplement/          open this folder as the project
  README.md
  requirements.txt
  code/                   every script and library; nothing is run from here
  outputs/                the deposited results the note quotes
  films/                  the deposited films
  work/                   created by reproduce.py
    bin/tpsim               the compiled simulation code
    tests/                  the two code tests
    sims/                   runs/<tag>/ (mergers) and halos/<tag>/ (assembly)
    films/                  runs/<tag>/ (film re-runs, compact frames)
    galaxy/                 the Galaxy model's outputs
    outputs/                regenerated results, named as in outputs/
    figures/                regenerated figures
  work_quick/             created by reproduce.py --quick, laid out as work/
\end{verbatim}}
Two rules follow from how the scripts are written. First, every file in \file{code/} must stay in that one folder: the scripts import one another by module name (\file{ics}, \file{render\_lib}, \file{sam2} and so on), and Python finds them because they sit beside the script being run. Second, the working directory matters. The simulation and measurement scripts read and write paths relative to the folder they are run from (\file{runs/}, \file{halos/}, \file{./tpsim}), so they must be run from \file{work/sims} (mergers, assembly, measurements) or \file{work/films} (film re-runs), never from \file{code/}. \file{reproduce.py} sets the working directory for each stage and copies \file{tpsim} into place, so the simplest course is to run everything through it.

**setting  (Laying out the files).** \textbf{In an IDE.} In Visual Studio Code, open \file{T14b\_supplement} with \emph{File, Open Folder} (on Windows, from inside WSL with the WSL extension's \emph{Open Folder in WSL}). Create a virtual environment in that folder, select it as the Python interpreter, and run the stages from the integrated terminal at the top folder. To run or debug one script inside the IDE, give its launch configuration the stage folder as working directory, for example \texttt{"cwd": "\$\{workspaceFolder\}/work/sims"}. In PyCharm, mark \file{code/} as a sources root and set each run configuration's working directory to \file{work/sims}, \file{work/films} or \file{work/galaxy}. No C tooling in the IDE is needed: \file{tpsim} is built once from the terminal.

**setting  (Running).** From the top folder:
{ \begin{verbatim}
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python code/reproduce.py figures --deposited   # the note's figures from outputs/
python code/reproduce.py all --quick           # check the whole chain on small runs
python code/reproduce.py all                   # the note's runs, half a day to a day
python code/reproduce.py compare               # regenerated against deposited
\end{verbatim}}
The first run of \file{reproduce.py} redraws the eight figures from the deposited results in a few seconds; with the library versions above and the Computer Modern font they are identical, pixel for pixel, to the note's, and with other versions the data are the same and the typography may differ. The \texttt{--quick} option runs three small mergers ($4000$ particles), two small cluster assemblies and coarse films, and one disk scale of the Galaxy model, so that every stage can be checked in about half an hour; its numbers are not the note's, and it works in \file{work\_quick/}, so it never occupies the folders of the full runs. The \texttt{figures} stage draws from \file{work/outputs/}, takes any result not regenerated there from the deposited \file{outputs/}, and says which it used for each file. Stages can be run one at a time, in the order of the table accompanying \claimref{simulations.mirror-galaxy}; each needs only the ones before it, and \texttt{--threads} sets the number of OpenMP threads for \file{tpsim} (default $2$, as in the note). A merger run that has finished is skipped if the stage is started again.

\centering \begin{tabular}{@{}l>{ \arraybackslash}p{0.48\textwidth}>{ \arraybackslash}p{0.24\textwidth}@{}}
\toprule
Stage & What it runs & Time on 2 cores \\
\midrule
\texttt{build} & compiles \file{tpsim.c} & seconds \\
\texttt{tests} & the two code tests of the section ``The simulation code'', at full size even with \texttt{--quick} & $5$ to $10$ min \\
\texttt{mergers} & the $13$ merger runs of the table accompanying \claimref{simulations.averaged-pair-operator} to $t = 1.3$ & $15$ to $60$ min each (CDM fastest, reading (W) slowest) \\
\texttt{halos} & the $13$ assembly runs ($4000$ particles per progenitor, $t = 2.0$, seeds $11$ and $23$) & $5$ to $25$ min each \\
\texttt{measure} & \file{analyze3.py}, \file{halo\_measure.py}, \file{proj\_ell.py}, \file{pk.py} & minutes \\
\texttt{films} & three re-runs with snapshots every $0.01$, then both films & $15$ to $60$ min per run, plus a few minutes' rendering \\
\texttt{galaxy} & both disk scales of the Galaxy model, the pass counts, the $F$ table (the table accompanying \claimref{simulations.halo-shapes}) & about $25$ min \\
\texttt{small} & \file{sheet\_sidm.py}, \file{scatter2d.py}, \file{mirror\_cosmo.py}, \file{imf\_feedback.py}, \file{ml\_baseline.py} & under a minute \\
\texttt{figures} & \file{make\_figs.py} on \file{work/outputs/} & seconds \\
\texttt{compare} & prints regenerated against deposited numbers & seconds \\
\bottomrule
\end{tabular}

\emph{The stages of \file{reproduce.py}.}

**setting  (Running).** \textbf{Single runs by hand.} Compile \file{tpsim} and copy it into the stage folder, then run from there:
{ \begin{verbatim}
mkdir -p work/bin work/sims
gcc -O3 -fopenmp -o work/bin/tpsim code/tpsim.c -lm
cp work/bin/tpsim work/sims/
cd work/sims
python ../../code/merger.py mirror random mirror_only
python ../../code/halo.py rule random rule_random_s2 4000 2.0 23
python ../../code/analyze3.py cdm mirror_only
\end{verbatim}}
\file{merger.py} takes a model, a sheet orientation and a run name, then optionally the particle numbers of the two clusters (default $60{,}000$ and $20{,}000$) and an end time (capped at $1.3$). The models are \texttt{cdm}, \texttt{rule}, \texttt{mixed}, \texttt{mixednm}, \texttt{rule1}, \texttt{rule1nm} and \texttt{mirror} (the table accompanying \claimref{simulations.averaged-pair-operator}); the orientations are \texttt{random}, \texttt{perp} and \texttt{par}. \file{halo.py} takes a model, \texttt{random}, a run name, then particles per progenitor, end time and seed; the note's runs used $4000$, $2.0$ and seeds $11$ and $23$ (the defaults are $5000$, $2.5$ and $11$). \file{analyze3.py} measures the named merger runs and should be given \texttt{cdm} first, since own mass is relative to it. \file{tpsim} itself takes the initial-conditions file, an output prefix, the end time, the snapshot interval, the softening, the opening angle $\theta$, the cooling coefficient $A$, the energy floor, and optionally $\Delta t_{\max}$ and $h_{\min}$; the scripts pass $0.02$ (mergers) or $0.5$ (assembly), $15$, $0.7$, \texttt{ics.cooling\_A()}, \texttt{ics.u\_of\_T(1e4)}, $0.002$ and $10$.

**setting  (What to expect).** Initial conditions are reproduced bit for bit: regenerated with the fixed seeds, all $26$ merger and assembly initial-conditions files match the SHA-256 checksums of the runs reported here, deposited as \file{outputs/ic\_sha256.txt}; from \file{work/sims},
{ \begin{verbatim}
sha256sum -c ../../outputs/ic_sha256.txt
\end{verbatim}}
\noindent checks them. The evolved runs are reproduced statistically, not bit for bit, since the OpenMP threads sum forces in a varying order and the time steps change with the snapshot spacing (the section ``The films''); the film re-runs show the size of the differences. The Galaxy model, the $F$ table, the mass-to-light baseline and the printed tables of the section ``Self-interaction within a sheet'' are deterministic and are reproduced exactly. The compiler's warnings about unused return values of \texttt{fread} are harmless.

## Results cited, not shown

**Fact (imported) 23 (The mirror share is one, and how fragile that is).** Write $m_{r} = c_{r}\Lambda_{r}$, with $\Lambda_{r}$ the confinement scale of tower $r$'s non-abelian sector and $c_{r}$ the constituent factor of its lightest charge-carrying composite.
\begin{enumerate}
\item[(i)] \emph{(The mirror.)} By Theorem \claimref{dark-matter.mirror-tower-copy-one}(iii), with the common ceiling and coupling of Premise \claimref{synthesis.common-ceiling-coupling-premise}, $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$ exactly, hence $f_{2} = 1$ under P4, which Theorem \claimref{dark-matter.mirror-tower-copy-one}(v) discharges for the mirror as an equality of the charge $B - L$, and under Hypothesis (equal conversion) stated below; the equality of $\Lambda$ and $c$ is an isomorphism of theories rather than a one-loop statement. As a ratio of mass densities it is a ratio of mean mass per baryon: ours is about $936.7$ MeV after helium, a mirror burnt entirely to helium (the completion limit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}'s burning branch) gives $931.8$ MeV, so $f_{2}$ is $0.995$ in that limit and $1$ on the proton-only branch, a one-sided systematic of half a percent at assembly level. Caveat (T14c): the two branches bracket the share where the mirror is helium or protons; at $\xi = 2.8$ to $3.2 \times 10^{-4}$, the gravitational floor's value with the production coefficients first imported, the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons, and at the present floor, $6.6 \times 10^{-4}$, it is moderately degenerate and ends $83$ to $96$ percent neutrons, in both cases a composition neither branch describes, and it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ (Computation \claimref{dark-tower-matter.mirrors-composition}); the half-percent bracket is established there and not at the floor.
\item[(ii)] \emph{(Fragility.)} The equality is unstable to any departure from the copy. Suppose the two towers shared a ceiling $M$ and coupling but differed in light content by $\Delta b$ over the running range, with $b_{6} \leq 11$; then at one loop
\[
\ln\frac{\Lambda_{2}}{\Lambda_{6}} \;\geq\; \frac{\Delta b}{b_{6} + \Delta b}\,\ln\frac{M}{\Lambda_{6}}.
\]
One Dirac flavour is $\Delta b = 2/3$, which with $\Lambda_{6} = 0.3$ GeV moves the mirror share by a factor between $4.89$ (bottom of the ceiling range, $b_{6} = 11$) and $21.4$ (top, $b_{6} = 7$), past the observed $5.364$ everywhere except at the bottom of the range on the most conservative branch. A coupling departure $\delta = \alpha_{2}(M)^{-1} - \alpha_{6}(M)^{-1}$ at the ceiling with identical content moves $\Lambda_{2}/\Lambda_{6}$ by $e^{-2\pi\delta/b}$, a factor $2.45$ per unit at $b = 7$, so the share stays within ten percent of one only for $|\delta| < 0.106$. So the mass factor of $f_{2}$ is exactly one, protected by the common-ceiling-coupling premise (Premise \claimref{synthesis.common-ceiling-coupling-premise}), and fragile; $f_{2} = 1$ itself holds under Hypothesis (equal conversion) in addition.
\item[(iii)] \emph{(The odd towers.)} In three and five dimensions the gauge coupling is dimensionful and the confinement scale is set by the coupling itself ($\Lambda_{3} \sim g_{3}^{2}N$, $\Lambda_{5} \sim 1/g_{5}^{2}$), so nothing about $\Lambda_{1,7,3,5}$ follows without a rule the series does not derive (Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}); the unit-ball rule of the section ``The dark matter ratio: the unit-ball rule'' constrains that rule, as shares per unit of our volume, without supplying it.
\end{enumerate}
\emph{Hypothesis (equal conversion).} The mirror's ratio of baryon number to $B - L$ equals this tower's. It is not shown, and it is a stated hypothesis of this result, not a registered premise: the inherited charge is the total $B - L$, and the copy equates the two towers' $B - L$, not their baryon number (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i), version 11). The mirror's unit of the observed dark-to-baryon total $5.364$ is conditional on it.

Level: (i) is Theorem \claimref{dark-matter.mirror-tower-copy-one}, with the Hypothesis; (ii) is one-loop arithmetic under its stated assumptions, flagged; (iii) is a scope statement.

*Provenance:* Physics Graph result dark-matter.mirror-share-one-how-fragile, version 10 (T14 Prop 4.7).

**Fact (imported) 24 (The mirror tower is a copy of this one).** Every item of Fact \claimref{dark-matter.imported-inputs-standard-model-chain} is invariant under the signature reversal $(p,q) \mapsto (q,p)$ that carries this tower's signature $(1,3)$ to the mirror's $(3,1)$ (the proof runs the list item by item; the tractor bundle over a $(3,1)$ conformal structure has ambient $\R^{4,2}$ and the same complexified fibre, Hypothesis (S) has no signature in it, and one-loop running depends on the content alone). Hence:
\begin{enumerate}
\item[(i)] the mirror tower's derived content is a copy of this tower's: gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$, the same global form, the same generation with the same hypercharges and the same chirality halves, including a massless mirror photon and mirror neutrinos;
\item[(ii)] the ground type (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}: $\R$ for the mirror, $\mathbb{H}$ for this tower) does not enter: the derivation uses the conformal spin group and its complex representations, never the tower's real Clifford module;
\item[(iii)] the mirror's light content, and therefore its $\beta$-functions at every scale, equal this tower's, so that with a common ceiling $M$ and a common coupling there its confinement scale and composite spectrum equal ours exactly, $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$, and with the equal asymmetry per mode of (v), which is an equality of the charge $B - L$, and under Hypothesis (equal conversion) stated after (v), its tower factor is $f_{2} = 1$ up to the ratio of mean mass per baryon of the two sectors, which their nuclear histories set (one on the proton-only branch, $0.995$ on the burning branch, Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)): $\Omega_{\mathrm{mirror}} = \Omega_{b}$ to half a percent, under that Hypothesis;
\item[(iv)] the common ceiling and the common coupling in (iii) are Premise \claimref{synthesis.common-ceiling-coupling-premise}, which equates them along the reversal orbit only: Premise \claimref{dark-matter.p2-indifference}, scoped to sector labels and not states, does not reach the coupling, which is neither (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), so the equality is a premise of its own; the odd towers, off that orbit relative to this one, get no such premise;
\item[(v)] the asymmetry per mode is equal in the two towers, $\epsilon_{2} = \epsilon_{6}$, by two routes, both carried: by the audit of Premise \claimref{dark-matter.p2-indifference} applied to the stored charge, under two premises stated here: the common-$N$ clause of Premise \claimref{dark-matter.p1-single-frozen-point} (the number $N$ is common to the towers), and the charge reading (C$\epsilon$), that $\epsilon$ is a datum of the descent and not of a tower's state, inherited and not generated, which is the stance registered as Premise \claimref{synthesis.matter-asymmetry-registered-free-input} and is taken here as a hypothesis of this route; under them the asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, a sector label of the descent (the charge is named as the total $B - L$ of the tower's matter; it is not the residue label $r$ and not baryon number), so that a difference between the two members of one reversal orbit would be an uncaused distinction (the reading is worked out, with its consequences, in Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i), which comes after this theorem and is not used here); and, more weakly (isomorphic theories share the function, not thereby the value of a datum of theory plus initial condition), by inheritance, both towers being oriented by the one flag under the orientation clause of Premise \claimref{dark-matter.p1-single-frozen-point}. This equality is the instance on the mirror of the former Premise P4 (democracy of the asymmetry over the oriented towers), which is retired as a postulate: it was this clause on the mirror, void on the odd residues, and a premise only on the fork $r = 0$, where no stored result uses it. The equality proved in this clause is of the charge $B - L$. The share of one in (iii) rests on P1, P2, the common ceiling coupling, the charge reading (C$\epsilon$) on the first route, the copy, and Hypothesis (equal conversion).
\end{enumerate}
\emph{Hypothesis (equal conversion).} The mirror's ratio of baryon number to $B - L$ equals this tower's. It is not shown, and it is a stated hypothesis of this result, not a registered premise: the inherited charge is the total $B - L$, and the copy equates the two towers' $B - L$, not their baryon number (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i), version 11). The mirror's unit of the observed dark-to-baryon total $5.364$ is conditional on it.

This is mirror matter in the sense of the literature \cite{FootMirror2004}, derived rather than posited: the framework's $r = 2$ tower is a second Standard Model.

Caveat (T14c): applied with its version-1 reach, the reach the paper used in (iv) and (v), Premise P2 also equates a third datum of the descent along the same orbit, the energy deposited per unit charge, and so gives $\xi = T'/T = 1$ and $\Delta\Neff = 7.45$ at recombination, which the record excludes (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}). The cold mirror the paper carries is an exception to P2 at its version-1 reach; P2 as scoped leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}). (i) to (iii) stand; (iv) is the common-ceiling-coupling premise, which equates no state, and (v) holds under P2 as scoped, given its two stated premises.

*Provenance:* Physics Graph result dark-matter.mirror-tower-copy-one, version 11 (T14 Thm 4.3).

**Fact (imported) 25 (The radiation audit: what the type-by-residue theorem closes, and what stays open).** The cosmic microwave background caps extra relativistic energy at $\Delta\Neff \lesssim 0.3$ \cite{Planck2018}, and one massless photon-like species (two polarisations) at the visible temperature contributes $\Delta\Neff = (8/7)(11/4)^{4/3} \approx 4.4$, so five democratically filled sectors with such photons would contribute of order twenty. The audit proceeds tower by tower, at two levels fixed by Theorem \claimref{dark-matter.type-residue-what-each-tower-can} and Remark \claimref{note.dark-matter.where-flag-defined-what-it-carries}: the \emph{ground} level, where the type decides whether the tower's spinors carry an intrinsic $U(1)$ (exactly at the complex member of each odd pair, $r = 3, 7$ in the paper's convention), and the \emph{rung} level, where every flagged tower carries abelian charges from its ladder pairs.
\begin{enumerate}
\item \emph{(The mirror tower, $r = 2$.)} Open, by theorem: the mirror's derived content is a copy of ours (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so it has a massless mirror photon and three light mirror neutrinos. The ground level is closed for the real member of the pair $\{2, 6\}$ (intrinsic group $\mathbb{Z}_{2}$, Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(i); which member depends on the labelling convention, Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}) and irrelevant, since the content is not at that level. This is the mirror-matter situation of the literature, costed in Proposition \claimref{dark-matter.open-channels-their-costs}.
\item \emph{(The three-dimensional towers, $r = 1, 7$.)} Closed at both levels: vector-like (no chirality in odd dimension), so Dirac masses are unforbidden and generic; with no massless charged matter left, each compact $U(1)$ in three dimensions, the intrinsic one of the complex member of $\{1, 7\}$ (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(ii)) and the rung-level ones of both, leaves no massless photon. The paper states that every such $U(1)$ confines by monopoles \cite{Polyakov1977}; with the half-integral bare Chern-Simons level that the parity anomaly forces (Proposition \claimref{dark-tower-matter.anomalies}(i)), that holds in the confining phase (C) only, and in phase (T) the photon is instead topologically massive (Proposition \claimref{dark-tower-matter.three-dimensional-phases}); both phases close the channel. The non-abelian factors confine.
\item \emph{(The five-dimensional towers, $r = 3, 5$.)} Open at both levels: the complex member of the pair $\{3, 5\}$ carries an intrinsic $U(1)$ by theorem (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(ii); which member depends on the convention), both carry rung-level ones, no Polyakov mechanism exists in five dimensions, and by Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones} a surviving photon dilutes as $a^{-4}$, exactly as ours.
\item \emph{(The Goldstone exposure.)} Confining dark sectors with chiral breaking could leave massless dark pions. The framework supplies its own gap: any tower's accidental global symmetries are broken by its own tower's higher rungs (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), so the Goldstones are pseudo-Goldstones with masses of order $\Lambda_{\mathrm{conf}}^{2}/M_{\mathrm{rung}}$, the existence input a theorem and the mass estimate dimensional analysis.
\end{enumerate}
Conclusion: the three-dimensional towers are closed by theorem plus Polyakov confinement or, in phase (T), topological mass; the mirror tower is open by theorem, with a known relativistic content, and closes only if it is cold, which by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} is an exception to P2 (applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), P2 gives $\xi = 1$ and $\Delta\Neff = 7.45$; that is an exception at P2's version-1 reach, P2 as scoped leaving $\xi$ free, Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}, and the cold mirror then needing a non-equilibrium descent, Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}); the five-dimensional towers are open with a content this paper does not derive. By the section ``Seeding by gravity, and why no coupling rule follows'' (proved given the production rate, now derived in the store) every dark tower's temperature is bounded below by gravitational heating, at about seven to eight parts in ten thousand of the visible temperature at the top of the ceiling range for the two contents computed, and above by whatever energy the descent deposited, which the $\Neff$ cap limits to $0.448$ for the mirror and the paper's hot-deposit estimate puts near $4 \times 10^{-3}$ (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}); across that interval both the mirror's channel and the five-dimensional towers' close by eight orders or more (eleven at the mirror's floor; the one case below eight is a nine-vector tower at the hot end, at $7.4$). $\Delta\Neff \approx 0$ is therefore a conditional stance, conditional on the open channels closing by one of the routes of Proposition \claimref{dark-matter.open-channels-their-costs} and on the deposit being no hotter than the estimate; so registered, and stated with that cost.

On self-interaction: in the three-dimensional towers it is at composite strength if their matter is the confined charged matter the closure leaves, which the series does not establish (the section ``The composition in galaxy clusters and in the Galaxy''); in the five-dimensional ones it is undetermined; and for the mirror the composite figure is the wrong one, since mirror matter recombines at a visible temperature of order a keV (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}) and enters structure formation as neutral mirror atoms, with an elastic cross-section per mass of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\mathrm{cm^{2}\,g^{-1}}$, and as a plasma once ionised inside a halo: collisional and dissipative like our gas, tested by the collisional-fraction and dark-disk bounds of refutation item 6. The rung-breaking scale of channel (4) is valued in Proposition \claimref{dark-matter.ceiling-valued-inherited-success}.

*Provenance:* Physics Graph result dark-matter.radiation-audit-what-theorem-closes-what, version 10 (T14 Prop 6.2).

**Fact (imported) 26 (A reduced response to gravity needs a supporting stress; the sheets move).** Let a pressureless component respond to the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; the perturbed FLRW field in the conformal Newtonian gauge of Fact \claimref{dark-matter.imported-linear-momentum-equation-traceless-field}, potentials $\psi$, $\phi$) at a fraction $g$ of the full strength, $\theta' = -\mathcal{H}\theta + g\,k^{2}\psi$. Then (i) it carries the anisotropic stress $\sigma = (1 - g)\psi$, and no other value; (ii) that stress enters the field equations, so that with the other components' stresses $\Sigma$,
\[
\psi \;=\; \frac{\phi - 12\pi G a^{2}\Sigma/k^{2}}{1 + 12\pi G a^{2}\rho\,(1 - g)/k^{2}} .
\]
For a three-dimensional tower whose sheets are held fixed, $g = \sin^{2}\theta$ for a wavevector at angle $\theta$ to the missing direction (script: $k_{\perp}^{2}/k^{2}$), $\tfrac{2}{3}$ averaged over orientations, and the stress of (i) is that of a medium holding the sheets in place. The series supplies no such medium: nothing in Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones} or in the towers' content gives the sheet family a rigidity along its normal, and the sourcing rule couples the sheets' matter to the one gravitational field $(\hb, \Omega)$ like any other. Hence, on the series as written, the sheets are displaced along their normal by the potential gradient, $g = 1$, and the three-dimensional towers respond to gravity in full at linear order.

*Provenance:* Physics Graph result dark-matter.reduced-response-gravity-needs-supporting-stress, version 3 (T14 Prop 7.28).

**Fact (imported) 27 (The stored asymmetry is a charge, not a number).** Under the classification of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, with $\epsilon$ initial data of the descent, inherited rather than generated, and the number $N$ common to the towers under P1 ($N = M_{P}/H$, which fixes a count of registered units, about $\pi N^{2}/\ln 2$, without being it: Observation \claimref{standard-model.largeness-number-universes-boundary-modes}; the light rays number $2\pi N^{2}/(c\ln 2)$ for $c$ boundary-mode arrays per light ray (\claimref{synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping}(iii)), and $c$ depends on the tower's content, a five-dimensional field counting one array set per Kaluza-Klein level, equivalently one per resolution cell of the extra direction, so the common count is that of registered units, not of light rays or of boundary modes; the argument uses only that $N$ is common):
\begin{enumerate}
\item[(i)] \emph{(Charge.)} The asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, fixed by the descent's data and independent of the tower's temperature; it is not a thermal number $n - \bar{n} \propto g\,\mu T^{2}$. Three objects have carried the word charge in the stored statements, and they are kept apart here: the residue label $r$ of the tower, constant on the tower's sector, which is what the superselection rule is about (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}, step 1); the total $B - L$ of the tower's matter; and its baryon number $n_{B}$, which is what the measured baryon density reads. By the maintainer's decision of 12 November 2026, $Q$ is the second, the total $B - L$ (Premise \claimref{synthesis.matter-asymmetry-registered-free-input}); the naming is a decision and not a result of this Proposition. What then holds at any mirror temperature is that the mirror carries the same $B - L$ as this tower. The mirror share $f_{2} = 1$ is an equality of baryon number, and it follows from the equal $B - L$ only if the mirror's ratio of baryon number to $B - L$ equals this tower's. That is not shown: in this tower the ratio is the equilibrium coefficient of the anomalous weak process, if that process equilibrated after the descent (a coefficient that is not a stored Fact, $\tfrac{28}{79}$ for one light doublet and $\tfrac{8}{23}$ for two, \claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(vi)), a number for a hot plasma, and at $\xi = 2.8$ to $3.2 \times 10^{-4}$, the floor's value with the production coefficients first imported, the mirror's plasma is degenerate from the moment it is seeded, and at the present floor of (iii) it is still degenerate there, though moderately: its quark chemical potential is $3.5$ times its temperature at seeding, where it is $18$ to $23$ at the lower values (Computation \claimref{dark-tower-matter.mirrors-composition}). So $f_{2} = 1$ at any mirror temperature is conditional on that equality of ratios; given it, a cold mirror carries the same baryon number as this tower, with negligible mirror radiation. The words ``equal baryon number'' in (iii) and the comparison of (iv) are read under the same condition.
\item[(ii)] \emph{(Origin.)} The three objects of (i) have three different statements. \emph{Between towers.} The residue $r$ is superselected, and the one channel superselection leaves open, gravitational production from the visible plasma (the section ``Seeding by gravity, and why no coupling rule follows''), yields $3.9 \times 10^{-14}$ mirror quanta per unit entropy at the ceiling reheating ($1.95 \times 10^{-14}$ creation events of two quanta each, Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(iii)) against the $8.7 \times 10^{-11}$ baryons per unit entropy that our baryon number requires, more than three orders too few even counting every produced quantum as a baryon. So the mirror's matter is not supplied from this tower after the descent. Superselection of $r$ forbids exchange between towers and implies nothing about a charge within a tower. \emph{Within a tower, $B - L$.} For one family, of the terms the store holds only the Majorana element changes $B - L$: the electroweak mass terms conserve it, the $24$ slot-pair generators carry it, and its mixed weak coefficient vanishes (\claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(ii) to (v)). Premise \claimref{neutrino.r-descent-reheats-below-lower-heavy} states that the descent reheats below the lower heavy scale, so that no heavy state thermalised and the descent's $B - L$ is untouched. So, argued and not proved, the charge $Q$ is the descent's and is not produced afterwards given that Premise, with the Majorana element the named exception: no rate of that element is computed with or without the Premise, the non-thermal injection by descent-populated heavy states vanishes only under the real-breaking assumption (\claimref{neutrino.leptogenesis-suppressed-alignment-reheating-premise-new}), and nothing is shown beyond one family. \emph{Within a tower, baryon number.} That it cannot be produced afterwards is not asserted. The $24$ slot-pair generators do not commute with $n_{B}$ (\claimref{synthesis.baryon-number-centraliser-in-the-five-mode-algebra}(iii); \claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(iv)), and no bound on their rate is stored; and the anomalous weak process, on the imported statement that it changes a charge of non-zero mixed weak coefficient (not a stored Fact), changes $n_{B}$ and keeps $B - L$, and its equilibrium, which the check of Computation \claimref{dark-tower-matter.mirrors-composition} uses, produces baryon number from $B - L$ after the descent. The $8.7 \times 10^{-11}$ baryons per unit entropy are then a figure derived from the datum, conditionally, as the Premise on $\epsilon$ states. Black holes are a sink for $Q$, not a source (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(iv), under P5): a mass-preserving rearrangement that erodes each tower's free baryon count and moves no share.
\item[(iii)] \emph{(Temperature.)} Taken as a free datum of the descent, which by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} is an exception to P2 (applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), P2 gives $\xi = 1$, which the record excludes; that is an exception at P2's version-1 reach, P2 as scoped leaving $\xi$ free, Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}, and the cold mirror then needing a non-equilibrium descent, Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}), the mirror's temperature ratio $\xi = T'/T$ is bounded below by the gravitational floor, $\xi = 6.6 \times 10^{-4}$ at the ceiling reheating (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii), with the derived production coefficients, which close the earlier species-counting bracket, and the mean energy per creation event computed from the rate; four parts in a thousand of this at the bottom of the ceiling range), and above by the $\Neff$ cap at $0.448$; a deposit of each unit of baryon number with energy of order the reheating temperature puts it at $\xi \approx 4 \times 10^{-3}$. The paper carries the whole interval. With $\eta = n_{B}/n_{\gamma} = 6.1 \times 10^{-10}$ here and equal baryon number,
\[
\eta' \;=\; \frac{\eta}{\xi^{3}}
\]
runs from $2.1$ at the floor down to about $0.008$ at the hot deposit, crossing one at $\xi = \eta^{1/3} = 8.5 \times 10^{-4}$: at least $10^{7}$ times ours throughout, with $\Delta\Neff$ eight orders or more below the cap.
\item[(iv)] \emph{(The two readings.)} The thermal reading would give $f_{2} \sim \xi_{2}^{3}$ instead, at most $0.090$ under the $\Neff$ cap ($0.448^{3}$) and $10^{-7}$ or less anywhere between the floor and the hot deposit; the two readings cannot both hold, and the paper's own classification decides for the charge.
\end{enumerate}
Level: the classification is Fact \claimref{dark-matter.imported-trichotomy-descents-data}'s; the incompatibility is arithmetic. The mirror's nucleosynthesis, which is not a copy of ours and on which the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) and the composition caveat of refutation item 6 rest, follows the proof, at assembly level. Caveat (T14c): the proof's thermal up-down ratio at freeze-out fails at the cold end: at $\xi = 2.8$ to $3.2 \times 10^{-4}$ (the floor's value with the coefficients first imported) the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons, and at the present floor $6.6 \times 10^{-4}$ it is moderately degenerate and ends $83$ to $96$ percent neutrons; it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate and not the floor (Computation \claimref{dark-tower-matter.mirrors-composition}). The burning branch is therefore not the floor's composition.

*Provenance:* Physics Graph result dark-matter.stored-asymmetry-charge-not-number, version 13 (T14 Prop 4.6).

**Fact (imported) 28 (Superselected, hence dark and exactly stable).** By Premise \claimref{dark-matter.p1-single-frozen-point} and the acoustic programme (Fact \claimref{dark-matter.imported-gravity-only-coupling}, the series' acoustic no-go, at its mixed level: within the s-wave current algebra, with the sphere step conditional on the Indifference premise and the thermal state on premise (Q)), matter in a neighbouring tower gravitates on this metric and does nothing else observable at first order: dark by structural necessity, at that level. Stability is then not suppressed but exact, in three steps, the first of which is proved given the sector decomposition of Definition \claimref{obj.dark-matter.frozen-phase-operators}.
\begin{enumerate}
\item The tower charge $r$ is superselected in the frozen phase: frozen-phase operators are built from the one soldering and preserve its signature (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}), so portal matrix elements between residues vanish identically away from walls.
\item The walls are unreachable: singular loci ascend within-tower, since the completion adjoins exactly $(1,1)$ and preserves the residue (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), while the mod-8 shadow walls that separate residues are displaced successively away from the physical region, by the wall-sequence theorem of the sheaf paper \cite[\S5]{ButlerT4}, under that theorem's hypotheses (a compact base and good couplings at every stage), carried here.
\item Therefore the only inter-tower event in the universe's history is the descent itself: the towers communicated once, at the origin, and have been in absolute mutual darkness but for weight ever since. The singular locus of a black hole is an inter-tower event for energy, as it already was for weight, and never for the residue of any quantum: energy crosses at the wall, the residue does not (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}).
\end{enumerate}
One residue is flagged at observation level: dark-tower matter crossing this tower's horizons carries superselected charge the four-dimensional boundary mode space cannot hold, which routes it into the tower-wise run of the singularity paper's ascend-then-descend structure \cite{ButlerT5}; the computation of that routing, with the mass range of its Gauss-law clause, is Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}.

*Provenance:* Physics Graph result dark-matter.superselected-hence-dark-exactly-stable, version 5 (T14 Prop 4.1).

**Fact (imported) 29 (The total as a function of the thickness).** Let the five-dimensional towers' matter count through a length $c\,d_{b}$ of the extra direction and the three-dimensional towers' sheets be stacked $c\,d_{b}$ apart, with R1, R2 and the sourcing rule otherwise as before, the four odd towers populated (Premise \claimref{dark-matter.odd-towers-populated}) and residues $0$ and $4$ empty (Premise \claimref{dark-matter.single-ideal-at-residues-zero-and-four}). Here $d_{b}$ is the cell radius, each tower's own and common to all towers under R2, so the thickness is measured in the unit R2 supplies. Then
\[
T(c) \;:=\; \frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; 1 + \frac{8}{3c} + \frac{16c}{3\pi},
\]
and:
\begin{enumerate}
\item[(i)] $T(c) = T\!\left(\dfrac{\pi}{2c}\right)$ for every $c > 0$;
\item[(ii)] $T$ has a single minimum,
\[
c_{\ast} = \sqrt{\frac{\pi}{2}} = 1.2533, \qquad T_{\ast} = 1 + 2\sqrt{\frac{128}{9\pi}} = 5.2554,
\]
which is $1.7\sigma$ below the observed value; no thickness gives less;
\item[(iii)] $T(c) = 5.3643$ exactly at $c = 1$ and $c = \tfrac{\pi}{2}$, the two roots of one quadratic, with product $\tfrac{\pi}{2}$;
\item[(iv)] against $5.364 \pm 0.065$ the allowed thicknesses are $c \in [0.943, 1.086]$ or $c \in [1.447, 1.667]$ at one standard deviation, and the single interval $c \in [0.898, 1.750]$ at two;
\item[(v)] the three-dimensional fraction of dark matter, which self-interacts if that matter is at composite strength (Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}), is
\[
\frac{2 f_{3\mathrm{D}}}{T(c)} \;=\; \frac{8}{3c\,T(c)} : \qquad 49.7\% \text{ at } c = 1, \quad 40.5\% \text{ at } c_{\ast}, \quad 31.6\% \text{ at } c = \tfrac{\pi}{2}.
\]
\end{enumerate}

*Provenance:* Physics Graph result dark-matter.total-function-thickness, version 6 (T14 Prop 7.15).

**Fact (imported) 30 (The unit-ball rule).** Under Premises E (\claimref{dark-matter.e-equal-mass-per-unit-ball}) and R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}), with the four odd towers populated (Premise \claimref{dark-matter.odd-towers-populated}) and residues $0$ and $4$ empty (Premise \claimref{dark-matter.single-ideal-at-residues-zero-and-four}):
\begin{enumerate}
\item[(i)] \emph{(The rule.)} The share of a tower whose space has $D$ dimensions is $f = \tfrac{V_{3}}{V_{D}}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; V_{3}\sum_{\text{dark }r}\frac{1}{V_{D_{r}}}
\;=\; \frac{V_{3}}{V_{3}} + 2\,\frac{V_{3}}{V_{2}} + 2\,\frac{V_{3}}{V_{4}}
\;=\; 1 + \frac{8}{3} + \frac{16}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.36432\ldots
\]
against the observed $5.364 \pm 0.065$.
\item[(ii)] \emph{(The quanta do not enter.)} Only the mass per unit ball enters. A filling that keeps E has the shares of (i) whatever its quanta weigh and however many they are. Premises R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) and R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}), in R2's common length, imply E in that length, so the rule holds under R1 to R3, as it was first stated; they are not needed.
\item[(iii)] \emph{(E and R3 are the closed form's shares, tower by tower.)} Write $\rho_{r}$ for the mass density of the tower of residue $r$ in its own space, $r = 6$ this world, let the three-dimensional towers' sheets be $s$ apart and let the five-dimensional towers' matter count through a length $t$ of the extra direction, so that in the sourcing rule
\[
f_{r} \;=\; \frac{\rho_{r}}{s\,\rho_{6}} \;\; (r = 1, 7), \qquad f_{2} \;=\; \frac{\rho_{2}}{\rho_{6}}, \qquad f_{r} \;=\; \frac{\rho_{r}\,t}{\rho_{6}} \;\; (r = 3, 5) .
\]
Then there is a length $d$ for which E holds with $s = t = d$, as R3 requires, if and only if $s = t$, each three-dimensional tower's share is $\tfrac{V_{3}}{V_{2}}$, each five-dimensional tower's share is $\tfrac{V_{3}}{V_{4}}$ and the mirror's share is $1$. In particular, for any densities of a three-dimensional tower and of this world the length $d = \rho_{1}V_{2}/(\rho_{6}V_{3})$ is the only one at which the two hold equal mass per ball, and with the sheets that far apart that tower's share is $\tfrac{V_{3}}{V_{2}}$ whatever the two densities are: there E with R3 puts no condition on the densities, it defines $d$ from them. The conditions that remain are that the other three-dimensional tower has the same density, that the mirror has ours, and that each five-dimensional tower has $\rho_{r}V_{4}d = \rho_{6}V_{3}$, which is its share. So E with R3 says what the closed form's shares say, tower by tower, and that the two thicknesses are one length, an equality the total does not see. The total says less than either: it fixes only the sum of the shares.
\item[(iv)] \emph{(One length.)} With towers of more than one space dimension populated, as Premise \claimref{dark-matter.odd-towers-populated} has it, E cannot hold in two different lengths: equal mass per ball at $d$ and at $d' \neq d$ would make $(d'/d)^{D}$ take one value at $D = 2$, $3$ and $4$.
\end{enumerate}
The agreement of (i) with the observed value is built in, not predicted: the relation was found by solving for the observed value, and its clauses were chosen with it known, and the closed form is one of fourteen equally simple candidates within the error bar (Observation \claimref{dark-matter.status-rule}). By (iii) the premises say what the closed form's shares say, with the two thicknesses equal, so they give the fit no support that is independent of the fitted number.

\emph{What the total rests on.} On the stored dependence edges the past cone of this closed form holds these postulates of the dark-matter subject: E and R3; P1 (\claimref{dark-matter.p1-single-frozen-point}), through the sourcing rule in which the shares are read (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}); P2 and P3, through the census of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}; and the two conditions registered as premises on 10 November 2026, the single-ideal clause \claimref{dark-matter.single-ideal-at-residues-zero-and-four} and the population of the odd towers \claimref{dark-matter.odd-towers-populated}. Until 19 November 2026 the cone held R1 and R2 in place of E, with R3's unit each tower's own cell radius and R2 entering twice; one length now does both jobs, as the radius of E's ball and as R3's unit. The democracy premise (\claimref{dark-matter.d-democracy-total-mass}) is not among them: it is E at the de Sitter radius, given the stored reading of the sphere form (Theorem \claimref{synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball}(ii)), a reading of its own. The total remains a fit. The mirror's share of one is derived separately (Proposition \claimref{dark-matter.population-count-one-share-half-percent}), so the closed form fixes two shares, $\tfrac{4}{3}$ and $\tfrac{8}{3\pi}$, against one measured number, the remainder $4.36 \pm 0.07$. Chosen with that number known, by the store's own record: the relation was found by solving for the observed value (Observation \claimref{dark-matter.status-rule}(i)); the clauses of the contact mechanism that returns R3's value were chosen with it known (the same, (ii)); the single-ideal clause was chosen knowing that the fit needs it (the same, (vi)); and the population of the odd towers is inferred from the remainder itself (Observation \claimref{dark-matter.which-towers-are-populated}). P1, P2 and P3 belong to the paper's earlier sections, written before the rule was proposed (Remark \claimref{note.dark-matter.setting-dark-matter-ratio-unit-ball}).

*Provenance:* Physics Graph result dark-matter.unit-ball-rule, version 7 (T14 Prop 7.6).

**Fact (imported) 31 (A vector times a multivector).** For a vector $a \in V$ and any $X \in \Cl(V, Q)$,
\begin{equation}
a X = a \rfloor X + a \wedge X, \qquad a \rfloor X = \tfrac12\bigl(a X - \hat{X} a\bigr), \qquad a \wedge X = \tfrac12\bigl(a X + \hat{X} a\bigr).
\end{equation}
For $X = X_k \in \Cl^{k}$, $a \rfloor X_k \in \Cl^{k-1}$ and $a \wedge X_k \in \Cl^{k+1}$, so $a X_k$ has only these two grades. In particular $a b = B(a, b) + a \wedge b$ for vectors.

*Provenance:* Physics Graph result std-algebra.product-decomposition, version 1.

**Fact (imported) 32 (The product of two vectors).** In $\Cl(V, Q)$, for all $u, v \in V$,
\begin{equation}
v^{2} = Q(v), \qquad u v + v u = 2 B(u, v).
\end{equation}
In particular $u v = B(u, v) + \tfrac12(u v - v u)$, the sum of a scalar and an antisymmetric part.

*Provenance:* Physics Graph result std-algebra.vector-squares, version 1.

**Prediction 33 (Direct detection stays null).** Permanent direct-detection nulls: dark matter couples through gravity alone, at first order.

**Prediction 34 (No dark radiation).** No dark radiation: $\Delta N_{\mathrm{eff}} \approx 0$, conditionally on the dark towers\' open channels closing, which holds if the descent\'s deposit is no hotter than the dark-matter paper\'s estimate, and only with the mirror\'s seeded temperature taken as a free datum: applied with the reach of the copy theorem, P2 gives the mirror $\xi = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$ (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}), so the stance rests on an exception to P2 for the mirror. This is an exception to P2 at its version-1 reach; P2 as scoped leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}). The seeding floor behind the radiation audit uses the rate of gravitational pair production, which is now derived in the store, with corrected coefficients and with no quantum of the gravitational field (Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v), under its hypothesis (OS), or on the standard account of Fact \claimref{dark-matter.imported-massless-graviton-production-rate}); with the corrected coefficients and the mean energy per creation event computed from the same rate integral the mirror's floor is $6.6 \times 10^{-4}$ and its channel closes by eleven orders there, where twelve stood (Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}), and the prediction is unchanged.

**Prediction 35 (No indirect dark-sector signals).** No indirect dark-sector signals: no decay products, since the tower charge is superselected, and annihilation products only at the rate of graviton exchange, suppressed by powers of $E/M_{P}$, and for the mirror, a charge-asymmetric relic, further by its negligible anti-mirror density. The words ``graviton exchange'' name the process as its sources compute it; the series holds no quantum of the gravitational field (conventions, section ``Gravity and the graviton''). The store now derives the transition of a pair of one species into a pair of another through the gravitational field from the operator source, with no such quantum, at a rate carrying $\bar{M}_{P}^{-4}$ and with corrected coefficients for the thermal rate (Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(ii) and (v), under its hypothesis (OS); the standard account gives the same tree-level rate), so the annihilation channel is the gravitationally suppressed one this stance assumes, and the prediction is unchanged.


