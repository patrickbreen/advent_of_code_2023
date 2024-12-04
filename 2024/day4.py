# Part 1
lines = open("day4_input.txt", "r").readlines()
lines = [l.strip() for l in lines]

l = len(lines)
w = len(lines[0])


ans1 = 0
xcoords = set()
mcoords = set()
acoords = set()
scoords = set()

# find coordinates of all 'X'

for i in range(l):
    for j in range(w):
        if 'X' == lines[i][j]:
            xcoords.add((i, j))
        if 'M' == lines[i][j]:
            mcoords.add((i, j))
        if 'A' == lines[i][j]:
            acoords.add((i, j))
        if 'S' == lines[i][j]:
            scoords.add((i, j))

# for each 'X' coordinate, BFS in each possible direction for 'XMAS
for i, j in xcoords:
    # forward
    if (i+1,j) in mcoords and (i+2,j) in acoords and (i+3,j) in scoords:
        ans1 += 1
    # backward
    if (i-1,j) in mcoords and (i-2,j) in acoords and (i-3,j) in scoords:
        ans1 += 1
    # up
    if (i,j+1) in mcoords and (i,j+2) in acoords and (i,j+3) in scoords:
        ans1 += 1
    # down
    if (i,j-1) in mcoords and (i,j-2) in acoords and (i,j-3) in scoords:
        ans1 += 1

    # plus plus
    if (i+1,j+1) in mcoords and (i+2,j+2) in acoords and (i+3,j+3) in scoords:
        ans1 += 1
    # plus minus
    if (i+1,j-1) in mcoords and (i+2,j-2) in acoords and (i+3,j-3) in scoords:
        ans1 += 1
    # minus plus
    if (i-1,j+1) in mcoords and (i-2,j+2) in acoords and (i-3,j+3) in scoords:
        ans1 += 1
    # minus minus
    if (i-1,j-1) in mcoords and (i-2,j-2) in acoords and (i-3,j-3) in scoords:
        ans1 += 1


print("Part1", ans1)


# Part 2
ans2 = 0

# for each 'X' coordinate, BFS in each possible direction for 'XMAS
for i, j in acoords:
    right_to_left = ((i-1,j-1) in mcoords and (i+1,j+1) in scoords) or ((i-1,j-1) in scoords and (i+1,j+1) in mcoords)
    left_to_right = ((i-1,j+1) in mcoords and (i+1,j-1) in scoords) or ((i-1,j+1) in scoords and (i+1,j-1) in mcoords)
    if right_to_left and left_to_right:
        ans2 += 1


print("Part2", ans2)