def solve():
    file = open('inputs/day01.txt').read()
    calories = sorted([sum([int(n) for n in elv.split('\n')]) for elv in file.split('\n\n')])[::-1]
    return calories[0], sum(calories[0:3])
