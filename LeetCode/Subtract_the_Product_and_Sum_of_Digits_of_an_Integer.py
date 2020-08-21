# Problem name: Subtract the Product and Sum of Digits of an Integer
# Description: Given an integer number n, return the difference between the product of its digits and the sum of its digits.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        n=list(n)
        s=0
        p=1
        for i in n:
            s+=int(i)
            p*=int(i)
        return p-s