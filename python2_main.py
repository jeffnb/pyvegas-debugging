from word_descrambler import find_matches

if __name__ == '__main__':
    """
    An imperfect matcher
    """
    print("Please enter the letters:")
    word_input = raw_input()

    print("Please enter length of words desired:")
    find_length = int(raw_input())

    matches = find_matches(word_input, find_length)

    print("Found {} matches".format(len(matches)))
    print(matches)
