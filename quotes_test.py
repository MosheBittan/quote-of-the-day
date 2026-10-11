from quotes import QUOTES, get_random_quote, format_quote


def test_random_quote_is_from_list():
    assert get_random_quote() in QUOTES


def test_quotes_have_text_and_author():
    for quote, author in QUOTES:
        assert quote and author


def test_format_quote():
    assert format_quote("Hello", "World") == '"Hello" - World'
