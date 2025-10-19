from crypto import crypt, decrypt

def test_crypt_pas_1():
    assert crypt("a") == "b1"
