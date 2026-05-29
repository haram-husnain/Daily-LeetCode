class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_numbers:
                return[seen_numbers[complement], i]
            seen_numbers[num] = i            

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#We have the dictionary initialization, the loop using enumerate(), the complement calculation, the check to see if the complement is already in the dictionary, and the fallback to store the current number if it isn't.

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.