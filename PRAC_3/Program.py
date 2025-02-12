import re

def load_code(file_path):
    """Load C code from a file, removing comments."""
    try:
        with open(file_path, "r") as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: Cannot read file '{file_path}'")
        return None
    
    # Remove comments
    comment_pattern = re.compile(r"//.*?$|/\*.*?\*/", re.DOTALL | re.MULTILINE)
    return re.sub(comment_pattern, "", code)


def categorize_token(token):
    """Classify a given token."""
    keywords = {"main", "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
                "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long", "register",
                "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef",
                "union", "unsigned", "void", "volatile", "while"}
    
    operators = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||"}
    
    punctuation = {";", ",", "{", "}", "(", ")", "[", "]", ":", "."}
    
    if token in keywords:
        return "Keyword"
    elif token in operators:
        return "Operator"
    elif token in punctuation:
        return "Punctuation"
    elif re.match(r"^\d+(\.\d+)?$", token):
        return "Constant"
    elif re.match(r'^".*?"|\'.*?\'$', token):
        return "String"
    elif re.match(r"\d+[A-Za-z]+", token):
        return "Lexical Error"
    else:
        return "Identifier"


def lexical_analyzer(file_path):
    """Perform lexical analysis on a C source file."""
    code = load_code(file_path)
    if code is None:
        return [], {}
    
    token_pattern = re.compile(r"\b\w+\b|[+\-*/=;,{}():]|\".*?\"|'.*?'")
    tokens = token_pattern.findall(code)
    
    categorized_tokens = [(token, categorize_token(token)) for token in tokens]
    symbol_table = {token: category for token, category in categorized_tokens if category == "Identifier"}
    
    return categorized_tokens, symbol_table


def display_results(tokens, symbol_table):
    """Display the lexical analysis results."""
    for token, category in tokens:
        if category != "Lexical Error":
            print(f"{category}: {token}")
    
    print("\nSymbol Table:")
    for symbol in symbol_table:
        print(symbol)
    
    errors = [token for token, category in tokens if category == "Lexical Error"]
    if errors:
        print("\nLexical Errors Found:")
        for error in errors:
            print(f"Invalid token: {error}")


if __name__ == "__main__":
    file_path = "/Users/niravlakhani/Desktop/Semester 6/DLP/PRAC_3/Example.c"
    tokens, symbol_table = lexical_analyzer(file_path)
    display_results(tokens, symbol_table)
