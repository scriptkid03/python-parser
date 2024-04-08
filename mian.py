import re

# Define sets of keywords, operators, and separators used in the language
keywords = {'int', 'float', 'char', 'if', 'else', 'while', 'for', 'return'}
operators = {'+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>='}
separators = {';', ',', '(', ')', '{', '}'}

# Regular expressions to match identifier, integer, float, and char patterns
identifier_pattern = r'^[a-zA-Z_]\w*$'
integer_pattern = r'^[+-]?\d+$'
float_pattern = r'^[+-]?\d+\.\d+$'
char_pattern = r"^'.{1}'$"

def parse_program(filename):
    # Function to parse the entire program file
    errors = []  # List to collect syntax errors

    # Read the file and process each line
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines, 1):
        parse_statement(line.strip(), i, errors)  # Parse each line

    # Output results based on errors found
    if errors:
        for error in errors:
            print(error)
    else:
        print("Syntax analysis performed successfully with no errors found")

def parse_statement(line, line_number, errors):
    # Function to parse a single statement within a line
    if not line:
        return

    # Tokenize the line into words and separators
    tokens = re.findall(r'\w+|[^\w\s]', line)

    if tokens[0] in keywords:
        # Check for keyword-based statements (if, while, for, return)
        if tokens[0] == 'if':
            parse_if_statement(tokens, line_number, errors)
        elif tokens[0] == 'while':
            parse_while_statement(tokens, line_number, errors)
        elif tokens[0] == 'for':
            parse_for_statement(tokens, line_number, errors)
        elif tokens[0] == 'return':
            parse_return_statement(tokens, line_number, errors)
        else:
            errors.append(f"ERROR at Line {line_number}: Invalid statement")
    elif re.match(identifier_pattern, tokens[0]):
        # Check for identifier-based statements (assignment or declaration/print)
        if tokens[1] == '=':
            parse_assignment(tokens, line_number, errors)
        else:
            parse_declaration_or_print(tokens, line_number, errors)
    else:
        errors.append(f"ERROR at Line {line_number}: Invalid statement")

def parse_if_statement(tokens, line_number, errors):
    # Function to parse if statement
    pass

def parse_while_statement(tokens, line_number, errors):
    # Function to parse while statement
    pass

def parse_for_statement(tokens, line_number, errors):
    # Function to parse for statement
    pass

def parse_return_statement(tokens, line_number, errors):
    # Function to parse return statement
    pass

def parse_assignment(tokens, line_number, errors):
    # Function to parse assignment statement
    pass

def parse_declaration_or_print(tokens, line_number, errors):
    # Function to parse declaration or print statement based on the first token
    if tokens[0] == 'i':
        parse_declaration(tokens[1:], line_number, errors, data_type='int')
    elif tokens[0] == 'f':
        parse_declaration(tokens[1:], line_number, errors, data_type='float')
    elif tokens[0] == 'p':
        parse_print(tokens[1:], line_number, errors)
    else:
        errors.append(f"ERROR at Line {line_number}: Invalid declaration or print statement")

def parse_declaration(tokens, line_number, errors, data_type):
    # Function to parse variable declaration
    if re.match(identifier_pattern, tokens[0]):
        # Valid variable name
        if len(tokens) > 1 and tokens[1] == '=':
            # Assignment after declaration
            parse_assignment(tokens[2:], line_number, errors, data_type)
        elif len(tokens) == 1:
            # Just a declaration
            print(f"Declaration of {data_type} variable '{tokens[0]}' at Line {line_number}")
        else:
            errors.append(f"ERROR at Line {line_number}: Invalid declaration syntax")
    else:
        errors.append(f"ERROR at Line {line_number}: Invalid variable name")

def parse_print(tokens, line_number, errors):
    # Function to parse print statement
    if re.match(identifier_pattern, tokens[0]):
        print(f"Print statement for variable '{tokens[0]}' at Line {line_number}")
    else:
        errors.append(f"ERROR at Line {line_number}: Invalid variable name")

# Accept filename as user input
filename = input("Enter the directory of the file to parse: ")
parse_program(filename)
