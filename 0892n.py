class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        # Initialize surface area to 0
        area = 0

        # Loop over each cell in the grid
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    area += 2  # Top and bottom surface area
                    
                    # For each of the four sides, add the difference in heights (if positive)
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        # If neighboring cell is within grid bounds, take its height; else it's 0
                        nv = grid[nr][nc] if 0 <= nr < N and 0 <= nc < N else 0
                        
                        area += max(grid[r][c] - nv, 0)

        return area
#time O(n^2)
#space O(1)
