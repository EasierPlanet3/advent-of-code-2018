from itertools import combinations

with open("advent02.txt") as f:
    data = f.read().split('\n')

for s1, s2 in combinations(data, 2):
    delta = ''.join([s1[i] for i in range(len(s1)) if s1[i] == s2[i]])
    if len(delta) == len(s1) - 1:
        print(delta)
        break
