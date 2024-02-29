# exit_command.py
from abc import ABC, abstractmethod

class ExitCommand(Command):
    def execute(self):
        print("Exiting the program.")
        exit()
