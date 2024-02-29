# goodbye_command.py
from abc import ABC, abstractmethod

class GoodbyeCommand(Command):
    def execute(self):
        print("Goodbye! Have a great day.")
