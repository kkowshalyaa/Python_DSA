'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Uses DP 
0 = 0000
1 = 0001 
2 = 0010
3 = 0011
4 = 0100 -> 1 + 1's in 4-4
5 = 0101 -> 1 + 1's in 5-4
6 = 0110 -> 1 + 1's in 6-4
7 = 0111 -> 1 + 1's in 7-4
8 = 1000 -> 1 + 1's in 8-8
9 = 1001 -> 1 + 1's in 9-8
10 = 1010 -> 1 + 1's in 10-8
11 = 1011 -> 1 + 1's in 11-8
12 = 1100 -> 1 + 1's in 12-8

https://leetcode.com/problems/counting-bits/
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1  # to track the latest power of two
        for i in range(1, n + 1):
            # update offset when we get to the next power of two
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
