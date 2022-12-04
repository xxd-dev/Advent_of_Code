import re


def solve():
    file = open('inputs/day04.txt').read().split('\n')
    task1 = task2 = 0
    for line in file:
        x1, y1, x2, y2 = [int(n) for n in re.findall('\d+', line)]
        task1 += (x2 <= x1 <= y1 <= y2 or x1 <= x2 <= y2 <= y1)
        task2 += (x1 <= y2 and x2 <= y1)
    return task1, task2
