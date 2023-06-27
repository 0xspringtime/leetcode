#dynamic programming
def maxProfit(prices):
    if not prices:
        return 0

    hold = -prices[0]
    cooldown = 0
    sell = 0

    for price in prices[1:]:
        hold, cooldown, sell = max(hold, cooldown - price), max(cooldown, sell), hold + price

    return max(sell, cooldown)
#time O(n)
#space O(1)
