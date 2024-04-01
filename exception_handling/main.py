import traceback

if __name__ == "__main__":
    try:
        1 / 0
    except Exception as e:
        # Only prints the error but not the stack trace
        print(e)

    try:
        1 / 0
    except Exception as e:
        # Print stack trace
        traceback.print_exc()
