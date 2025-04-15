grammar = {
    "S": [["A", "B", "C"], ["D"]],
    "A": [["a"], ["ε"]],
    "B": [["b"], ["ε"]],
    "C": [["(", "S", ")"], ["c"]],
    "D": [["A", "C"]],
}

terminals = ["a", "b", "(", ")", "c", "$"]
non_terminals = list(grammar.keys())

first = {nt: set() for nt in non_terminals}
follow = {nt: set() for nt in non_terminals}
follow["S"].add("$")


def get_first(symbol):
    if symbol not in grammar:
        return {symbol}
    if first[symbol]:
        return first[symbol]

    for prod in grammar[symbol]:
        for s in prod:
            f = get_first(s)
            first[symbol] |= f - {"ε"}
            if "ε" not in f:
                break
        else:
            first[symbol].add("ε")
    return first[symbol]


for nt in non_terminals:
    get_first(nt)

changed = True
while changed:
    changed = False
    for nt in non_terminals:
        for prod in grammar[nt]:
            for i, B in enumerate(prod):
                if B in non_terminals:
                    after = prod[i + 1 :]
                    trailer = set()
                    for sym in after:
                        trailer |= get_first(sym) - {"ε"}
                        if "ε" not in get_first(sym):
                            break
                    else:
                        trailer |= follow[nt]
                    if not trailer.issubset(follow[B]):
                        follow[B] |= trailer
                        changed = True

table = {nt: {} for nt in non_terminals}
is_LL1 = True

for nt in non_terminals:
    for prod in grammar[nt]:
        f_set = set()
        for s in prod:
            f_set |= get_first(s) - {"ε"}
            if "ε" not in get_first(s):
                break
        else:
            f_set.add("ε")

        for t in f_set:
            if t != "ε":
                if t in table[nt]:
                    is_LL1 = False
                table[nt][t] = prod
        if "ε" in f_set:
            for t in follow[nt]:
                if t in table[nt]:
                    is_LL1 = False
                table[nt][t] = prod

print("\nGrammar is LL(1)" if is_LL1 else "\nGrammar is NOT LL(1)")


def parse(input_str):
    stack = ["$", "S"]
    input_str += "$"
    i = 0

    while stack:
        top = stack.pop()
        curr = input_str[i]

        if top == curr:
            i += 1
        elif top in terminals:
            return False
        elif curr in table[top]:
            prod = table[top][curr]
            if prod != ["ε"]:
                stack.extend(reversed(prod))
        else:
            return False
    return i == len(input_str)


print("\nString Validation:")
test_cases = ["abc", "ac", "(abc)", "c", "(ac)", "a", "()", "(ab)", "abcabc", "b"]
for test in test_cases:
    print(f"{test:10} → {'Valid string' if parse(test) else 'Invalid string'}")
