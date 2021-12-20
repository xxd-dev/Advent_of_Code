def solve():
    file = open('inputs/day18.txt').read().split('\n')
    numbers = []
    for number in file:
        ret = []
        depth = 0
        for char in number:
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            elif char.isnumeric():
                ret.append([int(char), depth])
        numbers.append(ret)
    final_sum = numbers[0]
    for i in range(1, len(numbers)):
        final_sum = reduce(add(final_sum, numbers[i]))
    max_mag = 0
    for a in numbers:
        for b in numbers:
            max_mag = max(max_mag, magnitude(reduce(add(a, b))))
    return magnitude(final_sum), max_mag


def reduce(number):
    while any(n[1] > 4 for n in number) or any(n[0] > 9 for n in number):
        if any(n[1] > 4 for n in number):
            number = explode(number)
        else:
            number = split(number)
    return number


def split(number):
    for i in range(len(number)):
        if number[i][0] > 9:
            a = number[i][0] // 2
            b = number[i][0] - a
            val, depth = number.pop(i)
            number.insert(i, [b, depth + 1])
            number.insert(i, [a, depth + 1])
            return number


def explode(number):
    for i in range(len(number)):
        if number[i][1] > 4:
            if i-1 >= 0:
                number[i-1][0] += number[i][0]
            if i+2 < len(number):
                number[i+2][0] += number[i+1][0]
            number.pop(i+1)
            val, depth = number.pop(i)
            number.insert(i, [0, depth-1])
            return number


def add(number1, number2):
    tmp = []
    for number in number1:
        tmp.append([number[0], number[1]+1])
    for number in number2:
        tmp.append([number[0], number[1]+1])
    return tmp


def magnitude(number):
    while len(number) > 1:
        for i in range(len(number)-1):
            if number[i][1] == number[i+1][1]:
                break
        v1, d1 = number.pop(i)
        number[i][0] = 3 * v1 + 2 * number[i][0]
        number[i][1] -= 1
    return number[0][0]
