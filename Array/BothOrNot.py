'''
Given a number n, check if it's a multiple of x and y. Print both if it's a multiple of both, print one if it's a multiple of only one,
none if it's a multiple of neither.

https://leetcode.com/problems/fizz-buzz/description/ 
'''

def MultipleOfX(num, x):
    if num % x == 0:
        return True
    return False


if __name__ == '__main__':
    number = 15
    multipleOf_1 = 4
    multipleOf_2 = 2
    if MultipleOfX(number,multipleOf_1) and MultipleOfX(number,multipleOf_2):
        print("Both")
    elif MultipleOfX(number,multipleOf_1) or MultipleOfX(number,multipleOf_2):
        print("One")
    else:
        print("None")
