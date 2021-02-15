class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        i = 0
        while i <= n:
            a = a + b
            b = a - b
            i = i + 1
        return a
