def productExceptSelf(nums):
    n = len(nums)

    # Initialize the left_products and right_products array with 1's
    left_products = [1]*n
    right_products = [1]*n

    # Compute the left_products array
    for i in range(1, n):
        left_products[i] = nums[i - 1] * left_products[i - 1]

    # Compute the right_products array
    for i in reversed(range(n - 1)):
        right_products[i] = nums[i + 1] * right_products[i + 1]

    # Compute the final result array
    return [left_products[i] * right_products[i] for i in range(n)]

#time O(n)
#space O(1)
