import re
import math
from copy import deepcopy


def solve():
    monkeys = []
    for monkey_raw in open('inputs/day11.txt').read().split('\n\n'):
        lines = monkey_raw.split('\n')
        monkeys.append({"index": int(re.findall('[0-9]+', lines[0])[0]),
                        "items": [int(i) for i in re.findall('[0-9]+', lines[1])],
                        "operation": operation(
                            *re.findall('Operation: new = ([a-zA-Z0-9]+).([+*]).([a-zA-Z0-9]+)', lines[2])[0]),
                        "divisible": int(re.findall('[0-9]+', lines[3])[0]),
                        True: int(re.findall('[0-9]+', lines[4])[0]),
                        False: int(re.findall('[0-9]+', lines[5])[0])})
    return top_monkeys(True, 20, deepcopy(monkeys)), top_monkeys(False, 10000, monkeys)


def operation(n1, op, n2):
    if n1 == "old":
        if n2 == "old":
            if op == "*":
                return lambda old: old * old
            else:
                return lambda old: old + old
        else:
            n2 = int(n2)
            if op == "*":
                return lambda old: old * n2
            else:
                return lambda old: old + n2
    else:
        return operation(n2, n1, op)


def top_monkeys(divide_worry, iterations, monkeys):
    inspections = [0 for _ in range(len(monkeys))]
    mod = math.lcm(*[monkey['divisible'] for monkey in monkeys])
    for round in range(1, iterations + 1):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                inspections[monkey["index"]] += 1
                item = monkey["items"].pop(0)
                if divide_worry:
                    item = monkey["operation"](item)
                    item = item // 3
                else:
                    item = monkey["operation"](item) % mod
                if item % monkey["divisible"] == 0:
                    monkeys[monkey[True]]["items"].append(item)
                else:
                    monkeys[monkey[False]]["items"].append(item)
    inspections.sort(reverse=True)
    return inspections[0]*inspections[1]
