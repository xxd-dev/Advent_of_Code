def solve():
    illegal_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    lines = [corrupted(line) for line in open('inputs/day10.txt').read().split('\n')]
    invalid_score = sum(illegal_table[line[1]] for line in lines if not line[0])
    valid_scores = sorted([points(line[1]) for line in lines if line[0]])
    return invalid_score, valid_scores[len(valid_scores)//2]


def corrupted(line):
    stack = []
    for char in line:
        if len(stack) > 0 and (stack[-1], char) in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
            stack.pop(-1)
        elif char in ')}>]':
            return False, char
        else:
            stack.append(char)
    return True, stack


def points(array):
    score = 0
    for char in array[::-1]:
        score = (5 * score) + '.([{<'.index(char)
    return score
