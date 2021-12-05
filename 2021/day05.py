from aoc_util import *


def solve():
    lines = [[[int(x) for x in tuple.split(',')] for tuple in line.split(' -> ')]
             for line in open('inputs/day05.txt').read().split('\n')]
    map1 = dict()
    map2 = dict()
    for line in lines:
        if not_diagonal(line):
            add_to_map(line, map1)
            add_to_map(line, map2)
        else:
            add_to_map(line, map2)
    return sum([v >= 2 for v in map1.values()]), sum([v >= 2 for v in map2.values()])


def add_to_map(line, map):
    steps = max(abs(line[0][0]-line[1][0]), abs(line[0][1]-line[1][1])) + 1
    f1 = sign(line[1][0]-line[0][0])
    f2 = sign(line[1][1]-line[0][1])
    for i in range(steps):
        map[(line[0][0] + i * f1, line[0][1] + i * f2)] = map.get((line[0][0] + i * f1, line[0][1] + i * f2), 0) + 1


def not_diagonal(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]
