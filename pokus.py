def hello_world():
    print("Hello world")

#funkce ktera vypise pozadovany pocet hvezd 

def five_stars(limit):
    i  = 0
    while i<limit:
        print ("*")
        i += 1


#five_stars(10) #cislo 3 se nastavi jako parametr limit

#funkce overi zda je cislo v rozmezi minimum - maximum a vypise textovy vstup
def in_range(number, minimum, maximum):
    if(number>minimum and number<maximum):
        print("Number", number, "is in range 100 - 1000")

    else:
        print("Number", number, "is out of range") 


#in_range(560, 100, 1000)


#funkce vrati nejvetsi cislo
def max_number(a, b, c):
    if (a>b and a>b):
        return a 
    if  (b>a and b>c):
        return b
    return c
    


m = max_number(2.1, 4.2, 6.3)
print(m)