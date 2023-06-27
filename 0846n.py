#priority queue
import heapq
import collections

def isNStraightHand(hand, groupSize):
    # First, we check if the total number of cards is divisible by the group size
    if len(hand) % groupSize != 0:
        return False

    # Second, we count the number of each card
    count = collections.Counter(hand)
    # And add the cards to a priority queue
    pq = sorted(count)

    # Third, while the priority queue is not empty
    while pq:
        # We try to form a group with the smallest card
        start = pq[0]
        for _ in range(groupSize):
            if start not in count:
                return False
            count[start] -= 1
            if count[start] == 0:
                del count[start]
                pq.remove(start)
            start += 1

    # Finally, we return True if we can form all groups
    return True
#time O(nlogn)
#space O(n)
