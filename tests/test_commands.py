import pytest
from app import App

@pytest.mark.parametrize("user_inputs, expected_output", [
    (['greet', 'exit'], "Exiting..."),
    (['menu', 'exit'], "Exiting..."),
])
def test_app_commands(capfd, monkeypatch, user_inputs, expected_output):
    """Test various commands in the REPL."""
    inputs = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == expected_output, "The app did not exit as expected"

    captured = capfd.readouterr()
    assert expected_output in captured.out, f"Expected output not found in captured output for commands: {user_inputs}"
