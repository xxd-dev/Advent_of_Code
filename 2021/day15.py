from aoc_util import *
import bisect


def solve():
    risk_levels, width, height = as_2d_dict('inputs/day15.txt', True)
    return find(risk_levels, width, height, 1), find(risk_levels, width, height, 5)


def find(risk_levels, width, height, factor):
    distances = dict()
    current = [(0, 0, 0)]
    while current:
        (dist, x, y) = current.pop(0)
        cost = ((risk_levels[(x % width, y % height)] + x//width + y//height - 1) % 9) + 1 + dist
        if (x, y) not in distances:
            distances[(x, y)] = cost
            if x == width * factor - 1 and y == height * factor - 1:
                break
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (x + dir[0], y + dir[1]) not in distances \
                        and 0 <= x + dir[0] < width*factor and 0 <= y + dir[1] < height*factor:
                    bisect.insort(current, (cost, x + dir[0], y + dir[1]))
    return distances[(width * factor - 1, height * factor - 1)] - risk_levels[(0, 0)]
