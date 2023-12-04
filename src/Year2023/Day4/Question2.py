def get_list(num_list):
    new_list = []
    for num in num_list.split(" "):
        if num != "":
            new_list.append(int(num))
    return new_list


def main():
    grid = []
    with open("input", "r") as f:

        for i, line in enumerate(f.readlines()):
            winning_numbers, num_have = line.split(":")[1].split("|")
            num_have = get_list(num_have)
            winning_numbers = get_list(winning_numbers)
            cur = 0
            for num in num_have:
                if num in winning_numbers:
                    cur += 1
            grid.append(cur)

    cards = [1] * len(grid)
    for i in range(len(cards)):
        for num in range(i + 1, i + grid[i] + 1):
            cards[num] += cards[i]
    print(sum(cards))


if __name__ == "__main__":
    main()
