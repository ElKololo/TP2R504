from fizzbuzz import affiche

def test_affiche_with_n_15():
    expected = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
    assert affiche(15) == expected
