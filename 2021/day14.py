def solve():
    string, rules = open('inputs/day14.txt').read().split('\n\n')
    rules = [rule.split(' -> ') for rule in rules.split('\n')]
    for rule in rules:
        rule[1] = [rule[0][0]+rule[1][0], rule[1][0]+rule[0][1]]
    rules = dict(rules)
    counter = {rule: string.count(rule) for rule in rules}
    for i in range(40):
        counter = iterate(counter, rules)
        if i == 9:
            task1 = result(counter, string)
    return task1, result(counter, string)


def iterate(counter, rules):
    c2 = {key: 0 for key in rules}
    for value in counter:
        if counter[value] > 0:
            for nxt in rules[value]:
                c2[nxt] += counter[value]
    return c2


def result(counter, string):
    freq = {c: sum(counter[item] for item in counter if item[0] == c) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    freq[string[-1]] += 1
    return max(v for v in freq.values() if v > 0) - min(v for v in freq.values() if v > 0)
