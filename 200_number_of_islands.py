# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from collections import defaultdict


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] == "1"

        def dfs(row, col):
            for row_chg, col_chg in directions:
                new_row, new_col = row + row_chg, col + col_chg
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    num_islands += 1
                    seen.add((row, col))
                    dfs(row, col)

        return num_islands
