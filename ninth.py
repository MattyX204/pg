def dec_to_bin(cislo):

    cislo = int(cislo)
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    pow = 0
    i = 0
    while True:
        m = 2 ** i
        if m > cislo:
            pow = m = -1
            break
        vysledek = ""
        for i in range(pow, -1, -1):
            m = 2 ** i
            if m <= cislo:
                vysledek += "1"
                cislo -= m
            else:
                vylsedek += "0"
        return vysledek
    


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


if __name__ == "__main__":
    dec_to_bin(120)