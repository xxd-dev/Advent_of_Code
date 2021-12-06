def solve():
    rabbits = [int(n) for n in open('inputs/day06.txt').read().split(',')]
    table = dict()
    return sum([population(rabbit, 80, table) for rabbit in rabbits]), \
           sum([population(rabbit, 256, table) for rabbit in rabbits])


def population(rabbit, amount, table):
    if amount == 0:
        return 1
    if (rabbit, amount) in table:
        return table[(rabbit, amount)]
    if rabbit == 0:
        value = population(6, amount - 1, table) + population(8, amount - 1, table)
    else:
        value = population(rabbit - 1, amount - 1, table)
    table[(rabbit, amount)] = value
    return value
