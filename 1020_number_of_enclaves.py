# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:


# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        def isValidLand(row, col):
            return 0 <= row < h and 0 <= col < w and grid[row][col] == 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        seen = set()

        def dfs(row, col):
            for dy, dx in directions:
                new_row = row + dy
                new_col = col + dx
                if (new_row, new_col) not in seen and isValidLand(new_row, new_col):
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        # traverse the first and last row
        last_row = h - 1
        last_col = w - 1
        for col in range(w):
            if grid[0][col] == 1 and (0, col) not in seen:
                seen.add((0, col))
                dfs(0, col)
            if grid[last_row][col] == 1 and (last_row, col) not in seen:
                seen.add((last_row, col))
                dfs(last_row, col)

        # traverse the first and last cols
        for row in range(h):
            if grid[row][0] == 1 and (row, 0) not in seen:
                seen.add((row, 0))
                dfs(row, 0)
            if grid[row][last_col] == 1 and (row, last_col) not in seen:
                seen.add((row, last_col))
                dfs(row, last_col)

        ans = 0

        for row in range(h):
            for col in range(w):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    ans += 1

        return ans
