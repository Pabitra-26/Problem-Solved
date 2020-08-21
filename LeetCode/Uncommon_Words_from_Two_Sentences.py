# Problem name: Uncommon Words from Two Sentences
# Description: We are given two sentences A and B.  (A sentence is a string of space separated words.
# Each word consists only of lowercase letters.) A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Return a list of all uncommon words. You may return the list in any order.


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        table = {}
        A = A.split()
        B = B.split()
        for i in A:
            if (i not in table):
                table[i] = 1
            elif (i in table):
                table[i] += 1

        for i in B:
            if (i in table):
                table[i] += 1
            elif (i not in table):
                table[i] = 1
        li = []
        for i in table.keys():
            if (table[i] == 1):
                li.append(i)
        return li