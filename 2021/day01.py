depth = [int(line) for line in open('day01.txt').read().split('\n')]


def solve1():
    return len([1 for i in range(1, len(depth)) if depth[i] > depth[i - 1]])


def solve2():
    windows = [depth[i] + depth[i - 1] + depth[i - 2] for i in range(2, len(depth))]
    return len([1 for i in range(1, len(windows)) if windows[i] > windows[i - 1]])
