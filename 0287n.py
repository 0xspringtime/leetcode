#floyd
def findDuplicate(nums):
    # Initializing slow and fast pointers
    slow = fast = nums[0]

    # Phase 1: Finding intersection point of slow and fast pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Finding the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # Return the duplicate number
    return slow
#time O(n)
#space O(1)
