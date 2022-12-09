def move_head(head, direction):
    if direction == "R":
        return head[0] + 1, head[1]
    if direction == "L":
        return head[0] - 1, head[1]

    if direction == "U":
        return head[0], head[1] + 1
    if direction == "D":
        return head[0], head[1] - 1


def move_tail(head, tail):
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return tail
    if head[0] == tail[0]:
        return tail[0], (tail[1] + head[1]) // 2
    if head[1] == tail[1]:
        return (tail[0] + head[0]) // 2, tail[1]
    x = tail[0]
    y = tail[1]
    if head[0] > x:
        x += 1
    else:
        x -= 1
    if head[1] > y:
        y += 1
    else:
        y -= 1
    return x, y


def move_tails(head, tails):
    new_tails = []
    new_tails.append(move_tail(head, tails[0]))
    for i in range(1, len(tails)):
        new_tails.append(move_tail(new_tails[i - 1], tails[i]))
    return new_tails


def print_graph(width, height, points):
    for i in range(height - 1, -height, -1):
        for j in range(-width, width):
            special = False
            for point in points:
                if point == (j, i):
                    special = True

            if special:
                print("P", end="")
            else:
                print(".", end="")
        print()
    print()


def main():
    all_tails = []
    head = (0, 0)
    tails = []
    for _ in range(9):
        tails.append((0, 0))
    with open("input", "r") as f:
        for line in f.readlines():
            direction, num = line.split(" ")
            for _ in range(int(num)):
                head = move_head(head, direction)
                tails = move_tails(head, tails)
                if tails[8] not in all_tails:
                    all_tails.append(tails[8])
            temp = tails.copy()
            temp.append(head)
    print(len(all_tails))


if __name__ == "__main__":
    main()

#
