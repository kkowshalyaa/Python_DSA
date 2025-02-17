'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

https://leetcode.com/problems/majority-element/description/

Implemetation:
1. Create a Dictionary - Element : Freq
2. Max of Freq
3. Return Key, when Value matches Max Frequency
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        freq_max = max(freq.values())
        for key, value in freq.items():
            if value == freq_max:
                return key
