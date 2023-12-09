from typing import List


def next_line(num_list: List[int]):
    if sum([abs(i) for i in num_list])==0:
        return 0
    new_list=[]
    for i in range(len(num_list)-1):
        new_list.append(num_list[i+1]-num_list[i])
    return next_line(new_list)+new_list[-1]

def func2():
    pass


def main():
    num_lists=[]
    with open("input", "r") as f:

        for line in f.readlines():
            num_lists.append([int(i) for i in line.split(" ")])
    total=0
    for num_list in num_lists:
        total+=next_line(num_list)+num_list[-1]
    print(total)

if __name__ == "__main__":
    main()
