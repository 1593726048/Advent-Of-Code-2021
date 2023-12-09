def calc_value(instructions, nodes):
    node = "AAA"
    num=0
    while node != "ZZZ":
        for i in instructions:
            if i == "L":
                node = nodes[node][0]
            elif i == "R":
                node = nodes[node][1]
            num+=1
            if node=="ZZZ":
                return num



def main():

    with open("input", "r") as f:
        instructions=f.readline().strip()
        f.readline()
        nodes={}
        for line in f.readlines():
            node_val=line.split(" ")[0].strip()
            l=line.split("(")[1].split(",")[0].strip()
            r = line.split(")")[0].split(",")[1].strip()
            nodes[node_val]=[l,r]
        print(calc_value(instructions, nodes))


if __name__ == "__main__":
    main()

#
