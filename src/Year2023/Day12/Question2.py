def populate(springs, nums, cur, cur_num):
    if "?" not in springs:
        if check(springs, nums):
            return 1
        else:
            return 0
    if springs[cur] is not "?":
        return populate(springs, nums, cur + 1, cur_num)
    split=springs.split(".")
    splitten=[]
    for s in split:
        if s!="":
            splitten.append(s)

    total = 0
    springs_temp = springs[:]
    springs_temp[cur] = True
    total += populate(springs_temp, nums, cur + 1, cur_num)
    springs_temp[cur] = False
    total += populate(springs_temp, nums, cur + 1, cur_num)
    return total

def temp_check(springs, nums):
    cur_val=0
    cur_res = 0
    for i in springs:
        if i:
            cur_res += 1
        elif cur_res != 0:
            if cur_res> nums[cur_val]:
                return False
            total_results.append(cur_res)
            cur_res = 0
    if cur_res != 0:
        total_results.append(cur_res)
    if total_results == nums:
        return True
    return False


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
            springs, nums = line.strip().split(" ")
            nums = [int(i) for i in nums.split(",")]
            springs=springs.strip()


            total+=populate(springs, nums, 0)
    print(total)


if __name__ == "__main__":
    main()

#
