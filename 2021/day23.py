from aoc_util import *
import re


def solve():
    return 0, 0
    file = open('inputs/day23.txt').read()
    rooms = [['.' for i in range(7)], ['.', '.'], ['.', '.'], ['.', '.'], ['.', '.']]
    items = [item for item in re.findall('[A-D]', file)]
    for i, item in enumerate(items):
        rooms[1+(i % 4)][i // 4] = item

    print(rooms)

    print(possible_moves((0, rooms)))
    return 0, 0


def possible_moves(input):
    score, floor = input
    possible = []
    for i, amphipods in enumerate(floor[1:]):
        print(i, amphipods)
        if amphipods[0] != '.' or amphipods[1] != '.':
            print(reachable(floor, i))


def move_back(floor, hall_index):
    if floor[0][hall_index] == '.':
        return []
    val = floor[0][hall_index]
    room_index = '_ABCD'.index(val)
    if not (floor[room_index][0] == '.' and floor[room_index][1] == val or floor[room_index][0] == '.' and floor[room_index][1] == '.'):
        return []
    if room_index <= hall_index <= room_index+1:
        return 1
    if hall_index < room_index:
        if any(val != '.' for val in floor[0][hall_index:room_index]):
            return []


def reachable(floor, room_index):
    hallway, *rooms = floor
    if rooms[room_index][0] == '.' and rooms[room_index][1] == '.':
        return []
    offset = int(rooms[room_index][0] == '.')
    indices = []
    index = room_index + 1
    score = 2
    while index >= 0 and hallway[index] == '.':
        if index == 0:
            score -= 1
        indices.append((index, score+offset))
        index -= 1
        score += 2
    index = room_index + 2
    score = 2
    while index < len(hallway) and hallway[index] == '.':
        if index == len(hallway)-1:
            score -= 1
        indices.append((index, score+offset))
        index += 1
        score += 2
    return indices
