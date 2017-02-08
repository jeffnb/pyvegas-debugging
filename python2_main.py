from word_descrambler import find_matches

if __name__ == '__main__':
    """
    An imperfect matcher
    """

    word_input = "magnificent"
    find_length = 4

    matches = find_matches(word_input, find_length)

    print("Looking for scrambles of {} with length {}".format(word_input,
                                                              find_length))
    print("Found {} matches".format(len(matches)))
    print(matches)
