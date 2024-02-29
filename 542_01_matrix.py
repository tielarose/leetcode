# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.


# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        seen = set()

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    q.append((row, col))
                    seen.add((row, col))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        distance = 1

        while q:
            curr_level_len = len(q)

            for _ in range(curr_level_len):
                row, col = q.popleft()
                for dy, dx in directions:
                    new_row = row + dy
                    new_col = col + dx
                    if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                        seen.add((new_row, new_col))
                        q.append((new_row, new_col))
                        mat[new_row][new_col] = distance
            distance += 1

        return mat
