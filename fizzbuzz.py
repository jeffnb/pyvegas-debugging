def fizzbuzz():
    """
    Goal: loop from 1 to 100.  If number is divisible by 3 print "fizz" if divisible by 5 print "buzz"
    if it is divisible by 3 and 5 print "fizzbuzz".  Otherwise print the number
    :return:
    """

    for number in range(1, 100):
        result = ''
        if number % 3 == 0:
            result += "fizz"
        if number % 5:
            result = "buzz"

        print(result) if result else print(number)


if __name__ == '__main__':
    fizzbuzz()