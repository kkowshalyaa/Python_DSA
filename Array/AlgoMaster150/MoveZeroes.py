'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

https://leetcode.com/problems/move-zeroes/description/
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        flag = 0
        for index in range(0, len(nums)):
            if not nums[index] == 0:
                flag = 1
                continue
            else:
                flag = 0
                last_non_zero_found_at = index
                break
        if flag != 1: #There was no zero in the array
            for i in range(len(nums)):
                if nums[i] != 0 and i>last_non_zero_found_at:
                    nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                    last_non_zero_found_at += 1
