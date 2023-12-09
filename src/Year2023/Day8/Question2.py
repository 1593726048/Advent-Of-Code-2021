def calc_value(instructions, nodes, current_nodes):
    num=0
    while True:
        for i in instructions:
            new_nodes=[]
            for n in current_nodes:
                if i == "L":
                    new_nodes.append(nodes[n][0])
                elif i == "R":
                    new_nodes.append(nodes[n][1])
            num+=1
            works=True
            for n in new_nodes:
                if n[-1]!="Z":
                    works=False
                    continue

            if works:
                return num
            current_nodes=new_nodes



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
        starting_nodes=[]
        for node in nodes:
            if node[-1]=="A":
                starting_nodes.append(node)
        print(calc_value(instructions, nodes, starting_nodes))



if __name__ == "__main__":
    main()

#21251
