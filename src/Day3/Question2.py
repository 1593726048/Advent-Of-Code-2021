def answer(input_file_name):
    co2 = []
    oxygen = []
    with open(input_file_name, "r") as f:
        for line in f.readlines():
            oxygen.append(line.strip())
            co2.append(line.strip())
    i = 0

    while len(oxygen) > 1:
        zero = []
        one = []
        for num in oxygen:
            if int(num[i]) == 0:
                zero.append(num)
            else:
                one.append(num)
        if len(zero) > len(one):
            for n in one:
                oxygen.remove(n)
        else:
            for n in zero:
                oxygen.remove(n)
        i+=1
    i=0
    while len(co2) > 1:
        zero = []
        one = []
        for num in co2:
            if int(num[i]) == 0:
                zero.append(num)
            else:
                one.append(num)
        if len(zero) <= len(one):
            for n in one:
                co2.remove(n)
        else:
            for n in zero:
                co2.remove(n)
        i+=1
    co = int(co2[0], 2)
    ox = int(oxygen[0], 2)
    print(co * ox)


answer("input.txt")
