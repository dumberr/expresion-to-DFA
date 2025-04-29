class Parser:
    def __init__(self, regex):
        self.regex = regex
        self.out = []
        self.op = []
        self.ord = {
            '|': 1,
            '.': 2,
            '?': 3,
            '*': 3,
            '+': 3
        }
    
    def insert_con(self):
        new = ""
        for i in range(len(self.regex)):
            c1 = self.regex[i]
            new += c1
            if i + 1 <len(self.regex):
                c2 = self.regex[i+1]
                if (c1 not in "(|" and c2 not in ")|*+?"):
                    new += "."
        return new
    
    def fix(self):
        regex = self.insert_con()
        for c in regex:
            if c == '(':
                self.op.append(c)
            
            elif c == ')':
                while self.op and self.op[-1] != '(':
                    self.out.append(self.op.pop())
                self.op.pop()
            
            elif c in self.ord:
                while (self.op and self.op[-1] != '(' and self.ord[self.op[-1]] >= self.ord[c]):
                    self.out.append(self.op.pop())
                self.op.append(c)
            
            else:
                self.out.append(c)

        while self.op:
            self.out.append(self.op.pop())

        return ''.join(self.out)

# if __name__ == "__main__":
#    regex = "a(b|c)*"
#    parser = Parser(regex)
#    postfix = parser.fix()
#    print(f"Regex: {regex}")
#    print(f"Postfix: {postfix}")
