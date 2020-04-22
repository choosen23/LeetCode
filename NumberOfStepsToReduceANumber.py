"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.
"""

class Solution:
    #a normal solution
    def numSteps(self, s: str) -> int:
        def binaryToDecimal(binary):
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal
        number = binaryToDecimal(int(s))
        print(number)
        if (number == 1 ):
            return 0
        elif ( number == 2 ):
            return 1
        else:
            steps = 0
            while (number > 1):
                if (number % 2 == 1 ):
                    number += 1
                else:
                    number = number //2
                steps += 1

            return steps
