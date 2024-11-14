# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def going_Subtree(self, root):
        if root is None:
            return "#"
        
        left_serial = self.going_Subtree(root.left)
        right_serial = self.going_Subtree(root.right)
        serial = f"{root.val},{left_serial},{right_serial}"
        
        if serial in self.l:
            self.l[serial].append(root)
        else:
            self.l[serial] = [root]
        
        return serial

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.l = {}
        self.going_Subtree(root)
        
        duplicates = []
        for nodes in self.l.values():
            if len(nodes) > 1:
                duplicates.append(nodes[0])
        
        return duplicates
