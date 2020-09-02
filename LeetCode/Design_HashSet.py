# Problem name: Design HashSet
# Description: Design a HashSet without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.


class MyHashSet:

    def __init__(self):

        self.table = {}

    def add(self, key: int) -> None:
        self.table[key] = True

    def remove(self, key: int) -> None:
        if (key in self.table):
            self.table.pop(key)

    def contains(self, key: int) -> bool:

        if (key in self.table):
            return True
        return False