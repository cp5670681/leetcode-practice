# https://leetcode-cn.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 1, 1
            for i in range(n-2):
                d = a + b + c
                a, b, c = b, c, d
        return d