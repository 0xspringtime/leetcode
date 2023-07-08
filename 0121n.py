def maxProfit(prices):
    # Initialize minimum price with the first price in the list
    min_price = prices[0]
    # Initialize maximum profit as zero
    max_profit = 0
    # Iterate over the prices
    for price in prices:
        # If the current price is less than the minimum price we have seen so far,
        # update the minimum price
        if price < min_price:
            min_price = price
        # If the profit we can get by selling at the current price is greater than the maximum profit we have seen so far,
        # update the maximum profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
    # Return the maximum profit
    return max_profit
#time O(n)
#space O(1)
