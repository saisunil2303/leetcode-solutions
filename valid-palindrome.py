class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        j = 0
        result = []
        for i in list(s):
            if ( i.isalnum() is True):
                temp.append(i.lower())
        while (j < len(temp)):
            result.append(temp[len(temp) - j - 1])
            j = j + 1
        if (result == temp):
            return True
        return False
