# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sub_max(self, lis):
        if not lis:
            return None
        m = max(lis)
        ind = lis.index(m)
        return TreeNode(m, self.sub_max(lis[:ind]), self.sub_max(lis[ind+1:]))
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sub_max(nums)
