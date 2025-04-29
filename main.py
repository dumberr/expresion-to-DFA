import json
from parser import Parser
from nfa import NFAConstructor
from dfa import DFAConstructor
from simulator import Sim

def load_tests(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
def run(cases):
    for case in cases:
        name = case['name']
        regex = case['regex']
        tests = case['test_strings']

        print(f"\n[Test: {name}] Regex: {regex}")

        parser = Parser(regex)
        postfix = parser.fix()

        nfa_constructor = NFAConstructor(postfix)
        nfa = nfa_constructor.build()

        dfa_constructor = DFAConstructor(nfa)
        dfa = dfa_constructor.build()

        simulator = Sim(dfa)

        for test in tests:
            input_s = test['input']
            exp = test['expected']
            rez = simulator.accept(input_s)
            status = "PASS" if rez == exp else "FAIL"
            print(f" Input: '{input_s}' | Expected: {exp} | Result: {rez} | {status}")



if __name__ == "__main__":
    cases = load_tests("tests.json")
    print("Loaded", len(cases), "test cases.")
    run(cases)


