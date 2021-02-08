class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        flag = 2
        if not strs:
            return prefix
        pointer=sorted(strs, key=len)[0]
        for counter, value in enumerate(list(pointer)):
            if (flag == 0):
                break
            for i, j in enumerate(strs):
                if ( value == list(strs)[i][counter] ):
                    flag = 1
                else:
                    flag = 0
                    break
            if( flag == 1 ):
                prefix = prefix + value
        return prefix
