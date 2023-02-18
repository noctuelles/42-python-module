import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.tracebacklimit = 0
        assert len(sys.argv) != 2, ("more than one argument are provided")
        assert type(sys.argv[1]) == int, ("argument is not an integer")

        i = int(sys.argv[1])
        if i == 0:
            print("I'm Zero.")
        else:
            print("I'm Even.") if i % 2 == 0 else print("I'm Odd.")
