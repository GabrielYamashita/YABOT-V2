
def process_command(command, incoming_msg):
    # Implement command processing logic
    if command == 'show log':
        return f'Incoming Message:\n\n{incoming_msg}'


    return f"Command processed: '{command}'"