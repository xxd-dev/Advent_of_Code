def solve():
    course = [(item.split(' ')[0], int(item.split(' ')[1])) for item in open('inputs/day02.txt').read().split('\n')]
    horizontal = sum([cmd[1] for cmd in course if cmd[0] == "forward"])
    vertical1 = sum([cmd[1] for cmd in course if cmd[0] == "down"]) - \
                sum([cmd[1] for cmd in course if cmd[0] == "up"])
    vertical2 = aim = 0
    for cmd in course:
        if cmd[0] == 'forward':
            vertical2 += aim * cmd[1]
        else:
            aim += ((cmd[0] == 'down') - (cmd[0] == 'up')) * cmd[1]
    return horizontal * vertical1, horizontal * vertical2
