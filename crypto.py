import string

CARACTERES = string.ascii_letters + string.ascii_punctuation + string.digits + " "

def crypt(message, pas=1):
    resultat = ""
    for c in message:
        if c in CARACTERES:
            index = CARACTERES.index(c)
            resultat += CARACTERES[(index + pas) % len(CARACTERES)]
        else:
            resultat += c
    return resultat + str(pas)

def decrypt(message):
    # Décryptage ajouté plus tard
    pass
