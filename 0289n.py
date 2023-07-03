def gameOfLife(board):
    # Neighbors array to find 8 neighboring cells for a given cell
    neighbors = [(1,0), (1,-1), (-1,1), (-1,0), (-1,-1), (0,1), (0,-1), (1,1)]

    rows = len(board)
    cols = len(board[0])

    # Iterate through board cell by cell.
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0

            # For each cell count the number of live neighbors.
            for neighbor in neighbors:
                r = (row + neighbor[0])
                c = (col + neighbor[1])

                # Check the validity of the neighboring cell and if it was originally a live cell.
                if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                    live_neighbors += 1

            # Rule 1 or Rule 3
            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # Mark as Transition
                board[row][col] = -1
            # Rule 4
            if board[row][col] == 0 and live_neighbors == 3:
                # Mark as Transition
                board[row][col] = 2

    # Replace the board with the next stage.
    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0
#time O(m*n)
#space O(1)
