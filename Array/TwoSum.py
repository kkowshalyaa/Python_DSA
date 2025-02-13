'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

https://leetcode.com/problems/two-sum/description/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # Dictionary to store numbers and their indices
        for i, x in enumerate(nums):  # Loop through nums with index
            if (y := target - x) in d:  # Check if complement exists in dictionary
                return [d[y], i]  # If found, return indices
            d[x] = i  # Store the current number's index in dictionary
'''
Implementation:
It uses a dictionary d to store each number’s value as the key and its index as the value.
As we iterate through nums, we compute y = target - x, which is the complement needed to reach target.
If y already exists in d, that means we have found two numbers that sum to target, so we return their indices.
Otherwise, we store x in d with its index for future lookups.

Understanding if (y := target - x) in d:
This line of code uses the walrus operator (:=), which is a Python 3.8+ feature that allows assignment inside an expression.
if (y := target - x) in d:
is equivalent to:
y = target - x  # Compute the complement
if y in d:  # Check if it exists in the dictionary
'''
