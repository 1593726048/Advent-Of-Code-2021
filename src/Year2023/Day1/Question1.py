def main():
    total=0
    with open("input", "r") as f:
        for line in f.readlines():
            num=""
            for char in line:
                if char in "1234567890":
                    num+=char
            if num !="":
                total+= int(num[0]+num[-1])
    print(total)



if __name__ == "__main__":
    main()

