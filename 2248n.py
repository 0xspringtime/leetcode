def common_elements(nums):
    # Convert the first list into a set
    common_set = set(nums[0])

    # Perform intersection operation on all the lists
    for num_list in nums[1:]:
        common_set &= set(num_list)

    # Convert the set into a sorted list and return
    return sorted(list(common_set))
#time O(nmlog(m))
#space O(m)
