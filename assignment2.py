import numpy as np


class WeatherSimulation: 
    def __init__(self, transition_probabilities, holding_times):
        """_summary_

        Args:
            transition_probabilities (_type_): _description_
            holding_times (_type_): _description_

        Raises:
            RuntimeError: _description_
        """        ''''''
        self.transition_probabilities = transition_probabilities
        self.holding_times = holding_times
        self.state = 'sunny'
        self.hold_time = 0
        
        # Calculating total values of transition states
        for value in transition_probabilities:
            total = sum(transition_probabilities[value].values())
            # Raise error if total is greater than 1
            if total != 1.0:
                raise RuntimeError('The Value is greater than 1')

    # Returns the list of states
    def get_states(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return list(self.transition_probabilities.keys())

    # Returns the current state
    def current_state(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return self.state

    # Changes to next state 
    def next_state(self):      
        if self.hold_time <= 0:
            # Randomly chooses a state from transition probabilities
            self.state = np.random.choice(self.get_states(), p=list(self.transition_probabilities[self.state].values()))
            self.hold_time = self.holding_times[self.state]
        self.hold_time -= 1

    # Changes current state to new state
    def set_state(self, new_state):
        """_summary_

        Args:
            new_state (_type_): _description_
        """        
        self.state = new_state

    # Returns remaining hours in the current state
    def current_state_remaining_hours(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return self.hold_time

    # Simulates from current state to next state
    def iterable(self):
        """_summary_

        Yields:
            _type_: _description_
        """        
        while True:
            yield self.state
            self.next_state()

    def simulate(self, hours):
        """_summary_

        Args:
            hours (_type_): _description_

        Returns:
            _type_: _description_
        """        
        state_keys = dict()
        for i in self.transition_probabilities.keys():
            state_keys[i] = 0
        for i in range(hours):
            state_keys[self.current_state()] += 1
            self.next_state()
        state_values = list(state_keys.values())
        
        # percentages for each state
        state_percentages = []
        for i in range(len(state_values)):
            print(state_values[i], type(state_values[i]))
            state_percentages.append(state_values[i]/hours*100)
        return state_percentages


# Sample of input data types
my_transitions = {
    'sunny': {'sunny': 0.7, 'cloudy': 0.3, 'rainy': 0, 'snowy': 0},
    'cloudy': {'sunny': 0.5, 'cloudy': 0.3, 'rainy': 0.15, 'snowy': 0.05},
    'rainy': {'sunny': 0.7, 'cloudy': 0.2, 'rainy': 0.5, 'snowy': 0.05},
    'snowy': {'sunny': 0.7, 'cloudy': 0.1, 'rainy': 0.05, 'snowy': 0.15}
}
my_holding_times = {'sunny': 1, 'cloudy': 2, 'rainy': 2, 'snowy': 1}
