def append_count(cur_count, final_values):
    for val in cur_count:
        if val in final_values:
            final_values[val] += cur_count[val]
        else:
            final_values[val] = cur_count[val]
    return final_values


def recursive_loop(input, count, ten, num):
    final_values = {}
    if num == 0:
        return None
    else:
        for j in range(len(input) - 1):
            if num == 4:
                print(f"\033[94m{j}/{len(input)}")
            if num == 3:
                print(f"\033[96m{j}/{len(input)}")
            if input[j:j + 2] in ten:
                final_values = append_count(count[input[j:j + 2]], final_values)
                recursive_loop(ten[input[j:j + 2]], count, ten, num - 1)
    n = {}
    for i in input:
        if i in n:
            n[i] += 1
        else:
            n[i] = 1
    final_values = append_count(n, final_values)
    return final_values


def tentimes(input, values):
    for i in range(0, 10):
        ninput = ""
        for j in range(len(input) - 1):
            ninput += input[j]
            if input[j:j + 2] in values:
                ninput += values[input[j:j + 2]]
        ninput += input[-1]
        input = ninput
    return input


def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    values = {}
    input = lines[0].strip()
    for line in lines[2:]:
        values[line.split(" ")[0]] = line.split(" ")[-1].strip()
    ten = {}
    count = {}
    for val in values:
        ten[val] = tentimes(val, values)
        pcount = {}
        for i in ten[val][1:-1]:
            if i in pcount:
                pcount[i] += 1
            else:
                pcount[i] = 1
        count[val] = pcount
    print(recursive_loop(input, count, ten, 4))
    return input


print(answer("input.txt"))
# 1908
# 2482
# {'N': 3108, 'V': 1492, 'K': 2472, 'S': 1749, 'H': 2184, 'P': 2528, 'C': 2366, 'B': 1530, 'F': 1522, 'O': 506}