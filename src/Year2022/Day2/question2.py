def count_points(opp, you):
    score = {"X": 0,  # Lose
             "Y": 3,  # draw
             "Z": 6}[you]  # win
    if opp == "A":  # Rock
        score += {"X": 3,
                  "Y": 1,
                  "Z": 2}[you]
    if opp == "B":  # Paper
        score += {"X": 1,
                  "Y": 2,
                  "Z": 3}[you]
    if opp == "C":  # Sissors
        score += {"X": 2,
                  "Y": 3,
                  "Z": 1}[you]
    #print(score)
    return score


def main():
    with open("input", "r") as f:
        total_score = 0
        for line in f.readlines():
            opp, you = line.strip().split(" ")
            total_score += count_points(opp, you)
    print(total_score)

    # 722032


if __name__ == "__main__":
    main()