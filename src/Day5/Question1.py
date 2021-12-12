from typing import List
import numpy as np


class LineSegment:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self):
        return f"({self.x1},{self.y1}) -> ({self.x2},{self.y2})"


def ymxb(line: LineSegment):
    if line.x1 == line.x2:
        return False, line.x1
    m = (line.y1 - line.y2) / (line.x1 - line.x2)
    b = line.y1 - m * line.x1
    return m, b


def between(val, num1, num2):
    if num1 > num2:
        if val > num1:
            return False
        if val < num2:
            return False
    else:
        if val < num1:
            return False
        if val > num2:
            return False
    return True


def get_intersect(line1: LineSegment, line2: LineSegment):
    """lowX_line1 = line1.x1 if line1.x1 < line1.x2 else line1.x2
    highX_line1 = line1.x1 if line1.x1 > line1.x2 else line1.x2

    lowX_line2 = line2.x1 if line2.x1 < line2.x2 else line2.x2
    highX_line2 = line2.x1 if line2.x1 > line2.x2 else line2.x2

    lowY_line1 = line1.y1 if line1.y1 < line1.y2 else line1.y2
    highY_line1 = line1.y1 if line1.y1 > line1.y2 else line1.y2

    lowY_line2 = line2.y1 if line2.y1 < line2.y2 else line2.y2
    highY_line2 = line2.y1 if line2.y1 > line2.y2 else line2.y2

    if lowX_line1 > highX_line2:
        return False, False
    if lowX_line2 > highX_line1:
        return False, False
    if lowY_line1 > highY_line2:
        return False, False
    if lowY_line2 > highY_line1:
        return False, False
    """  # This chunk of code doesn't work at all

    m1, b1 = ymxb(line1)
    m2, b2 = ymxb(line2)
    if abs(m1) != 0:  # abs of false is 0 so this works
        return False, False
    if abs(m2) != 0:
        return False, False
    y = False
    if (not np.logical_xor(type(m1) is bool, type(m2) is bool)) and m1 == m2:
        if b1 != b2:
            return False, False
        lowX_line1 = line1.x1 if line1.x1 < line1.x2 else line1.x2
        highX_line1 = line1.x1 if line1.x1 > line1.x2 else line1.x2

        lowX_line2 = line2.x1 if line2.x1 < line2.x2 else line2.x2
        highX_line2 = line2.x1 if line2.x1 > line2.x2 else line2.x2

        lowY_line1 = line1.y1 if line1.y1 < line1.y2 else line1.y2
        highY_line1 = line1.y1 if line1.y1 > line1.y2 else line1.y2

        lowY_line2 = line2.y1 if line2.y1 < line2.y2 else line2.y2
        highY_line2 = line2.y1 if line2.y1 > line2.y2 else line2.y2

        if lowX_line1 > highX_line2:
            return False, False
        if lowX_line2 > highX_line1:
            return False, False
        if lowY_line1 > highY_line2:
            return False, False
        if lowY_line2 > highY_line1:
            return False, False
        if m1 is False:
            x = b1
            y_vals = [lowY_line2, lowY_line1, highY_line2, highY_line1]
            y_vals.sort()
            ans = [(x, yy) for yy in range(y_vals[1], y_vals[2] + 1)]
        else:
            x_vals = [lowX_line2, lowX_line1, highX_line2, highX_line1]
            ans = []
            for x in range(x_vals[1], x_vals[2] + 1):
                yy = m1 * x + b1
                ans.append((int(x), int(yy)))
        return True, ans
    elif m1 is False:
        x = b1
        y = m2 * x + b2
    elif m2 is False:
        x = b2
        y = m1 * x + b1
    else:
        x1 = (b2 - b1) / (m1 - m2)
        x2 = (b1 - b2) / (m2 - m1)
        if x1 != x2:
            print("Error")
        x = x1

    if y is False:
        y1 = m1 * x + b1
        y2 = m2 * x + b2
        if y1 != y2:
            print("Error")
        y = y1

    if between(y, line1.y1, line1.y2) and \
            between(y, line2.y1, line2.y2) and \
            between(x, line1.x1, line1.x2) and \
            between(x, line2.x1, line2.x2):
        return int(x), int(y)

    return False, False


def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    line_segments = []
    for line in lines:
        line_segments.append(LineSegment(
            x1=int(line.split(",")[0]),
            y1=int(line.split(",")[1].split(" ")[0]),
            x2=int(line.split(" ")[-1].split(",")[0]),
            y2=int(line.split(" ")[-1].split(",")[1])
        ))
    intersections = [(False, False)]  # I'm sorry
    for i in range(0, len(line_segments)):
        for j in range(i + 1, len(line_segments)):
            x, y = get_intersect(line_segments[i], line_segments[j])
            if x is True:
                for xy in y:
                    if xy not in intersections:
                        intersections.append(xy)
            elif (x, y) not in intersections:
                intersections.append((x, y))
    for i in intersections:
       print(i)
    # print(intersections)
    print(len(intersections) - 1) # -1 for false, false


answer("input.txt")
# 13102
# 5933
# 5911
# 5932
# 8186