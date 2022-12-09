def highlight_print(trees, x1, y1):
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if x1 == x and y1 == y:
                print("\033[1;32m", end=str(trees[x][y]))
            else:
                print("\033[1;31m", end=str(trees[x][y]))
        print()
    print()


def count_visible(trees):
    total = 0
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if is_visible(trees, x, y):
                total += 1
    return total


def is_visible(trees, x, y):
    if x == 0 or y == 0:
        return True
    if x == len(trees) - 1 or y == len(trees[x]) - 1:
        return True

    visible = True
    for x1 in range(0, x):
        if trees[x][y] <= trees[x1][y]:
            visible = False
    if visible:
        return True

    visible = True
    for x1 in range(x + 1, len(trees)):
        if trees[x][y] <= trees[x1][y]:
            visible = False
    if visible:
        return True

    visible = True
    for y1 in range(0, y):
        if trees[x][y] <= trees[x][y1]:
            visible = False
    if visible:
        return True

    visible = True
    for y1 in range(y + 1, len(trees[x])):
        if trees[x][y] <= trees[x][y1]:
            visible = False
    if visible:
        return True
    return False


def main():
    trees = []
    with open("input", "r") as f:
        for line in f.readlines():
            tree_line = []
            for char in line.replace("\n", ""):
                tree_line.append(int(char))
            trees.append(tree_line)
    print(count_visible(trees))


if __name__ == "__main__":
    main()

#
