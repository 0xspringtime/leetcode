#greedy
def carFleet(target, position, speed):
    # Initialize the number of car fleets to 0
    fleets = 0
    # Store the arrival times of cars
    arrival_times = []

    # Create a list of tuples with (position, speed) and sort it by position in descending order
    for pos, sp in sorted(zip(position, speed), reverse=True):
        # Calculate the time required to reach the target and store it in arrival_times
        arrival_times.append((target - pos) / sp)

    # Loop through the arrival_times
    for i in range(1, len(arrival_times)):
        # If the current car arrives earlier, it forms a fleet with the previous car(s)
        if arrival_times[i] <= arrival_times[i-1]:
            arrival_times[i] = arrival_times[i-1]
        # If the current car arrives later, it forms a new fleet
        else:
            fleets += 1

    # If there are cars, the last one forms a fleet by itself
    if arrival_times:
        fleets += 1

    return fleets
#time O(nlogn)
#space O(n)
