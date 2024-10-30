def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """

    typ_figury = figurka["typ"]
    vychozi_pozice = figurka["pozice"]
    radek_vychozi, sloupec_vychozi = vychozi_pozice
    radek_cilovy, sloupec_cilovy = cilova_pozice

    
    if (radek_cilovy < 1 or radek_cilovy > 8):
        return False
    if cilova_pozice in obsazene_pozice:
        return False
    
    if typ_figury == "pěšec":
        if sloupec_cilovy == sloupec_vychozi and radek_cilovy == radek_vychozi +1:
            return True
        elif sloupec_cilovy == sloupec_vychozi and radek_cilovy == radek_vychozi -2:
            return True
        else:
            return False
    if typ_figury == "jezdec":
        if abs(radek_cilovy - radek_vychozi) == 2 and abs(sloupec_cilovy - sloupec_vychozi) == 1: 
            return True
        elif abs(sloupec_cilovy - sloupec_vychozi) == 2 and abs(radek_cilovy - radek_vychozi) == 1:
            return True
        else: 
            return False
    if typ_figury == "věž":
        if radek_cilovy == radek_vychozi or sloupec_cilovy == sloupec_vychozi:
            return True
        else:
            return False
    if typ_figury == "střelec":
        if abs(radek_cilovy - radek_vychozi) == abs(sloupec_cilovy - sloupec_vychozi):
            return True
        else:
            return False
    if typ_figury == "dáma":
        if  radek_cilovy == radek_vychozi or sloupec_cilovy == sloupec_vychozi:
            return True
        elif abs(radek_cilovy - radek_vychozi) == abs(sloupec_cilovy - sloupec_vychozi):
            return True
        else:
            return False
        
    if typ_figury == "král":
        if abs(radek_cilovy - radek_vychozi <= 1) and (sloupec_cilovy - sloupec_vychozi <=1):
            return True
        else:
            return False
    


    
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True 
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura  
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura 
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True