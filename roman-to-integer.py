class Solution:
    def romanToInt(self, s: str) -> int:
        roman_lookup = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000 , 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        result = 0
        concat = ''
        next_one = ''
        flag = 0
        for counter, value in enumerate(list(s)):
            if (flag == 1):
                flag = 0
                continue
            else:
                if (value == 'I' or value == 'X' or value == 'C'):
                    if ( counter != len(list(s))-1 and ((value + list(s)[counter+1]) == 'IV' or (value + list(s)[counter+1]) == 'IX' or (value + list(s)[counter+1]) == 'XL' or (value + list(s)[counter+1]) == 'XC' or (value + list(s)[counter+1]) == 'CD' or (value + list(s)[counter+1]) == 'CM')):
                        result = result + roman_lookup[value + list(s)[counter+1]]
                        flag = 1
                    else:
                        result = result + roman_lookup[value]
                else:
                    result = result + roman_lookup[value]
        return result
