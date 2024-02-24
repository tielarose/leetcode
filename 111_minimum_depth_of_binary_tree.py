# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # case 1: no root, depth = 0
        if not root:
            return 0

        # case 2: this is a leaf, in which case depth = 1
        if not root.left and not root.right:
            return 1

        # case 3: no L child, but path continues to R
        if not root.left:
            return self.minDepth(root.right) + 1

        # case 4: no R child, but path continues to L
        if not root.right:
            return self.minDepth(root.left) + 1

        # case 5: path continues L and R. Return the min
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1
