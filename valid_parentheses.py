# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenDict = {'}':'{',
                           ')':'(',
                           ']':'['}
        stack = []
        for char in s:
            if char in closeToOpenDict:
                if stack and stack[-1] == closeToOpenDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False