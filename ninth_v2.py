def dec_to_bin(cislo):
    if cislo == 0:
        return "0"
    elif cislo == 1:
        return "1"
    else:
        return dec_to_bin(cislo //2) + str(cislo % 2)
    

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


if __name__ == "__main__":
    dec_to_bin(120)