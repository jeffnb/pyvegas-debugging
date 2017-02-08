from word_descrambler import find_matches

if __name__ == '__main__':
    """
    An imperfect matcher
    """
    print("Please enter the letters:")
    word_input = input()

    print("Please enter length of words desired:")
    find_length = int(input())

    matches = find_matches("hello", find_length)

    print("Found {} matches".format(len(matches)))
    print(matches)
