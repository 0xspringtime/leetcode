def subtractProductAndSum(n):
    # Convert the integer to string for easy access to digits
    digits_str = str(n)
    
    # Initialize product to 1 and sum to 0
    product = 1
    sum_ = 0
    
    # Iterate over each character (digit) in the string
    for digit_str in digits_str:
        # Convert the character back to an integer
        digit = int(digit_str)
        
        # Update product and sum
        product *= digit
        sum_ += digit
    
    # Return the difference between the product and the sum
    return product - sum_
#time O(d)
#space O(1)
