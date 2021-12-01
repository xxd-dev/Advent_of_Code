def as_int_list(file):
    return list(map(int, open(file).read().split('\n')))
