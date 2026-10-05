class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def bfs(start):
            q = deque([start])

            while q:
                x, y = q.popleft()

                if (x, y) in visited:
                    continue

                visited.add((x, y))

                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        if grid[nx][ny] == '1' and (nx, ny) not in visited:
                            q.append((nx, ny))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs((i, j))
                    res += 1

        return res
