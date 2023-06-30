#two pointer
#DFS
def maxArea(height):
    # Initialize left and right pointers
    left, right = 0, len(height) - 1

    # Initialize max_area as 0
    max_area = 0

    # While left pointer is less than right pointer
    while left < right:
        # Calculate the area
        area = min(height[left], height[right]) * (right - left)

        # Update max_area if area is greater than max_area
        max_area = max(max_area, area)

        # If the height at left pointer is less than or equal to the height at right pointer
        if height[left] <= height[right]:
            # Move the left pointer towards right
            left += 1
        else:
            # Move the right pointer towards left
            right -= 1

    # Return the max_area
    return max_area
#time O(n+m)
#space O(n+m)
