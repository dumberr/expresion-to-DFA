class Sim:
    def __init__(self, dfa):
        self.dfa = dfa

    def accept(self, input_s):
        stare_curenta = self.dfa.stare_start
        for simbol in input_s:
            if simbol not in stare_curenta.trans:
                return False
            stare_curenta = stare_curenta.trans[simbol]
        
        return stare_curenta.is_final
    
if __name__ == "__main__":
    from nfa import NFAConstructor
    from dfa import DFAConstructor

    postfix = "ab."
    nfa_constructor = NFAConstructor(postfix)
    nfa = nfa_constructor.build()
    dfa_constructor = DFAConstructor(nfa)
    dfa = dfa_constructor.build()

    simulator = Sim(dfa)

    test_strings = ["ab", "a", "b", ""]
    for s in test_strings:
        result = simulator.accept(s)
        print(f"Input: '{s}', Acceptat: {result}")