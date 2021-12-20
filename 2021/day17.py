import re


def solve():
    x_min, x_max, y_min, y_max = [int(x) for x in re.findall('-?[0-9]+', open('inputs/day17.txt').read())]
    task2 = 0
    for start_x in range(int(x_min ** 0.5), x_max + 1):
        for start_y in range(y_min, -y_min):
            pos_x = pos_y = 0
            vel_x, vel_y = start_x, start_y
            while pos_x <= x_max and pos_y >= y_min and (vel_x != 0 or x_min <= pos_x <= x_max):
                pos_x, pos_y = pos_x + vel_x, pos_y + vel_y
                vel_x, vel_y = max(0, vel_x - 1), vel_y - 1
                if x_min <= pos_x <= x_max and y_min <= pos_y <= y_max:
                    task2 += 1
                    break
    return y_min * (y_min + 1) // 2, task2