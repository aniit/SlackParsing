import re

def parse_and_format_messages(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    formatted_lines = []
    for line in lines:
        # Customize this regular expression based on your input format
        match = re.match(r'(\d{4}-\d{2}-\d{2}) - (\w+): (.*)', line)
        if match:
            date, user, message = match.groups()
            formatted_line = f"**{date} {user}**: {message}\n\n"
            formatted_lines.append(formatted_line)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("# Slack Conversation Documentation\n\n")
        output_file.writelines(formatted_lines)

if __name__ == "__main__":
    input_file_path = 'path/to/your/input.txt'  # Update this path
    output_file_path = 'path/to/your/output.md'  # Update this path
    parse_and_format_messages(input_file_path, output_file_path)
