class Game:
    def __init__(self, p1_pos, p2_pos):
        self.p2_pos = p2_pos
        self.p1_pos = p1_pos

        self.p1_wins = 0
        self.p2_wins = 0

        self.p1_points = 0
        self.p2_points = 0

    def increase_p1(self, num):
        self.p1_pos += num
        self.p1_pos %= 10
        if self.p1_pos == 0:
            self.p1_points += 10
        self.p1_points += self.p1_pos

    def decrease_p1(self, num):
        if self.p1_pos == 0:
            self.p1_points -= 10
        self.p1_points -= self.p1_pos
        self.p1_pos += 10
        self.p1_pos -= num
        self.p1_pos %= 10
        
    def increase_p2(self, num):
        self.p2_pos += num
        self.p2_pos %= 10
        if self.p2_pos == 0:
            self.p2_points += 10
        self.p2_points += self.p2_pos

    def decrease_p2(self, num):
        if self.p2_pos == 0:
            self.p2_points -= 10
        self.p2_points -= self.p2_pos
        self.p2_pos += 10
        self.p2_pos -= num
        self.p2_pos %= 10




def recurser(game: Game, player_1_going: bool, num_games=1):
    roll = range(3, 10)
    probability = [1, 3, 6, 7,  6, 3, 1]
    if player_1_going:
        if game.p2_points >= 21:
            game.p2_wins += num_games
            return
        for r, prob in zip(roll, probability):
            game.increase_p1(r)
            recurser(game, not player_1_going, num_games * prob)
            game.decrease_p1(r)

    else:
        if game.p1_points >= 21:
            game.p1_wins += num_games
            return

        for r,prob in zip(roll, probability):
            game.increase_p2(r)
            recurser(game, not player_1_going, num_games * prob)
            game.decrease_p2(r)

def answer(input_file_name):
    p1_starting = 3
    p2_starting = 5
    #p1_starting = 4
    #p2_starting = 8
    game = Game(p1_starting, p2_starting)
    recurser(game, True)
    print(game.p1_wins)
    print(game.p2_wins)


print(answer("input.txt"))
