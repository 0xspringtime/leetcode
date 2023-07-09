def intersection(nums1, nums2):
    # Convert arrays to sets
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Perform intersection operation and convert the result back into list
    return list(set1 & set2)
#time O(n+m)
#space O(n+m)
