from __future__ import annotations

from typing import List


class Pipe:
    def __init__(self, name: str, flow_rate: int):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels: List[Pipe] = []
        self.is_open = False
        self.minute_open = 0
        self.distances: dict[Pipe, int] = {self: 0}

    def __str__(self):
        strin = f"Valve {self.name} has flow rate={self.flow_rate}; tunnels lead to valves "
        for pipe in self.tunnels:
            strin += pipe.name + ", "
        return strin

    def calc_flow(self):
        return self.flow_rate * self.minute_open

    def open(self, minutes_left: int):
        self.is_open = True
        self.minute_open = minutes_left

    def close(self):
        self.is_open = False
        self.minute_open = 0


def distance_between(pipe1: Pipe, pipe2: Pipe, going_depth):
    if pipe1 is pipe2:
        return 0
    if going_depth == 0:
        return -1
    if pipe1.tunnels == []:
        return -1
    else:
        for i in range(0, going_depth):
            for pipe in pipe1.tunnels:
                if distance_between(pipe, pipe2, i) != -1:
                    return i + 1
    return -1


def print_values(pipes: List[Pipe]):
    valves_open = []
    for pipe in pipes:
        if pipe.is_open:
            valves_open.append(pipe)
    if valves_open == []:
        print("No valves are open.")
    else:
        print(f"Valves", end=" ")
        total = 0
        for pipe in valves_open:
            total += pipe.flow_rate
            print(pipe.name, end=", ")
        print(f"are open, releasing {total} pressure.")


def create_pipe(line: str, pipes: List[Pipe]):
    pipe = Pipe(name=line.split(" ")[1], flow_rate=int(line.split("=")[1].split(";")[0]))
    for connector in line.split("valve")[1].replace("s", "").split(','):
        for p in pipes:
            if connector.strip() == p.name:
                pipe.tunnels.append(p)
                p.tunnels.append(pipe)
    pipes.append(pipe)


def greedy_open(pipe: Pipe, minutes_left: int, pipes):
    print_values(pipes)
    if minutes_left == 0:
        return
    goto_pipe: Pipe | None = None
    for p in pipe.tunnels:
        if (goto_pipe is None or p.flow_rate > goto_pipe.flow_rate) and not p.is_open:
            goto_pipe = p
    goto_pipe.open(minutes_left)
    greedy_open(pipe, minutes_left - 2, pipes)


def calc_routes(pipe: Pipe, pipes: List[Pipe], minutes_left: int):
    if minutes_left < 0:
        return -1
    if minutes_left == 0:
        total = 0
        for p in pipes:
            total += p.calc_flow()
        return total
    best = 0
    for p in pipe.tunnels:
        p.open(minutes_left)
        temp = calc_routes(p, pipes, minutes_left - 2)
        if temp > best:
            best = temp
        p.close()
        temp = calc_routes(p, pipes, minutes_left - 1)
        if temp > best:
            best = temp
    return best


def get_best_next(pipe: Pipe, pipes: List[Pipe], minutes_left: int):
    print_values(pipes)
    if minutes_left == 0:
        return
    go_to_pipe = (pipe, 0, 1)
    for p in pipes:
        if p.is_open:
            flow, dist = 0, 1
        else:
            flow, dist = p.flow_rate, distance_between(pipe, p, pipes) + 1
        if go_to_pipe[1] / go_to_pipe[2] < flow / dist and dist < minutes_left:
            go_to_pipe = (p, flow, dist)
            # print(go_to_pipe)
    go_to_pipe[0].open(minutes_left - go_to_pipe[2])
    get_best_next(go_to_pipe[0], pipes, minutes_left - go_to_pipe[2])


def get_total_flow(pipes: List[Pipe]):
    temp = 0
    for p2 in pipes:
        temp += p2.calc_flow()
    return temp


def get_total_maximum(pipe, pipes: List[Pipe], minutes_left: int):
    total_max = 0
    for p in pipes:
        if p.is_open:
            total_max += p.calc_flow()
        else:
            val = p.flow_rate * (minutes_left - pipe.distances[p] - 1)  # distance_between(pipe, p, pipe_length) - 1)
            if val > 0:
                total_max += val
    return total_max


def get_best(pipe: Pipe, pipes: List[Pipe], minutes_left: int):
    best = 0
    if minutes_left < 0:
        return -1
    if minutes_left in [0, 1]:
        for p in pipes:
            best += p.calc_flow()
        return best

    for p in pipes:
        if not p.is_open:
            if pipe == pipes[0]:
                print(p)
            dist = pipe.distances[p]  # distance_between(pipe, p, pipe_length) + 1
            if dist <= minutes_left and best < get_total_maximum(pipe, pipes, minutes_left):
                p.open(minutes_left - dist)
                is_all_open = True
                for p2 in pipes:
                    if not p2.is_open:
                        is_all_open = False
                if is_all_open:
                    temp = get_total_flow(pipes)
                else:
                    temp = get_best(p, pipes, minutes_left - dist)
                if temp > best:
                    best = temp
                p.close()
    return best


def get_best_limiting(pipe: Pipe, pipes: List[Pipe], minutes_left: int, best: int = 0):
    if minutes_left < 2:
        pipe.close()
        return get_total_flow(pipes)
    maximums = []
    for p in pipes[1:]:
        if not p.is_open:
            dist = pipe.distances[p]  # distance_between(pipe, p, pipe_length)
            p.open(minutes_left - dist - 1)
            maximums.append((p, get_total_maximum(p, pipes, minutes_left - dist - 1)))
            p.close()

    maximums.sort(key=lambda m: m[1])
    maximums.reverse()
    for p, maxi in maximums:
        if pipe is pipes[0]:
            print(p)
        if maxi <= best:
            return best
        p.open(minutes_left - pipe.distances[p] - 1)
        temp = get_best_limiting(p, pipes, minutes_left - pipe.distances[p] - 1, best)
        p.close()
        if temp > best:
            best = temp
    return max(best, get_total_flow(pipes))


def initialize_distances(pipes: List[Pipe], pipe_length):
    for i in range(len(pipes)):
        for j in range(i, len(pipes)):
            dist = distance_between(pipes[i], pipes[j], pipe_length)
            pipes[i].distances[pipes[j]] = dist
            pipes[j].distances[pipes[i]] = dist


def main():
    pipes = []
    with open("input", "r") as f:
        for line in f.readlines():
            create_pipe(line, pipes)
    pipes[0].open(30)
    useful_pipes = []
    for pipe in pipes:
        if pipe.flow_rate != 0:
            useful_pipes.append(pipe)
    useful_pipes.sort(key=lambda pipe: pipe.flow_rate)
    useful_pipes.append(pipes[0])
    useful_pipes.reverse()
    initialize_distances(useful_pipes, len(pipes))
    print(get_best_limiting(pipes[0], useful_pipes, 30))


if __name__ == "__main__":
    main()
