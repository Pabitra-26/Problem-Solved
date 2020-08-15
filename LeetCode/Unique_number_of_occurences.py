# Problem name: Unique Number of Occurrences
# Description: Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
# Strategy: Use hashing

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        table = {}
        for i in range(len(arr)):
            if (arr[i] not in table):
                table[arr[i]] = 1
            elif (arr[i] in table):
                table[arr[i]] += 1
        li = list(table.values())
        for i in range(len(li)):
            for j in range(i + 1, len(li)):
                if (li[i] == li[j]):
                    return False

        return True