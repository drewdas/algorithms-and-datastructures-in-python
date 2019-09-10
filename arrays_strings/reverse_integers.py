# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321

# Example 2:

# Input: -123
# Output: -321

# Example 3:

# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    temp = str(x)
    temp = temp[::-1]
        
    if temp[-1]=="-":
        temp = 0-int(temp[:len(temp)-1])
    if int(temp) >= 2**31-1 or int(temp) <= -2**31: 
        return 0    
    return int(temp)