import math

from aoc_util import as_2d_dict


def navigate_map(height_map, start, end):
    points = [start]
    visited = {start: 0}

    while len(points) > 0:
        curr = points.pop(0)
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            possible = (curr[0] + dir[0], curr[1] + dir[1])
            if possible in visited or possible not in height_map:
                continue
            if ord(height_map[possible]) > ord(height_map[curr]) + 1:
                continue
            if possible == end:
                # print('omg wtf found it', (possible, visited[curr] + 1))
                return visited[curr] + 1
            points.append(possible)
            visited[possible] = visited[curr] + 1
    return math.inf


def solve():
    height_map = as_2d_dict('inputs/day12.txt', False)[0]
    print(height_map)
    start = [(x, y) for (x, y) in height_map.keys() if height_map[(x, y)] == 'S'][0]
    end = [(x, y) for (x, y) in height_map.keys() if height_map[(x, y)] == 'E'][0]
    height_map[start] = 'a'
    height_map[end] = 'z'

    task1 = navigate_map(height_map, start, end)

    task2 = task1
    possible_starts = [(x, y) for (x, y) in height_map.keys() if height_map[(x, y)] == 'a']
    print(possible_starts)
    for start in possible_starts:
        task2 = min(task2, navigate_map(height_map, start, end))

    return task1, task2