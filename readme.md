# Tema 2 - Regex to DFA

## Descriere

Această aplicație construiește un automat finit determinist (DFA) echivalent cu o expresie regulată dată. Se parcurg următorii pași:

1. Parsarea expresiei regulate și conversia în notație postfixată.
2. Construirea unui NFA folosind algoritmul lui Thompson.
3. Conversia NFA în DFA folosind metoda subset construction.
4. Simularea DFA pentru a verifica dacă un șir este acceptat.
5. Testarea automată a expresiilor și a rezultatelor într-un fișier `tests.json`.

## Structura proiectului

- `parser.py` – Parser pentru expresii regulate și conversie în postfix.
- `nfa.py` – Constructor NFA pe baza postfixului (algoritmul Thompson).
- `dfa.py` – Constructor DFA folosind subset construction.
- `simulator.py` – Simularea execuției pe DFA.
- `main.py` – Rulează testele definite în `tests.json`.
- `tests.json` – 20 de cazuri de test pentru validarea implementării.

## Cum se rulează

### Cerințe
- Python 3.x

### Comenzi

1. Clonează repository-ul (dacă este pe GitHub):
   ```bash
   git clone <link_repository>
   cd <folder_proiect>
   ```

2. Rulează programul:
   ```bash
   python main.py
   ```

Se vor afișa rezultatele testelor cu statusul PASS/FAIL pentru fiecare.

## Decizii de implementare

- Reprezentarea NFA urmează modelul propus de Thompson cu stări și tranziții epsilon.
- DFA-ul este construit iterativ folosind cozi (BFS) și conversia prin mulțimi.
- Simularea DFA este realizată simplu, parcurgând stările după simbolurile din cuvânt.
- Testele sunt separate într-un fișier JSON, pentru modularitate și ușurința adăugării de cazuri noi.

