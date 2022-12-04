def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    values = {}
    input = lines[0].strip()
    for line in lines[2:]:
        values[line.split(" ")[0]] = line.split(" ")[-1].strip()
    for i in range(0, 10):
        print(f"{i}: {input}")
        ninput = ""
        for j in range(len(input) - 1):
            ninput += input[j]
            if input[j:j + 2] in values:
                ninput += values[input[j:j + 2]]
        ninput += input[-1]
        input = ninput

    count_vals = {}
    for i in input:
        if i in count_vals:
            count_vals[i] += 1
        else:
            count_vals[i] = 1
    print(count_vals)
    least = 100000
    most = 0
    lc = "A"
    mc = "A"
    for val in count_vals:
        if count_vals[val] > most:
            most = count_vals[val]
            mc = val
        if count_vals[val] < least:
            least = count_vals[val]
            lc = val
    print(least)
    print(lc)
    print(most)
    print(mc)
    print(most - least)
    return input


print(answer("input.txt"))
# 1908
# 2482
