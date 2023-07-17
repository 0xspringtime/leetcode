#pass iterable (such as list or string)
from collections import Counter

my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
counter = Counter(my_list)

print(counter)
#Output:
#print(counter[1])  # Output: 4
#print(counter[2])  # Output: 3
#print(counter[5])  # Output: 0 (since 5 is not present in the Counter)

#can also retrieve a list of unique elements from the Counter using the .keys() method, and you can retrieve the frequencies using the .values() method. Additionally, you can get a list of element-frequency pairs using the .items() method
print(list(counter.keys()))    # Output: [1, 2, 3, 4]
print(list(counter.values()))  # Output: [4, 3, 2, 1]
print(list(counter.items()))   # Output: [(1, 4), (2, 3), (3, 2), (4, 1)]

