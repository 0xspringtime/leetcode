#Fisher-Yates
import random

class Solution:

    def __init__(self, nums):
        # Original array is stored for reset operation
        self.original = nums
        # Working copy of the array for shuffle operation
        self.array = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        # Reset to the original array
        self.array = list(self.original)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        # For each index in array
        for i in range(len(self.array)):
            # Pick a remaining element
            swap_idx = random.randrange(i, len(self.array))
            # And swap it with the current element
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
#time O(n)
#space O(n)
