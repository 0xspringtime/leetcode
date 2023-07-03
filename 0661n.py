def imageSmoother(img):
    # Get the number of rows and columns
    m, n = len(img), len(img[0])
    
    # Initialize a two-dimensional list with the same dimensions to store the results
    result = [[0] * n for _ in range(m)]
    
    # Define the directions of the 8 neighbours for each cell
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    # Iterate over each cell in the image
    for i in range(m):
        for j in range(n):
            # Initialize the sum and the count of valid cells
            sum_val, count = img[i][j], 1
            
            # Iterate over the 8 neighbours
            for dx, dy in directions:
                # Calculate the coordinates of the neighbour
                x, y = i + dx, j + dy
                
                # Check if the neighbour is within the image
                if 0 <= x < m and 0 <= y < n:
                    # Add the value of the neighbour to the sum and increase the count
                    sum_val += img[x][y]
                    count += 1
            
            # Calculate the average and floor the value to get the final result of this cell
            result[i][j] = sum_val // count
    
    # Return the image after applying the smoother
    return result
#time O(m * n)
#space O(m * n)
