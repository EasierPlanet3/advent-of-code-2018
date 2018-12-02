import re
from time import clock

start = clock()

with open("advent01.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

index = 0
h = 0
seen = set()

while h not in seen:
    seen.add(h)
    h += data[index]
    index += 1
    if index == len(data): index = 0

print(h)
