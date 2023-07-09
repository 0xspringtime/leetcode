#greedy
def minSwaps(grid):
    n = len(grid)
    zeroes = [0]*n

    # Count trailing zeroes for each row
    for i in range(n):
        count = 0
        for j in range(n-1, -1, -1):
            if grid[i][j] == 0:
                count += 1
            else:
                break
        zeroes[i] = count

    swaps = 0
    # For each row from top to bottom
    for i in range(n):
        target_zeroes = n - i - 1
        if zeroes[i] < target_zeroes:
            for j in range(i+1, n):
                if zeroes[j] >= target_zeroes:
                    swaps += j - i
                    zeroes = zeroes[:i] + [zeroes[j]] + zeroes[i:j] + zeroes[j+1:]
                    break
            else:
                return -1
    return swaps
#time O(n^2)
#space O(n)
