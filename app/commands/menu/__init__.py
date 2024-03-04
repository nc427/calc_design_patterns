# menu_command.py
from abc import ABC, abstractmethod

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
