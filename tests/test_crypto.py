from crypto import crypt, decrypt

def test_crypt_pas_1():
    assert crypt("a") == "b1"
def test_crypt_pas_3():
    assert crypt("az", 3)[0] == "d"
