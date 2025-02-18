'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

There are many easier ways to do this by converting the number to string, but this solution solves the problem without converting to string. 

https://leetcode.com/problems/palindrome-number/description/

Implementation:
1. Divide number by 10, i.e. 121/10 -> q=12, r=1
2. Now, q becomes new number. 
3. Maintain product = 0, and basically reverse the number by p*10 + remainder
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = 0
        temp_n = x
        while x>0:
            p = p*10 + x%10
            x = int(x/10)
        if p == temp_n:
            return True
        return False
