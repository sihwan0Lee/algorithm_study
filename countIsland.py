def numIslands(grid):
    def dfs(i, j):
        if i < 0 or j >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        print(grid[i])
        for j in range(len(grid[0])):
            print([i][j])
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count


print(numIslands([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
