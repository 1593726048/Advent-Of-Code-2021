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


def sort(values):
    for i in range(0, len(values)):
        for j in range(i + 1, len(values)):
            if not compare_values(values[i], values[j]):
                values[i], values[j] = values[j], values[i]


def main():
    values = []
    with open("input", "r") as f:  # note input got changed
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            values.extend(get_pairs(lines[i:i + 2]))
    sort(values)
    for i in range(len(values)):
        if values[i] == [[2]] or values[i] == [[6]]:
            print(i + 1)


if __name__ == "__main__":
    main()
