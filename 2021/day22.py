import re


def solve():
    cubes = []
    for line in open('inputs/day22.txt').read().split('\n'):
        x1, x2, y1, y2, z1, z2 = [int(n) for n in re.findall('-?[0-9]+', line)]
        cubes.append([x1, x2 + 1, y1, y2 + 1, z1, z2 + 1, int(line[1] == 'n')])
    small_cubes = [[v for v in cube] for cube in cubes if not
    (cube[1] < -50 or cube[0] > 50 or cube[3] < -50 or cube[2] > 50 or cube[5] < -50 or cube[4] > 50)]
    return count_cubes(small_cubes), count_cubes(cubes)


def count_cubes(cubes):
    seen = []
    for cube in cubes:
        curr = []
        for item in seen:
            if cube[1] > item[0] and cube[0] < item[1] and cube[3] > item[2] and cube[2] < item[3] \
                    and cube[5] > item[4] and cube[4] < item[5]:
                for i in range(6):
                    if i % 2 == 0 and item[i] < cube[i] or i % 2 == 1 and item[i] > cube[i]:
                        cut = [v for v in item]
                        cut[1 - (i % 2) + (i - i % 2)] = cube[i]
                        item[i] = cube[i]
                        curr.append(cut)
            else:
                curr.append(item)
        curr.append(cube)
        seen = curr
    return sum((item[1] - item[0]) * (item[3] - item[2]) * (item[5] - item[4]) for item in seen if item[6])
