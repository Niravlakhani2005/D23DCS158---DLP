import re


def tokenize(expr):
    return re.findall(r"\d+\.\d+|\d+|[a-zA-Z_]\w*|[+\-*/^()]", expr)


def is_number(s):
    return re.fullmatch(r"\d+(\.\d+)?", s)


def fold_constants(tokens):
    stack = []
    ops = []
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    def apply():
        b = stack.pop()
        a = stack.pop()
        op = ops.pop()
        if is_number(a) and is_number(b):
            stack.append(str(eval(f"{a}{op}{b}")))
        else:
            stack.append(f"{a} {op} {b}")

    i = 0
    while i < len(tokens):
        t = tokens[i]
        if is_number(t) or t.isalpha():
            stack.append(t)
        elif t == "(":
            ops.append(t)
        elif t == ")":
            while ops[-1] != "(":
                apply()
            ops.pop()
        elif t in prec:
            while ops and ops[-1] != "(" and prec[ops[-1]] >= prec[t]:
                apply()
            ops.append(t)
        i += 1

    while ops:
        apply()

    return stack[0]


expr = input("Enter expression: ")
tokens = tokenize(expr)
result = fold_constants(tokens)
print("Optimized:", result)
