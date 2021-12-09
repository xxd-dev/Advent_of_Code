from aoc_util import *


def solve():
    heightmap, w, h = as_2d_dict('inputs/day09.txt', parseints=True)
    lows = [(x, y) for x in range(w) for y in range(h) if
            all(heightmap[(x, y)] < heightmap.get((x+d[0], y+d[1]), 9) for d in [(0, 1), (0, -1), (1, 0), (-1, 0)])]
    basins = []
    for low in lows:
        seen = set()
        curr = [low]
        while len(curr) > 0:
            p = curr.pop()
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (p[0]+d[0], p[1]+d[1]) not in seen and heightmap.get((p[0]+d[0], p[1]+d[1]), 9) < 9:
                    curr.append((p[0]+d[0], p[1]+d[1]))
                    seen.add((p[0]+d[0], p[1]+d[1]))
        basins.append(len(seen))
    basins.sort(reverse=True)
    return sum(heightmap[x]+1 for x in lows), basins[0]*basins[1]*basins[2]
