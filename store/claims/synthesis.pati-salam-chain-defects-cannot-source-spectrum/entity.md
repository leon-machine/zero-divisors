---
id: synthesis.pati-salam-chain-defects-cannot-source-spectrum
kind: claim
version: 3
title: 'Pati-Salam chain defects cannot source the spectrum'
status: proved
region: synthesis
subject: dark-energy
tags: [no-go, confronted-with-data, cosmological-constant, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - standard-model.majorana-element@7
  - standard-model.imported-pati-salam-representation-theory-survival@1
  - standard-model.what-angle-asks-neutrino-sector@4
  - synthesis.untuned-fit-caps-lightest-heavy-neutrino@1
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@5
  - std-algebra.spin-double-cover@1
  - synthesis.imported-macro-monopole-flux-limit@1
  - synthesis.imported-nielsen-olesen-string-tension@1
  - synthesis.imported-planck-2013-cosmic-string-bounds@1
  assumes:
  - neutrino.r-descent-reheats-below-lower-heavy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_matter_parity_in_stabiliser
- kind: check
  ref: check.py::check_matter_parity_not_in_identity_component
- kind: check
  ref: check.py::check_controls
- kind: check
  ref: check.py::check_generator_is_spin_rotor_minus_one
- kind: check
  ref: check.py::check_r_window_below_restoration
- kind: check
  ref: check.py::check_string_tension_and_cmb_fraction
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - synthesis.pati-salam-monopoles-bound-descent-history
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U5 with U1: the complex matrices of the defining representations of SU(4), SU(2)_L, SU(2)_R and U(1)_Y (exp(3 pi i(B - L)), diag(e^{i theta/6}U_3, e^{-i theta/2}), exp(i theta Y), the centre {i^a 1_4}, exp(2 pi i t Y)) are written with entries in span{1, I_4}, the store''s complex field, beside the Clifford (rotor) form already given. No bare i remains, so the outside_ga declaration (bridge, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the phases are entries of the complex defining representations of the Pati-Salam factors, stated beside their Clifford (rotor) form; declared as a bridge (version and levels unchanged).'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Premise (R) (neutrino.r-descent-reheats-below-lower-heavy), which clause (ii) and the title use directly, is now an explicit assumes edge rather than reaching the claim only through the untuned fit; uses edges added to the new Facts synthesis.imported-nielsen-olesen-string-tension and synthesis.imported-planck-2013-cosmic-string-bounds, which pin the tension and the string bounds of clause (iii), previously cited from memory. Version 1 -> 2.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    The problem's third line of attack (a defect or scaling network of the descended phase), answered
    negatively for the topological defects of the stored chain by importing its vacuum manifold from
    the standard-model subject. The Z2 strings are new to the store: the unbroken matter parity of the
    (10,1,3) breaking is not in the identity component of the stabiliser (the Pati-Salam analogue of the
    Z2 strings of SO(10) broken by the 126, Kibble, Lazarides and Shafi 1982, cited from memory).
    Transport-absent: standard defect physics on the series' chain. Literature cited from memory in the
    proof: pi_1(G/H) = pi_0(H) for connected simply connected G; the electroweak vacuum manifold is the
    three-sphere; the Nielsen-Olesen tension mu = 2 pi eps eta^2 with eps of order one (below 10 for
    every quartic-to-gauge ratio up to about 10^4); scaling of string networks from any initial density;
    the Planck 2013 and 2015 string bounds (Nambu-Goto G mu < 1.5e-7 at f_10 < 0.015, Abelian-Higgs
    G mu < 3.2e-7 at f_10 < 0.028); the LISA reach for string backgrounds (G mu of order 1e-17).
---

## formal
Work on the stored chain: $G = SU(4) \times SU(2)_{L} \times SU(2)_{R}$, simply connected (the store's $\mathrm{Spin}(6) \times \mathrm{Spin}(4)$), broken in one step at $M_{I} = 1.95 \times 10^{10}$ GeV to the Standard Model by the $\nu^{c}\nu^{c}$ component of the $(10,1,3)$ (Theorem \claimref{standard-model.majorana-element}), with $v_{R} = M_{I}/g_{R}$, $g_{R} = 0.469$ (Proposition \claimref{standard-model.what-angle-asks-neutrino-sector}); let $H$ be the stabiliser of that vacuum and $H_{0} = SU(3) \times SU(2)_{L} \times U(1)_{Y}$, $Y = T_{3R} + \tfrac12(B - L)$, its identity component. Let $M_{r} = 2.435 \times 10^{18}$ GeV be the reduced Planck mass and $A_{s} = 2.1 \times 10^{-9}$ the measured amplitude (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}).
\begin{enumerate}
\item[(i)] \emph{($\mathbb{Z}_{2}$ strings.)} The matter parity $m = (-1_{4}, 1, 1) = \exp(3\pi I_{4}(B - L))$ on the $16$ (numbers, and the entries of the defining representations of the factors, are read in $\mathrm{span}\{1, I_{4}\}$, conventions U1), which is the rotor $-1$ of $\mathrm{Spin}(6) = SU(4)$ (the $2\pi$ rotor, the kernel element of Proposition \claimref{std-algebra.spin-double-cover}; its image in $\mathrm{Spin}(10)$ is the rotor $-1$ there), lies in $H$ (it fixes every vector and so every tensor, and the $(10,1,3)$ is a tensor: self-dual $3$-vectors of the six-dimensional factor and self-dual bivectors of the four-dimensional one) and not in $H_{0}$: every central element of $G$ in $H_{0}$ has equal $SU(4)$ and $SU(2)_{R}$ scalars, and $m$ does not. Hence $\pi_{1}(G/H) = \pi_{0}(H)$ contains $\mathbb{Z}_{2}$: the chain has topologically stable $\mathbb{Z}_{2}$ strings at the scale $v_{R}$, besides the monopoles of $\pi_{2}(G/H) = \pi_{1}(H_{0}) \supseteq \mathbb{Z}$ (the hypercharge circle is a noncontractible loop of $H_{0}$ that closes in the simply connected $G$).
\item[(ii)] \emph{(No formation after the descent.)} Under Premise \claimref{neutrino.r-descent-reheats-below-lower-heavy} on the untuned fit (Proposition \claimref{synthesis.untuned-fit-caps-lightest-heavy-neutrino}) the descent reheats below $7.3 \times 10^{8}$ GeV $< 0.0176\,v_{R}$, so unless the restoration temperature of the chain lies below $0.0176\,v_{R}$ the descended bath never restores Pati-Salam, and the chain's monopoles and strings exist after the descent only as part of the deposit. The later transitions form no topologically stable defect: the electroweak vacuum manifold is the three-sphere and the strong interaction breaks no gauge symmetry.
\item[(iii)] \emph{(A deposited network is negligible.)} A deposited $\mathbb{Z}_{2}$ string network reaches scaling with $G\mu = \epsilon\,\eta^{2}/(4M_{r}^{2})$; for $\epsilon \in [\tfrac12, 10]$ and $\eta \in [v_{R}/\sqrt2, \sqrt2\,v_{R}]$, $G\mu \in (1.8 \times 10^{-17}, 1.46 \times 10^{-15})$, central value $7.3 \times 10^{-17}$. Its share of the temperature power at $\ell = 10$ is $f_{10} = \kappa\,(G\mu)^{2}$ with $\kappa < 10^{13}$ for both string models, so, with the mirror copy doubling it, $f_{10} < 4.3 \times 10^{-17}$.
\item[(iv)] \emph{(Monopoles.)} Deposited monopoles are a pressureless gas with fluctuations of finite range, in the class of Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}, and are bounded in density by the flux limit of Fact \claimref{synthesis.imported-macro-monopole-flux-limit} (argued).
\end{enumerate}
So no topological defect network of the stored chain, formed after the descent or deposited by it, supplies more than $10^{-16}$ of the CMB temperature power at $\ell = 10$, an active source and not a primordial spectrum, so it is no source of the measured primordial spectrum; the third line of attack of the open problem is closed for the chain's defects. Sources outside the chain (global symmetries broken in the descended phase, sectors not in the store) are not covered.

## technical
The series' grand-unified chain breaks $SU(4) \times SU(2)_{L} \times SU(2)_{R}$ to the Standard Model in one step with the $(10,1,3)$. Topological defects of a breaking $G \to H$ are read from the homotopy of $G/H$: monopoles from $\pi_{2}$, strings from $\pi_{1}$. The store already has the monopoles. The new point is that the breaking leaves matter parity $(-1)^{3(B-L)}$ unbroken, and that this element, $(-1_{4}, 1, 1)$, is not in the connected part $SU(3) \times SU(2)_{L} \times U(1)_{Y}$ of the unbroken group: on the connected part the central elements have the same sign on $SU(4)$ and $SU(2)_{R}$, and matter parity has opposite signs. So $\pi_{1}(G/H) = \pi_{0}(H) \supseteq \mathbb{Z}_{2}$ and the chain has stable $\mathbb{Z}_{2}$ strings. Under Premise (R) the descent reheats below $7.3 \times 10^{8}$ GeV, under two percent of $v_{R}$, so, unless the chain's restoration temperature is below that, its symmetry is never restored after the descent and these defects can only be deposited; the electroweak and strong transitions make none. A deposited string network relaxes to scaling with tension set by $v_{R}$: $G\mu$ about $10^{-16}$, at most $1.5 \times 10^{-15}$, and its contribution to the CMB power is proportional to $(G\mu)^{2}$, below $10^{-16}$ of the measured temperature power at $\ell = 10$ even with the mirror copy. Deposited monopoles are a finite-range deposit, already covered. The open problem's third attack line, a defect or scaling network of the descended phase, is therefore closed for the defects of the stored chain.

## lay
When a symmetry of the forces breaks as the universe cools, it can leave behind defects: point-like monopoles, or long thin strings of trapped energy. Moving strings were once a candidate source for the ripples in the cosmic microwave background. The framework's unified theory does produce stable strings, as well as the monopoles already known. But the strings carry a tension set by an energy scale far below the one that would matter, so a network of them would contribute less than a ten-million-billionth of the ripples' strength. And in the framework's account, unless the symmetry returns at an unusually low temperature, the universe never got hot enough after its origin to remake these defects at all. Defects of this theory cannot explain the primordial ripples.

## one-liner
On the stored Pati-Salam chain the unbroken matter parity, the rotor $-1$ of $\mathrm{Spin}(6)$, lies outside the identity component of the stabiliser, so $\pi_{1}(G/H) \supseteq \mathbb{Z}_{2}$ (stable $\mathbb{Z}_{2}$ strings) besides the monopoles; under Premise (R) the descent reheats below $0.0176\,v_{R}$, so, unless the chain's restoration temperature is below that, these defects exist after the descent only if deposited, and a deposited network has $G\mu < 1.46 \times 10^{-15}$ and supplies $f_{10} < 4.3 \times 10^{-17}$ of the temperature power at $\ell = 10$: no defect network of the chain sources the primordial spectrum.
