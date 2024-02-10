# You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

# Two squares are called adjacent if they are next to each other in any of the 4 directions.

# Two squares belong to the same connected component if they have the same color and they are adjacent.

# The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

# You should color the border of the connected component that contains the square grid[row][col] with color.

# Return the final grid.


# Example 1:

# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]
# Example 2:

# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]
# Example 3:

# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n


class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        m = len(grid)  # num rows
        n = len(grid[0])  # num cols

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        target_num = grid[row][col]

        def isValidSquare(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] == target_num

        def isOnBorder(r, c):
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                return True
            for dy, dx in directions:
                new_row = r + dy
                new_col = c + dx
                if grid[new_row][new_col] != target_num:
                    return True
            return False

        def dfs(r, c):
            seen.add((r, c))
            if isOnBorder(r, c):
                to_change.add((r, c))
            for dy, dx in directions:
                new_row = r + dy
                new_col = c + dx
                if (new_row, new_col) not in seen and isValidSquare(new_row, new_col):
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        seen = set()
        to_change = set()
        dfs(row, col)

        for r, c in to_change:
            grid[r][c] = color

        return grid
