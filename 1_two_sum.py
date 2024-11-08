# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

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
