from functools import reduce
if __name__ == "__main__":
    # Apply a function to every element of an iterable
    ls = list(range(10))
    mapped = list(map(lambda x: x + 1, ls))
    print(f"mapped: {mapped}")

    filtered = list(filter(lambda x: True if x % 2 == 0 else False, ls))
    print(f"filtered: {filtered}")
        
    reduced = reduce(lambda x, y: x + y, filtered)
    print(f"reduced: {reduced}")