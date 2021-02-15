class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        result = []
        while ( i < len(nums)):
            if (nums[i] not in result):
                result.append(nums[i])
            elif(nums[i] in result):
                result.remove(nums[i])
            i = i + 1
        return result[0]
