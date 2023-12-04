from typing import List


class Coord:
    def __init__(self, x: int, y: int):
        self.y = y
        self.x = x

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Number:
    def __init__(self, start: Coord, finish: Coord, value: int):
        self.value = value
        self.finish = finish
        self.start = start

    def inc(self, val: int):
        self.value = self.value * 10 + val

    def __repr__(self):
        return f"{self.value} : {self.start}-{self.finish}"


def adjacency(number: Number, coord: Coord):
    if coord.y in range(number.start.y - 1, number.finish.y + 2) and coord.x in range(number.start.x - 1,
                                                                                      number.finish.x + 2):
        if number.value == 58:
            print(coord)
            print(number)
        return True


def double_adjacnecies(coord: Coord, numbers: List[Number]):
    adjs = []
    for number in numbers:
        if adjacency(number, coord):
            adjs.append(number)
    if len(adjs) == 2:
        return adjs[0].value * adjs[1].value
    return 0


def main():
    symbol_locations = []
    number_locations = []
    with open("input", "r") as f:
        cur_num = None
        lines = f.readlines()
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in "1234567890":
                    if cur_num is None:
                        cur_num = Number(Coord(i, j), Coord(0, 0), int(char))
                    else:
                        cur_num.inc(int(char))
                elif cur_num is not None:
                    cur_num.finish = Coord(i, j - 1)
                    number_locations.append(cur_num)
                    cur_num = None
                if char =="*":
                    symbol_locations.append(Coord(i, j))
            if cur_num is not None:
                cur_num.finish = Coord(i, j)
                number_locations.append(cur_num)
                cur_num = None
    total=0
    for coord in symbol_locations:
        total+=double_adjacnecies(coord, number_locations)
    print(total)


if __name__ == "__main__":
    main()
