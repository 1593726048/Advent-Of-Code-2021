def func1(line):
    pass


def func2():
    pass


def main():
    with open("input", "r") as f:
        total = 0
        for line in f.readlines():
            game_id = int(line.split(":")[0].split(" ")[1])
            games = line.split(":")[1].split(";")
            id_works = True
            max_color = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for game in games:

                balls = [ball.strip() for ball in game.split(",")]
                for ball in balls:
                    num, color = ball.split(" ")
                    num = int(num)
                    if num > max_color[color]:
                        max_color[color] = num
            total += (max_color["red"] * max_color["blue"] * max_color["green"])
        print(total)


if __name__ == "__main__":
    main()

# 10736
