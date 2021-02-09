class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        p=list(s)

        for j,i in enumerate(p):
            if (i == '(' or i == '{' or i == '['):
                result.append(i)
            elif result:
                if ( ( i == ')' and result[-1] == '(' ) or ( i == '}' and result[-1] == '{') or (i == ']' and result[-1] == '[')):
                    result.pop()
                else:
                    return False
            else:
                return False
        if not result:
            return True
        else:
            return False
