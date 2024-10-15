def cislo_text(cislo):


  cisla = {
    0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 
    6: "šest", 7: "sedm", 8: "osm", 9: "devět", 10: "deset", 
    11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 
    15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct", 
  }


  desitky = {
    2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát", 
    6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát", 10: "sto",
  }

  if 0 <= cislo <= 19:
    return cisla[cislo]
  elif 20 <= cislo <= 100:
    desitky_cislo = cislo // 10
    jednotky_cislo = cislo % 10
    if jednotky_cislo == 0:
        return desitky [desitky_cislo]
    else:
        return desitky[desitky_cislo] + (" ") + cisla[jednotky_cislo]

  else:
   return "Číslo musí být mezi 0 a 100"
  
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(text)