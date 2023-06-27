def maximumWealth(accounts):
    # Initialize maximum wealth to be -infinity
    max_wealth = float('-inf')

    # Iterate through each customer's accounts
    for customer_accounts in accounts:
        # Compute the customer's wealth
        customer_wealth = sum(customer_accounts)

        # If this customer's wealth is greater than the current max wealth, update max wealth
        if customer_wealth > max_wealth:
            max_wealth = customer_wealth

    # After going through all customers, return the max wealth
    return max_wealth
#time O(m*n)
#space O(1)
