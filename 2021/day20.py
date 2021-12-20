from scipy.ndimage import convolve  # had to use this to get runtime below 1s
import numpy as np


def solve():
    enhancement, floor = open('inputs/day20.txt').read().split('\n\n')
    enhancement = np.array([int(c == '#') for c in enhancement])
    floor = np.pad(np.array([[int(c == '#') for c in line] for line in floor.split('\n')]), 51, mode='constant')
    mult = np.array([2 ** n for n in range(9)]).reshape(3, 3)
    for iteration in range(50):
        floor = enhancement[convolve(floor, mult, mode="nearest")]
        if iteration == 1:
            task1 = floor.sum()
    return task1, floor.sum()
