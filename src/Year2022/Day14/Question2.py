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
    for x, y in sand:
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
def put_sand(rocks, sand_loc, sand, fallen, sand_start):
    x, y = sand_loc
    if y > fallen + 1:
        sand.append((x, y - 1))
        return True
    if (x, y + 1) not in rocks and (x, y + 1) not in sand:
        return put_sand(rocks, (x, y + 1), sand, fallen, sand_start)

    if (x - 1, y + 1) not in sand and (x - 1, y + 1) not in rocks:
        return put_sand(rocks, (x - 1, y), sand, fallen, sand_start)

    if (x + 1, y + 1) not in sand and (x + 1, y + 1) not in rocks:
        return put_sand(rocks, (x + 1, y), sand, fallen, sand_start)

    if (x, y) not in rocks and (x, y) not in sand:
        if (x, y) == sand_start:
            return False
        sand.append((x, y))
        return True
    raise ValueError


def sandstone(rocks, sand, min_y, fallen):
    min_sandstone = [-1] * (fallen - min_y + 2)
    max_sandstone = [-1] * (fallen - min_y + 2)
    rock_removal = []
    for x, y in rocks:
        if y in range(min_y, fallen + 2):
            rock_removal.append((x, y))
            if x > max_sandstone[y - min_y]:
                max_sandstone[y - min_y] = x
            if x < min_sandstone[y - min_y] or min_sandstone[y - min_y] == -1:
                min_sandstone[y - min_y] = x
    sand_removal = []
    for x, y in sand:
        if y in range(min_y, fallen + 2):
            sand_removal.append((x, y))
            if x > max_sandstone[y - min_y]:
                max_sandstone[y - min_y] = x
            if x < min_sandstone[y - min_y] or min_sandstone[y - min_y] == -1:
                min_sandstone[y - min_y] = x
    for r in rock_removal:
        rocks.remove(r)
    for s in sand_removal:
        sand.remove(s)

    # is 3 blocks because my code doesn't handle corners well
    for y, x in enumerate(min_sandstone):
        rocks.append((x, y + min_y))
        rocks.append((x + 1, y + min_y))
        rocks.append((x + 2, y + min_y))
    for y, x in enumerate(max_sandstone):
        rocks.append((x, y + min_y))
        rocks.append((x - 1, y + min_y))
        rocks.append((x - 2, y + min_y))


def main():
    rock_paths = []
    with open("input", "r") as f:

        for line in f.readlines():
            rock_paths.append(read_coords(line))
    sand_start = (500, 0)
    sand = []
    rocks = expand_rocks(rock_paths)
    fallen = print_data(rocks, sand_start, sand)
    put_sand(rocks, sand_start, sand, fallen, sand_start)
    for i in range(30000):
        if not put_sand(rocks, sand_start, sand, fallen, sand_start):
            print(i + 2)
            return
        if i % 1000 == 0 and i != 0:
            j = i // 1000
            print(j)
            print_data(rocks, sand_start, sand)
            k = [150, 158, 119, 119, 119, 138, 130, 88, 76, 75, 95, 90, 85, 68, 44, 43, 31, 61, 57, 53, 50, 48, 54, 50,
                 10, 7, 4]  # these values are came up with via looking at the printed image, code is not automated.
            if j - 1 < len(k):
                sandstone(rocks, sand, k[j - 1], fallen)


if __name__ == "__main__":
    main()

# 27324
