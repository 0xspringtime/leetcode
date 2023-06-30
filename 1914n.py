def rotateGrid(grid, k):
    m, n = len(grid), len(grid[0])
    
    for layer in range(min(m, n) // 2):
        layer_elements = []
        
        # Get all elements in the current layer and put them in layer_elements list
        for i in range(layer, m - layer):
            for j in range(layer, n - layer):
                if i == layer or i == m - layer - 1 or j == layer or j == n - layer - 1:
                    layer_elements.append(grid[i][j])
        
        # Perform the rotation
        l = len(layer_elements)
        rotated_elements = layer_elements[-k % l:] + layer_elements[:-k % l]
        
        # Replace the original layer elements with rotated elements
        idx = 0
        for i in range(layer, m - layer):
            for j in range(layer, n - layer):
                if i == layer or i == m - layer - 1 or j == layer or j == n - layer - 1:
                    grid[i][j] = rotated_elements[idx]
                    idx += 1
    
    return grid
#time  O(mnk)
#space O(m*n)
