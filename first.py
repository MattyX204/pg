#funkce vypise zda je cislo sude nebo liche

def sudy_nebo_lichy(cislo):
  if cislo % 2 == 0:
    print("Číslo", cislo, "je sudé")
  else:
    print("Číslo", cislo, "je liché")

# Volání funkce 
#sudy_nebo_lichy(2)
sudy_nebo_lichy(1000000)