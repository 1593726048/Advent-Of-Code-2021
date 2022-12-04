def print_g(g):
    for val in g:
        if val == 0:
            print(" ", end="")
        else:
            print("#", end="")
    print()


def flip(point_val, flip_val):
    dif = point_val - flip_val
    return flip_val - dif


def flipOnX(points, val):
    npoints = []
    for point in points:
        if point[0] <= val:
            npoints.append(point)
        else:
            npoints.append((flip(point[0], val), point[1]))
    return npoints


def flipOnY(points, val):
    npoints = []
    for point in points:
        if point[1] <= val:
            npoints.append(point)
        else:
            npoints.append((point[0], flip(point[1], val)))
    return npoints


def answer(input_file_name):
    points = []
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    i = 0
    while lines[i].strip() != "":
        points.append((int(lines[i].strip().split(",")[0]), int(lines[i].strip().split(",")[1])))
        i += 1
    i += 1
    lowest_x = 10000000
    lowest_y = 10000000
    for line in lines[i:]:
        if "x" in line:
            points = flipOnX(points, int(line.split("=")[1]))
            if lowest_x > int(line.split("=")[1]):
                lowest_x = int(line.split("=")[1])
        if "y" in line:
            points = flipOnY(points, int(line.split("=")[1]))
            if lowest_y > int(line.split("=")[1]):
                lowest_y = int(line.split("=")[1])
    npoints = []
    for point in points:
        if point not in npoints:
            npoints.append(point)
    print(npoints)
    print(lowest_x)
    print(lowest_y)
    ghraph = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, ],
    ]
    for p in npoints:
        print()
        ghraph[p[1]][p[0]] = 1
    for g in ghraph:
        print_g(g)
    print("\n\n")
    print(ghraph)
    return len(npoints)


print(answer("input.txt"))
# 151
