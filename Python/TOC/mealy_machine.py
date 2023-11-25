class MealyMachine:
    def __init__(self):
        self.state = "OFF"

    def transition(self, input):
        if input == "toggle":
            if self.state == "OFF":
                self.state = "ON"
                return "Light is ON"
            else:
                self.state = "OFF"
                return "Light is OFF"
        else:
            return "Invalid input"

# Example usage
mealy_machine = MealyMachine()

while True:
    user_input = input("Enter 'toggle' to switch the light (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    output = mealy_machine.transition(user_input)
    print(output)
