def main():
    funny_nums={}
    x=1
    loop_num=0
    with open("input", "r") as f:
        commands=f.readlines()
    for command in commands:
        if command.strip()=="noop":
            loop_num += 1
            if loop_num %20==0:
                funny_nums[loop_num]=x
        else:
            loop_num+=2
            if loop_num%20==0 or loop_num%20==1:
                funny_nums[loop_num]=x
            x+=int(command.split(" ")[1])
    total=0
    for key in funny_nums:
        val=(key//20)*20
        if val in [20,60,100,140,180,220]:
            total+=val*funny_nums[key]
    print(total)


if __name__ == "__main__":
    main()

#
