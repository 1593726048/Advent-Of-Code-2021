from typing import List, Tuple


class Packet():
    def evaluate(self) -> int:
        return 0

class LiteralPacket(Packet):
    def __init__(self, value:int):
        self.value=value

    def evaluate(self) -> int:
        return self.value


class AddPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        summ = 0
        for packet in self.packets:
            summ += packet.evaluate()
        return summ


class ProductPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        product = 1
        for packet in self.packets:
            product *= packet.evaluate()
        return product


class MinimumPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        minn= self.packets[0].evaluate()
        for packet in self.packets:
            if packet.evaluate() <minn:
                minn=packet.evaluate()
        return minn

class MaximumPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        maxx= self.packets[0].evaluate()
        for packet in self.packets:
            if packet.evaluate() > maxx:
                maxx=packet.evaluate()
        return maxx

class GreaterPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        if len(self.packets) != 2:
            print("ERROR, GREATER THAN HAS NON 2 PACKETS")
        if self.packets[0].evaluate() > self.packets[1].evaluate():
            return 1
        return 0

class LessPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        if len(self.packets) != 2:
            print("ERROR, LESS THAN HAS NON 2 PACKETS")
        if self.packets[0].evaluate() < self.packets[1].evaluate():
            return 1
        return 0

class EqualPacket(Packet):
    def __init__(self, packets: List[Packet] = None):
        if packets is None:
            packets = []
        self.packets = packets

    def evaluate(self) -> int:
        if len(self.packets) != 2:
            print("ERROR, LESS THAN HAS NON 2 PACKETS")
        if self.packets[0].evaluate() == self.packets[1].evaluate():
            return 1
        return 0



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


def de_packitify(binary_array, i) -> Tuple[Packet, int]:
    version = unbit_array(binary_array[i:i + 3])
    id = unbit_array(binary_array[i + 3:i + 6])
    if id == 4:
        i+=6
        binary_ans=[]
        while binary_array[i]:
            binary_ans.extend(binary_array[i+1:i+5])
            i+=5
        binary_ans.extend(binary_array[i + 1:i + 5])
        i += 5
        return LiteralPacket(unbit_array(binary_ans)), i
    else:
        sub_packets = []
        if not binary_array[i + 6]:
            length = unbit_array(binary_array[i + 7:i + 22])
            j = i + 22

            while length> j -22-i:
                sub_packet, j = de_packitify(binary_array, j)
                sub_packets.append(sub_packet)
        else:
            num = unbit_array(binary_array[i + 7:i + 18])
            j = i + 18
            for _ in range(num):
                sub_packet, j = de_packitify(binary_array, j)
                sub_packets.append(sub_packet)
        if id ==0:
            return AddPacket(packets=sub_packets), j
        if id ==1:
            return ProductPacket(packets=sub_packets), j
        if id ==2:
            return MinimumPacket(packets=sub_packets), j
        if id ==3:
            return MaximumPacket(packets=sub_packets), j
        if id ==5:
            return GreaterPacket(packets=sub_packets), j
        if id ==6:
            return LessPacket(packets=sub_packets), j
        if id ==7:
            return EqualPacket(packets=sub_packets), j


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
    return ans.evaluate()


def test_binary():
    for i in range(0, 10):
        print(hex2bi(str(i)))
    print()
    for i in range(ord("a"), ord("g")):
        print(hex2bi(chr(i)))


#print(answer("t4.txt"))
print(answer("input.txt"))
#39215262724 too low