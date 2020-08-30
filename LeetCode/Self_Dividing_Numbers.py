# Problem name: Self Dividing Numbers
# Description: A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li = []
        if (left < 10 and right < 10):
            li = list(range(left, right + 1))
            return li

        elif (left < 10 and right > 10):
            li = list(range(left, 10))
            for i in range(10, right + 1):
                if (i % 10 == 0):
                    continue
                else:
                    m = i
                    m = str(m)
                    if ('0' in m):
                        continue

                    m = list(m)
                    flag = 0
                    for j in range(len(m)):
                        if (i % int(m[j]) == 0):
                            continue
                        else:
                            flag = 1
                            break
                    if (flag == 1):
                        continue
                    else:
                        li.append(i)
            return li
        else:
            for i in range(left, right + 1):
                if (i % 10 == 0):
                    continue
                else:
                    m = i
                    m = str(m)
                    if ('0' in m):
                        continue
                    m = list(m)
                    flag = 0
                    for j in range(len(m)):
                        if (i % int(m[j]) == 0):
                            continue
                        else:
                            flag = 1
                            break
                    if (flag == 1):
                        continue
                    else:
                        li.append(i)
            return li