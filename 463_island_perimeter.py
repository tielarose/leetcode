# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4


# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValidLand(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] == 1

        def dfs(row, col):
            for dy, dx in directions:
                new_row = row + dy
                new_col = col + dx
                if isValidLand(new_row, new_col):
                    self.edges += 1
                    if (new_row, new_col) not in seen:
                        seen.add((new_row, new_col))
                        self.land += 1
                        dfs(new_row, new_col)

        self.land = 0
        self.edges = 0

        seen = set()

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    self.land = 1
                    seen.add((row, col))
                    dfs(row, col)

        return (4 * self.land) - self.edges
