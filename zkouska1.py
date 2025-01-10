# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
    result = []  # vytvori prazdny seznam pro ukladani vysledku
    for string in strings:
        if string == "STOP":  # Pokud nalezneme STOP, prerusi se zpracovani cyklu
            break
        if len(string) > 3:  # Kontroluje delku retezce
            result.append(string.upper())  # Prida retezce delsi nez 3 znaky napsane velkymi pismeny do seznamu result
    return result


# Pytest testy pro Příklad 2
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]