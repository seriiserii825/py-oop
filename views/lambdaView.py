def lambdaView():
    squared = lambda x: x**2
    print(f"squared(2): {squared(2)}")

    # its equivalent to
    def myfunc(n):
        return n**2

    addTwo = lambda x: x + 2
    print(f"addTwo(4): {addTwo(4)}")

    sum = lambda x, y: x + y
    print(f"sum(3,8): {sum(3, 8)}")

    ################################################################################################

    def funcBuilder(x):
        return lambda n: n + x

    addTen = funcBuilder(10)
    addTwenty = funcBuilder(20)

    print(f"addTen(5): {addTen(5)}")
    print(f"addTwenty(5): {addTwenty(5)}")

    ################################################################################################

    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"squared: {squared}")

    ################################################################################################

    numbers = [1, 2, 3, 4, 5]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"even: {even}")

    ################################################################################################

    from functools import reduce

    numbers = [1, 2, 3, 4, 5]

    sum = reduce(lambda acc, curr: acc + curr, numbers)
    print(f"sum: {sum}")

    ################################################################################################

    names = ["John", "Paul", "George", "Ringo"]

    names_length = reduce(lambda acc, curr: acc + len(curr), names, 0)
    print(f"names_length: {names_length}")
