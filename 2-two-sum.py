class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This function returns the indices of two numbers from the given list 'nums'
        that add up to the 'target' value.
        Args:
        nums (List[int]): The list of integers to search through.
        target (int): The target sum to achieve by adding two numbers from 'nums'.
        Returns:
        List[int]: A list containing the indices of the two numbers that add up to 'target'.
        """
        # Initialize an empty list to store the answer (indices of the two numbers)
        answer = []
        # Iterate through the list 'nums'
        for i in range(len(nums)):
            # For each element at index i, iterate through the remaining elements
            for j in range(i + 1, len(nums)):
                # If the sum of nums[i] and nums[j] equals the target, return their indices
                if nums[i] + nums[j] == target:
                    # Add the indices i and j to the answer list
                    answer.append(i)
                    answer.append(j)
                    # Return the answer immediately after finding the solution
                    return answer
