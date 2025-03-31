class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")
        self.index = 0
    
    def peek(self):
        return self.input[self.index] if self.index < len(self.input) else None
    
    def match(self, char):
        if self.peek() == char:
            self.index += 1
            return True
        return False
    
    def S(self):
        if self.match('('):
            if self.L():
                return self.match(')')
            return False
        elif self.match('a'):
            return True
        return False
    
    def L(self):
        if self.S():
            return self.L_prime()
        return False
    
    def L_prime(self):
        if self.match(','):
            if self.S():
                return self.L_prime()
            return False
        return True
    
    def parse(self):
        return self.S() and self.index == len(self.input)


if __name__ == "__main__":
    test_cases = [
        "(a)", "a", "(a,a)", "(a,(a,a),a)", "(a,a),(a,a)",
        "a)", "(a a,a", "a a, (a,a),a"
    ]
    
    for test in test_cases:
        parser = RecursiveDescentParser(test)
        result = "Valid string" if parser.parse() else "Invalid string"
        print(f"Input: {test} => Output: {result}")
