def do_command(stacks, line):
    num = int(line.split(" ")[1])
    start = int(line.split(" ")[3]) - 1
    end = int(line.split(" ")[5]) - 1
    temp = []
    for i in range(num):
        temp.append(stacks[start].pop())
    temp.reverse()
    stacks[end].extend(temp)
    return stacks


def weird_split(line):
    temp = line.replace("[", "").replace("]", "").replace("\n", "").split(" ")
    final = []
    i = 0
    while i < len(temp):
        if temp[i] == "" and temp[i + 1] == "" and temp[i + 2] == "" and temp[i + 3] == "":
            i += 4
            final.append("")
        else:
            final.append(temp[i])
            i += 1
    return final


def print_final(stacks):
    for stack in stacks:
        print(stack[-1], end="")


def main():
    stacks = []
    for i in range(0, 9):
        stacks.append([])
    with open("input", "r") as f:
        is_top = True
        lines = f.readlines()
        i = 0
        while is_top:
            if lines[i] == " 1   2   3   4   5   6   7   8   9 \n":
                is_top = False
                i += 1
            else:
                line = weird_split(lines[i])
                for j in range(len(line)):
                    if line[j] != "":
                        stacks[j].append(line[j])
            i += 1
        for stack in stacks:
            stack.reverse()
        for i in range(i, len(lines)):
            stacks = do_command(stacks, lines[i].strip())
    print_final(stacks)

    # 536


if __name__ == "__main__":
    main()
