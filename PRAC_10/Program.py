import re

token_pattern = r"(\d+\.\d+|\d+|[+\-*/^()])"
token_regex = re.compile(token_pattern)


def tokenize(expression):
    return [token for token in token_regex.findall(expression) if token.strip()]


def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    if op == "^":
        return 3
    return 0


def apply_operator(operators, values):
    try:
        operator = operators.pop()
        right = values.pop()
        left = values.pop()

        if operator == "+":
            values.append(left + right)
        elif operator == "-":
            values.append(left - right)
        elif operator == "*":
            values.append(left * right)
        elif operator == "/":
            values.append(left / right)
        elif operator == "^":
            values.append(left**right)
    except (IndexError, ZeroDivisionError):
        raise ValueError("Invalid expression")


def evaluate_expression(expression):
    try:
        tokens = tokenize(expression)
        values = []
        operators = []

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.isdigit() or "." in token:
                values.append(float(token))
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    apply_operator(operators, values)
                if not operators:
                    raise ValueError("Mismatched parentheses")
                operators.pop()
            elif token in "+-*/^":
                while (
                    operators
                    and operators[-1] != "("
                    and precedence(operators[-1]) >= precedence(token)
                    and token != "^"
                ):
                    apply_operator(operators, values)
                operators.append(token)

            i += 1

        while operators:
            if operators[-1] == "(":
                raise ValueError("Mismatched parentheses")
            apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("Invalid expression")

        result = values[-1]
        return int(result) if result == int(result) else result

    except:
        return "Invalid expression"


expression = input("Enter an arithmetic expression: ")
result = evaluate_expression(expression)
print("Result:", result)

