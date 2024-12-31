class DFA:
    def __init__(self, num_states, input_symbols, start_state, final_states, transition_function):
        self.num_states = num_states
        self.input_symbols = input_symbols
        self.start_state = start_state
        self.final_states = final_states
        self.transition_function = transition_function

    def is_accepting(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol not in self.input_symbols:
                return False

            current_state = self.transition_function.get((current_state, symbol))

            if current_state is None:
                return False

        return current_state in self.final_states


def main():
    print("Enter DFA configuration:")

    num_states = int(input("Number of states: "))

    input_symbols = input("Input symbols (space-separated): ").split()

    start_state = input("Starting state: ")

    num_final_states = int(input("Number of final states: "))
    final_states = input("Final states (space-separated): ").split()

    print("Enter transition function as: current_state input_symbol next_state")
    print("Type 'END' to stop entering transitions.")
    transition_function = {}

    while True:
        transition = input("Transition: ")

        if transition.strip().upper() == 'END':
            break

        current_state, input_symbol, next_state = transition.split()
        transition_function[(current_state, input_symbol)] = next_state

    dfa = DFA(num_states, input_symbols, start_state, final_states, transition_function)

    print("\nDFA created successfully! Test it below:")

    while True:
        test_string = input("Enter a string to test (or type 'EXIT' to quit): ")

        if test_string.strip().upper() == 'EXIT':
            break

        if dfa.is_accepting(test_string):
            print(f"String '{test_string}' is accepted.")
        else:
            print(f"String '{test_string}' is rejected.")


if __name__ == "__main__":
    main()
