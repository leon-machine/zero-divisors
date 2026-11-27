from dev import *
import cProfile, pstats
cProfile.run("ck.check_pairing_with_a_displacement_is_the_field_equation_plus_a_divergence()", "/tmp/corner.prof")
p = pstats.Stats("/tmp/corner.prof"); p.sort_stats("cumulative").print_stats(18)
