def highlight_print(trees, x1, y1):
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if x1 == x and y1 == y:
                print("\033[1;32m", end=str(trees[x][y]))
            else:
                print("\033[1;31m", end=str(trees[x][y]))
        print()
    print()


def best_scenic(trees):
    highest = 0
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            score = scenic_score(trees, x, y)
            if score > highest:
                highest = score
    return highest


def scenic_score(trees, x, y):
    if x == 0 or y == 0:
        return 0
    if x == len(trees) - 1 or y == len(trees[x]) - 1:
        return 0

    view1 = 0
    for x1 in range(x - 1, -1, -1):
        if trees[x][y] > trees[x1][y]:

            view1 += 1
        else:
            view1 += 1
            break

    view2 = 0
    for x1 in range(x + 1, len(trees)):
        if trees[x][y] > trees[x1][y]:
            view2 += 1
        else:
            view2 += 1
            break

    view3 = 0
    for y1 in range(y - 1, -1, -1):
        if trees[x][y] > trees[x][y1]:
            view3 += 1
        else:
            view3 += 1
            break

    view4 = 0
    for y1 in range(y + 1, len(trees[x])):
        if trees[x][y] > trees[x][y1]:
            view4 += 1
        else:
            view4 += 1
            break

    return view1 * view2 * view3 * view4


def main():
    trees = []
    with open("input", "r") as f:
        for line in f.readlines():
            tree_line = []
            for char in line.replace("\n", ""):
                tree_line.append(int(char))
            trees.append(tree_line)

    print(best_scenic(trees))


if __name__ == "__main__":
    main()

#
