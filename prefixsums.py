def prefix_sums(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix

#can be used to simplify certain types of calculations in an array. The idea is to create a new array where each element is the sum of all elements in the original array up to and including that index. Once the prefix sums are calculated, you can find the sum of any subarray in the original array by subtracting two elements in the prefix sum array
