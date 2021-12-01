from aoc_util import as_int_list


def solve():
    depth = as_int_list('inputs/day01.txt')
    return len([1 for i in range(1, len(depth)) if depth[i] > depth[i - 1]]), \
           len([1 for i in range(3, len(depth)) if depth[i] > depth[i - 3]])
