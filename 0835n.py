def largestOverlap(img1, img2):
    n = len(img1)
    max_overlap = 0

    for dy in range(n):  # slide image 2 vertically
        for dx in range(n):  # slide image 2 horizontally
            overlap = 0
            for r in range(n):  # count overlapping 1s
                for c in range(n):
                    if r + dy < n and c + dx < n and img1[r][c] == img2[r+dy][c+dx] == 1:
                        overlap += 1
            max_overlap = max(max_overlap, overlap)
    
    return max_overlap
#time O(n^4)
#space O(1)
