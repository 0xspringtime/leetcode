class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Reverse the whole array
        self.reverse(nums, 0, len(nums) - 1)
        # Calculate the actual number of steps to rotate (in case k > len(nums))
        k %= len(nums)
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums, start, end):
        """
        Helper function to reverse a sublist
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
#time O(n)
#space O(1)
