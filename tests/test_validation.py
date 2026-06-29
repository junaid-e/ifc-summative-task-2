from validation import validate_name


def test_valid_name():
    assert validate_name("Junaid") is True

def test_empty_name():
    assert validate_name("") is False

def test_spaces_only():
    assert validate_name("   ") is False