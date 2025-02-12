# Given an array, return the duplicates in the array. Other variations of the problem could be 1. Returning a boolean True if
# there are any duplicates present 2. Returning the first duplicate value etc.
# Implementation - Use a python dictionary. Iterate through the array, check if array element is an existing key in dict, if not add it.
# If array element is already present then it's a duplicate.
# Solution might not be optimised for scenarios where the array size is large.

# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

def duplicatesInArray(nums):
    dup_dict = dict()
    for num in nums:
        if num not in dup_dict.keys():
            dup_dict[num] = 1
        elif num in dup_dict.keys():
            dup_dict[num] += 1
    for key, value in dup_dict.items():
        if value > 1:
            print(key)

if __name__ == '__main__':
    numbers_0 = [1,7,45,6,7,8,9]
    duplicatesInArray(numbers_0)

