from aoc_util import *


def solve():
    input = as_2d_list('inputs/day12.txt', '-', False)
    paths = {cave: [] for cave in set(item for sublist in input for item in sublist)}
    for line in input:
        paths[line[0]].append(line[1])
        paths[line[1]].append(line[0])
    return find_possible([['1', 'start']], paths), find_possible([['0', 'start']], paths)


def find_possible(current, paths):
    possible = set()
    while len(current) > 0:
        item = current.pop()
        pos = item[-1]
        if pos == 'end':
            possible.add(','.join(item))
        else:
            for available in paths[pos]:
                if ord(available[0]) <= ord('Z') or available not in item:
                    current.append(item + [available])
                elif item[0] == '0' and available != 'start':
                    current.append(['1'] + item[1:] + [available])
    return len(possible)
