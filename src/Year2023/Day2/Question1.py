def func1(line):
    pass

def func2():
    pass


def main():
    max_color={
        "red": 12,
        "green": 13,
        "blue": 14
    }
    with open("input", "r") as f:
        total=0
        for line in f.readlines():
            game_id=int(line.split(":")[0].split(" ")[1])
            games=line.split(":")[1].split(";")
            id_works=True
            for game in games:
                balls= [ball.strip() for ball in game.split(",")]
                for ball in balls:
                    num, color=ball.split(" ")
                    num=int(num)
                    if num>max_color[color]:
                        id_works=False
            if id_works:
                total+=game_id
    print(total)




if __name__ == "__main__":
    main()

#