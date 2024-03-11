import pytest
from commands import CommandHandler, ConcreteCommand, AnotherCommand, GreetCommand, GoodbyeCommand, ExitCommand, MenuCommand, GenerateLuckyNumbersCommand

@pytest.fixture
def command_handler():
    handler = CommandHandler()
    handler.register_command("concrete", ConcreteCommand())
    handler.register_command("another", AnotherCommand())
    handler.register_command("greet", GreetCommand())
    handler.register_command("goodbye", GoodbyeCommand())
    handler.register_command("exit", ExitCommand())
    handler.register_command("menu", MenuCommand({"1": ConcreteCommand, "2": AnotherCommand}))
    handler.register_command("generate_lucky_numbers", GenerateLuckyNumbersCommand())
    return handler

def test_execute_concrete_command(capfd, command_handler):
    command_handler.execute_command("concrete")
    captured = capfd.readouterr()
    assert "Executing ConcreteCommand" in captured.out

def test_execute_another_command(capfd, command_handler):
    command_handler.execute_command("another")
    captured = capfd.readouterr()
    assert "Executing AnotherCommand" in captured.out

def test_execute_greet_command(capfd, command_handler):
    command_handler.execute_command("greet")
    captured = capfd.readouterr()
    assert "Hello! Welcome to the command example." in captured.out

def test_execute_goodbye_command(capfd, command_handler):
    command_handler.execute_command("goodbye")
    captured = capfd.readouterr()
    assert "Goodbye! Have a great day." in captured.out

def test_execute_exit_command(capfd, command_handler):
    with pytest.raises(SystemExit):
        command_handler.execute_command("exit")

def test_execute_menu_command_choice_1(capfd, monkeypatch, command_handler):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    command_handler.execute_command("menu")
    captured = capfd.readouterr()
    assert "Executing ConcreteCommand" in captured.out

def test_execute_menu_command_choice_2(capfd, monkeypatch, command_handler):
    monkeypatch.setattr('builtins.input', lambda _: "2")
    command_handler.execute_command("menu")
    captured = capfd.readouterr()
    assert "Executing AnotherCommand" in captured.out

def test_execute_menu_command_invalid_choice(capfd, monkeypatch, command_handler):
    monkeypatch.setattr('builtins.input', lambda _: "invalid_choice")
    command_handler.execute_command("menu")
    captured = capfd.readouterr()
    assert "Invalid choice. Please enter a valid option." in captured.out

def test_execute_generate_lucky_numbers_command(capfd, command_handler):
    command_handler.execute_command("generate_lucky_numbers")
    captured = capfd.readouterr()
    assert "Your lucky numbers are:" in captured.out

