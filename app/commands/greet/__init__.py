# greet_command.py
from abc import ABC, abstractmethod

class GreetCommand(Command):
    def execute(self):
        print("Hey Queen!")
