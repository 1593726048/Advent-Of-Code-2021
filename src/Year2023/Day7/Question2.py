from enum import Enum


class Card:
    class Type(Enum):
        five = 6
        four = 5
        full = 4
        three = 3
        pair = 2
        one = 1
        high = 0

    def __init__(self, line):
        card, val = line.split(" ")
        self.type: Card.Type
        self.card = card
        self.num = int(val)
        repeats = {}
        for c in card:
            if c in repeats:
                repeats[c] += 1
            else:
                repeats[c] = 1
        m = 0
        for c in repeats:
            if c != "J":
                if repeats[c] > m:
                    m = repeats[c]
        if "J" in repeats.keys():
            m += repeats["J"]

        if m == 3 and len(repeats.keys()) == 2:
            self.type = Card.Type.full
        elif m ==3 and len(repeats.keys())== 3 and "J" in repeats.keys():
            self.type = Card.Type.full
        elif m == 2 and len(repeats.keys()) == 3:
            self.type = Card.Type.pair
        elif m==2 and len(repeats.keys())==4 and "J" in repeats.keys():
            self.type = Card.Type.pair
        else:
            self.type = {
                1: Card.Type.high,
                2: Card.Type.one,
                3: Card.Type.three,
                4: Card.Type.four,
                5: Card.Type.five
            }[m]

    def __lt__(self, other):
        if self.type != other.type:
            return self.type.value < other.type.value
        card_value = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10}
        for c, d in zip(self.card, other.card):
            if c != d:
                if c in card_value.keys():
                    c_val = card_value[c]
                else:
                    c_val = int(c)
                if d in card_value.keys():
                    d_val = card_value[d]
                else:
                    d_val = int(d)
                return c_val < d_val
        print("AAAAAAH")

    def other_rep(self):
        return f"{self.card}: {self.type}"

    def __repr__(self):
        return self.card


def main():
    with open("input", "r") as f:
        cards = []
        for line in f.readlines():
            cards.append(Card(line))
    cards.sort()
    print(cards)
    total = 0

    for i, card in enumerate(cards):
        total += (i + 1) * card.num
    print(total)


if __name__ == "__main__":
    main()

# 245682144
# Part 1: 246163188
# 246308347