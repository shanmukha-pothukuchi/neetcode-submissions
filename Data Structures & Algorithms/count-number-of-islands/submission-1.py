class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    stack = [(i, j)]
                    visited.add((i, j))

                    while stack:
                        x, y = stack.pop()

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < m and 0 <= ny < n:
                                if grid[nx][ny] == '1' and (nx, ny) not in visited:
                                    visited.add((nx, ny))
                                    stack.append((nx, ny))

        return res