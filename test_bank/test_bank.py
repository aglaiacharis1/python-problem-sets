from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello, Nana") == 0

def test_value_h():
    assert value("hey") == 20
    assert value("Hi there") == 20

def test_value_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100