from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_uppercase():
    assert shorten("PYTHON") == "PYTHN"

def test_shorten_numbers():
    assert shorten("123") == "123"

def test_shorten_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"