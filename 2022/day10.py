def solve():
    file = open('inputs/day10.txt').read().split()
    screen = [['  ' for _ in range(40)] for _ in range(6)]
    sprite_pos, signal_strength = 1, 0
    for cycle, instruction in enumerate(file):
        if (cycle+1) % 40 == 20:
            signal_strength += sprite_pos*(cycle+1)
        if abs(cycle % 40 - sprite_pos) <= 1:
            screen[cycle // 40][cycle % 40] = '██'
        if not'a' <= instruction[0] <= 'n':
            sprite_pos += int(instruction)
    return signal_strength, '\n'+'\n'.join([''.join(line) for line in screen])
