def bin_to_dec(binarni_cislo):

    binarni_cislo = str(binarni_cislo)

    dec_cislo = 0
    for i, cifra in enumerate(reversed(binarni_cislo)):
        if cifra == "1":
            dec_cislo += 2**i

        
    return dec_cislo


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

if __name__ == "__main__":
    binarni_cislo = "10011101"
    dec_cislo = bin_to_dec(binarni_cislo)
    print(f"Binarni cislo {binarni_cislo} je v desitkove soustave {dec_cislo}")
   
