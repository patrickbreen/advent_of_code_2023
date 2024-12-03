# Part 1
s = open("day3_input.txt", "r").read().strip()

import re
pattern = r"mul\((\d+),(\d+)\)"

matches = re.finditer(pattern, s)

ans1 = 0
l = 0
for match in matches:
    ans1 += int(match.group(1)) * int(match.group(2))
    print(match.groups())
    l += 1

print("Part1", ans1)


# Part 2
pattern = r"mul\((\d+),(\d+)\)"

remove_middle_pattern = r"don't\(\)[\s\S]*?do\(\)"
removed_middle = s

while bool(re.search(remove_middle_pattern, removed_middle)):
    removed_middle = "".join(re.split(remove_middle_pattern, removed_middle))
removed_middle_and_end = re.sub(r"don't\(\)[\s\S]*$", "", removed_middle)
matches = re.finditer(pattern, removed_middle_and_end)

ans2 = 0
l = 0
for match in matches:
    ans2 += int(match.group(1)) * int(match.group(2))
    print(match.groups())
    l += 1

print("Part2", ans2)