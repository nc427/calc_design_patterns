# concrete_command.py
from abc import ABC, abstractmethod

class ConcreteCommand(Command):
    def execute(self):
        print("Executing ConcreteCommand")
