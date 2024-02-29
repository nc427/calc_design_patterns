# another_command.py
from abc import ABC, abstractmethod

class AnotherCommand(Command):
    def execute(self):
        print("Executing AnotherCommand")
