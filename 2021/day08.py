def solve():
    entries = [[[''.join(sorted(digit)) for digit in part.split(' ')] for part in entry.split(' | ')] for entry in
               open('inputs/day08.txt').read().split('\n')]
    return sum(sum(1 for digit in entry[1] if len(digit) in [2, 3, 4, 7]) for entry in entries), \
           sum(decode(entry) for entry in entries)


def decode(entry):
    table = ['' for _ in range(10)]
    lengths = {2: 1, 3: 7, 4: 4, 7: 8}
    for digit in entry[0]:
        if len(digit) in lengths:
            table[lengths[len(digit)]] = digit
    for digit in entry[0]:
        if len(digit) == 5:
            if len([1 for segment in digit if segment not in table[4]]) == 3:
                table[2] = digit
            elif len([1 for segment in digit if segment not in table[1]]) == 3:
                table[3] = digit
            else:
                table[5] = digit
        elif len(digit) == 6:
            if len([1 for segment in digit if segment not in table[4]]) == 2:
                table[9] = digit
            elif len([1 for segment in digit if segment not in table[1]]) == 4:
                table[0] = digit
            else:
                table[6] = digit
    return int(''.join(str(table.index(n)) for n in entry[1]))
