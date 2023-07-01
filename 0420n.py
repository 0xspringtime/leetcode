def strongPasswordChecker(password):
    # The minimum number of steps needed.
    steps = 0

    # The number of each type of character.
    num_lowercase, num_uppercase, num_digits = 0, 0, 0

    # Keep track of the number of characters in the current sequence.
    sequence_length = 1
    prev_char = password[0] if password else None

    for i in range(1, len(password) + 1):
        # If we're still in the same sequence, increase sequence_length.
        # Otherwise, reset sequence_length to 1.
        if i < len(password) and password[i] == prev_char:
            sequence_length += 1
        else:
            # If we've ended a sequence of 3 or more identical characters,
            # we'll need to replace some of them.
            if sequence_length >= 3:
                steps += sequence_length // 3

            # Start a new sequence.
            sequence_length = 1

        # Keep track of the number of each type of character.
        if i < len(password):
            if password[i].islower():
                num_lowercase += 1
            elif password[i].isupper():
                num_uppercase += 1
            elif password[i].isdigit():
                num_digits += 1
            prev_char = password[i]

    # Calculate the number of types of characters missing.
    num_types_missing = 3 - (num_lowercase > 0) - (num_uppercase > 0) - (num_digits > 0)

    if len(password) < 6:
        # If the password is too short, we can insert the missing types while
        # also extending the password to 6 characters.
        steps = max(6 - len(password), num_types_missing)
    elif len(password) > 20:
        # If the password is too long, we need to delete some characters.
        # We can also use these deletions to remove some sequences of three identical characters,
        # reducing the number of replacements we need to make.
        num_deletions = len(password) - 20

        # If we have any sequences of length 3k, we can make them non-sequences
        # by deleting a single character.
        steps += num_deletions

        # If there are still any sequences of three identical characters, we'll need to replace them.
        steps = max(steps, num_types_missing)
    else:
        # If the length is okay, we just need to make sure we have all types of characters.
        steps = max(steps, num_types_missing)

    return steps

