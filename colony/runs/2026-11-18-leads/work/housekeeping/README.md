# Housekeeping work files, run 2026-11-18-leads

- MIR_rerun_extended_grid_output.txt: output of the papers suite's `MIR/verify_MIR.py` (staged from the papers suite
  on 18 November 2026, unmodified apart from one line: the grid `XIS` gains 5.2e-4, 6.6e-4 and 8.1e-4). 24 checks,
  0 failures. The rows at the added values are the recomputation of clause (i) of
  dark-tower-matter.mirrors-composition at the floors restated on 18 November.
- CHECK_COS_rerun_extended_grid_output.txt: output of the suite's `CHECK_COS/check_mirror_entropy.py` with the same
  three values added to its loop.
- op-number-n.yaml: the open-problem entry for the cluster on the number N (survey row 10).
The scripts themselves are not copied into the lab (they need numpy and scipy and are the suite's files).
