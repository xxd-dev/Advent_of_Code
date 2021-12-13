def solve():
    components = open('inputs/day13.txt').read().split('\n\n')
    folds = components[1].split('\n')
    dots = {(int(line.split(',')[0]), int(line.split(',')[1])) for line in components[0].split('\n')}
    for i in range(len(folds)):
        dots = fold(dots, folds[i])
        if i == 0:
            task1 = len(dots)
    return task1, '\n'.join([''.join(['#' if (i, j) in dots else ' ' for i in range(39)]) for j in range(6)])


def fold(dots, instruction):
    crease = int(instruction.split('=')[1])
    return {dot
            if 'x' in instruction and dot[0] < crease or 'y' in instruction and dot[1] < crease
            else (crease-abs(dot[0]-crease), dot[1]) if 'x' in instruction
            else (dot[0], crease-abs(dot[1]-crease))
            for dot in dots}
