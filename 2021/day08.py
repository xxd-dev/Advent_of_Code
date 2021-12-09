def solve():
    entries = [[[''.join(sorted(digit)) for digit in part.split(' ')] for part in entry.split(' | ')] for entry in
               open('inputs/day08.txt').read().split('\n')]
    return sum(sum(1 for digit in entry[1] if len(digit) in [2, 3, 4, 7]) for entry in entries), \
           sum(decode(entry) for entry in entries)


def decode(entry):
    lookup = {42: 0, 17: 1, 34: 2, 39: 3, 30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9}
    occurrences = dict()
    for c in 'abcdefg':
        occurrences[c] = ''.join(entry[0]).count(c)
    return int(''.join(str(lookup[sum(occurrences[c] for c in digit)]) for digit in entry[1]))
