import sys
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print("Menu from the MenuCommandPlugin!")
        