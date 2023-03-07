import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.tracebacklimit = 0
        assert len(sys.argv) == 2, "more than one argument are provided"
        assert (
            sys.argv[1].isdigit()
            if sys.argv[1][0] != "-"
            else sys.argv[1][1:].isdigit()
        ), "argument is not an integer"

        i = int(sys.argv[1])
        if i == 0:
            print("I'm Zero.")
        else:
            print("I'm Even.") if i % 2 == 0 else print("I'm Odd.")
