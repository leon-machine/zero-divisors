---
id: dark-matter.imported-composition-simulated
kind: claim
version: 3
title: 'Imported: the composition simulated'
status: conjectured
region: dark-matter
subject: dark-matter
tags:
- halos-and-clusters
- mirror-sector
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
lineage:
  motivated_by:
  - dark-matter.imported-composition-simulated-external
  - simulations.confinement-scale-does-not-matter
  - simulations.effective-cross-section-sheet-matter
  - simulations.halo-shapes
  - simulations.merger
  - simulations.mirror-galaxy
locators:
  paper: T14
  number: Fact 7.32
  label: fact:simulated
  line: 1237
extraction:
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L4
    open_problem: op.small-findings
    note: 'The parenthetical cites T14''s own numbered refutation conditions, a list distinct from the series'' seventeen refutations (whose sixth is the internal ladder); it now says so.'
  source_formal: '\begin{enumerate}
\item[(i)] Quanta confined to a sheet scatter in two dimensions. Per unit of the mass gravity sees, the three-dimensional towers'' matter at composite strength has a cross-section of $10^{8}$ to $10^{13}\ \mathrm{cm^{2}\,g^{-1}}$ in galaxy clusters, eight to thirteen orders of magnitude above the galaxy-cluster bounds, whatever its confinement scale: it is a fluid whose pressure acts within its sheets.
\item[(ii)] In the merger, with the three-dimensional towers'' matter colliding, the subcluster''s sheet fluid and mirror gas are held back with its gas, and with randomly oriented sheets the subcluster has no separate lensing peak. With the odd towers'' matter collisionless, the subcluster keeps a lensing peak on its galaxies with its gas $355$ kpc behind, and its mass-to-light change, $0.82$, is consistent with the observed ratio $0.84 \pm 0.07$ \cite{Randall2008}, as cold dark matter''s is; the cost is a puffier subcluster, with lensing contrast $4.7$ against cold dark matter''s $7.5$.
\item[(ii$''$)] The exchanged assignment of Remark \ref{rem:forms}, with the three-dimensional towers'' matter colliding, fails in the same way: lensing contrast $1.1$, the subcluster''s own mass $0.27$ of cold dark matter''s, and galaxy-cluster ellipticity $0.49$ of cold dark matter''s. With the mirror settled it is marginal, contrast $2.7$ and mass $0.44$.
\item[(iii)] In the assembled galaxy clusters, two seeds each, the projected ellipticity is $0.43$ of cold dark matter''s with the three-dimensional towers colliding, both seeds below cold dark matter''s, the sheet fluid forming a cored component rounder than the collisionless dark matter; with the odd towers'' matter collisionless it is $0.77$, rounder, with one seed inside the range of the cold-dark-matter seeds, so not excluded.
\item[(iv)] In the Milky Way, the proton-only branch is excluded at the Sun. On the burning branch a helium mirror, cooling slowly and with helium-star supernovae giving $3.6$ to $7.3$ times our feedback per unit mass formed, fits the $2\sigma$ room for extra disk-like mass at the Sun under some normalisations of its gas, and fits the bulge only if the bulge holds over twice the mirror''s proportional share of its dark mass. With the consistent yield, extra disk-like mass at the Sun below $5\ M_{\odot}\,\mathrm{pc^{-2}}$, or disk-like dark mass in the bulge volume below $1.7 \times 10^{9}\ M_{\odot}$, would exclude it. Neither has yet been made (Section \ref{sec:premises}, refutation 6).
\end{enumerate}
\emph{Provenance:} \cite[Prop.~3.1, Cor.~3.4, Obs.~7.1, 7.2, 9.1, Tables~3, 4]{ButlerT14b}; the observations compared are those of \cite{Clowe2006, Randall2008}.'
  env: fact
  context_refs:
  - simulations.confinement-scale-does-not-matter
  - simulations.effective-cross-section-sheet-matter
  - simulations.halo-shapes
  - simulations.merger
  - simulations.mirror-galaxy
  unresolved_refs:
  - rem:forms
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Made conjectured: the fact restates simulation outputs that the store holds as conjectured
      observations (halo shapes, the merger, the mirror galaxy), so it cannot be proved; its former premises
      are now its motivated_by, and the derivation, checked_by and proof file (which only repeated the
      statement) were removed. Levels pass: the lay and one-liner now keep the composite-strength qualifier
      and the helium mirror''s two conditions (some gas normalisations; the bulge share), and the lay
      adds the puffier-subcluster cost.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: T14's restatement of the T14b simulation outputs, kept conjectured with lineage to them; nothing
      derived relies on it and no definition in the store bears on it.
---

