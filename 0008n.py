#string
#FSM
def myAtoi(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    # Initial state
    state = 'start'
    # Finite State Machine: it defines the next state and tells whether to add the digit to number
    fsm = {
        'start': {'space': ('start', False), 'sign': ('signed', False), 'number': ('in_number', True), 'other': ('end', False)},
        'signed': {'space': ('end', False), 'sign': ('end', False), 'number': ('in_number', True), 'other': ('end', False)},
        'in_number': {'space': ('end', False), 'sign': ('end', False), 'number': ('in_number', True), 'other': ('end', False)},
        'end': {'space': ('end', False), 'sign': ('end', False), 'number': ('end', False), 'other': ('end', False)},
    }

    number = 0
    sign = 1

    for c in s:
        if c == ' ':
            category = 'space'
        elif c in '-+':
            category = 'sign'
        elif c.isdigit():
            category = 'number'
        else:
            category = 'other'

        state, should_add = fsm[state][category]

        if state == 'end':
            break
        elif state == 'signed':
            sign = -1 if c == '-' else 1
        elif state == 'in_number':
            number = number * 10 + int(c)
            number = min(number, INT_MAX if sign == 1 else -INT_MIN)

    return sign * number
#time O(n)
#space O(1)
