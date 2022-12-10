def check_line(lines, num_loops, x):
    if num_loops%40 in (x,x+1,x-1):
        lines[num_loops//40][num_loops%40]=True
    return lines


def noop(lines, num_loops, x):
    lines=check_line(lines, num_loops, x)
    return lines, num_loops + 1, x


def addx(lines, num, num_loops, x):
    lines=check_line(lines, num_loops, x)
    lines = check_line(lines, num_loops+1, x)
    x+=num
    return lines, num_loops + 2, x


def new_line():
    line = []
    for i in range(40):
        line.append(False)
    return line


def print_computer(lines):
    for line in lines:
        for i in range(len(line)):
            char = line[i]
            if char:
                print("\033[1;32m#", end="")
            else:
                print("\033[1;31m.", end="")
        print()


def main():
    x = 1
    loop_num = 0
    lines = []
    for i in range(0, 6):
        lines.append(new_line())
    with open("input", "r") as f:
        for command in f.readlines():
            print(x)
            if command.strip() == "noop":
                lines, loop_num, x = noop(lines, loop_num, x)
            else:
                lines, loop_num, x = addx(lines, int(command.split(" ")[1]), loop_num, x)
    total = 0
    print_computer(lines)
    print(total)


if __name__ == "__main__":
    main()


#
