from aoc_util import *


def solve():
    file = open('inputs/day24.txt').read().split('\n')
    instructions = [line.split(' ') for line in file]
    model_number = ['9' for _ in range(14)]
    model_number = [c for c in '61191516111322']
    return 0, 0
    # indices = []
    # for i in range(14):
    #     results = []
    #     model_number = ['9' for _ in range(14)]
    #     for j in range(1, 10):
    #         model_number[i] = str(j)
    #         results.append(ALU(instructions, model_number))
    #     for index in range(len(results))[::-1]:
    #         if results[index] == min(results):
    #             indices.append(str(index+1))
    #             break
    # print(''.join(indices))
    # print(ALU(instructions, indices))

    while True:
        ret = ALU(instructions, model_number)
        if ret < 5500000:
            print(''.join(model_number), ret)
        if ret == 0:
            return ''.join(model_number)
        model_number = sub1(model_number)
    return 0, 0

# 99999991633866 3703514213


def sub1(model_number):
    number = int(''.join(model_number))
    number -= 1
    new_number = '{:014d}'.format(number)
    while '0' in new_number:
        number = int(''.join(new_number))
        number -= 1
        new_number = '{:014d}'.format(number)
    return new_number


def ALU(instructions, model_number):
    inputs = [v for v in model_number]
    reg = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for instruction in instructions:
        if instruction[0] == 'inp':
            print(reg)
            reg[instruction[1]] = int(inputs.pop(0))
        elif instruction[0] == 'add':
            reg[instruction[1]] += (int(instruction[2]) if instruction[2] not in reg else reg[instruction[2]])
        elif instruction[0] == 'mul':
            reg[instruction[1]] *= (int(instruction[2]) if instruction[2] not in reg else reg[instruction[2]])
        elif instruction[0] == 'div':
            reg[instruction[1]] = reg[instruction[1]] // (int(instruction[2]) if instruction[2] not in reg else reg[instruction[2]])
        elif instruction[0] == 'mod':
            reg[instruction[1]] = reg[instruction[1]] % (int(instruction[2]) if instruction[2] not in reg else reg[instruction[2]])
        else:
            reg[instruction[1]] = int(reg[instruction[1]] == (int(instruction[2]) if instruction[2] not in reg else reg[instruction[2]]))
    return reg['z']
