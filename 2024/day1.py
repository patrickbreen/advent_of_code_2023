# Part 1
lines = open("day1_input.txt", "r").readlines()

a = []
b = []

for l in lines:
    x, y = [int(x) for x in l.strip().split("   ")]
    a.append(x)
    b.append(y)

ans1 = sum([abs(x-y) for x, y in zip(sorted(a), sorted(b))])

print("Part 1", ans1)


# Part 2
from collections import defaultdict
a = []
b = defaultdict(int)

for l in lines:
    x, y = [int(x) for x in l.strip().split("   ")]
    a.append(x)
    b[y] += 1

ans2 = sum([b[x] * x for x in a if x in b])
print("Part 2", ans2)