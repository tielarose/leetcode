# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


# Example 1:


# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
# Example 2:


# Input: root = [5,4,2,3,3,7]
# Output: false
# Explanation: The node values on each level are:
# Level 0: [5]
# Level 1: [4,2]
# Level 2: [3,3,7]
# Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
# Example 3:


# Input: root = [5,9,1,3,5,7]
# Output: false
# Explanation: Node values in the level 1 should be even integers.


# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 106

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        even_level = True

        while q:
            curr_level_len = len(q)
            last_val = None

            for _ in range(curr_level_len):
                node = q.popleft()
                if even_level:
                    # all vals on even levels must be odd
                    if node.val % 2 == 0:
                        return False

                    # all vals on even levels must be strictly increasing
                    if last_val == None:
                        last_val = node.val
                    else:
                        if node.val <= last_val:
                            return False
                else:
                    # all vals on odd levels must be even
                    if node.val % 2 == 1:
                        return False

                    # all vals on odd levels must be strictly decreasing
                    if last_val == None:
                        last_val = node.val
                    else:
                        if node.val >= last_val:
                            return False

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                last_val = node.val

            even_level = not even_level

        return True
