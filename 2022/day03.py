def solve():
    file = open('inputs/day03.txt').read().split('\n')
    alphabet = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    task1 = sum([alphabet.index((set(rucksack[:len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2:])).pop())
                 for rucksack in file])
    task2 = sum([alphabet.index((set(file[i]) & set(file[i+1]) & set(file[i+2])).pop())
                 for i in range(0, len(file), 3)])
    return task1, task2
