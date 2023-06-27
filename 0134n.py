#greedy
def canCompleteCircuit(gas, cost):
    # If the total gas is less than the total cost, we can't make the trip
    if sum(gas) < sum(cost):
        return -1

    # The index of the starting station
    start_station = 0

    # The amount of gas left over
    gas_left = 0

    for i in range(len(gas)):
        # If adding the current gas amount makes the gas_left negative, we can't start at the current start_station,
        # so we move to the next station and reset gas_left to 0
        if gas_left + gas[i] - cost[i] < 0:
            start_station = i + 1
            gas_left = 0
        else:
            # Otherwise, we add the current gas amount to gas_left
            gas_left += gas[i] - cost[i]

    return start_station
#time O(n)
#space O(1)
