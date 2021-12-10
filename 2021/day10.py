import re


def solve():
    lines = [strip(line) for line in open('inputs/day10.txt').read().split('\n')]
    illegal_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    a = sorted([points(x[1]) for x in lines if x[0]])
    return sum(illegal_table[line[1]] for line in lines if not line[0]), a[len(a)//2]


def strip(line):
    while len(re.findall('\\(\\)|\\[\\]|\\{\\}|<>', line)) > 0:
        line = re.sub('\\(\\)|\\[\\]|\\{\\}|<>', '', line)
    cut = min([line.index(c) if c in line else len(line)+1 for c in ')]}>'])
    return (False, line[cut]) if cut != len(line)+1 else (True, line[:cut])


def points(array):
    score = 0
    for char in array[::-1]:
        score = (5 * score) + ' ([{<'.index(char)
    return score
