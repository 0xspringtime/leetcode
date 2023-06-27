#greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:  # if the array only has one element, we are already at the destination
            return 0
        
        # Initialize our variables
        jump = 1
        max_reach = nums[0]
        furthest = nums[0]
        
        for i in range(1, len(nums)):
            if i > max_reach:  # if the current index is out of reach with the current jumps
                jump += 1  # we need one more jump
                max_reach = furthest  # and we update our max_reach
            
            furthest = max(furthest, nums[i] + i)  # we update the furthest index we can reach

        return jump
#time O(n)
#space O(1)
