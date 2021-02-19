class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            if (str(x) == str(x)[::-1]):
                return True
        return False
