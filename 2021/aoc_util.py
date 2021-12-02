def as_int_list(file):
    return list(map(int, open(file).read().split('\n')))


def as_2d_list(file, delimiter, parseints):
    ret = []
    for line in open(file).read().split('\n'):
        sublist = line.split(delimiter)
        if parseints:
            for i in range(len(sublist)):
                if sublist[i].isnumeric():
                    sublist[i] = int(sublist[i])
        ret.append(sublist)
    return ret