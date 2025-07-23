from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs_convert_to_zeros(row: int, col: int) -> None:
            print(row, col)
            if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == '1':
                grid[row][col] = '0'
                dfs_convert_to_zeros(row + 1, col)
                dfs_convert_to_zeros(row - 1, col)
                dfs_convert_to_zeros(row, col + 1)
                dfs_convert_to_zeros(row, col - 1)
            else:
                return
                
        
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs_convert_to_zeros(i, j)
        return num_islands