## formal
\begin{enumerate}
\item[(i)] Quanta confined to a sheet scatter in two dimensions. Per unit of the mass gravity sees, the three-dimensional towers' matter at composite strength has a cross-section of $10^{8}$ to $10^{13}\ \mathrm{cm^{2}\,g^{-1}}$ in galaxy clusters, eight to thirteen orders of magnitude above the galaxy-cluster bounds, whatever its confinement scale: it is a fluid whose pressure acts within its sheets.
\item[(ii)] In the merger, with the three-dimensional towers' matter colliding, the subcluster's sheet fluid and mirror gas are held back with its gas, and with randomly oriented sheets the subcluster has no separate lensing peak. With the odd towers' matter collisionless, the subcluster keeps a lensing peak on its galaxies with its gas $355$ kpc behind, and its mass-to-light change, $0.82$, is consistent with the observed ratio $0.84 \pm 0.07$ \cite{Randall2008}, as cold dark matter's is; the cost is a puffier subcluster, with lensing contrast $4.7$ against cold dark matter's $7.5$.
\item[(ii$'$)] The exchanged assignment of Remark \ref{rem:forms}, with the three-dimensional towers' matter colliding, fails in the same way: lensing contrast $1.1$, the subcluster's own mass $0.27$ of cold dark matter's, and galaxy-cluster ellipticity $0.49$ of cold dark matter's. With the mirror settled it is marginal, contrast $2.7$ and mass $0.44$.
\item[(iii)] In the assembled galaxy clusters, two seeds each, the projected ellipticity is $0.43$ of cold dark matter's with the three-dimensional towers colliding, both seeds below cold dark matter's, the sheet fluid forming a cored component rounder than the collisionless dark matter; with the odd towers' matter collisionless it is $0.77$, rounder, with one seed inside the range of the cold-dark-matter seeds, so not excluded.
\item[(iv)] In the Milky Way, the proton-only branch is excluded at the Sun. On the burning branch a helium mirror, cooling slowly and with helium-star supernovae giving $3.6$ to $7.3$ times our feedback per unit mass formed, fits the $2\sigma$ room for extra disk-like mass at the Sun under some normalisations of its gas, and fits the bulge only if the bulge holds over twice the mirror's proportional share of its dark mass. With the consistent yield, extra disk-like mass at the Sun below $5\ M_{\odot}\,\mathrm{pc^{-2}}$, or disk-like dark mass in the bulge volume below $1.7 \times 10^{9}\ M_{\odot}$, would exclude it. Neither has yet been made (the dark-matter paper's own refutation condition 6, Section \ref{sec:premises}, not the series' sixth refutation).
\end{enumerate}
\emph{Provenance:} \cite[Prop.~3.1, Cor.~3.4, Obs.~7.1, 7.2, 9.1, Tables~3, 4]{ButlerT14b}; the observations compared are those of \cite{Clowe2006, Randall2008}.

## technical
This collects the simulation results for the dark towers' matter. Quanta confined to a sheet scatter in two dimensions, and per unit of the mass gravity sees the three-dimensional towers' matter at composite strength has a cross-section of $10^{8}$ to $10^{13}\ \cmg$ in galaxy clusters, eight to thirteen orders of magnitude above the cluster bounds whatever its confinement scale: it is a fluid whose pressure acts within its sheets. In the merging cluster, if that matter collides the subcluster has no separate lensing peak (and the exchanged assignment fails likewise, marginally with the mirror settled); if the odd towers' matter is collisionless the subcluster keeps a lensing peak with its gas $355$ kpc behind and a mass-to-light change of $0.82$, consistent with the observed $0.84 \pm 0.07$, at the cost of lensing contrast $4.7$ against cold dark matter's $7.5$.

In assembled clusters the projected ellipticity is $0.43$ of cold dark matter's with colliding sheet matter and $0.77$, not excluded, with the odd towers' matter collisionless. In the Milky Way the proton-only mirror branch is excluded at the Sun; on the burning branch a helium mirror fits the room for extra disk-like mass at the Sun under some gas normalisations and the bulge only if the bulge holds over twice the mirror's proportional share of its dark mass. With the consistent yield, a bound below $5\ \Msun\,\mathrm{pc^{-2}}$ on extra disk-like mass at the Sun, or below $1.7 \times 10^{9}\ \Msun$ on disk-like dark mass in the bulge, would exclude it.

## lay
Computer simulations test how the hidden worlds' matter would behave in colliding galaxy clusters and in our own galaxy. Matter confined to flat sheets, interacting at the strength the framework's composites would have, collides far too strongly to match what is seen, while collisionless matter from the odd-dimensional worlds reproduces the observed separation of mass and gas, at the cost of a somewhat puffier cluster. A mirror world made mostly of helium is still allowed in our galaxy, but only for some assumptions about its gas, and in the central bulge only if the mirror's matter there exceeds twice its proportional share of the dark mass; a somewhat sharper measurement of hidden disk-like mass near the Sun could rule it out.

## one-liner
In simulation, colliding sheet matter at composite strength fails the cluster merger and cluster shapes, collisionless odd-tower matter passes, the proton-only mirror is excluded at the Sun, and the helium mirror survives, under some gas normalisations and a heavy bulge share, pending a sharper local disk-mass bound.
