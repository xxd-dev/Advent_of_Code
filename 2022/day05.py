import copy
import re
from itertools import zip_longest


def solve():
    file = open('inputs/day05.txt').read()
    position, instructions = file.split('\n\n')
    original = [[c if c.isalpha() else None for c in line] for line in position.split('\n')]
    task1 = [[c for c in array if c] for array in list(map(list, zip_longest(*original)))[1::4]]
    task2 = copy.deepcopy(task1)
    for n, f, t in [map(int, v) for v in re.findall('(\d+).*(\d+).*(\d+)', instructions)]:
        task1[t - 1], task1[f - 1] = task1[f - 1][:n][::-1] + task1[t - 1], task1[f - 1][n:]
        task2[t - 1], task2[f - 1] = task2[f - 1][:n] + task2[t - 1], task2[f - 1][n:]
    return ''.join([elem[0] for elem in task1]), ''.join([elem[0] for elem in task2])
