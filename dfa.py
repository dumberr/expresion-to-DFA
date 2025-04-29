from collections import deque

class Stare:
    def __init__(self, nfa_stare):
        self.nfa_stare = frozenset (nfa_stare)
        self.trans = {}
        self.is_final = False

class DFA:
    def __init__(self, stare_start):
        self.stare_start = stare_start
        self.states = []

class DFAConstructor:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa_stare = {}

    def ep (self, stare):
        stiva = list(stare)
        fin = set(stare)
        while stiva:
            s = stiva.pop()
            for next in s.trans.get('', []):
                if next not in fin:
                    fin.add(next)
                    stiva.append(next)
    
        return fin
    
    def move (self, stare, simbol):
        rez = set()
        for s in stare:
            for next in s.trans.get(simbol, []):
                rez.add(next)
        
        return rez
    
    def build(self):
        start_fin = self.ep([self.nfa.start])
        stare_start = Stare(start_fin)
        if self.nfa.end in start_fin:
            stare_start.is_final = True

        dfa = DFA(stare_start)
        self.dfa_stare[stare_start.nfa_stare] = stare_start
        coada = deque([stare_start])

        simboluri = self.gets()

        while coada:
            current = coada.popleft()
            for simbol in simboluri:
                if simbol == '':
                    continue
                rez = self.move(current.nfa_stare, simbol)
                fin = self.ep(rez)
                if not fin:
                    continue
                fin_frozen = frozenset(fin)
                if fin_frozen not in self.dfa_stare:
                    new = Stare(fin)
                    if self.nfa.end in fin:
                        new.is_final = True
                    self.dfa_stare[fin_frozen] = new
                    coada.append(new)
                current.trans[simbol] = self.dfa_stare[fin_frozen]
        
        dfa.stare = list(self.dfa_stare.values())
        return dfa
    
    def gets(self):
        simboluri = set()
        stare = deque([self.nfa.start])
        trecut = set()

        while stare:
            s = stare.popleft()
            if s in trecut:
                continue
            trecut.add(s)
            for simbol, next in s.trans.items():
                simboluri.add(simbol)
                for x in next:
                    stare.append(x)

        return simboluri
    



if __name__ == "__main__":
    from nfa import NFAConstructor

    postfix = "ab."
    nfa_constructor = NFAConstructor(postfix)
    nfa = nfa_constructor.build()

    dfa_constructor = DFAConstructor(nfa)
    dfa = dfa_constructor.build()

    print("DFA construit pentru postfixul:", postfix)
    for state in dfa.stare:
        print(f"Stare: {state.nfa_stare}, Finala: {state.is_final}")
        for simbol, target in state.trans.items():
            print(f"  {simbol} -> {target.nfa_stare}")

    
