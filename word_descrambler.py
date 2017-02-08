import re


def is_match(word, scrambled):
    """
    Simply takes the word and determines if its letters are part of scrambled
    :param word: word to try to match
    :param scrambled: scrambled letters
    :return: boolean
    """
    # Loop through the letters and make sure they all match
    match = True
    for letter in word:
        if letter not in scrambled:
            match = False

    return match


def find_matches(scrambled, find_len):
    """
    Opens the dictionary and loops through to find matches
    :param scrambled: the letters to find words out of
    :param find_len: the length of word to find
    :return: list of matches
    """
    with open('/usr/share/dict/words') as word_file:
        words = word_file.readlines()

    # Strip all surrounding whitespace
    words = [x.strip() for x in words]

    # Find matching words
    matches = []
    for word in words:
        if len(word) == find_len and is_match(word, scrambled):
            matches.append(word)

    return matches