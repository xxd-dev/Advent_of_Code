def solve():
    working_dir = root = {}
    for cmd in open('inputs/day07.txt').read().split('\n'):
        if cmd.startswith('$ cd'):
            working_dir = root if cmd[5:] == '/' else working_dir[cmd[5:]]
        elif cmd[0] != '$':
            contents, file = cmd.split(' ')
            working_dir[file] = ({'..': working_dir} if contents == 'dir' else int(contents))
    root_weight, weights = get_weight(root, [])
    task1 = sum([weight if weight <= 100000 else 0 for weight in weights])
    needed = root_weight - 40000000
    for weight in sorted(weights):
        if weight >= needed:
            return task1, weight


def get_weight(working_dir, weights):
    total_size = 0
    for file, contents in [(file, contents) for (file, contents) in working_dir.items() if file != '..']:
        total_size += contents if isinstance(contents, int) else get_weight(working_dir[file], weights)[0]
    weights.append(total_size)
    return total_size, weights
