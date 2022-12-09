def move_head(head, direction):
    if direction == "R":
        return head[0] + 1, head[1]
    if direction == "L":
        return head[0] - 1, head[1]

    if direction == "U":
        return head[0], head[1] + 1
    if direction == "D":
        return head[0], head[1] - 1


def move_tail(head, tail, prev_head):
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return tail
    if head[0] == tail[0]:
        return tail[0], (tail[1] + head[1]) // 2
    if head[1] == tail[1]:
        return (tail[0] + head[0]) // 2, tail[1]
    return prev_head


def print_graph(width, height, points):
    for i in range(height - 1, -1, -1):
        for j in range(width):
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
    tail = (0, 0)
    with open("input", "r") as f:
        for line in f.readlines():
            direction, num = line.split(" ")
            for _ in range(int(num)):
                prev_head = head
                head = move_head(head, direction)
                tail = move_tail(head, tail, prev_head)
                if tail not in all_tails:
                    all_tails.append(tail)
    print(len(all_tails))


if __name__ == "__main__":
    main()

#
