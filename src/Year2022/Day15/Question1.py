from typing import List


def get_sens_beacon(line):
    sensor = int(line.split("=")[1].split(",")[0]), int(line.split("=")[2].split(":")[0])
    beacon = int(line.split("=")[3].split(",")[0]), int(line.split("=")[4].split("\n")[0])
    return sensor, beacon


def get_dist(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def check_line_single(beacon, sensor, line_number):
    distance = get_dist(sensor, beacon)
    x1 = sensor[0] - (distance - abs(sensor[1] - line_number))
    x2 = sensor[0] + (distance - abs(sensor[1] - line_number))
    if x1 <= x2:
        return x1, x2


def get_length(invalid_xs: List[List[int]]):
    total = 0
    for x0, x1 in invalid_xs:
        total += x1 - x0 + 1
    return total


def get_beacons_in_length(invalid_xs: List[List[int]], beacons, y_level):
    values = []
    for beacon in beacons:
        if beacon[1] == y_level:
            for x_s, x_f in invalid_xs:
                if x_s <= beacon[0] <= x_f and beacon[0] not in values:
                    values.append(beacon[0])
    return len(values)


def sort_out(invalid_xs: List[List[int]]):
    new_xs = [invalid_xs[0], ]
    for j in range(1, len(invalid_xs)):
        x_s0, x_f0 = invalid_xs[j]
        for i in range(len(new_xs)):
            x_s1, x_f1 = new_xs[i]
            con1 = x_s1 <= x_f0 <= x_f1 or x_s0 <= x_f1 <= x_f0
            con2 = x_s1 <= x_s0 <= x_f1 or x_s0 <= x_s1 <= x_f0
            if con1 or con2:
                new_xs[i][0] = min(x_s0, x_s1)
                new_xs[i][1] = max(x_f0, x_f1)
                new_xs.extend(invalid_xs[j + 1:])
                return new_xs, True
        new_xs.append([x_s0, x_f0])
    return new_xs, False


def check_line(beacons, sensors, line_number):
    invalid_xs = []
    for beacon, sensor in zip(beacons, sensors):
        xs = check_line_single(beacon, sensor, line_number)
        if xs is not None:
            invalid_xs.append([xs[0], xs[1]])  # detupling
    is_changed = True
    while is_changed:
        invalid_xs, is_changed = sort_out(invalid_xs)
    return invalid_xs


def main():
    line_number = 2000000
    # line_number=10
    sensors = []
    beacons = []
    with open("input", "r") as f:
        for line in f.readlines():
            sensor, beacon = get_sens_beacon(line)
            sensors.append(sensor)
            beacons.append(beacon)
    xs = check_line(beacons, sensors, line_number)
    print(get_length(xs)
          - get_beacons_in_length(xs, beacons, line_number)
          - get_beacons_in_length(xs, sensors, line_number))


if __name__ == "__main__":
    main()

