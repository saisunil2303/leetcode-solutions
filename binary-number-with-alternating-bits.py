class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = 0
        result = []
        temp = -1
        while ( n > 0 ):
            if ( i % 2 == 0 ):
                if ((n & 1 == 1 and temp == 0) or (i == 0 and n & 1 == 1) ):
                    temp = 1
                elif((n & 1 != 1 and temp == 1) or (i == 0 and n & 1 != 1) ):
                    temp = 0  
                else:
                    return False
            else:
                if ( n & 1 == 1 and temp == 0 ):
                    temp = 1
                elif( n & 1 != 1 and temp == 1):
                    temp = 0
                else:
                    return False
            i = i + 1
            n = n // 2
        return True
