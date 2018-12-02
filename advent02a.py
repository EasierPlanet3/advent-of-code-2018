from collections import Counter

with open("advent02.txt") as f:
    data = f.read().split('\n')

twos = 0
threes = 0

for s in data:
    count = Counter(s)
    twos += 1 if any(count[c] == 2 for c in count) else 0
    threes += 1 if any(count[c] == 3 for c in count) else 0

print(twos*threes)
