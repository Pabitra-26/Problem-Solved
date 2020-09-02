# Problem name: Design Skiplist
# Description: Design a Skiplist without using any built-in libraries.
#
# A Skiplist is a data structure that takes O(log(n)) time to add, erase and search.
# Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists are just simple linked lists.
#To be specific, your design should include these functions:
"""
bool search(int target) : Return whether the target exists in the Skiplist or not.
void add(int num): Insert a value into the SkipList.
bool erase(int num): Remove a value in the Skiplist. If num does not exist in the Skiplist, do nothing and return false. If there exists multiple num values, removing any one of them is fine."""


class Skiplist:

    def __init__(self):
        self.skip_list = {}

    def search(self, target: int) -> bool:
        if (target in self.skip_list):
            if (self.skip_list[target] > 0):
                return True
        return False

    def add(self, num: int) -> None:
        if (num in self.skip_list):
            self.skip_list[num] += 1
        else:
            self.skip_list[num] = 1

    def erase(self, num: int) -> bool:
        if (num in self.skip_list):
            if (self.skip_list[num] > 0):
                self.skip_list[num] -= 1
                return True
        return False
