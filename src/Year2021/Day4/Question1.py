from typing import List


class Board():
    def __init__(self, numbers: List[List[int]]):
        self.numbers = numbers
        self.hits = [[False, False, False, False, False],  # interestingly I can't use [[False]*5]*5
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     ]

    def add_hit(self, num):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if num == self.numbers[i][j]:
                    print(i)
                    print(j)
                    print(self.hits)
                    self.hits[i][j] = True
                    print(self.hits)

    def check_won(self) -> bool:
        for line in self.hits:
            line_complete = True
            for val in line:
                if val is False:
                    line_complete = False
            if line_complete is True:
                return True
        for i in range(len(self.hits[0])):
            col_complete = True
            for j in range(len(self.hits)):
                if self.hits[j][i] is False:
                    col_complete = False
            if col_complete is True:
                return True
        return False

    def sum_not_hits(self):
        total = 0
        for i in range(len(self.hits)):
            for j in range(len(self.hits[i])):
                if self.hits[i][j] == False:
                    total += self.numbers[i][j]

        return total


def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    input_nums = lines[0]

    boards = []
    cur_board = []
    i = 2
    while i < len(lines):
        if lines[i] == "\n":
            board_grid = []
            for line in cur_board:
                nums = line.replace("  ", " ").strip().split(" ")
                board_grid.append([])
                for num in nums:
                    board_grid[-1].append(int(num))
            boards.append(Board(board_grid))
            cur_board = []
        else:
            cur_board.append(lines[i])
        i += 1
    for num in input_nums.split(","):
        print(num)
        for board in boards:
            print(board.numbers)
            print(board.hits)
            board.add_hit(int(num))
            print(board.hits)
            print()
            if board.check_won():
                print(num)
                print(board.sum_not_hits())
                print(board.sum_not_hits() * int(num))
                return


answer("input.txt")
