class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_list = []
        y = list(str(x))
        for i in range(len(y)):
            new_list.append(y.pop())
        z = ''.join(new_list)
        if (z == str(x)):
            return 1
        else:
            return 0
