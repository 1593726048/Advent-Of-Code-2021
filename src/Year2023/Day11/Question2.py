class Galaxy:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.sy = y
        self.sx = x


def calc_distance(a, b):
    x = abs(a.x - b.x)
    y = abs(a.y - b.y)
    return x + y


def expand(galaxies):
    y_galaxies = []
    x_galaxies = []
    for galaxy in galaxies:
        if galaxy.x not in x_galaxies:
            x_galaxies.append(galaxy.x)
        if galaxy.y not in y_galaxies:
            y_galaxies.append(galaxy.y)
    y_not = []
    x_not = []
    for y in range(max(y_galaxies)):
        if y not in y_galaxies:
            y_not.append(y)
    for x in range(max(x_galaxies)):
        if x not in x_galaxies:
            x_not.append(x)
    for x in x_not:
        for galaxy in galaxies:
            if x < galaxy.sx:
                galaxy.x += 1000000 - 1
    for y in y_not:
        for galaxy in galaxies:
            if y < galaxy.sy:
                galaxy.y += 1000000 - 1


def main():
    galaxies = []
    with open("input", "r") as f:
        lines = f.readlines()
        for x, line in enumerate(lines):
            for y, char in enumerate(line):
                if char == "#":
                    galaxies.append(Galaxy(x, y))
        expand(galaxies)
        total = 0
        for i, a in enumerate(galaxies):
            for j, b in enumerate(galaxies[i + 1:]):
                total += calc_distance(a, b)
        print(total)


if __name__ == "__main__":
    main()
