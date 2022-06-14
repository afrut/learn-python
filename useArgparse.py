#python useArgparse.py foo 3 --optional val1 --optionalFlag -of2 --restrictedOption a
#python useArgparse.py foo 3 --optional val1 --optionalFlag -of2 --restrictedOption a --optionalWithDefault
#python useArgparse.py foo 3 --optional val1 --optionalFlag -of2 --restrictedOption a --optionalWithDefault someValue
import subprocess as sp
import argparse
if __name__ == "__main__":
    sp.call("cls", shell = True)
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", help = "Description of first argument")
    parser.add_argument("num", type = int, help = "Any number")
    parser.add_argument("--optional", help = "An optional argument")
    parser.add_argument("--optionalFlag", action = "store_true", help = "An optional flag")
    parser.add_argument("-of2", "--optionalFlag2", action = "store_true", help = "Another optional flag")
    parser.add_argument("-ro", "--restrictedOption", choices = ["a", "b", "c"], help = "One of [a, b, c]")
    parser.add_argument("--optionalWithDefault", nargs = "?", const = "valueWhenSpecifiedButNoValue", type = str, default = "valueWhenNotSpecified")
    args = parser.parse_args()

    print(f"First positional argument is {args.arg1}")
    print(f"Second positioning argument is {args.num}")
    if args.optional:
        print(f"Optional parameter: {args.optional}")
    if args.optionalFlag:
        print(f"Optional flag enabled")
    if args.optionalFlag2:
        print(f"Optional flag2 enabled")
    if args.restrictedOption:
        print(f"Restricted option value: {args.restrictedOption}")
    print(f"Optional argument with default value: {args.optionalWithDefault}")