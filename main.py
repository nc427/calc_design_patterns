from app import App

# Run the application
if __name__ == "__main__":
    app = App()
    app.load_plugins()

    print("Type 'exit' to exit.")
    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == 'exit':
            break

        app.command_handler.execute_command(user_input)
