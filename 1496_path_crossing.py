# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

# Example 1:

# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:

# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

# Constraints:

# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.


# class Solution:
#     def isPathCrossing(self, path: str) -> bool:
#         seen = set()

#         curr_x = 0
#         curr_y = 0

#         seen.add((curr_x, curr_y))

#         for direction in path:
#             if direction == "N":
#                 curr_y += 1
#             if direction == "S":
#                 curr_y -= 1
#             if direction == "E":
#                 curr_x += 1
#             if direction == "W":
#                 curr_x -= 1

#             if (curr_x, curr_y) in seen:
#                 return True
#             else:
#                 seen.add((curr_x, curr_y))

#         return False


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        seen = {(0, 0)}

        x = 0
        y = 0

        for dir in path:
            dx, dy = moves[dir]
            x += dx
            y += dy
            if (x, y) in seen:
                return True
            seen.add((x, y))

        return False
