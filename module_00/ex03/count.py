import string
import sys

def text_analyzer(text):
    """This function counts the number of upper characters, lower characters,
       punctuation and spaces in a given text."""
    sys.tracebacklimit = 0
    assert type(text) is str and text is not None, ("argument is not a string.")
    while text is None or len(text) == 0:
        text = input('Type a text to be analyze : ')

    count = lambda l1,l2: sum(1 for x in l1 if x in l2)

    upper_case = count(text, string.ascii_uppercase);
    lower_case = count(text, string.ascii_lowercase);
    punc = count(text, string.punctuation);
    space = count(text, " ");

    print(f"""The text contains {len(text)} character(s):
- {upper_case} upper letter(s)
- {lower_case} lower letter(s)
- {punc} punctuation mark(s)
- {space} space(s)""")

if __name__ == "__main__":
    sys.tracebacklimit = 0
    assert len(sys.argv) <= 2, ("more than one argument is provided")
    if len(sys.argv) > 1:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer(None)
