from aoc_util import *
import re
all_scanners = set()


def solve():
    beacons = dict()
    for s in open('inputs/day19.txt').read().split('\n\n'):
        key, *values = s.split('\n')
        key = int(re.findall('[0-9]+', key)[0])
        values = [tuple(int(x) for x in line.split(',')) for line in values]
        beacons[key] = values
    triangles = dict()
    for key in beacons:
        tmp = dict()
        beacon = beacons[key]
        for i in range(len(beacon)):
            for j in range(i+1, len(beacon)):
                for k in range(j+1, len(beacon)):
                    tmp[tuple(sorted(circumference(beacon[i], beacon[j], beacon[k])))] = [beacon[i], beacon[j], beacon[k]]
        triangles[key] = tmp
    reachable = {n: [] for n in range(len(beacons))}
    for key1 in range(len(beacons)):
        for key2 in range(key1, len(beacons)):
            if key1 != key2:
                if len([item for item in triangles[key1].keys() if item in triangles[key2].keys()]) >= 220:
                    reachable[key1].append(key2)
                    reachable[key2].append(key1)
    seen = set()
    scanners = []
    seen.add(0)
    for item in reachable[0]:
        rec_align(0, item, beacons, triangles, reachable, seen, scanners)
    all_beacons = {beacon for sub in beacons for beacon in beacons[sub]}
    max_dist = 0
    scanners.append((0, 0, 0))
    for i in range(len(scanners)):
        for j in range(i+1, len(scanners)):
            max_dist = max(man_dist(scanners[i], scanners[j]), max_dist)
    return len(all_beacons), max_dist


def rec_align(id1, id2, beacons, ids, reachable, seen, scanners):
    align(beacons, ids, id1, id2, scanners)
    seen.add(id2)
    for new_id in reachable[id2]:
        if new_id not in seen:
            rec_align(id2, new_id, beacons, ids, reachable, seen, scanners)


def align(beacons, ids, id1, id2, scanners):
    alignment_triangle = (0, 0, 0)
    for triangle in ids[id1]:
        if triangle in ids[id2] and len(set(triangle)) == 3:
            alignment_triangle = triangle
            break
    triangle1 = ids[id1][alignment_triangle]
    triangle2 = ids[id2][alignment_triangle]
    circumference1 = circumference(ids[id1][alignment_triangle][0], ids[id1][alignment_triangle][1], ids[id1][alignment_triangle][2])
    circumference2 = circumference(ids[id2][alignment_triangle][0], ids[id2][alignment_triangle][1], ids[id2][alignment_triangle][2])
    triangle2 = [triangle2[circumference2.index(circumference1[i])] for i in range(3)]
    for rot in range(24):
        triangle_p = [rotate(t, rot) for t in triangle2]
        if all((triangle1[0][i // 2] - triangle1[1 + i % 2][i // 2]) == (triangle_p[0][i // 2] - triangle_p[1 + i % 2][i // 2]) for i in range(6)):
            triangle2 = triangle_p
            break
    delta = (triangle1[0][0] - triangle2[0][0], triangle1[0][1] - triangle2[0][1], triangle1[0][2] - triangle2[0][2])
    scanners.append(delta)
    for i in range(len(beacons[id2])):
        beacons[id2][i] = add(delta, rotate(beacons[id2][i], rot))
    for key in ids[id2]:
        for i in range(len(ids[id2][key])):
            ids[id2][key][i] = add(delta, rotate(ids[id2][key][i], rot))


def circumference(t1, t2, t3):
    return [dist(t2, t3), dist(t1, t3), dist(t1, t2)]


def rotate(tuple, n):
    n1 = tuple[[0, 1, 2, 2, 1, 0][n%6]] * (1 if n < 12 else -1)
    n2 = tuple[[1, 2, 0, 1, 0, 2][n%6]] * (1 if (n//6)%2 == 0 else -1)
    n3 = tuple[[2, 0, 1, 0, 2, 1][n%6]] * [1, -1, -1, 1, -1, 1, 1, -1][(n//3)]
    return n1, n2, n3


def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]


def dist(tuple1, tuple2):
    return (tuple1[0]-tuple2[0])**2 + (tuple1[1]-tuple2[1])**2 + (tuple1[2]-tuple2[2])**2


def man_dist(t1, t2):
    return abs(t1[0]-t2[0])+abs(t1[1]-t2[1])+abs(t1[2]-t2[2])
