import random

class RandomizedSet:

    def __init__(self):
        # Initialize our data structures
        self.dict = {}    # Dictionary for O(1) insert and remove
        self.list = []    # List for O(1) get random element

    def insert(self, val: int) -> bool:
        # If value is not in dict, add it to both dict and list
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # If value is in dict, swap it with the last element in list and remove it
        if val in self.dict:
            idx, last = self.dict[val], self.list[-1]
            self.list[idx], self.dict[last] = last, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        # Return a random element
        return random.choice(self.list)
#time O(1)
#space O(n)
