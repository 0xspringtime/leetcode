from collections import Counter

def intersect(nums1, nums2):
    # Create Counter objects for nums1 and nums2
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    
    # Initialize an empty list for the intersection
    intersection = []
    
    # For each unique element in counter1
    for num in counter1:
        # If the element also exists in counter2
        if num in counter2:
            # Add the element min(counter1[num], counter2[num]) times to the intersection
            intersection.extend([num]*min(counter1[num], counter2[num]))
            
    return intersection
#time O(m+n)
#space O(m+n)
