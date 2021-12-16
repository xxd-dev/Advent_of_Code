from aoc_util import *


def solve():
    return parse([''.join(['{:04b}'.format('0123456789ABCDEF'.index(c)) for c in open('inputs/day16.txt').read()])])


def pop(data, n):
    ret = data[0][:n]
    data[0] = data[0][n:]
    return ret


def parse(data):
    func = {0: lambda array: sum(array),
            1: lambda array: prod(array),
            2: lambda array: min(array),
            3: lambda array: max(array),
            5: lambda array: int(array[0] > array[1]),
            6: lambda array: int(array[0] < array[1]),
            7: lambda array: int(array[0] == array[1])}
    v, t = int(pop(data, 3), 2), int(pop(data, 3), 2)
    if t == 4:
        return v, int(''.join([pop(data, 5)[1:] for _ in range(data[0][::5].index('0') + 1)]), 2)
    i = int(pop(data, 1), 2)
    if i == 1:
        evaluated = [parse(data) for _ in range(int(pop(data, 11), 2))]
    else:
        evaluated = []
        sub = [pop(data, int(pop(data, 15), 2))]
        while len(sub[0]) > 0:
            evaluated.append(parse(sub))
    return v + sum([item[0] for item in evaluated]), func[t]([item[1] for item in evaluated])
