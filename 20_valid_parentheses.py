# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ('{', '[', '('):
                stack.append(char)
            else:
                if stack == []:
                    return False  
                curr = stack.pop()
                if curr == '[' and char != ']':
                    return False
                if curr == '{' and char != '}':
                    return False
                if curr == '(' and char != ')':
                    return False

        return stack == []
