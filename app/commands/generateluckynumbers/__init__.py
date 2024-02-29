# generate_lucky_numbers_command.py
from abc import ABC, abstractmethod
import random

class GenerateLuckyNumbersCommand(Command):
    def execute(self):
        lucky_numbers = [random.randint(1, 100) for _ in range(3)]
        print(f"Your lucky numbers are: {lucky_numbers}")
