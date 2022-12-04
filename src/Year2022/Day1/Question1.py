def main():
    with open("input", "r") as f:
        current = 0
        highest = 0
        for line in f.readlines():
            if line == "\n":
                if current > highest:
                    highest = current
                current = 0
            else:
                current += int(line)
    print(highest)

    #722032


if __name__ == "__main__":
    main()
