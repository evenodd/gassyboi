from typing import Callable

class StateAlerter:
    def __init__(self, states : dict, start : str, escalate_handler : Callable, de_escalate_handler : Callable):
        self.states = states
        self.curr_state = start
        self.last_state = None
        self.escalate_handler = escalate_handler
        self.de_escalate_handler = de_escalate_handler

    def get_curr_state_value(self):
        return self.states[self.curr_state]

    def update(self, value:int) -> bool :
        new_state = self._get_state(value)
        if new_state is not self.curr_state:
            self.last_state = self.curr_state
            self.curr_state = new_state
            
            if (self.states[self.curr_state] > self.states[self.last_state]):
                self.escalate_handler(self, value)
            else:
                self.de_escalate_handler(self, value)
            return True
        return False

    def _get_state(self, value:int):
        potential_value_candidate = -1
        potential_label_candidate = None
        for label, bound in self.states.items():
            print("testing for state {} with bound {}, using candidate {} : {}".format(label, bound, potential_value_candidate, potential_label_candidate))
            if value >= bound and bound > potential_value_candidate:
                potential_label_candidate = label
                potential_value_candidate = bound
        return potential_label_candidate 

