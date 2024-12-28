import re


def text_has_cyrillic_characters(text):
    """
    Returns ``True`` if given text contains one or more cyrillic character.

    Arguments:
        text (string): The text to inspect.

    Returns:
        boolean: A true value if any cyrillic character has been found else a false
        value.
    """
    return bool(re.search("[\u0400-\u04FF]", text))
