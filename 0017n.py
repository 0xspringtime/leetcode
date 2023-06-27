#BFS
def letterCombinations(digits):
    if not digits:
        return []

    # mapping of digits to letters
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Initialize the queue with an empty string
    queue = ['']

    for digit in digits:
        # For each character in the queue, remove it and append all possible letters
        for _ in range(len(queue)):
            element = queue.pop(0)
            # map the digit to its corresponding letters and add them to the queue
            for letter in phone[digit]:
                queue.append(element + letter)

    return queue
#time O(4^n)
#space O(4^n)
