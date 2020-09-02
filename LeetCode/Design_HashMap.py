# Problem name: Design HashMap
# Description: Design a HashMap without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


class MyHashMap:

    def __init__(self):
        self.table = {}

    def put(self, key: int, value: int) -> None:
        if (key in self.table):
            self.table[key] = value
        else:
            self.table[key] = value

    def get(self, key: int) -> int:
        if (key in self.table):
            return self.table[key]
        return -1

    def remove(self, key: int) -> None:
        if (key in self.table):
            del self.table[key]

