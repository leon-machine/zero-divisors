# Brief for the resolve sweep (groups G1-G5)

You are a maintainer agent acting for Leon. LAB = /home/claude/phys-graph (branch ga-units-and-bridge-survey;
never commit, never spawn agents, never kill processes, at most one tp check at a time).
Read in this order:
1. colony/runs/2026-11-07-ga-units/RESOLVE.md: Leon's instruction (resolve every imaginary unit) and the unit
   principle U1-U6. It supersedes RULINGS.md R1 and the "what stays" parts of SWEEP.md.
2. colony/runs/2026-11-07-ga-units/core.md: the two core results and the exact signs to use
   (std-algebra.complexification-is-the-odd-extension, I5 and I7; synthesis.transverse-bivector-is-the-
   complex-unit-of-the-radial-atom, J = e2 e3 = I4 sigma, J K = I4/2, tau_t(v) = e^{-Jt} v, lambda = J t,
   KMS for tau_{J beta}). Cite them with \claimref where an entity now relies on the unit they establish
   (a mention, not a new uses edge, unless the proof uses their content as a step: then add a pinned uses edge;
   both hold given no postulate).
3. colony/runs/2026-11-07-ga-units/SWEEP.md: bookkeeping (version + 1 when the formal level or proofs change,
   at most one above the 8eef5a4 version: if the entity was already bumped in this pass, keep its version and
   add to its notes; credit entry for that version; an extraction note `maintainer_pass_resolve_units`; keep
   every file; no change of mathematics, links, statuses or ledgers).
4. store/conventions.md, "The imaginary units" (now with the unit principle).

Your group's entities: colony/runs/2026-11-07-ga-units/resolve_<G>.txt (id, folder, hit count, current
outside_ga kind); plain ids in ids_<G>.txt. For each: read it in full, decide each occurrence's unit by U1-U6
(what does the number multiply?), replace exactly, and remove the outside_ga declaration if no bare i remains
and the declaration was for i only (keep it, with its reason narrowed, if it also covers Pauli or Dirac
matrices, a cross product, or an imported quotation that U4 cannot restate). Imported Facts (U4): restate in
GA, move the source's form into extraction.source_formal (keep an existing one), add "the source writes i for
<unit>". Where one entity carries two units, say once which acts where; never identify I4, I5, I6, I7 or J.

Detector (both forms):
  python3 - <<'PY'
  import sys; sys.path.insert(0, '/home/claude/phys-graph')
  from tp import galang; from tp.model import load_store
  st = load_store('/home/claude/phys-graph/store')
  for eid in open('/home/claude/phys-graph/colony/runs/2026-11-07-ga-units/ids_<G>.txt').read().split():
      e = st.entities[eid]
      t = '\n'.join([e.levels.get(k) or '' for k in ('formal', 'technical', 'lay', 'one-liner')] + list((e.proofs or {}).values()))
      h = galang.bare_unit_hits(t)
      if h: print(eid, bool(galang.declared(e)), h[:6])
  PY
Read the texts too: the detector misses some forms.
Validation: python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | grep -F -f
colony/runs/2026-11-07-ga-units/ids_<G>.txt; fix every error or warning on your entities.
Report: colony/runs/2026-11-07-ga-units/resolve-<G>.md, one line per entity (old -> new version, unit chosen,
declaration removed or kept and why), then "Could not resolve" (U6, with the precise reason) and "Possible
errors found". Final reply: counts and the Could-not-resolve list.
