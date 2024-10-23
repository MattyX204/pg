def je_prvocislo(cislo):
    
    #Funkce zkontroluje jestli je číslo prvočíslem a vrátí True nebo False


    if cislo <= 1:
        return False  
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False  
    return True

def vrat_prvocisla(maximum):
    
    #Funkce vrátí seznam všech prvočísel menších nebo rovných zadanému maximu
 
    prvocisla = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)