class Solution:
    def reverseBits(self, n: int) -> int:
        result = []
        i = 0
        while ( i < 32 ):
            if ( n & 1 == 1):
                result.append('1')
            else:
                result.append('0')
            n = n >> 1
            i = i + 1
        return (int(''.join(map(str, result)), 2))
