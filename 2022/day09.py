def solve():
    file = open('inputs/day09.txt').read().split('\n')
    instructions = []
    for line in file:
        direction, count = line.split(' ')
        for i in range(int(count)):
            instructions.append(direction)
    return knot_chain(instructions, 2), knot_chain(instructions, 10)


def knot_chain(instructions, length):
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    visited = set([(0, 0)])
    knots = [(0, 0) for i in range(length)]
    for instr in instructions:
        direction = dirs[instr]
        knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])
        for i in range(1, len(knots)):
            knots[i] = follow(knots[i - 1][0], knots[i - 1][1], knots[i][0], knots[i][1])
        visited.add(knots[-1])
    return len(visited)


def follow(xs, ys, xf, yf):
    dx = abs(xs-xf)
    dy = abs(ys-yf)
    if dx < 2 and dy < 2:
        return xf, yf
    if dx >= 2:
        new_x = (xs + xf)//2
        return new_x, ys
    new_y = (ys + yf) // 2
    return xs, new_y
