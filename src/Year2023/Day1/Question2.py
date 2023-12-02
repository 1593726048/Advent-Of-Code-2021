def main():
    total = 0
    numbers = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    with open("input", "r") as f:
        for line in f.readlines():
            num = ""
            for i in range(len(line)):
                if line[i] in "1234567890":
                    num += line[i]
                else:
                    for number in numbers:
                        if len(number) + i < len(line) and line[i: i + len(number)] == number:
                            num += str(numbers[number])
            if num != "":
                total += int(num[0] + num[-1])

    print(total)


if __name__ == "__main__":
    main()

