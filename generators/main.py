def evens_below_20():
    """
    A function that returns a generator that gives even numbers below 20
    """
    for x in range(0, 20, 2):
        yield x

def odds_below_20():
    """
    A function that returns a generator that gives odd numbers below 20
    """
    for x in range(1, 20, 2):
        yield x

if __name__ == "__main__":
    # g is a generator. Generators are useful because they don't load all
    # elements into memory. Suppose a large series of numbers are computed that
    # cannot fit into memory. Instead of using a list, a generator can be used
    # to compute the next value only when it is ready to be processed.
    g = evens_below_20()

    # Iterate through all elements of a generator
    print("Even numbers < 20")
    for x in g:
        print(f"    {x}")

    # When no more elements are present, calling next() on the generator raises
    # an error
    print("Odds < 20")
    g = odds_below_20()
    while True:
        try:
            x = next(g)
            print(f"    {x}")
        except StopIteration:
            # No more elements in generator. Exit from loop
            break