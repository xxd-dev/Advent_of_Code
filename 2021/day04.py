import re


def solve():
    components = open('inputs/day04.txt').read().split('\n\n')
    numbers = [int(n) for n in components[0].split(',')]
    boards = [[[[int(n) for n in re.findall('[0-9]+', line)] for line in item.split('\n')],
               [[False for _ in range(5)]for _ in range(5)]] for item in components[1:]]
    wins = []
    for index in range(len(numbers)):
        for board in boards:
            for (i, j) in [(i, j) for i in range(5) for j in range(5)]:
                if board[0][i][j] == numbers[index]:
                    board[1][i][j] = True
        for board_num in [i for i in range(len(boards))[::-1] if is_winner(boards[i])]:
            wins.append(winning_score(boards[board_num]) * numbers[index])
            boards.remove(boards[board_num])
    return wins[0], wins[-1]


def is_winner(board):
    return any([board[1][i][0] and board[1][i][1] and board[1][i][2] and board[1][i][3] and board[1][i][4] or
                board[1][0][i] and board[1][1][i] and board[1][2][i] and board[1][3][i] and board[1][4][i] for i in range(5)])


def winning_score(board):
    return sum([board[0][i][j] for i in range(5) for j in range(5) if not board[1][i][j]])
