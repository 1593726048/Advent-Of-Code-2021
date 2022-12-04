def get_val(letter):

    if ord(letter) in range(ord("a"), ord("z")+1):
        return ord(letter)-ord("a")+1
    else:
        return ord(letter)-ord("A")+27



def main():
    for letter in "ABCXYZabcxyz":
        print(get_val(letter))
    with open("input", "r") as f:
        total=0
        for line in f.readlines():
            line=line.strip()
            first_half, second_half=line[:len(line)//2], line[len(line)//2:]
            letters_used=[]
            for letter in first_half:
                if letter in second_half and letter not in letters_used:
                    total+=get_val(letter)
                    letters_used.append(letter)

    print(total)


    #4224
    #8800
    #11980


if __name__ == "__main__":
    main()
