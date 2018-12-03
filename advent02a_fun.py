with open("advent02.txt") as f:
    data = f.read().split('\n')

def count_n_repeats(n, ss):
    if not ss: return 0
    return (1 if any(ss[0].count(c) == n for c in ss[0]) else 0) + count_n_repeats(n, ss[1:])

print(count_n_repeats(2, data)*count_n_repeats(3, data))
