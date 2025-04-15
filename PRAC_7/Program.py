grammar = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

non_terminals = grammar.keys()
first = {nt: set() for nt in non_terminals}
follow = {nt: set() for nt in non_terminals}
follow['S'].add('$')

def get_first(symbol):
    if symbol not in grammar:
        return {symbol}
    if 'ε' in first[symbol]:
        return first[symbol]
    for rule in grammar[symbol]:
        for s in rule:
            s_first = get_first(s)
            first[symbol] |= s_first - {'ε'}
            if 'ε' not in s_first:
                break
        else:
            first[symbol].add('ε')
    return first[symbol]

for nt in non_terminals:
    get_first(nt)

changed = True
while changed:
    changed = False
    for head, rules in grammar.items():
        for rule in rules:
            for i, B in enumerate(rule):
                if B in grammar:
                    trailer = set()
                    for s in rule[i+1:]:
                        trailer |= get_first(s) - {'ε'}
                        if 'ε' not in get_first(s):
                            break
                    else:
                        trailer |= follow[head]
                    if not trailer.issubset(follow[B]):
                        follow[B] |= trailer
                        changed = True

for nt in grammar:
    print(f"First({nt}) = {{{', '.join(sorted(first[nt]))}}}")
for nt in grammar:
    print(f"Follow({nt}) = {{{', '.join(sorted(follow[nt]))}}}")