class MooreMachine:
    def __init__(self):
        self.state = "OFF"

    def transition(self, input_str):
        if input_str.isalpha():
            input_str = input_str.lower()  # Convert to lowercase for case-insensitive comparison
            if input_str == "toggle":
                if self.state == "OFF":
                    self.state = "ON"
                else:
                    self.state = "OFF"

    def output(self):
        if self.state == "OFF":
            return "Light is OFF"
        else:
            return "Light is ON"


# Example usage
moore_machine = MooreMachine()

while True:
    user_input = input("Enter 'toggle' to switch the light (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    moore_machine.transition(user_input)
    print(moore_machine.output())
