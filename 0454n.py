idef fourSumCount(nums1, nums2, nums3, nums4):
    # Initialize a dictionary to store the frequency of sums of pairs in nums1 and nums2
    count = {}

    # Calculate all possible sums of pairs in nums1 and nums2 and store their frequency in count
    for num1 in nums1:
        for num2 in nums2:
            sum_pair = num1 + num2
            if sum_pair in count:
                count[sum_pair] += 1
            else:
                count[sum_pair] = 1

    # Initialize the count of four numbers sum to 0
    four_sum_count = 0

    # Calculate all possible sums of pairs in nums3 and nums4
    for num3 in nums3:
        for num4 in nums4:
            sum_pair = num3 + num4
            # Check if the negative of this sum exists in count
            # If it does, add the frequency of this sum to the four_sum_count
            if -sum_pair in count:
                four_sum_count += count[-sum_pair]

    return four_sum_count
#time O(n^2)
#space O(n^2)
