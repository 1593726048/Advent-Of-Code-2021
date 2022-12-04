def get_val(letter):
    if ord(letter) in range(ord("a"), ord("z")+1):
        return ord(letter)-ord("a")+1
    else:
        return ord(letter)-ord("A")+27


def main():
    total = 0
    with open("input", "r") as f:
        lines=f.readlines()
        for i in range(0,len(lines)//3):
            for letter in lines[i*3]:
                if letter in lines[i*3+1] and letter in lines[i*3+2]:
                    print(letter)
                    total+=get_val(letter)
                    break


    print(total)
    #383


if __name__ == "__main__":
    main()
