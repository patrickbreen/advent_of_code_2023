# Part 1
lines = open("day5_input.txt", "r").readlines()

ans1 = 0
rules = dict()
blank_line_ind = 0
for i, line in enumerate(lines):
    line = line.strip()
    if line == "":
        blank_line_ind = i
        break
    a, b = [int(x) for x in line.split("|")]
    if a in rules:
        rules[a].append(b)
    else:
        rules[a] = []

print(rules)

for i in range(blank_line_ind+1, len(lines)):
    line = lines[i].strip()

    l = [int(x) for x in line.split(",")]

    order = {x: i for i, x in enumerate(l)}
    

    if all([x not in rules or all([r not in order or order[x] < order[r] for r in rules[x]]) for x in l]):
        mid = int((len(l) -1)/2)
        print(l, len(l), mid)
        ans1 += l[mid]

ans2 = 0





print("Part1", ans1)


# Part 2
# skipping part 2 :(
ans2 = 0



print("Part2", ans2)