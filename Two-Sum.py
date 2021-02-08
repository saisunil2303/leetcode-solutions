class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for counter, value in enumerate(nums):
            if ( target - value ) in num_set:
                return [num_set[target-value], counter]
            num_set[value] = counter
            print (num_set)
