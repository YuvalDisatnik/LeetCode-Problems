"""
9. Palindrome Number

Problem Description:
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        This function checks if the given integer is a palindrome.
        
        A palindrome is a number that reads the same forward and backward.
        
        Args:
        x (int): The integer to check.
        
        Returns:
        bool: True if x is a palindrome, False otherwise.
        """
        # Convert the integer to a string for character comparisons
        num = str(x)
        
        # Iterate over half the length of the string to compare both ends
        for i in range(len(num) // 2):
            # If any characters don't match, it's not a palindrome
            if num[i] != num[-1 - i]:
                return False
        
        # If all characters match, it's a palindrome
        return True
