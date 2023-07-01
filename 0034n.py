#binary search
def searchRange(nums, target):
    def findFirst(nums, target):
        # initialize the left and right pointers
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target: # if target is greater, ignore left half
                left = mid + 1
            else: # if target is smaller or equal, ignore right half
                right = mid
        return left if nums[left] == target else -1

    def findLast(nums, target):
        # initialize the left and right pointers
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1 # make middle biased to the right
            if nums[mid] > target: # if target is smaller, ignore right half
                right = mid - 1
            else: # if target is greater or equal, ignore left half
                left = mid
        return left if nums[left] == target else -1

    return [findFirst(nums, target), findLast(nums, target)]
#time O(logn)
#space O(1)
