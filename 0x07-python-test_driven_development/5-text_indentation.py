#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":
        # print(delim, text.split(delim))
        text = (delimiter + "\n\n").join(
                    [line.strip(" ") for line in text.split(delimiter)])

    print(text, end="")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/5-text_indentation.txt")
