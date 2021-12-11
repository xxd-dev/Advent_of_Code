from aoc_util import *


def solve():
    octopuses, _, _ = as_2d_dict('inputs/day11.txt', True)
    index = total_flashes = 0
    flashed = set()
    while len(flashed) < 100 or index < 100:
        flashed = set()
        for key in octopuses:
            octopuses[key] += 1
        while any(value > 9 for value in octopuses.values()):
            for key in octopuses:
                if octopuses[key] > 9:
                    octopuses[key] = 0
                    flashed.add(key)
                    for neighbour in neighbours_2D(key):
                        if neighbour not in flashed and neighbour in octopuses:
                            octopuses[neighbour] += 1
        index += 1
        if index <= 100:
            total_flashes += len(flashed)
    return total_flashes, index
