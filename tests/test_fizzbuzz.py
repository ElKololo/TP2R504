from fizzbuzz import affiche

def test_affiche_with_n_15():
    expected = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
    assert affiche(15) == expected
def test_affiche_range_5_10():
    assert affiche(5, 10) == "BuzzFizz78FizzBuzz"

def test_affiche_range_10_16():
    assert affiche(10, 16) == "Buzz11Fizz1314FrisBee16"
