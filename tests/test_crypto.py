from crypto import crypt, decrypt

def test_crypt_pas_1():
    assert crypt("a") == "b1"
def test_crypt_pas_3():
    assert crypt("az", 3)[0] == "d"
def test_decrypt_inverse_crypt():
    message = "Hello!"
    chiffre = crypt(message, 4)  # on chiffre
    assert decrypt(chiffre) == message  # on déchiffre
