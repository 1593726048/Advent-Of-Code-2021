def answer(input_file_name):
    with open(input_file_name, "r") as f:
        prev = f.readline()
        line = f.readline()
        i = 0
        while line != "":
            if int(prev) < int(line):
                i += 1
            prev = line
            line = f.readline()


    print(i)
answer("input.txt")