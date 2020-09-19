# Problem name: Same Tree
# Description: Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p is None and q is None):
            return True
        elif(p is None or q is None):
            return False
        elif(p.val!=q.val):
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)