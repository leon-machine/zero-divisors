## What this changes

<!-- New claims, changed claims, new evidence, or toolkit changes. One result per folder,
store/<kind>/<id>/. For a correction, say what changed and why. -->

## Checklist

- [ ] The pull request adds or changes only result folders under `store/` (no `build/`, `site/`,
      `store/.tp-lock.json` or `store/.tp-layer4.json`; the maintainer updates those on merging)
- [ ] `python -m tp check --store store --keep-going` passes locally (the same checks run here)
- [ ] Every new or changed claim states `proposed_by` and `ai_involved` truthfully
- [ ] Every new claim has a `credit` list: your name as you want it shown, and the AI model,
      with its version, that drafted the proof or amendment (shown as you give it)
- [ ] Substantive edits (statement, derivations, status, evidence) bump `version`
- [ ] New claims have `subject`, and their levels are written or marked `pending`
- [ ] No new `assumes` edge or postulate unless a maintainer has agreed it
- [ ] I agree to the result being published under CC BY 4.0, credited as stated
