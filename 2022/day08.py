def solve():
    grid = [[int(t) for t in row] for row in open('inputs/day08.txt').read().split('\n')]
    vis = []
    total_visible = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            height = grid[i][j]
            total_visibility, hidden = 1, 0
            for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                visibility, dist = 0, 1
                while 0 <= i + dist * dir[0] < len(grid) and 0 <= j + dist * dir[1] < len(grid[0]):
                    visibility += 1
                    if grid[i + dist * dir[0]][j + dist * dir[1]] >= height:
                        hidden += 1
                        break
                    dist += 1
                total_visibility *= visibility
            if hidden < 4:
                total_visible += 1
            vis.append(total_visibility)
    return total_visible, max(vis)
