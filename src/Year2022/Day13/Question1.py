def get_pairs(lines):
    val1, _ = get_array(lines[0].strip())
    val2, _ = get_array(lines[1].strip())
    return val1, val2


def compare_values(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if right < left:
            return False
        return None
    if isinstance(left, int) and isinstance(right, list):
        return compare_values([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_values(left, [right])
    i = 0
    while True:
        if i == len(left) == len(right):
            return None
        if i >= len(left):
            return True
        if i >= len(right):
            return False
        val = compare_values(left[i], right[i])
        if val is not None:
            return val
        i += 1


def get_array(line, i=1):
    array = []
    temp_val = ""
    while i < len(line):
        if line[i] == "[":
            val, i = get_array(line, i + 1)
            array.append(val)
        elif line[i] == "]":
            if temp_val != "":
                array.append(int(temp_val))
            return array, i
        elif line[i] == ",":
            if temp_val != "":
                array.append(int(temp_val))
            temp_val = ""
        else:
            temp_val += line[i]
        i += 1
    raise ValueError


def main():
    total = 0
    pairs = []
    with open("input", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            pairs.append(get_pairs(lines[i:i + 2]))
    for i in range(len(pairs)):
        pair = pairs[i]
        if compare_values(pair[0], pair[1]):
            total += i + 1
    print(total)


if __name__ == "__main__":
    main()

