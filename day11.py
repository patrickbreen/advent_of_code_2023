lines = [line.strip() for line in open("day11_input.txt", "r").readlines()]

# lines = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....""".split("\n")


expansion_factor = 1000000

# expand universe by columns
expand_these_columns = []
for col in range(len(lines[0])):
    expand_these_columns.append(all([lines[i][col] == "." for i in range(len(lines))]))

# expand universe by rows
expand_these_rows = []
for line in lines:
    expand_these_rows.append(all([c == "." for c in line]))

def make_grid(expand_these):
    grid = []
    for i in range(len(expand_these)):
        row = []
        for j in range(len(expand_these)):
            if j>i:
                row.append(sum([elem == True for elem in expand_these[i:j]]))
            else:
                row.append(sum([elem == True for elem in expand_these[i:j:-1]]))
        grid.append(row)
    return grid

cols_grid = make_grid(expand_these_columns)
rows_grid = make_grid(expand_these_rows)

print("expand_these_columns:", expand_these_columns)
print("expand_these_rows:", expand_these_rows)
print("cols_grid:", cols_grid)
print("rows_grid:", rows_grid)

# for each galaxy1, for each galaxy 2, calculate distance using math, then sum those
coords = []
for i, line in enumerate(lines):
    for j, elem in enumerate(line):
        if elem == "#":
            coords.append((i,j))

s = 0
for a in coords:
    for b in coords:
        if a != b:
            s += abs(b[0]-a[0]) - rows_grid[b[0]][a[0]] + expansion_factor * rows_grid[b[0]][a[0]]
            s += abs(b[1]-a[1]) - cols_grid[b[1]][a[1]] + expansion_factor * cols_grid[b[1]][a[1]]
print("sum shortest path:", s/2)


