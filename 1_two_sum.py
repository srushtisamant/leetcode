# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = []
        for i in range(0, len(nums)):
            item = target - nums[i]
            if item in nums:
                if i != nums.index(item):
                    stack.append(i)
                    stack.append(nums.index(item))
                    return stack
