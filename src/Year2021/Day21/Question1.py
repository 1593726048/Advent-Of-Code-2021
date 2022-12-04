class Roller():
    def __init__(self):
        self.current = 1

    def roll3Dice(self):
        n = self.current
        if self.current == 0:
            n += 100
        self.current += 1
        self.current %= 100

        n += self.current
        if self.current == 0:
            n += 100

        self.current += 1
        self.current %= 100

        n += self.current
        if self.current == 0:
            n += 100

        self.current += 1
        self.current %= 100
        return n


class Player():
    def __init__(self, pos):
        self.position = pos
        self.points = 0

    def increase(self, num):
        self.position += num
        self.position %= 10
        if self.position == 0:
            self.points += 10
        self.points += self.position


def answer(input_file_name):
    p1_starting = 3
    p2_starting = 5
    #p1_starting = 4
    #p2_starting = 8
    p1 = Player(p1_starting)
    p2 = Player(p2_starting)
    roller = Roller()
    dice_rolled = 0
    player1_going = True
    while p1.points < 1000 and p2.points < 1000:
        num = roller.roll3Dice()
        dice_rolled += 3
        if player1_going:
            p1.increase(num)
        else:
            p2.increase(num)
        player1_going = not player1_going
    print(dice_rolled)
    print(p1.points)
    print(p2.points)
    if player1_going:
        return p1.points * dice_rolled
    else:
        return p2.points * dice_rolled


print(answer("input.txt"))
