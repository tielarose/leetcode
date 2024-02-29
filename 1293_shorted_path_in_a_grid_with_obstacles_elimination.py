# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.


# Example 1:


# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation:
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# Example 2:


# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0

from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m = len(grid)
        n = len(grid[0])
        q = deque()

        # in the q: row, col, removals remaining, steps taken so far
        q.append((0, 0, k, 0))

        # in the seen set: row, col, removals remaining
        # the same square can be visited in multiple paths, provided
        # it's been reached with a different number of removals
        seen = set()
        seen.add((0, 0, k))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            row, col, remains, steps = q.popleft()
            # is this the lower right corner? then return steps
            if row == m - 1 and col == n - 1:
                return steps
            else:
                for dy, dx in directions:
                    new_row = row + dy
                    new_col = col + dx
                    if is_valid(new_row, new_col):
                        # if it's clear
                        if grid[new_row][new_col] == 0:
                            if (new_row, new_col, remains) not in seen:
                                seen.add((new_row, new_col, remains))
                                q.append((new_row, new_col, remains, steps + 1))
                        # if it's blocked AND we have removals left (remains > 0)
                        elif remains and (new_row, new_col, remains - 1) not in seen:
                            seen.add((new_row, new_col, remains - 1))
                            q.append((new_row, new_col, remains - 1, steps + 1))

        return -1
