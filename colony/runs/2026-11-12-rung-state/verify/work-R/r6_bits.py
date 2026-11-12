"""Candidates C4/E4: reading unread rungs (uniform weight 2^-k on k rungs) with a deterministic rule.
(a) With a fixed finite number k of rungs read, every outcome probability is j/2^k: 9/25 is never exact.
(b) With the sequential rule 'read rungs until the binary expansion of 9/25 is decided', the outcome has
    probability exactly 9/25 in the limit, the read terminates with probability 1, P(read > k) = 2^-k,
    and the expected number of rungs read is 2. Exact enumeration for k <= 14."""
from fractions import Fraction as F
target = F(9, 25)
# (a)
print("(a) 9/25 dyadic? denominator 25 is not a power of 2:", target.denominator & (target.denominator - 1) != 0)
# binary digits of 9/25
digs, r = [], target
for _ in range(40):
    r *= 2
    d = int(r >= 1); digs.append(d); r -= d
period = next(p for p in range(1, 21) if digs[:20] == digs[p:p + 20])
print("    binary expansion of 9/25:", "0." + "".join(map(str, digs[:24])) + "...", "period", period)
# (b) enumerate all k-bit strings u; decided at step j if u_1..u_j differs from the digits of 9/25 at j
for k in (2, 4, 8, 12, 14):
    yes = no = undecided = 0
    for u in range(2 ** k):
        bits = [(u >> (k - 1 - i)) & 1 for i in range(k)]
        res = None
        for i in range(k):
            if bits[i] != digs[i]:
                res = bits[i] < digs[i]          # uniform U < 9/25 iff first differing bit is smaller
                break
        if res is None:
            undecided += 1
        elif res:
            yes += 1
        else:
            no += 1
    print(f"    k={k:2d}: P(yes decided) = {F(yes, 2**k)}, P(undecided) = {F(undecided, 2**k)},"
          f" |9/25 - P(yes decided)| <= P(undecided): {abs(target - F(yes, 2**k)) <= F(undecided, 2**k)}")
print("    expected rungs read = sum_{k>=0} P(read > k) = sum 2^-k = 2")
