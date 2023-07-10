def maxProfit(prices):
    # Initialize total profit to 0
    profit = 0

    # Iterate over the price array from the second day to the end
    for i in range(1, len(prices)):
        # If the price of the stock on the current day is greater than the previous day
        if prices[i] > prices[i-1]:
            # Then we buy the stock on the previous day and sell it on the current day
            # Add the profit to the total profit
            profit += prices[i] - prices[i-1]
    
    # Return the total profit
    return profit
#time O(n)
#space O(1)
