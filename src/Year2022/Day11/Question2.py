import math

lcd = 0 #I'm sorry for the global variable


class Monkey:
    def __init__(self, items: list, operation, op_num, is_divisible, if_true, if_false):
        self.if_false = if_false
        self.if_true = if_true
        self.is_divisible = is_divisible
        self.op_num = op_num
        self.operation = operation
        if items is None:
            items = []
        self.items = items
        self.num_inspects = 0

    def inspect_and_throw(self):
        throw_items = []
        for item in self.items:
            self.num_inspects += 1
            if self.operation == "ADD":
                item += self.op_num
            elif self.operation == "MULTIPLY":
                item *= self.op_num
            elif self.operation == "SQUARE":
                item **= 2
            item %= lcd
            if item % self.is_divisible == 0:
                throw_items.append((item, self.if_true))
            else:
                throw_items.append((item, self.if_false))

        self.items = []
        return throw_items


def create_monkey(lines):
    items = []
    for i in lines[1].split(":")[1].split(","):
        items.append(int(i))
    if "+" in lines[2]:
        operation = "ADD"
        op_num = int(lines[2].split(" ")[-1])
    elif "old * old" in lines[2]:
        operation = "SQUARE"
        op_num = None
    elif "*" in lines[2]:
        operation = "MULTIPLY"
        op_num = int(lines[2].split(" ")[-1])
    else:
        raise ValueError

    is_divisible = int(lines[3].split(" ")[-1])
    if_true = int(lines[4].split(" ")[-1])
    if_false = int(lines[5].split(" ")[-1])

    return Monkey(items, operation, op_num, is_divisible, if_true, if_false)


def main():
    with open("input", "r") as f:
        lines = f.readlines()
    monkeys = []
    for i in range(len(lines) // 7 + 1):
        monkeys.append(create_monkey(lines[i * 7:i * 7 + 7]))
    nums = []
    for monkey in monkeys:
        nums.append(monkey.is_divisible)
    print(nums)  # prints it out to be put in the lcd = math.lcm(<NUMS>) because it doesn't accept lists.
    global lcd
    lcd = math.lcm(2, 17, 19, 3, 5, 13, 7, 11)
    # lcd = math.lcm(23, 19, 13, 17) # for test input
    for i in range(10000):
        for monkey in monkeys:
            items = monkey.inspect_and_throw()
            for j in items:
                item, monk = j
                monkeys[monk].items.append(item)
    for monkey in monkeys:
        print(monkey.num_inspects)


if __name__ == "__main__":
    main()


