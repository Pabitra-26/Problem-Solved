# Problem name: N-Repeated Element in Size 2N Array
# Description: In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.
# Strategy: determine the N value and use hashing

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) // 2
        table = {}
        for i in range(len(A)):
            if (A[i] in table):
                table[A[i]] += 1
                if (table[A[i]] == N):
                    return A[i]
            elif (A[i] not in table):
                table[A[i]] = 1
