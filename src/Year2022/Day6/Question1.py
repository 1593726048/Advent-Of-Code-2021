def count_dupes(substr):
    character_dict = {}
    for char in substr:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict


def handle_line(line):
    for i in range(0, len(line)):
        substr = line[i:i + 4]
        char_dict = count_dupes(substr)
        if len(char_dict) == 4:
            return i + 4


def main():
    with open("input", "r") as f:
        for line in f.readlines():
            marker = handle_line(line)
            print(marker)
            print()


if __name__ == "__main__":
    main()

# 1778
