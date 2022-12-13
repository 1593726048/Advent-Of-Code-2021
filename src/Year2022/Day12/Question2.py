def get_start_finish(graph):
    start_pos = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "S" or graph[i][j] == 0:
                start_pos.append((i, j))
            if graph[i][j] == "E":
                print(i, j)
    return start_pos


def print_active(graph, positions):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            char = graph[i][j]
            if graph[i][j] == "S" or graph[i][j] == "E":
                print("\033[1;33m", end=char)
            elif (i, j) in positions:
                print("\033[1;32m", end=chr(char + ord("a")))
            else:
                print("\033[1;31m", end=chr(char + ord("a")))
        print()
    print()


def print_pos_graph(pos_graph, graph):
    for i in range(len(pos_graph)):
        for j in range(len(pos_graph[i])):
            if graph[i][j] == "S" or graph[i][j] == "E":
                print("\033[1;33m", end="")
            else:
                print("\033[1;31m", end="")
            print(pos_graph[i][j], end="\t")
        print()
    print()


def get_num(graph, current_pos, past_pos):
    future_pos = []
    for (i, j) in current_pos:
        for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= i2 < len(graph) and 0 <= j2 < len(graph[i2]) and \
                    (i2, j2) not in future_pos and \
                    (i2, j2) not in past_pos and \
                    (i2, j2) not in current_pos:
                val_s = graph[i][j]
                val_f = graph[i2][j2]
                if val_s == "S":
                    val_s = 0
                if val_f == "E":
                    val_f = 25
                if val_f - val_s <= 1:
                    if graph[i2][j2] == "E":
                        return 1
                    future_pos.append((i2, j2))
    if len(future_pos) == 0:
        past_pos.extend(current_pos)
        print_active(graph, past_pos)
        raise ValueError
    current_pos.extend(past_pos)
    return get_num(graph, future_pos, current_pos) + 1


def get_empty_pos_graph(graph):
    pos_graph = []
    for line in graph:
        line2 = []
        for _ in line:
            line2.append(-1)
        pos_graph.append(line2)
    return pos_graph


def get_squares(graph, pos_graph, current_pos, current_val):
    future_pos = []
    for (i, j) in current_pos:
        for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= i2 < len(graph) and 0 <= j2 < len(graph[i2]) and \
                    (i2, j2) not in future_pos and \
                    (i2, j2) not in current_pos and \
                    pos_graph[i2][j2] == -1:
                val_s = graph[i][j]
                val_f = graph[i2][j2]
                if val_s == "S":
                    val_s = 0
                if val_f == "E":
                    val_f = 25
                print(val_f)
                print(val_s)
                if val_f - val_s <= 1:
                    pos_graph[i2][j2] = current_val
                    if graph[i2][j2] == "E":
                        return pos_graph
                    future_pos.append((i2, j2))
    if len(future_pos) == 0:
        print_pos_graph(pos_graph, graph)
        raise ValueError
    return get_squares(graph, pos_graph, future_pos, current_val + 1)


def main():
    graph = []
    with open("input", "r") as f:
        for line in f.readlines():
            ff = []
            for char in line.strip():
                if char in ("E", "S"):
                    ff.append(char)
                else:
                    ff.append(ord(char) - ord("a"))
            graph.append(ff)
    start = get_start_finish(graph)
    num = get_num(graph, start, [])
    print(num)


if __name__ == "__main__":
    main()
