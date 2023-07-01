def laser_beams(bank):
    # Convert strings to lists of indices of '1's
    rows = [[i for i, x in enumerate(row) if x == '1'] for row in bank]

    # Initialize total count of beams
    total_beams = 0

    # Iterate over all pairs of rows
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            # Check if there is no security device in between
            if all(not rows[k] for k in range(i + 1, j)):
                # Add the number of beams between the two rows
                total_beams += len(rows[i]) * len(rows[j])

    return total_beams
#time O(n^3)
#space O(n)
