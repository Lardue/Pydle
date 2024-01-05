from project import get_word, check_guess, check_input, get_definition


def test_get_word():
    word = get_word()
    assert len(word) == 5


def test_check_guess():
    won, result = check_guess("Brain", "brain")
    assert won == True
    assert len(result) == 5

    won, result = check_guess("Stola", "Hello")
    assert won == False
    assert len(result) == 5

    won, result = check_guess("Cruise", "Chain")
    assert won == False
    assert result[0] == "1"


def test_check_input():
    assert check_input("stare") == True
    assert check_input("cruise") == False
    assert check_input("") == False
    assert check_input(12345) == False


def test_get_definition():
    definition = get_definition("stare")
    assert len(definition) == 7
    assert definition[0].startswith("Noun") == True
