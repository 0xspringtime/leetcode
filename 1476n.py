class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        # Iterate over the subrectangle and update each value with newValue
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row, col):
        # Return the value at the specified row and column coordinates
        return self.rectangle[row][col]
#time O((row2 - row1 + 1) * (col2 - col1 + 1))
#space O(1)
