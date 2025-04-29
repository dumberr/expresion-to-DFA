class Stare:
    def __init__(self):
        self.trans = {}

class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class NFAConstructor:
    def __init__(self, ord):
        self.ord = ord
        self.stiva = []


    def build(self):
        for c in self.ord:
            if c == '*':
                nfa = self.stiva.pop()
                self.stiva.append(self.ks(nfa))

            elif c == '+':
                nfa = self.stiva.pop()
                self.stiva.append(self.plus(nfa))

            elif c == '?':
                nfa = self.stiva.pop()
                self.stiva.append(self.optional(nfa))

            elif c == '|':
                nfa2 = self.stiva.pop()
                nfa1 = self.stiva.pop()
                self.stiva.append(self.alt(nfa1,nfa2))

            elif c =='.':
                nfa2 = self.stiva.pop()
                nfa1 = self.stiva.pop()
                self.stiva.append(self.con(nfa1,nfa2))

            else:
                self.stiva.append(self.none(c))

        return self.stiva.pop()
    
    def none(self, c):
        start = Stare()
        end = Stare()
        start.trans[c] = [end]
        return NFA(start, end)
    
    def con(self, nfa1, nfa2):
        nfa1.end.trans[''] = [nfa2.start]
        return NFA(nfa1.start, nfa2.end)
    
    def alt(self, nfa1, nfa2):
        start = Stare()
        end = Stare()
        start.trans[''] = [nfa1.start, nfa2.start]
        nfa1.end.trans[''] = [end]
        nfa2.end.trans[''] = [end]

        return NFA(start, end)
    
    def plus(self, nfa):
        start = Stare()
        end = Stare()
        start.trans[''] = [nfa.start]
        nfa.end.trans[''] = [nfa.start, end]

        return NFA(start, end)
    
    def optional(self, nfa):
        start = Stare()
        end = Stare()
        start.trans[''] = [nfa.start, end]
        nfa.end.trans[''] = [end]

        return NFA(start, end)
    
    def ks(self, nfa):
        start = Stare()
        end = Stare()
        start.trans[''] = [nfa.start, end]
        nfa.end.trans[''] = [nfa.start, end]

        return NFA(start, end)



