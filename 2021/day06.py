def solve():
    n = [int(x) for x in open('inputs/day06.txt').read().split(',')]
    table = dict()
    return sum([rabbits_rec(rabbit, 80, table) for rabbit in n]), \
           sum([rabbits_rec(rabbit, 256, table) for rabbit in n])


def rabbits_rec(rabbit, amount, table):
    if amount == 0:
        return 1
    if (rabbit, amount) in table:
        return table[(rabbit, amount)]
    if rabbit == 0:
        value = rabbits_rec(6, amount - 1, table) + rabbits_rec(8, amount - 1, table)
    else:
        value = rabbits_rec(rabbit - 1, amount - 1, table)
    table[(rabbit, amount)] = value
    return value
