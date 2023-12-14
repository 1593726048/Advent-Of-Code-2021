def populate(springs, nums, cur):
    if None not in springs:
        if check(springs, nums):
            return 1
        else:
            return 0
    if springs[cur] is not None:
        return populate(springs, nums, cur + 1)

    total = 0
    springs_temp = springs[:]
    springs_temp[cur] = True
    total += populate(springs_temp, nums, cur + 1)
    springs_temp[cur] = False
    total += populate(springs_temp, nums, cur + 1)
    return total


def check(springs, nums):
    if None in springs:
        return False
    total_results = []
    cur_res = 0
    for i in springs:
        if i:
            cur_res += 1
        elif cur_res != 0:
            total_results.append(cur_res)
            cur_res = 0
    if cur_res !=0:
        total_results.append(cur_res)
    if total_results == nums:
        return True
    return False


def main():
    with open("input", "r") as f:
        total=0
        for line in f.readlines():
            spr, nums = line.strip().split(" ")
            nums = [int(i) for i in nums.split(",")]
            springs = []
            for s in spr:
                if s == "?":
                    springs.append(None)
                elif s == "#":
                    springs.append(True)
                elif s == ".":
                    springs.append(False)


            total+=populate(springs, nums, 0)
    print(total)


if __name__ == "__main__":
    main()

#
