class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif ( len(needle) > len(haystack) ):
            return -1            
        else:
            i = 0
            while i < len(haystack):
                if ( haystack[i:i+len(needle)] == needle ):
                    return i
                else:
                    i = i + 1
            return -1
