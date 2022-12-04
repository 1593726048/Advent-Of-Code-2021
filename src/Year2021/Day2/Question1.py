"""
Instructions

figure out how to pilot a sub

series of commands ie
forawrd 1, -> increases horizontal pos by X
down 2, -> increases depth by X
up 3 -> decreases depth by X

"""


class Sub():
    def __init__(self, fb: int = 0, depth: int = 0):
        self.fb = fb
        self.depth = depth

    def forward(self, x):
        self.fb += x

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x


def answer(input_file_name):
    sub = Sub()
    with open(input_file_name, "r") as f:
        line = f.readline()
        while line != "":
            command = line.split(" ")
            if command[0] == "down":
                sub.down(int(command[1]))
            elif command[0] == "up":
                sub.up(int(command[1]))
            elif command[0] == "forward":
                sub.forward(int(command[1]))
            else:
                print(f"Unknown command, {command[0]}")
            line = f.readline()
    print(sub.depth)
    print(sub.fb)
    print(sub.fb * sub.depth)


answer("input.txt")
