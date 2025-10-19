import string

CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "


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
    pas = int(message[-1])  # dernier caractère = pas utilisé
    message = message[:-1]  # on enlève le pas à la fin
    resultat = ""
    for c in message:
        if c in CARACTERES:
            index = CARACTERES.index(c)
            resultat += CARACTERES[(index - pas) % len(CARACTERES)]
        else:
            resultat += c
    return resultat

