class FSM:
    def __init__(self):
        self.state = self.start_state
        # Define your states and transitions in a nested dictionary
        self.transitions = { 
            'state1': {
                'input1': self.state2,
                'input2': self.state3
            },
            'state2': {
                'input1': self.state1,
                'input3': self.state3
            }
            # add as many states and transitions as needed...
        }

    def process(self, inputs):
        for input in inputs:
            self.transition(input)

    def transition(self, input):
        if input in self.transitions[self.state]:
            self.state = self.transitions[self.state][input]
        else:
            raise ValueError(f"Invalid input {input} for current state {self.state}")

    # define your states
    def start_state(self):
        # do something...
        pass

    def state1(self):
        # do something...
        pass

    def state2(self):
        # do something...
        pass

    # add as many states as needed...
fsm = FSM()
fsm.process(['input1', 'input2', 'input1'])
#useful when you need to design a system that has a specific, defined set of states, and where it's possible to model transitions between those states based on certain conditions or inputs
