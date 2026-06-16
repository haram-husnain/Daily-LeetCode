class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) # if nums[3] = [1,2,3,3], n = 4
        count = [0] * n # count will have 4 items of 0
        for i in nums: # each item in the list
            if i > (n-1): # if its greater than base, false
                return False
            
            count[i] += 1 #add 1 to 0 for frequency of each number

        # check if 1 to n-1 appears once
        for x in range(1, n-1):
            if count[x] != 1:
                return False

        # check if n-1 appears twice
        return count[n-1] == 2

# You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
# Return true if the given array is good, otherwise return false.