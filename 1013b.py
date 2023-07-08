def canThreePartsEqualSum(arr):
    # Calculate the total sum of the array
    total_sum = sum(arr)

    # If the total sum is not divisible by 3, we cannot partition the array into three parts with equal sums
    if total_sum % 3 != 0:
        return False

    # The sum of each part should be the total sum divided by 3
    target_sum = total_sum // 3
    running_sum = 0
    count = 0

    for num in arr:
        running_sum += num
        if running_sum == target_sum:
            running_sum = 0
            count += 1

    # If we have found three parts with equal sums, we return True. 
    # We check count >= 3 to handle cases where the array contains all zeros.
    return count >= 3
#time O(n)
