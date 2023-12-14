from numpy import transpose


def calc_mirror_v(grid):

    for i in range(1, len(grid) ):
        end = min(i, len(grid) - i)+1
        works = True
        for j in range(1, end):
            if grid[i + j-1] != grid[i - j]:
                works = False
                continue
        if works:
            return i


def calc_mirror_h(grid):
    new_grid = grid[:]
    return calc_mirror_v([list(n) for n in transpose(new_grid)])


def main():
    grids=[]
    grid = []
    total=0
    with open("input", "r") as f:

        for line in f.readlines():
            if line =="\n":
                grids.append(grid)
                grid=[]
            else:
                grid_line = []
                for char in line.strip():
                    grid_line.append(char)
                grid.append(grid_line)
    grids.append(grid)
    for grid in grids:
        v=calc_mirror_v(grid)
        h=calc_mirror_h(grid)
        if v is not None:
            total+=v*100
        if h is not None:
            total+=h
    print(total)


if __name__ == "__main__":
    main()
