class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        counter = 0
        flag = -1
        while i < len(s):
            if ( s[i] == " " ):
                i = i + 1
                flag = 1
            else:
                if (flag == 1):
                    counter = 0
                    flag = 0
                counter = counter + 1
                i = i + 1
        return counter
