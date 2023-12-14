from numpy import transpose


def calc_mirror_v(grid):
    for i in range(1, len(grid)):
        end = min(i, len(grid) - i) + 1
        off_by = 0
        for j in range(1, end):
            if grid[i + j - 1] != grid[i - j]:
                for a, b in zip(grid[i + j - 1], grid[i - j]):
                    off_by += int(a != b)
                if off_by > 1:
                    continue
        if off_by == 1:
            return i


def calc_mirror_h(grid):
    new_grid = grid[:]
    return calc_mirror_v([list(n) for n in transpose(new_grid)])


def calc_smudge(grid):
    v = calc_mirror_v(grid)
    h = calc_mirror_h(grid)
    if v is None:
        for i, grid_line in enumerate(grid):
            for j, val in enumerate(grid_line):
                temp = "#"
                if grid_line[j] == "#":
                    temp = "."
                grid[i][j] = temp
                v = calc_mirror_v(grid)
                if v is not None:
                    return v * 100
                grid[i][j] = "#" if temp == "." else "."
        print("ALLL")
        return h

    if h is None:
        for i, grid_line in enumerate(grid):
            for j, val in enumerate(grid_line):
                temp = "#"
                if grid_line[j] == "#":
                    temp = "."
                grid[i][j] = temp
                h = calc_mirror_h(grid)
                if h is not None:
                    return h
                grid[i][j] = "#" if temp == "." else "."
        print("ALLL")
        return v * 100


def main():
    grids = []
    grid = []
    total = 0
    with open("input", "r") as f:

        for line in f.readlines():
            if line == "\n":
                grids.append(grid)
                grid = []
            else:
                grid_line = []
                for char in line.strip():
                    grid_line.append(char)
                grid.append(grid_line)
    grids.append(grid)
    for grid in grids:
        v = calc_mirror_v(grid)
        h = calc_mirror_h(grid)
        if v is not None:
            total += v * 100
        if h is not None:
            total += h
    print(total)


if __name__ == "__main__":
    main()

# 13250
