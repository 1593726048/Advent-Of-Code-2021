def main():
    elves=[]
    with open("input", "r") as f:
        current = 0
        for line in f.readlines():
            if line == "\n":
                elves.append(current)
                current = 0
            else:
                current += int(line)
    elves.sort()
    print(elves[-1]+elves[-2]+elves[-3])

    #722032


if __name__ == "__main__":
    main()
