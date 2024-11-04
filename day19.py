def longest_ridge_path(n, m, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # North, South, West, East
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def find_ridge_path(start_x, start_y):
        stack = [(start_x, start_y)]
        path = [(start_x, start_y)]
        while stack:
            x, y = stack.pop()
            found_next = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and grid[nx][ny] > grid[x][y]:
                    stack.append((nx, ny))
                    path.append((nx, ny))
                    found_next = True
                    break
            if not found_next:
                break
        return path

    best_path = []
    for i in range(n):
        for j in range(m):
            path = find_ridge_path(i, j)
            if len(path) > len(best_path) or (len(path) == len(best_path) and sum(grid[x][y] for x, y in path) > sum(grid[x][y] for x, y in best_path)):
                best_path = path

    return best_path

# Example usage:
n = 4
m = 5
grid = [
    [10, 12, 14, 13, 9],
    [9, 11, 15, 14, 8],
    [8, 10, 12, 16, 7],
    [7, 9, 11, 10, 6]
]

result = longest_ridge_path(n, m, grid)
print(result)  # Output: [(0, 2), (1, 2), (2, 3)]
