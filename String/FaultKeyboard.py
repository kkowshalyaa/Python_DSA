'''
Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.
You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
Return the final string that will be present on your laptop screen.
Example 1:
Input: s = "string"
Output: "rtsng"
Example 2:
Input: s = "poiinter"
Output: "ponter"
Explanation: 
Since the third character you type is an 'i', the text gets reversed and becomes "op". 
Since the fourth character you type is an 'i', the text gets reversed again and becomes "po".

https://leetcode.com/problems/faulty-keyboard/description/
'''

class Solution:
    def finalString(self, s: str) -> str:
        i_out = s.split("i")
        for index in range(0, len(i_out)-1):
            i_out[index] = self.reverseString(i_out[index])
        return "".join(i_out)
        
    def reverseString(self, temp_s):
        list_s = list(temp_s)
        i, j = 0, len(temp_s) - 1
        while i < j:
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i, j = i + 1, j - 1
        return "".join(list_s)

'''
Above solution did not work, as letters are typed linearly and also two i's can be typed consecutively which cannot be detected when using split
'''

class Solution:
    def finalString(self, s: str) -> str:
        i_out = s.split("i")
        for index in range(0, len(i_out)-1):
            i_out[index] = self.reverseString(i_out[index])
        return "".join(i_out)
        
        
    def reverseString(self, temp_s):
        list_s = list(temp_s)
        i, j = 0, len(temp_s) - 1
        while i < j:
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i, j = i + 1, j - 1
        return "".join(list_s)
