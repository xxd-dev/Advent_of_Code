def solve():
    pos1, pos2 = [int(line[-1]) for line in open('inputs/day21.txt').read().split('\n')]
    score1 = score2 = rolls = 0
    while score1 < 1000 and score2 < 1000:
        for _ in range(3):
            rolls += 1
            pos1 += ((rolls-1) % 100) + 1
        pos1 = ((pos1 - 1) % 10) + 1
        score1 += pos1
        pos1, pos2, score1, score2 = pos2, pos1, score2, score1
    return min(score1, score2)*rolls, max(rec_play2(7, 8, 0, 0, dict()))


def rec_play2(pos1, pos2, score1, score2, lookup):
    if (pos1, pos2, score1, score2) in lookup:
        return lookup[(pos1, pos2, score1, score2)]
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1
    dirac = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    p1s = p2s = 0
    for i in range(3, 10):
        new_pos = ((pos1 + i - 1) % 10) + 1
        new_score = score1 + new_pos
        p2r, p1r = rec_play2(pos2, new_pos, score2, new_score, lookup)
        p1s += dirac[i] * p1r
        p2s += dirac[i] * p2r
    lookup[(pos1, pos2, score1, score2)] = p1s, p2s
    return p1s, p2s
