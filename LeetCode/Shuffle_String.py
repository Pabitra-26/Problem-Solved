# Problem name: Shuffle String
# Description: Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Strategy: use a dictionary to map the characters to the index values and the sort the indices list

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = dict()
        for i in range(len(indices)):
            d[indices[i]] = s[i]
        s = ""
        indices.sort()
        for i in indices:
            s += d[i]
        return s
