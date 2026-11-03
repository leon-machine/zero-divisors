---
id: simulations.imported-milky-ways-mass-budget
kind: claim
version: 1
title: 'Imported: the Milky Way''s mass budget'
status: imported
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
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
  source: authorship disclosure of T14b, deposited version
review: typed
imported_from:
- citation: J. Bovy and H.-W. Rix, A direct dynamical measurement of the Milky Way's disk surface density
    profile, disk scale length, and dark matter profile at 4 kpc $lesssim R lesssim$ 9 kpc, Astrophys.
    J. 779 (2013) 115.
  key: BovyRix2013
- citation: C. F. McKee, A. Parravano and D. J. Hollenbach, Stars, gas, and dark matter in the solar neighborhood,
    Astrophys. J. 814 (2015) 13.
  key: McKee2015
- citation: A. Widmark, C. F. P. Laporte, P. F. de Salas and G. Monari, Weighing the Galactic disk using
    phase-space spirals. II. Most stringent constraints on a thin dark disk using Gaia EDR3, Astron. Astrophys.
    653 (2021) A86.
  key: Widmark2021
- citation: 'M. Portail, O. Gerhard, C. Wegg and M. Ness, Dynamical modelling of the galactic bulge and
    bar: the Milky Way''s pattern speed, stellar and dark matter mass distribution, Mon. Not. R. Astron.
    Soc. 465 (2017) 1621.'
  key: Portail2017
- citation: J.-S. Roux and J. M. Cline, Constraining galactic structures of mirror dark matter, Phys.
    Rev. D 102 (2020) 063518.
  key: RouxCline2020
locators:
  paper: T14b
  number: Fact 2.6
  label: fact:mw
  line: 122
extraction:
  typing:
    by: ai-typing-pass
    note: Imported observational fact; levels only, no edges to review.
  env: fact
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - dark-tower-matter.mirror-against-record (motivated_by)
    added_about: []
    verdict: connected
    note: Observational import; lineage from the Galaxy observation and now from the T14c mirror-against-record
      observation, which confronts the same bounds.
---

## formal
At the Sun the total surface density within $1.1$ kpc of the plane is $68 \pm 4\ \Msun\,\mathrm{pc^{-2}}$, of which stars and stellar remnants contribute $38 \pm 4$ dynamically \cite{BovyRix2013}; counted, stars and remnants are $33.4 \pm 3$ and gas $13.7 \pm 1.6$, a total of $47.1 \pm 3.4$ \cite{McKee2015}. A thin dark disk is bounded at $95$ percent by $4.56$ ($h \le 50$ pc) and $5.59\ \Msun\,\mathrm{pc^{-2}}$ ($h = 100$ pc), with $68$ percent bounds $2.17$ and $2.71$ \cite{Widmark2021}. The bulge region holds a dynamical mass of $(1.85 \pm 0.05) \times 10^{10}\ \Msun$ with a dark fraction of $17 \pm 2$ percent \cite{Portail2017}. A mirror analysis bounds the excess bulge mass, dynamical minus photometric, by $0.83 \times 10^{10}\ \Msun$ at $2\sigma$, and finds $\Omega_{b'} \lesssim 0.8\,\Omega_{b}$ at low mirror temperature \cite{RouxCline2020}.

## technical
At the Sun the total surface density within $1.1$ kpc of the Galactic plane is $68 \pm 4\ \Msun\,\mathrm{pc^{-2}}$, of which stars and stellar remnants contribute $38 \pm 4$ dynamically; direct counts give $33.4 \pm 3$ in stars and remnants and $13.7 \pm 1.6$ in gas, a total of $47.1 \pm 3.4$. A thin dark disk is bounded at $95$ percent by $4.56\ \Msun\,\mathrm{pc^{-2}}$ for scale height $h \le 50$ pc and $5.59$ for $h = 100$ pc.

The bulge region has a dynamical mass of $(1.85 \pm 0.05) \times 10^{10}\ \Msun$, $17 \pm 2$ percent of it dark. A mirror-matter analysis bounds the excess of dynamical over photometric bulge mass by $0.83 \times 10^{10}\ \Msun$ at $2\sigma$ and finds $\Omega_{b'} \lesssim 0.8\,\Omega_{b}$ at low mirror temperature.

## lay
The Milky Way's disk near the Sun and its central bulge can be weighed both from the motions of stars and by counting stars and gas. The two methods leave little room for extra hidden matter concentrated in a thin disk or in the bulge. Any form of dark matter that cools and settles like ordinary gas must fit inside that small margin.

## one-liner
Mass measurements of the Milky Way bound a thin dark disk at the Sun at $4.56$ to $5.59\ \Msun\,\mathrm{pc^{-2}}$ ($95$ percent) and put the bulge's dark fraction at $17 \pm 2$ percent.
