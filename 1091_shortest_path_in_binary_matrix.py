# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        n = len(grid)
        directions = [(-1,0), (-1, 1), (0,1), (1, 1), (1, 0), (1,-1),(0,-1),(-1,-1)]

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        q = deque()
        q.append((0,0))

        seen = set()
        seen.add((0,0))

        path_len = 1

        while q:
            curr_q_len = len(q)

            for _ in range(curr_q_len):
                row, col = q.popleft()
                if row == n - 1 and col == n - 1:
                    return path_len

                for dy, dx in directions:
                    new_row = row + dy
                    new_col = col + dx
                    if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                        seen.add((new_row, new_col))
                        q.append((new_row,new_col))

            path_len += 1

        return -1