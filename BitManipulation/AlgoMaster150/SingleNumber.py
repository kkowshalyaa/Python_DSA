'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Implementation:
2 - 010
2 - 010
1 - 001

How XOR Works, 
The XOR operation returns true (or 1) if exactly one of the two inputs is true (or 1).
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0

Bascially, when there are pairs, it cancels out and single integer is left out.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
    
        # XOR all the elements in the array
        for num in nums:
            result ^= num
        
        # The result holds the single number now
        return result
