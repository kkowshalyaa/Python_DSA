'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

https://leetcode.com/problems/reverse-vowels-of-a-string/description/

Implementation:
1. Two pointers, one pointing at beginning and one at end
2. Main while loop checks if left index is less than right index
3. Inner loops, if left index is not point to vowel, keep incrementing as long it's lesser than right index, vice versa for right index
4. When both left index and right index are point to vowels, inner while loop ends
5. Now, swap chars at both indexes, increment left index and decrement right index
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        cs = list(s)
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            cs[i], cs[j] = cs[j], cs[i]
            i, j = i + 1, j - 1
        return "".join(cs)
