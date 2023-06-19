def floyd_cycle_detection(f, x0):
    # Step 1: Find the cycle
    tortoise = f(x0)
    hare = f(f(x0))

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Step 2: Find the start of the cycle
    hare = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)

    return hare

# Pseudo-random number generator function
def generate_number(x):
    return (a * x + c) % m

# Parameters for the pseudo-random number generator
a = 1103515245
c = 12345
m = 2**31 - 1

# Starting point for the generator
x0 = 1

# Find the cycle using Floyd's algorithm
cycle_start = floyd_cycle_detection(generate_number, x0)
cycle_length = 1

# Determine the length of the cycle
pointer = generate_number(cycle_start)
while pointer != cycle_start:
    pointer = generate_number(pointer)
    cycle_length += 1

# Print the cycle start and length
print("Cycle Start:", cycle_start)
print("Cycle Length:", cycle_length)

