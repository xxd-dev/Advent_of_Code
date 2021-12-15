def solve():
    string, rules = open('inputs/day14.txt').read().split('\n\n')
    rules = [rule.split(' -> ') for rule in rules.split('\n')]
    rules = {rule[0]: [rule[0][0]+rule[1][0], rule[1][0]+rule[0][1]] for rule in rules}
    rules = {key: [item for item in rules if key in rules[item]]
              for key in [i for sub in rules.values() for i in sub] + [i for i in rules.keys()]}
    counter = {rule: string.count(rule) for rule in rules}
    for i in range(40):
        counter = {key: sum(counter[value] for value in rules.get(key, [])) for key in rules}
        if i == 9:
            task1 = result(counter, string)
    return task1, result(counter, string)


def result(counter, string):
    freq = {c: sum(counter[item] for item in counter if item[0] == c) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    freq[string[-1]] += 1
    return max(v for v in freq.values() if v > 0) - min(v for v in freq.values() if v > 0)