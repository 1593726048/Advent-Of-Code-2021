def get_list(num_list):
    new_list=[]
    for num in num_list.split(" "):
        if num!="":
            new_list.append(int(num))
    return new_list

def main():
    total = 0
    with open("input", "r") as f:

        for line in f.readlines():
            winning_numbers, num_have= line.split(":")[1].split("|")
            num_have=get_list(num_have)
            winning_numbers = get_list(winning_numbers)
            cur=0
            for num in num_have:
                if num in winning_numbers:
                    if cur==0:
                        cur=1
                    else:
                        cur*=2
            total+=cur
    print(total)

if __name__ == "__main__":
    main()
