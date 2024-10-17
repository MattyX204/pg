
#def my_range(start, stop, step=1):
   # """
 #   Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
  #  """
    
 #   results = []
   # i = start  #i se nastaví na hodnotu 1
  #  while i < stop: #pokračuje dokud i není větší než stop (10)
   #     results.append(i)
  #      i += step #inkrementace i, step nastaví o kolik má inkrementovat, stačí zadat čisla=> smazat parametr step
 #   return results

#if __name__ =="__main__":
 #   seznam=list(range(1,10))
  #  print(seznam)

   # seznam = my_range(1, 10) #2 argumenty = start 1, stop 10, 
    #print (seznam)


    #------------------ENUMERATE---------------------

def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """

    results = []

    index = 0 
    for value in iterable:
        results.append((index, value))
        index += 1
    return results




if __name__=="__main__":
   seznam=list(enumerate(["ahoj", "cau", "jak", "se", "mas"], 2))
   print(seznam)
   sezanm = my_enumerate (["ahoj", "cau", "jak", "se", "mas"], 2)
   print(sezanm)

   



   ## seznam=list(enumerate(["ahoj", "cau", "jak", "se", "mas"]))
 #   print(seznam)
#
 #   for i, hodnota in seznam:
#        print(f"slovo {hodnota} je na {i} pozici")




#_____________Funkce zip ____________

def my_zip(*iterables):  #provádí spojení více seznamů
    """
    Nase vlastni implementace zip()
    """

    results = []
    lenght = len(iterables[0])
    u = 0
    while u < lenght:           #zavoláme cyklus pro každou položku,  v něm se vytváří mezivýsledek 
        subresult = []          #položky se postupně uloží do subresult a pak do result
        for iterable in iterables:
            subresult.append(iterable[u])
        results.append(subresult)
        u += 1
    return results


if __name__ == "__main__":

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [30,        20,     24,     18,     27  ]
    vaha =  [50,        80,     90,     55,     67  ]

    vysledek = list ( zip(jmena, vek, vaha))     #spojeni seznamu
 #   for jmeno, vek, vaha in vysledek:
 #       print (f"{jmeno} je {vek} a vazi {vaha}")
    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)