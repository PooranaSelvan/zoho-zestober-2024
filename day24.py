def find_best_camping_site(map_grid):
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] == 'E':
                count = 0
                found_terrain = {'T': False, 'R': False, 'W': False}

                # Check the above value
                if i > 0 and not found_terrain[map_grid[i-1][j]]:
                    if map_grid[i-1][j] in ['T', 'R', 'W']:
                        found_terrain[map_grid[i-1][j]] = True
                        count += 1
                
                # Check the below value
                if i < len(map_grid) - 1 and not found_terrain[map_grid[i+1][j]]:
                    if map_grid[i+1][j] in ['T', 'R', 'W']:
                        found_terrain[map_grid[i+1][j]] = True
                        count += 1
                
                # Check the left value
                if j > 0 and not found_terrain[map_grid[i][j-1]]:
                    if map_grid[i][j-1] in ['T', 'R', 'W']:
                        found_terrain[map_grid[i][j-1]] = True
                        count += 1
                
                # Check the right value
                if j < len(map_grid[i]) - 1 and not found_terrain[map_grid[i][j+1]]:
                    if map_grid[i][j+1] in ['T', 'R', 'W']:
                        found_terrain[map_grid[i][j+1]] = True
                        count += 1

                if count >= 2:
                    return (i, j)

    return (-1, -1)

map_grid = [
    ['E', 'W', 'E', 'T'],
    ['W', 'E', 'T', 'E'],
    ['E', 'E', 'W', 'E'],
    ['T', 'E', 'E', 'R']
]

print(find_best_camping_site(map_grid))
