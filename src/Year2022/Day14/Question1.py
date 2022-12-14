def read_coords(line):
    coords = []
    for coord in line.split("->"):
        x, y = coord.split(",")
        coords.append((int(x), int(y)))
    return coords


def expand_rocks(rock_path):
    rocks = []
    for path in rock_path:
        x0, y0 = path[0]
        for x1, y1 in path[1:]:
            x, y = min(x0, x1), min(y0, y1)
            while x != max(x0, x1) or y != max(y0, y1):
                if (x, y) not in rocks:
                    rocks.append((x, y))
                if x != max(x0, x1):
                    x += 1
                if y != max(y0, y1):
                    y += 1
            if (x, y) not in rocks:
                rocks.append((x, y))
            x0, y0 = x1, y1
    return rocks


def print_data(rocks, sand_start, sand):
    min_x, min_y = sand_start
    max_x, max_y = sand_start
    for x, y in rocks:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    for y in range(min_y, max_y + 1):
        print(y, end=" ")
        for x in range(min_x, max_x + 1):
            if (x, y) in rocks:
                print("\033[1;31m#", end=" ")
            elif (x, y) == sand_start:
                print("\033[1;32m+", end=" ")
            elif (x, y) in sand:
                print("\033[1;33mo", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
    return max_y


# Technically can go through corners
def put_sand(rocks, sand_loc, sand, fallen):
    x, y = sand_loc
    if y > fallen:
        return False
    if (x, y + 1) not in rocks and (x, y + 1) not in sand:
        return put_sand(rocks, (x, y + 1), sand, fallen)

    if (x - 1, y + 1) not in sand and (x - 1, y + 1) not in rocks:
        return put_sand(rocks, (x - 1, y), sand, fallen)

    if (x + 1, y + 1) not in sand and (x + 1, y + 1) not in rocks:
        return put_sand(rocks, (x + 1, y), sand, fallen)

    if (x, y) not in rocks and (x, y) not in sand:
        sand.append((x, y))
        return True
    raise ValueError


def main():
    rock_paths = []
    with open("input", "r") as f:

        for line in f.readlines():
            rock_paths.append(read_coords(line))
    sand_start = (500, 0)
    sand = []
    rocks = expand_rocks(rock_paths)
    fallen = print_data(rocks, sand_start, sand)
    i = 0
    while put_sand(rocks, sand_start, sand, fallen):
        # print_data(rocks, sand_start, sand)
        i += 1
    print(i)


if __name__ == "__main__":
    main()

# 512, 644
