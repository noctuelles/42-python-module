import sys
import string

if __name__ == "__main__":
    sys.tracebacklimit = 0
    assert len(sys.argv) == 3, ("invalid number of arguments.")
    args = sys.argv[1:3]

    assert args[1].isdigit(), ("second argument must be a positive integer.")
    words = args[0].split(" ")
    n = int(args[1])

    # Create a new list of string that contains more than n non-punctuation character.
    filtered_words = [word for word in words
                      if sum(1 for c in word if c not in string.punctuation) > n]
    # Then remove all the punctuation character.
    no_punctuation_words = [word.translate(str.maketrans('', '', string.punctuation))
                            for word in filtered_words]
    print(no_punctuation_words)
