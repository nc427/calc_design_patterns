from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

# Concrete Command Implementations

class ConcreteCommand(Command):
    def execute(self):
        print("Executing ConcreteCommand")

class AnotherCommand(Command):
    def execute(self):
        print("Executing AnotherCommand")

class GreetCommand(Command):
    def execute(self):
        print("Hello! Welcome to the command example.")

class GoodbyeCommand(Command):
    def execute(self):
        print("Goodbye! Have a great day.")

class ExitCommand(Command):
    def execute(self):
        print("Exiting the program.")
        exit()

class MenuCommand(Command):
    def __init__(self, command_mapping):
        self.command_mapping = command_mapping

    def execute(self):
        print("Menu:")
        for key, value in self.command_mapping.items():
            print(f"{key}. {value.__name__}")

        choice = input("Enter your choice: ")

        try:
            chosen_command = self.command_mapping[choice]
            chosen_command().execute()
        except KeyError:
            print("Invalid choice. Please enter a valid option.")

class GenerateLuckyNumbersCommand(Command):
    def execute(self):
        import random
        lucky_numbers = [random.randint(1, 100) for _ in range(3)]
        print(f"Your lucky numbers are: {lucky_numbers}")
