#import numpy as np
#from scipy.linalg import expm
#
#def fibonacci(n):
#    # Define the matrix A for Fibonacci sequence
#    A = np.array([[1, 1], [1, 0]])
#
#    # Compute the matrix exponential of A
#    exp_A = expm(A)
#
#    # Extract the Fibonacci number from the exponential matrix
#    fib = exp_A[0, 1]
#
#    # Return the Fibonacci number rounded to the nearest integer
#    return int(round(fib))
#
## Generate the 10th Fibonacci number
#fibonacci_number = fibonacci(5)
#print(fibonacci_number)

import numpy as np

def fib(n):
    F = np.matrix([[1, 1], [1, 0]], dtype='int64')
    return (F ** (n))[0, 1]

print(fib(89))
