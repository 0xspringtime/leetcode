def multiply(num1: str, num2: str) -> str:
    n1 = len(num1)
    n2 = len(num2)
    # initialising result array with zeros
    result = [0] * (n1 + n2)
    
    for i in range(n1-1, -1, -1):  # starting from last digit of num1
        for j in range(n2-1, -1, -1):  # starting from last digit of num2
            # Multiply the digits, and add it to the position where it should be added
            product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1 = i + j  # position of next digit
            p2 = i + j + 1  # position of current digit
            
            # Add the product to the existing result at the position
            total = product + result[p2]
            
            # Update the result array
            result[p2] = total % 10  # this digit
            result[p1] += total // 10  # carry for the next digit

    # Removing the leading zeros
    i = 0
    while i < len(result) and result[i] == 0:
        i += 1
    result = result[i:]
    
    # converting each digit in the result to string and joining them
    final_result = ''.join(map(str, result))
    
    # return final result if not empty, otherwise return "0"
    return final_result if final_result != '' else "0"
#time O(n*m)
#space O(n+m)
