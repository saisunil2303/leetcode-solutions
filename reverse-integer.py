class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        z = 0
        def recursive() -> int:
            nonlocal x
            nonlocal y
            nonlocal z
            z = x % 10
            x = (x - z )/ 10
            y = y * 10 + z
            if (x!=0):
                x = int(x)
                recursive()
            else:
                return y
        if (x < 0):
            x = x * -1
            recursive()
            if ( y > (2**31)-1 or y < -(2**31)):
                return 0
            else:
                return y * -1
        else:
            recursive()
            if ( y > (2**31)-1 or y < -(2**31)):
                return 0
            else:
                return y
