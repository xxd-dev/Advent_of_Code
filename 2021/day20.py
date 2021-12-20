def solve():
    enhancement, map = open('inputs/day20.txt').read().split('\n\n')
    new = dict()
    map = map.split('\n')
    for i in range(len(map)):
        for j in range(len(map[i])):
            new[(i, j)] = 1 if map[i][j] == '#' else 0
    map = new
    enhancement = [1 if c == '#' else 0 for c in enhancement]
    for iter in range(50):
        nxt = dict()
        for i in range(-100+iter, 200-iter):
            for j in range(-100+iter, 200-iter):
                bin = 256*map.get((i-1, j-1), 0)+128*map.get((i-1, j), 0)+64*map.get((i-1, j+1), 0)+\
                      32*map.get((i, j-1), 0)+16*map.get((i, j), 0)+8*map.get((i, j+1), 0)+\
                      4*map.get((i+1, j-1), 0)+2*map.get((i+1, j), 0)+map.get((i+1, j+1), 0)
                new_val = enhancement[bin]
                nxt[(i, j)] = new_val
        map = nxt
        if iter == 1:
            task1 = len([x for x in map.values() if x == 1])
    return task1, len([x for x in map.values() if x == 1])
