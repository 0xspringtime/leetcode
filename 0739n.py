#stack
def dailyTemperatures(temperatures):
    # Initialize a list of zeros with the length of temperatures.
    answer = [0]*len(temperatures)
    # Initialize an empty stack to store the temperatures.
    stack = []
    # Start iterating over the array from the end to the beginning.
    for i in range(len(temperatures)-1, -1, -1):
        # While the stack is not empty and the current temperature is
        # greater or equal to the temperature at the top of the stack.
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            # Pop the top temperature from the stack.
            stack.pop()
        # If the stack is not empty, calculate the number of days until
        # a warmer temperature.
        if stack:
            answer[i] = stack[-1] - i
        # Push the current day to the stack.
        stack.append(i)
    # Return the final list of days until a warmer temperature.
    return answer
#time O(n)
#space O(n)
