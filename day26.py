def is_fully_covered(grid):
    grid_list = list(grid)
    n = len(grid_list)

    for i in range(n):
        if grid_list[i] == 'C':
            grid_list[i] = '#'  
            if (i > 0 and grid_list[i - 1] == '.') or (i < n - 1 and grid_list[i + 1] == '.'):
                if i > 0 and grid_list[i - 1] == '.':
                    grid_list[i - 1] = '#'
                if i < n - 1 and grid_list[i + 1] == '.':
                    grid_list[i + 1] = '#'

    return '.' not in grid_list

grid = {'C', '.', '.', '.', 'X', '.', 'C', '.', '.', 'X', '.', 'C'}
print(is_fully_covered(grid))
