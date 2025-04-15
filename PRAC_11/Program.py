import re

token_pattern = r"(\d+\.\d+|\d+|[+\-*/()])"
token_regex = re.compile(token_pattern)


def tokenize(expression):
    return [token for token in token_regex.findall(expression) if token.strip()]


temp_var_count = 0
quadruples = []


def new_temp():
    global temp_var_count
    temp_var_count += 1
    return f"t{temp_var_count}"


def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0


def generate_quadruples(expression):
    global temp_var_count, quadruples
    temp_var_count = 0
    quadruples = []

    tokens = tokenize(expression)
    values = []
    operators = []

    def apply():
        op = operators.pop()
        right = values.pop()
        left = values.pop()
        temp = new_temp()
        quadruples.append((op, left, right, temp))
        values.append(temp)

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit() or "." in token:
            values.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                apply()
            operators.pop()
        elif token in "+-*/":
            while (
                operators
                and operators[-1] != "("
                and precedence(operators[-1]) >= precedence(token)
            ):
                apply()
            operators.append(token)
        i += 1

    while operators:
        apply()

    return quadruples


expression = input("Enter an arithmetic expression: ")
quadruples = generate_quadruples(expression)

print("\nOperator  Operand1  Operand2  Result")
for q in quadruples:
    print(f"{q[0]:^8}  {q[1]:^8}  {q[2]:^8}  {q[3]:^6}")
