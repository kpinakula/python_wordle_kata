from python_linting_exploration.example_python_file import wordle_checker


def test_completely_wrong_guess():
    result = wordle_checker("AAAAA", "BBBBB")
    assert result == "00000"


def test_all_characters_correct():
    result = wordle_checker("AAAAA", "AAAAA")
    assert result == "22222"


def test_first_character_is_correct():
    result = wordle_checker("AZZZZ", "AAAAA")
    assert result == "20000"


def test_first_character_is_wrong():
    result = wordle_checker("AZZZZ", "BBBBB")
    assert result == "00000"


def test_second_character_is_correct():
    result = wordle_checker("ZAZZZ", "AAAAA")
    assert result == "02000"
