def solve():
    crabs = sorted([int(x) for x in open('inputs/day07.txt').read().split(',')])
    median = crabs[len(crabs)//2]
    task1 = sum([abs(x-median) for x in crabs])
    d = 1 if fuel_score(crabs, median+1) < fuel_score(crabs, median) else -1
    while fuel_score(crabs, median) > fuel_score(crabs, median + d):
        median += d
    return task1, fuel_score(crabs, median)


def fuel_score(n, m):
    return sum((abs(x-m) * (abs(x-m)+1))//2 for x in n)
