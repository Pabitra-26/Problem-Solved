# Problem name: Balanced Brackets
"""Description: A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].
By this logic, we say a sequence of brackets is balanced if the following conditions are met:
It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given n strings of brackets, determine whether each sequence of brackets is balanced.
If a string is balanced, return YES. Otherwise, return NO."""
# Strategy: Stacks





import math
import os
import random
import re
import sys


class Stack():                         # create a class stack
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]

def is_match(p1,p2):                 # this function is to check whether the brackets match or not
    if(p1=="(" and p2==")"):
        return True
    elif(p1=="{" and p2=="}"):
        return True
    elif(p1=="[" and p2=="]"):
        return True
    else:
        return False

def isBalanced(s):
    stack=Stack()                       # create a stack object
    index=0
    balanced=True                       # set this flag to true
    while(index<len(s) and balanced):
        s1=s[index]
        if( s1 in "{[("):               # if its an opening bracket, then push it onto the stack
            stack.push(s1)
        else:                           # if it's a closing bracket, then check if the stack is empty or not; if it's empty: then there are no openeing brackets, meaning, its not balanced
            if(stack.is_empty()):
                balanced=False
            else:                       # if the stack is not empty, pop the last item
                top=stack.pop()
                if(not is_match(top,s1)):  # compare it with the current string element
                    balanced=False
        index+=1
    if(balanced and stack.is_empty()):   # after going through the entire string, check the flag the stack contents
        return "YES"                     # if flag is not changed and if stack is empty, it means, all the openeing brackets have been popped
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
