import numpy as np

def minOperations(grid, x):
    # Convert the grid to a numpy array for easier manipulation
    grid_np = np.array(grid)
    
    # Flatten the array and calculate the mod of each element with respect to x
    mods = np.mod(grid_np.flatten(), x)
    
    # If not all mods are equal, return -1
    if not np.all(mods == mods[0]):
        return -1
    
    # Calculate the number of operations needed to transform each number to the median
    grid_np = grid_np // x
    median = np.median(grid_np.flatten())
    
    # Calculate the minimum number of operations
    operations = np.sum(np.abs(grid_np.flatten() - median))
    
    return int(operations)
#time O(mnlog(mn))
#space O(m*n)
