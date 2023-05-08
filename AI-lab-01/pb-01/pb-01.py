"""
    Find the last alphabetically word in a text.
    input: string representing the text
    output: string representing the last alphabetically word in the text
            None if the text is None or the empty string
"""


def last_word(text):
    if text is None:
        return None
    if len(text.split()) == 0:
        return None
    currentLastWord = ''
    for currentWord in text.split():
        if currentWord > currentLastWord:
            currentLastWord = currentWord
    return currentLastWord


def test_last_word():
    assert (last_word(None) is None)
    assert (last_word(' ') is None)
    assert (last_word('   ') is None)
    assert (last_word('Ana are mere rosii si galbene') == 'si')
    assert (last_word('Ana are mere rosii si zebre galbene') == 'zebre')
    assert (last_word('Ana') == 'Ana')
    assert (last_word('si Si') == 'si')


test_last_word()
