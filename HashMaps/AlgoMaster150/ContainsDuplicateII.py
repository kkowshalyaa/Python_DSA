'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

https://leetcode.com/problems/contains-duplicate-ii/description/

Implementation:
Imp --> nums[i] == nums[j] and abs(i - j) <= k

1. Use a dict
2. If element not in dict,  add element:index
3. If element in dict, check if old index - new index <=k, if not update the dict to reflect current index
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = dict()
        for index, item in enumerate(nums):
            if item not in ans:
                ans[item] = index
            elif item in ans:
                if abs(ans[item] - index) <= k:
                    return True
                else:
                    ans[item] = index
        return False
