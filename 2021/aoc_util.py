import numpy as np
import cv2
import numpy
import pytesseract
from PIL import Image


def as_int_list(file):
    return list(map(int, open(file).read().split('\n')))


def as_2d_list(file, delimiter, parseints):
    ret = []
    for line in open(file).read().split('\n'):
        if delimiter == '':
            sublist = [char for char in line]
        else:
            sublist = line.split(delimiter)
        if parseints:
            for i in range(len(sublist)):
                if sublist[i].isnumeric():
                    sublist[i] = int(sublist[i])
        ret.append(sublist)
    return ret


def as_2d_dict(file, parseints):
    temp_list = as_2d_list(file, '', parseints)
    ret = dict()
    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            ret[(i, j)] = temp_list[i][j]
    return ret, len(temp_list), len(temp_list[0])


def sign(number):
    if number > 0:
        return 1
    if number < 0:
        return -1
    return 0


def neighbours_2D(tuple):
    return [(tuple[0]+dir[0], tuple[1]+dir[1])
            for dir in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]]


def ocr(array):
    img = numpy.array(array, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, None, fx=15, fy=15, interpolation=cv2.INTER_NEAREST)
    img = cv2.erode(img, np.ones((5, 5), np.uint8), iterations=1)
    # pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/4.1.3/bin/tesseract'
    text = pytesseract.image_to_string(img, lang='eng')
    print(": "+text)
    return 'a'


def prod(array):
    a = 1
    for item in array:
        a *= item
    return a


# from aoc_util import *
#
#
# def solve():
#     components = open('inputs/day13.txt').read().split('\n\n')
#     folds = [[int(x) if x.isdigit() else x for x in instruction.split(' ')[-1].split('=')]
#              for instruction in components[1].split('\n')]
#     dots = {tuple(int(x) for x in line.split(',')) for line in components[0].split('\n')}
#     for i in range(len(folds)):
#         dots = fold(dots, folds[i])
#         if i == 0:
#             task1 = len(dots)
#
#     valuesx = [point[0] for point in dots]
#     valuesy = [point[1] for point in dots]
#     array = []
#     for i in range(min(valuesy)-1, max(valuesy)+2):
#         tmp = []
#         for j in range(min(valuesx)-1, max(valuesx)+2):
#             tmp.append([0, 0, 0] if (j, i) in dots else [255, 255, 255])
#         array.append(tmp)
#     print(ocr(array))
#     return task1, '\n'.join([''.join(['#' if (i, j) in dots else ' ' for i in range(39)]) for j in range(6)])
#
#
# def fold(dots, instruction):
#     return {dot
#             if instruction[0] == 'x' and dot[0] < instruction[1] or instruction[0] == 'y' and dot[1] < instruction[1]
#             else (instruction[1]-abs(dot[0]-instruction[1]), dot[1]) if 'x' in instruction
#             else (dot[0], instruction[1]-abs(dot[1]-instruction[1])) for dot in dots}
