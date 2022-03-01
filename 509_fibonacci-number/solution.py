# https://leetcode-cn.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return c

s = Solution()
print(s.fib(40))
