class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid[0]), len(grid)
        cnt = 0

        def dfs(x,y):
            if x < 0 or x >= row: return
            if y < 0 or y >= col: return

            if grid[y][x] == '1':
                grid[y][x] = 0

                dfs(x-1, y)
                dfs(x, y-1)
                dfs(x+1, y)
                dfs(x, y+1)
        
        for y in range(col):
            for x in range(row):
                if grid[y][x] == '1':
                    dfs(x, y)
                    cnt += 1
                    
        return cnt