from typing import List


def bit_array(num) -> List[bool]:
    """Copied from another project
    :param char_string: a string of characters
    :return: a list of bits based on the string
    """
    bits = []
    for i in range(4):
        bits.append(num % (pow(2, i) * 2) >= pow(2, i))
    bits.reverse()
    return bits


def unbit_array(bits) -> int:
    """ copied from another project
    :param bits: the list of the bits
    :return: the bits converted to a string
    """
    bits.reverse()
    num = 0
    for i in range(len(bits)):
        if bits[i]:
            num += pow(2, i)
    bits.reverse()

    return num


def hex2bi(hex_value):
    if ord(hex_value) <= ord("9"):
        dex_value = ord(hex_value) - ord("0")
    else:
        dex_value = ord(hex_value) - ord("a") + 10
    return bit_array(dex_value)


def de_packitify(binary_array, i) -> (int, int):
    version = unbit_array(binary_array[i:i + 3])
    id = unbit_array(binary_array[i + 3:i + 6])
    if id == 4:
        i+=6
        binary_ans=[]
        while binary_array[i]:
            print(binary_ans)
            binary_ans.extend(binary_array[i+1:i+5])
            i+=5
        binary_ans.extend(binary_array[i + 1:i + 5])
        i += 5
        print(f"Literal: {unbit_array(binary_ans)}")
        return version, i
    else:
        if not binary_array[i + 6]:
            length = unbit_array(binary_array[i + 7:i + 22])
            j = i + 22
            while length> j -22-i:
                v, j = de_packitify(binary_array, j)
                version += v
            print(f"len:\t{length}\n\tj:\t{j}")
        else:
            num = unbit_array(binary_array[i + 7:i + 18])
            j = i + 18
            for _ in range(num):
                v, j = de_packitify(binary_array, j)
                version += v
        return version, j


def answer(input_file_name):
    with open(input_file_name, "r") as f:
        line = f.readline().strip()
    print(line)
    binary_array = []
    for cha in line:
        binary_array.extend(hex2bi(cha))
    ans, i = de_packitify(binary_array, 0)
    print(f"len of binary: \n\t\t{len(binary_array)}\n\ti:\t{i}")
    print()
    return ans


def test_binary():
    for i in range(0, 10):
        print(hex2bi(str(i)))
    print()
    for i in range(ord("a"), ord("g")):
        print(hex2bi(chr(i)))


print(answer("input.txt"))
#print(answer("t3.txt"))
# test_binary()
