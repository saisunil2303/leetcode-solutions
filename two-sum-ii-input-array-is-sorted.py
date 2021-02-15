class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        num_set = {}
        for counter, value in enumerate(numbers):
            if(( target - value ) in num_set ):
                result = [counter+1, num_set[target-value]+1]
            num_set[value] = counter
        result.sort()
        return result
