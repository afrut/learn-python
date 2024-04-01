#python in_funcs.py --in_func1_known value --other_args other_value
import argparse

def func():
    # Can access arguments from within a function
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_func1_known")
    known_args, other_args = parser.parse_known_args()
    print(f"known_args = {known_args}")
    print(f"other_args = {other_args}")

if __name__ == "__main__":
    func()