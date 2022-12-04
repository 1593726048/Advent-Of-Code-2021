def recursive_loop(verticies: dict, list_cur: list):
    total = 0
    if list_cur[-1] == "end":
        print(list_cur)
        return 1
    for point in verticies[list_cur[-1]]:
        if ord(point[0]) in range(ord("A"), ord("Z")+1) or point not in list_cur:
            cc=[]
            for p in list_cur:
                cc.append(p)
            cc.append(point)
            total += recursive_loop(verticies, cc)
    return total


def answer(input_file_name):
    verticies = {}
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    for line in lines:
        part1 = line.split("-")[0].strip()
        part2 = line.split("-")[1].strip()
        if part1 in verticies.keys():
            verticies[part1].append(part2)
        else:
            verticies[part1] = [part2, ]

        if part2 in verticies.keys():
            verticies[part2].append(part1)
        else:
            verticies[part2] = [part1, ]
    return recursive_loop(verticies, ["start"])

print(answer("input.txt"))

#407
#4691