#Dutch national flag problem
#two pointer
def sortColors(nums):
    low, mid = 0, 0
    high = len(nums) - 1

    # Iterate through the array
    while mid <= high:
        # Case if the element is '0'
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        # Case if the element is '1'
        elif nums[mid] == 1:
            mid += 1
        # Case if the element is '2'
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
#time O(n)
#space O(1)
