# lines = [line.strip() for line in open("day11_input.txt", "r").readlines()]

lines = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")


expansion_factor = 2
expand_these_columns = [all([lines[i][col] == "." for i in range(len(lines))]) for col in range(len(lines[0]))]
expand_these_rows = [all([c == "." for c in line]) for line in lines]

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

cols_grid, rows_grid = make_grid(expand_these_columns), make_grid(expand_these_rows)
# for each galaxy 1, for each galaxy 2, calculate distance using math, then sum those
coords = [(i,j) for i, line in enumerate(lines) for j, elem in enumerate(line) if elem == "#"]

s = sum([
    (abs(b[0]-a[0]) - rows_grid[b[0]][a[0]] + expansion_factor * rows_grid[b[0]][a[0]] + \
    abs(b[1]-a[1]) - cols_grid[b[1]][a[1]] + expansion_factor * cols_grid[b[1]][a[1]]
) for a in coords for b in coords if a != b])
print("sum shortest path:", s/2)


