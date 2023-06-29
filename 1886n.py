idef findRotation(mat, target):
    # The matrix is rotated four times in the for loop.
    for _ in range(4):
        # If the matrix equals the target at any rotation, return True
        if mat == target:
            return True
        # Steps for rotating the matrix 90 degrees clockwise
        # Reverse the original matrix
        mat = mat[::-1]
        # Swap the symmetric elements
        for i in range(len(mat)):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # If after all rotations the matrices are not equal, return False
    return False
#time O(n^2)
#space O(n^2)
