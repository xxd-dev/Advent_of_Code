from aoc_util import as_2d_list


def solve():
    numbers = as_2d_list('inputs/day03.txt', delimiter='', parseints=False)
    gamma_rate = ''.join(str(1*count(numbers, i)) for i in range(12))
    epsilon_rate = ''.join(['0' if c == '1' else '1' for c in gamma_rate])
    oxygen_generator = filter_false(numbers, True)
    co2_scrubber = filter_false(numbers, False)
    return int(gamma_rate, 2)*int(epsilon_rate, 2), int(oxygen_generator, 2)*int(co2_scrubber, 2)


def count(array, index):
    return sum(1 for c in array if c[index] == '1') >= len(array)/2


def filter_false(array, most):
    index = 0
    while len(array) > 1:
        keep = count(array, index)
        array = [item for item in array if (item[index] == '1') != keep ^ most]
        index = (index + 1) % len(array[0])
    return ''.join(array[0])
