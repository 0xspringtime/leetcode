def tictactoe(moves):
    # Create a 3x3 grid to represent the Tic-Tac-Toe board
    grid = [[' ' for _ in range(3)] for _ in range(3)]

    # Variable to keep track of the current player (A or B)
    current_player = 'A'

    # Perform moves one by one
    for row, col in moves:
        # Mark the current move on the grid with the current player's symbol
        grid[row][col] = current_player

        # Check if the current player has won
        if is_winner(grid, current_player):
            return current_player

        # Switch the player for the next move
        current_player = 'B' if current_player == 'A' else 'A'

    # Check if the game is still pending or ended in a draw
    if len(moves) == 9:
        return 'Draw'
    else:
        return 'Pending'


def is_winner(grid, player):
    # Check rows
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(grid[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    # No winning condition found
    return False
#time O(1)
#space O(1)
