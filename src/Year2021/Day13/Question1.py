def flip(point_val, flip_val):
    dif = point_val - flip_val
    return flip_val - dif


def flipOnX(points, val):
    print(val)
    npoints = []
    for point in points:
        if point[0] <= val:
            npoints.append(point)
        else:
            npoints.append((flip(point[0], val), point[1]))
    return npoints


def flipOnY(points, val):
    print(val)
    npoints = []
    for point in points:
        if point[1] <= val:
            npoints.append(point)
        else:
            npoints.append((point[0], flip(point[1], val)))
    return npoints


def answer(input_file_name):
    lowest_x = 0
    lowest_y = 0
    points = []
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    i = 0
    while lines[i].strip() != "":
        points.append((int(lines[i].strip().split(",")[0]),int(lines[i].strip().split(",")[1])))
        if lowest_x < int(lines[i].split(",")[0]):
            lowest_x = int(lines[i].split(",")[0])
        if lowest_y < int(lines[i].split(",")[1]):
            lowest_y = int(lines[i].split(",")[1])
        i += 1
    i += 1

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
        for p in npoints:
            print(p)
        print(lowest_x)
        print(lowest_y)
        return len(npoints)
    npoints=[]
    for point in points:
        if point not in npoints:
            npoints.append(point)
    print(npoints)
    print(lowest_x)
    print(lowest_y)

    return lowest_y*lowest_x-len(npoints)



print(answer("input.txt"))
#151
#584875