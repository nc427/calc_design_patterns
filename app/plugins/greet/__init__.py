# app/plugins/greet_plugin.py

from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        print("Hello from the GreetCommandPlugin!")