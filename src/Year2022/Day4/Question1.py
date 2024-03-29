def get_values(line):
    elves = []
    for i in line.split(","):
        ln = []
        for j in i.split("-"):
            ln.append(int(j))
        elves.append(ln)
    return elves


def compare_elves(elves):
    if elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]:
        return True
    if elves[1][0] >= elves[0][0] and elves[1][1] <= elves[0][1]:
        return True
    return False


def main():
    total=0
    with open("input", "r") as f:
        for line in f.readlines():
            elves = get_values(line)
            if compare_elves(elves):
                total += 1
    print(total)

    # 536


if __name__ == "__main__":
    main()
