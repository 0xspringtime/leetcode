def numMagicSquaresInside(grid):
    R, C = len(grid), len(grid[0])

    def is_magic(square):
        # Check if square is a permutation of [1, 2, 3, 4, 5, 6, 7, 8, 9]
        vals = {x for row in square for x in row}
        if vals != set(range(1, 10)):
            return False

        # Check if sum of rows, columns and diagonals is 15
        sums = [sum(row) for row in square]
        sums.extend(sum(square[i][j] for i in range(3)) for j in range(3))
        sums.append(sum(square[i][i] for i in range(3)))
        sums.append(sum(square[i][2-i] for i in range(3)))

        return len(set(sums)) == 1 and sums[0] == 15

    # Check each 3x3 subgrid
    return sum(is_magic([grid[i+di][j+dj] for di in range(3) for dj in range(3)])
               for i in range(R-2) for j in range(C-2))
#time O(m*n)
#space O(1)
