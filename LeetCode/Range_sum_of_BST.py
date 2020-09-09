# Problem name: Range Sum of BST
# Description: Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        s=0
        node=None
        q=[]
        q.append(root)
        while(q!=[]):
            node=q.pop(0)
            if(node.val>=L and node.val<=R):
                s+=node.val
            if(node.left is not None):
                q.append(node.left)
            if(node.right is not None):
                q.append(node.right)
        return s