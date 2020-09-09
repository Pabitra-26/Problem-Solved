# Problem name:Binary Tree Inorder Traversal
# Description: Given a binary tree, return the inorder traversal of its nodes' values.

class Solution:
    def __init__(self):
        self.li = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.inorderTraversal(root.left)
        self.li.append(root.val)
        self.inorderTraversal(root.right)
        return self.li
