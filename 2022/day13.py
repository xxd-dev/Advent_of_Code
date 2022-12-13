import functools


def solve():
    lists = open('inputs/day13.txt').read().split('\n\n')
    count = 0
    for index, tuple in enumerate(lists):
        list1, list2 = tuple.split('\n')
        list_left = eval(list1)
        list_right = eval(list2)
        if is_ordered(list_left, list_right) == 1:
            count += index + 1

    lists = [eval(line) for line in open('inputs/day13.txt').read().split('\n') if line != ""]
    spacer1 = [[2]]
    lists.append(spacer1)
    spacer2 = [[6]]
    lists.append(spacer2)
    lists = sorted(lists, key=functools.cmp_to_key(is_ordered), reverse=True)

    return count, (lists.index(spacer1)+1) * (lists.index(spacer2)+1)


def is_ordered(list1, list2):
    for index in range(min(len(list1), len(list2))):
        if isinstance(list1[index], int) and isinstance(list2[index], int):
            if list1[index] < list2[index]:
                return 1
            elif list1[index] > list2[index]:
                return -1
        elif isinstance(list1[index], int):
            sub = is_ordered([list1[index]], list2[index])
            if sub != 0:
                return sub
        elif isinstance(list2[index], int):
            sub = is_ordered(list1[index], [list2[index]])
            if sub != 0:
                return sub
        else:
            sub = is_ordered(list1[index], list2[index])
            if sub != 0:
                return sub
    if len(list1) < len(list2):
        return 1
    elif len(list1) > len(list2):
        return -1
    else:
        return 0
