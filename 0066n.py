def plusOne(digits):
    # Start from the last element in digits
    for i in range(len(digits) - 1, -1, -1):
        # If the digit is less than 9, just increment the digit and return digits
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the digit is 9, make it 0 and continue the loop to the next digit
        digits[i] = 0

    # If all digits are 9's, the code will come to this line
    # We add 1 at the start of the array
    return [1] + digits
#time O(n)
#space O(1)
