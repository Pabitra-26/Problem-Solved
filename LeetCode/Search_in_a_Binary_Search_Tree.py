# Problem name: Search in a Binary Search Tree
# Description: Given the root node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the given value.
# Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if(root==None):
            return None
        elif(val==root.val):
            return root
        elif(val<root.val):
            return self.searchBST(root.left,val)
        elif(val>root.val):
            return self.searchBST(root.right,val)

