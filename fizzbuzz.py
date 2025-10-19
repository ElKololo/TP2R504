def _fizzbuzz_value(i):
    if i % 15 == 0:
        return "FrisBee"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

def affiche(n1=None, n2=None):
    if n1 is None and n2 is None:
        start, end = 1, 15  # pour l’instant 1..15 juste pour passer le 1er test TDD
    elif n2 is None:
        start, end = 1, n1
    else:
        start, end = n1, n2
    return "".join(_fizzbuzz_value(i) for i in range(start, end + 1))
