#binary search
def minEatingSpeed(piles, H):
    # Define the possible range of Koko's speed
    left, right = 1, max(piles)

    while left < right:
        # Try the middle value as Koko's speed
        mid = (left + right) // 2

        # Calculate the total time it takes for Koko to eat all the bananas at this speed
        time = sum((pile - 1) // mid + 1 for pile in piles)

        # If the total time is greater than the number of hours before the guards return, Koko's speed must be higher
        if time > H:
            left = mid + 1
        # Otherwise, Koko's speed can be lower
        else:
            right = mid

    return left
#time O(logm)
#space O(1)
