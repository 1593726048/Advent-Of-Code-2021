class Pipe:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.neighbors = []
        self.x = x
        self.y = y

    def __repr__(self):
        return self.symbol


class FalsePipe:
    def __init__(self, barrier):
        self.barrier = barrier
        self.neighbors = []

    def __repr__(self):
        return "+" if self.barrier else " "


def main():
    grid = []
    pipes = []
    checking_pipes = []
    non_enclosed = []
    with open("input", "r") as f:
        lines = f.readlines()
        for x, line in enumerate(lines):
            grid_line = []
            grid.append(grid_line)
            for y, char in enumerate(line.strip()):
                if char != ".":
                    pipe = Pipe(char, x, y)
                    grid_line.append(pipe)
                    pipes.append(pipe)
                    if (char == "-" or char == "7" or char == "J" or char == "S") and y != 0:
                        p = grid[x][y - 1]
                        if p.symbol in ["-", "L", "F", "S"]:
                            p.neighbors.append(pipe)
                            pipe.neighbors.append(p)

                    if (char == "|" or char == "L" or char == "J" or char == "S") and x != 0:
                        p = grid[x - 1][y]
                        if p.symbol in ["F", "7", "|", "S"]:
                            p.neighbors.append(pipe)
                            pipe.neighbors.append(p)
                    if char == "S":
                        checking_pipes = [pipe]

                else:
                    pipe = Pipe(char, x, y)
                    if y == len(line.strip()) - 1 or y == 0 or x == 0 or x == len(lines) - 1:
                        non_enclosed.append(pipe)
                    grid_line.append(pipe)
                    if y != 0:
                        p = grid[x][y - 1]
                        if p.symbol == ".":
                            p.neighbors.append(pipe)
                            pipe.neighbors.append(p)
                    if x != 0:
                        p = grid[x - 1][y]
                        if p.symbol == ".":
                            p.neighbors.append(pipe)
                            pipe.neighbors.append(p)

    for grid_line in grid:
        print(grid_line)

    already_searched = []
    already_searched.extend(checking_pipes)
    new_pipes = []
    while checking_pipes:
        for pipe in checking_pipes:
            for p in pipe.neighbors:
                if p not in already_searched and p not in new_pipes:
                    new_pipes.append(p)
        already_searched.extend(new_pipes)
        checking_pipes = new_pipes
        new_pipes = []


    for pipe in pipes:
        if pipe not in already_searched:
            pipe.symbol = "."

    for x, grid_line in enumerate(grid):
        for y, pipe in enumerate(grid_line):
            if pipe.symbol == ".":
                if x != 0:
                    p = grid[x - 1][y]
                    if p.symbol == "." and p not in pipe.neighbors:
                        pipe.neighbors.append(p)
                        p.neighbors.append(p)
                if y != len(grid_line) - 1:
                    p = grid[x][y + 1]
                    if p.symbol == "." and p not in pipe.neighbors:
                        pipe.neighbors.append(p)
                        p.neighbors.append(p)
                if y != 0:
                    p = grid[x][y - 1]
                    if p.symbol == "." and p not in pipe.neighbors:
                        pipe.neighbors.append(p)
                        p.neighbors.append(p)
                if x != len(grid) - 1:
                    p = grid[x + 1][y]
                    if p.symbol == "." and p not in pipe.neighbors:
                        pipe.neighbors.append(p)
                        p.neighbors.append(p)

    new_grid = []
    for x, grid_line in enumerate(grid):
        cur_grid_line = []
        next_grid_line = []
        for y, pipe in enumerate(grid_line):
            cur_grid_line.append(pipe)
            if y != len(grid_line) - 1:
                cur_grid_line.append(FalsePipe(grid[x][y + 1] in pipe.neighbors and pipe.symbol != "."))
            if x != len(grid) - 1:
                next_grid_line.append(FalsePipe(grid[x + 1][y] in pipe.neighbors and pipe.symbol != "."))
            next_grid_line.append(FalsePipe(False))
        new_grid.append(cur_grid_line)
        new_grid.append(next_grid_line)

    for x, grid_line in enumerate(new_grid[:-2]):
        for y, pipe in enumerate(grid_line[:-2]):
            if isinstance(pipe, FalsePipe) or pipe.symbol == ".":
                p = new_grid[x + 1][y]
                if (isinstance(p, FalsePipe) and not p.barrier) or (isinstance(p, Pipe) and p.symbol == "."):
                    pipe.neighbors.append(p)
                    p.neighbors.append(pipe)
                p = new_grid[x][y + 1]
                if (isinstance(p, FalsePipe) and not p.barrier) or (isinstance(p, Pipe) and p.symbol == "."):
                    pipe.neighbors.append(p)
                    p.neighbors.append(pipe)

    new_pipes = []
    for pipe in new_grid[0]:
        if isinstance(pipe, Pipe) and pipe.symbol == "." and pipe not in non_enclosed:
            non_enclosed.append(pipe)
    for pipe in new_grid[-1]:
        if isinstance(pipe, Pipe) and pipe.symbol == "." and pipe not in non_enclosed:
            non_enclosed.append(pipe)
    for line in new_grid:
        pipe = line[0]
        if isinstance(pipe, Pipe) and pipe.symbol == "." and pipe not in non_enclosed:
            non_enclosed.append(pipe)
        pipe = line[-1]
        if isinstance(pipe, Pipe) and pipe.symbol == "." and pipe not in non_enclosed:
            non_enclosed.append(pipe)
    checking_pipes = non_enclosed
    old_search = already_searched[:]
    already_searched.extend(checking_pipes)
    while checking_pipes:
        for pipe in checking_pipes:
            for p in pipe.neighbors:
                if p not in already_searched and p not in new_pipes:
                    new_pipes.append(p)
        already_searched.extend(new_pipes)
        checking_pipes = new_pipes
        new_pipes = []
    print()

    num = 0
    for grid_line in grid:
        for val in grid_line:
            if val.symbol == "." and val not in already_searched:
                num += 1
                val.symbol = "I"
    for grid_line in new_grid:
        for val in grid_line:
            if isinstance(val, Pipe) and val.symbol == "I":
                print(f"\033[91m{val}\033[0m", end=" ")
            elif val in old_search:
                print(f"\033[92m{val}\033[0m", end=" ")
            else:
                print(val, end=" ")

        print()
        # print(grid_line)
    print(num)


#


if __name__ == "__main__":
    main()

# 53
# 53
