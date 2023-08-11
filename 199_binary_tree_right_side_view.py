# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Input: root = [1,null,3]
# Output: [1,3]

# this prints all the right-hand side nodes, but this is not what the question is actually asking. If there isn't a right-side node, you could "see" the left-side node even standing on the right, and this problem wants you to print that node, too
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         output = []
#         print(root)

#         if not root:
#             return output
#         else:
#             output.append(root.val)
#             if root.right:
#                 output.extend(self.rightSideView(root.right))

#         return output


