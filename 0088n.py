#two pointer
def merge(nums1, m, nums2, n):
    # Two get pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    
    # And also the pointer for the current position in nums1
    p = m + n - 1
    
    # While there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    
    # Add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]
#time O(m+n)
#space O(1)
