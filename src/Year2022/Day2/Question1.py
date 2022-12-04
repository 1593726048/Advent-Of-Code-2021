def count_points(opp, you):
    score = {"X": 1,  # Rock
             "Y": 2,  # Paper
             "Z": 3}[you]  # sissors
    if opp == "A":  # Rock
        if score == 1:
            score += 3
        if score == 2:
            score += 6
    if opp == "B":  # Paper
        if score == 2:
            score += 3
        if score == 3:
            score += 6
    if opp == "C":  # Sissors
        if score == 3:
            score += 3
        if score == 1:
            score += 6
    return score


def main():
    with open("input", "r") as f:
        total_score = 0
        for line in f.readlines():
            opp, you = line.strip().split(" ")
            total_score += count_points(opp, you)
    print(total_score)

if __name__ == "__main__":
    main()
