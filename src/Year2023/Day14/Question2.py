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

def cycle(grid):
    grid=transpose(rocks_fall_everyone_dies(transpose(grid)))
    grid = rocks_fall_everyone_dies(grid)
    grid = transpose(rocks_fall_everyone_dies(transpose(grid[::-1])))[::-1]
    grid = [g[::-1] for g in rocks_fall_everyone_dies( [g[::-1] for g in grid])]
    return [list(g) for g in grid]


def main():
    grid = []
    grid_forms={}
    with open("input", "r") as f:

        for line in f.readlines():
            grid_line = []
            for char in line.strip():
                grid_line.append(char)
            grid.append(grid_line)
    num=0
    for i in range(1000000000):

        grid=cycle(grid)
        if grid in grid_forms.values():
            for key in grid_forms:
                if grid_forms[key]==grid:
                    num=key
            break
        else:
            grid_forms[i]=grid
    print(num)
    print(i)
    print(i-num)
    num_extra=(1000000000 -i)% (i-num)-1
    for i in range(num_extra):
        grid=cycle(grid)

    print(calc_load(grid))
        #print_grid(grid)


if __name__ == "__main__":
    main()

#
