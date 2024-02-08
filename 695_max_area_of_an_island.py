# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.


# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        # capture 4 possible neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # helper function to ensure it's not out of bounds and is land
        def isLand(row, col):
            return (
                0 <= row <= height - 1 and 0 <= col <= width - 1 and grid[row][col] == 1
            )

        def dfs(row, col):
            print(row, col)
            area = 1
            for dy, dx in directions:
                new_row = row + dy
                new_col = col + dx
                if (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    if isLand(new_row, new_col):
                        area += dfs(new_row, new_col)
            return area

        seen = set()
        max_area = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    max_area = max(max_area, dfs(row, col))

        return max_area
