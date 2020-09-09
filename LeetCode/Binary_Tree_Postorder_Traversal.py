# Problem name: Binary Tree Postorder Traversal
# Description: Given the root of a binary tree, return the postorder traversal of its nodes' values.

class Solution:
    def __init__(self):
        self.li=[]
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.li.append(root.val)
        return self.li