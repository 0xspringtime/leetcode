from collections import Counter

def topKFrequent(nums, k):
    # Create a Counter from the nums list
    count = Counter(nums)
    # Use the most_common() method to get the k most common elements
    # The result will be a list of tuples, where each tuple is (element, count)
    most_common = count.most_common(k)
    # Extract the elements from the most_common list and return them
    return [item[0] for item in most_common]
#time O(nlogk)
#space O(n)
