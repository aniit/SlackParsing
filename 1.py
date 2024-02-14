def parse_message(line):
    """Parses a single message line and returns its components."""
    # Assuming format: 'Timestamp - Username: Message'
    try:
        timestamp_user, message = line.split(':', 1)
        timestamp, user = timestamp_user.split(' - ', 1)
        return timestamp.strip(), user.strip(), message.strip()
    except ValueError:
        return None, None, None

def generate_documentation(input_filepath, output_filepath):
    """Generates a Markdown file from the parsed messages."""
    with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
        outfile.write("# Support Documentation Generated from Slack Messages\n\n")
        
        for line in infile:
            timestamp, user, message = parse_message(line)
            if timestamp and user and message:
                # Format and write the message to the Markdown file
                outfile.write(f"**{timestamp} - {user}**\n\n{message}\n\n---\n\n")

if __name__ == "__main__":
    input_filepath = 'path/to/your/messages.txt'  # Update with the path to your text file
    output_filepath = 'path/to/your/documentation.md'  # Update with your desired output path
    generate_documentation(input_filepath, output_filepath)
    print("Documentation has been generated successfully.")
