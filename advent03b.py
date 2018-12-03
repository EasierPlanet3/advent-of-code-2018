from collections import Counter
from itertools import product
import re
import time

def double_range(x, y, dx, dy):
    return product(range(x,x+dx),range(y,y+dy))

start = time.time()

with open("advent03.txt") as f:
    data = f.read().split('\n')

pattern = re.compile("#\d+ @ (\d+),(\d+): (\d+)x(\d+)", re.ASCII)

count = Counter()
atlas = list()

for s in data:
    datum = tuple(int(n) for n in pattern.match(s).groups())
    count.update(double_range(*datum))
    atlas.append(datum) 

print(sum(1 for t in count if count[t] >= 2))

for num, t in enumerate(atlas):
    if all(count[dt] == 1 for dt in double_range(*t)):
        print(num+1)
        break

print("----------{:.3f} seconds----------".format(time.time() - start))




    






