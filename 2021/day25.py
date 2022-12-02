from aoc_util import *

def solve():
    file = open('inputs/day25.txt').read().split('\n')
    cucumbers_e = set()
    cucumbers_s = set()
    height = len(file)
    width = len(file[0])
    for x in range(len(file)):
        for y in range(len(file[x])):
            if file[x][y] == '.':
                continue
            if file[x][y] == '>':
                cucumbers_e.add((x, y))
            else:
                cucumbers_s.add((x, y))
    seen = set()
    iterations = 0

    while not (frozenset(cucumbers_e), frozenset(cucumbers_s)) in seen:
        seen.add((frozenset(cucumbers_e), frozenset(cucumbers_s)))
        cucumbers_e, cucumbers_s = iterate(cucumbers_e, cucumbers_s, width, height)
        iterations += 1
    print(iterations)


    return 0, 0


def iterate(cucumbers_e, cucumbers_s, width, height):
    new_e = set()
    for item in cucumbers_e:
        to = (item[0], (item[1]+1)%width)
        if to in cucumbers_e or to in cucumbers_s:
            new_e.add(item)
        else:
            new_e.add(to)
    new_s = set()
    for item in cucumbers_s:
        to = ((item[0]+1)%height, item[1])
        if to in cucumbers_s or to in new_e:
            new_s.add(item)
        else:
            new_s.add(to)
    return new_e, new_s


def prnt(cucumbers_e, cucumbers_s, width, height):
    for i in range(height):
        for j in range(width):
            if (i, j) in cucumbers_e:
                print('>', end='')
            elif (i, j) in cucumbers_s:
                print('v', end='')
            else:
                print('.', end='')
        print()
