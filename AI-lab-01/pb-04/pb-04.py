"""
    Find words appearing only once in a text.
    input: string representing the text
    output: set of words that appear only once in the given text
"""


def words_appearing_once(text):
    if text is None:
        return set()
    all_words = set()
    duplicate_words = set()
    for word in text.split():
        if word in all_words:
            if word not in duplicate_words:
                duplicate_words.add(word)
        else:
            all_words.add(word)
    return all_words - duplicate_words


def test_words_appearing_once():
    assert (words_appearing_once(None) == set())
    assert (words_appearing_once("ana ana are are") == set())
    assert (words_appearing_once("") == set())
    assert (words_appearing_once("ana are ana are mere rosii ana") == {"mere", "rosii"})
    assert (words_appearing_once("ana ana are mere rosii ana") == {"are", "mere", "rosii"})


test_words_appearing_once()
