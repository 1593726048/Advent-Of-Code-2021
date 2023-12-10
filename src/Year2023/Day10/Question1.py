class Pipe:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.neighbors = []
        self.x = x
        self.y = y

    def __repr__(self):
        return self.symbol



def main():
    grid = []
    pipes = []
    checking_pipes = []
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
                    grid_line.append(Pipe(".", x, y))


    for grid_line in grid:
        print(grid_line)

    already_searched = []
    already_searched.extend(checking_pipes)
    new_pipes=[]
    num=-1
    while checking_pipes:
        print(checking_pipes)
        num+=1
        for pipe in checking_pipes:
            for p in pipe.neighbors:
                if p not in already_searched and p not in new_pipes:
                    new_pipes.append(p)
        already_searched.extend(new_pipes)
        checking_pipes=new_pipes
        new_pipes=[]
    print(num)


if __name__ == "__main__":
    main()

#
