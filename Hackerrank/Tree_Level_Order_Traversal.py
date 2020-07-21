# Problem name:Tree: Level Order Traversal
#Description: You are given a pointer to the root of a binary tree. You need to print the level order traversal of this tree.
# In level order traversal, we visit the nodes level by level from left to right. You only have to complete the function.
# Strategy: Visit the root--> while trversing level l, keep all the elements of level l+1 in queue-->Go to the next level and visit all the nodes at tht level--> Repeat this until all levels are completed

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def levelOrder(root):
    if not root:
        return
    q = []
    q.append(root)
    node = None
    while not q == []:
        node = q.pop(0)
        print(node.info, end=" ")
        if (node.left is not None):
            q.append(node.left)
        if (node.right is not None):
            q.append(node.right)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
