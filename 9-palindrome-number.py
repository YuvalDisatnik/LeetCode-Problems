class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string for character comparisons
        num = str(x)
        
        # Iterate over half the length of the string to compare both ends
        for i in range(len(num) // 2):
            # If any characters don't match, it's not a palindrome
            if num[i] != num[-1 - i]:
                return False
        
        # If all characters match, it's a palindrome
        return True
