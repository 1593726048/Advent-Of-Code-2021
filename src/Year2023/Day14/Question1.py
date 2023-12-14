from numpy import transpose


def rocks_fall_everyone_dies(grid):
    for grid_line in grid:
        cur_rock = 0
        for i, val in enumerate(grid_line):
            if i == cur_rock and val in "#O":
                cur_rock += 1
            elif val == ".":
                pass
            elif val == "#":
                cur_rock = i + 1
            elif val == "O":
                grid_line[i] = "."
                grid_line[cur_rock] = "O"
                cur_rock += 1
    return grid

def calc_load(grid):
    total=0
    for i, grid_line in enumerate(grid[::-1]):
        for val in grid_line:
            if val=="O":
                total+=i+1
    return total


def print_grid(grid):
    for g in grid:
        print(g)
    print()


def main():
    grid = []
    with open("input", "r") as f:

        for line in f.readlines():
            grid_line = []
            for char in line.strip():
                grid_line.append(char)
            grid.append(grid_line)
    print_grid(transpose(grid))
    grid_new = transpose(rocks_fall_everyone_dies(transpose(grid)))
    print_grid(grid_new)
    print(calc_load(grid_new))


if __name__ == "__main__":
    main()

#
