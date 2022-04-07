# Print the members of any object
def printAttr(x):
    print(f"Type: {type(x)}")
    for attr in sorted(dir(x)):
        print(f"    {attr}")

if __name__ == "__main__":
    ls = []
    printAttr(ls)
