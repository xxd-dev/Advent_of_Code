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
