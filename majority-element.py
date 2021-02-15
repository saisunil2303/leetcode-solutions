class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        result = {}
        max_value = -1
        max_key = -1
        while (i < len(nums)):
            if (nums[i] not in result.keys()):
                result[nums[i]] = 0
            else:
                result[nums[i]] = result[nums[i]] + 1
            i = i + 1
        for key,value in result.items():
            if (value > max_value):
                max_value = value
                max_key = key
        return max_key
