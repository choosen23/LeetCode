"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid.

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        minCount = 0
        maxCount = 0
        for i in range(len(s)):
            if s[i] == '(':
                minCount += 1
                maxCount += 1
            elif s[i] == ')':
                minCount -= 1
                maxCount -= 1
            elif s[i] == '*':
                minCount -= 1
                maxCount += 1
            if(maxCount < 0):
                return False
            if(minCount < 0):
                minCount = 0

        if minCount == 0:
            return True
        else:
            return False
