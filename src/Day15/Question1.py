class Pathway:
    def __init__(self):
        pass

def solve_pathway(pathway, x, y, pathways):
    print(f"x:\t{x}\ty:\t{y}")
    list_prev_pos.append((x, y))
    p=pathway[x][y]
    if x == len(pathway)-1 and y == len(pathway[0])-1:
        return 0
    paths = []
    if x != len(pathway)-1 and (x + 1, y) not in list_prev_pos:
        paths.append(solve_pathway(pathway, x + 1, y, list_prev_pos)+p)
    if y != len(pathway[0])-1 and (x, y + 1) not in list_prev_pos:
        paths.append(solve_pathway(pathway, x, y + 1, list_prev_pos)+p)
    #if x != 0 and (x - 1, y) not in list_prev_pos:
    #    paths.append(solve_pathway(pathway, x - 1, y, list_prev_pos)+p)
    #if y != 0 and (x, y - 1) not in list_prev_pos:
    #    paths.append(solve_pathway(pathway, x, y - 1, list_prev_pos)+p)
    if paths==[]:
        return 100000000
    return min(paths)


def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    pathway = []
    for line in lines:
        p_way = []
        for num in line.strip():
            p_way.append(int(num))
        pathway.append(p_way)
    print(f"x:\t{len(pathway)}\ty:\t{len(pathway[0])}")
    print(solve_pathway(pathway, 0, 0, []))

answer("input.txt")
#877 too high