#DFS
def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    # Store the original color at the start pixel
    origColor = image[sr][sc]
    # If the original color is the same as the new color, return the image as is
    if origColor == newColor:
        return image
    # Define the DFS function
    def dfs(r, c):
        # If the current pixel is within the image bounds and its color is the same as the original color
        if r >= 0 and r < len(image) and c >= 0 and c < len(image[0]) and image[r][c] == origColor:
            # Change the color of the current pixel to the new color
            image[r][c] = newColor
            # Make recursive calls for pixels that are up, down, left or right to the current one
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
    # Call the DFS function for the start pixel
    dfs(sr, sc)
    # Return the modified image
    return image
#time O(n)
#space O(n)
