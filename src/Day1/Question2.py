def answer(input_file_name):
    with open(input_file_name, "r") as f:
        num1 = f.readline()  # oldest
        num2 = f.readline()
        num3 = f.readline()
        num4 = f.readline()  # newest

        i = 0
        while not (num4 == ""):
            print(num4)
            if int(num1) + int(num2) + int(num3) < int(num2) + int(num3) + int(num4):
                i += 1
            num1 = num2
            num2 = num3
            num3 = num4
            num4 = f.readline()

    print(i)


answer("input.txt")
