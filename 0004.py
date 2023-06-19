def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)

    # Choose the smaller array for binary search
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    low, high = 0, m

    while low <= high:
        mid = (low + high) // 2  # Partition point for the smaller array
        partition_larger = ((m + n + 1) // 2) - mid  # Corresponding partition point for the larger array

        # Calculate left_max and right_min for the smaller array
        left_max1 = float('-inf') if mid == 0 else nums1[mid - 1]
        right_min1 = float('inf') if mid == m else nums1[mid]

        # Calculate left_max and right_min for the larger array
        left_max2 = float('-inf') if partition_larger == 0 else nums2[partition_larger - 1]
        right_min2 = float('inf') if partition_larger == n else nums2[partition_larger]

        # Check if elements in left halves are smaller than elements in right halves
        if left_max1 <= right_min2 and left_max2 <= right_min1:
            # Total number of elements is odd
            if (m + n) % 2 != 0:
                return max(left_max1, left_max2)
            # Total number of elements is even
            else:
                return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2.0
        # Adjust the partition points for binary search
        elif left_max1 > right_min2:
            high = mid - 1
        else:
            low = mid + 1

    # No median found
    return None

