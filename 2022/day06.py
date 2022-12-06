def solve():
    file = open('inputs/day06.txt').read()
    return find_marker(file, 4), find_marker(file, 14)


def find_marker(string, length):
    for i in range(len(string)-length):
        if len(set(string[i:i+length])) == length:
            return i+length
