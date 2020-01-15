# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.vals = []
        self.add_data_to_vals(root)
        reduced_vals = list(set(self.vals))
        reduced_vals.sort()
        return reduced_vals[k-1]

    def add_data_to_vals(self, root):
        self.vals.append(root.val)
        if root.left:
            self.add_data_to_vals(root.left)
        if root.right:
            self.add_data_to_vals(root.right)
