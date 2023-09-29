import re
from typing import List

if __name__ == "__main__":
    with open("resources/a-scandal-in-bohemia.txt", "rt") as fl:
        contents = fl.read()
    with open("resources/webpage.html", "rt") as fl:
        webpage = fl.read()

    # A compiled regex pattern is more efficient when a pattern will be used
    # multiple times
    words_that_start_with_th = re.compile(r"\bth.*?\b")
    links_in_webpage = re.compile(r"\"(https://.+?)\"")
    no_match = re.compile(r"foobar")

    # Return all non-overlapping matches of pattern in string
    ret: List[str] = re.findall(pattern=words_that_start_with_th, string=contents)

    # Return all links in webpage
    ret: List[str] = re.findall(pattern=links_in_webpage, string=webpage)

    # Find the first location where the pattern matches
    ret: re.Match = re.search(pattern=words_that_start_with_th, string=contents)
    print(ret)
    ret.start()  # start of match
    ret.end()  # end of match
    ret.span()  # returns tuple (start, end) of match
    contents[ret.start() : ret.end()]  # string that matched

    # Check if the string matches the pattern starting from the beginning of the
    # string
    ret: re.Match = re.match(
        pattern=words_that_start_with_th,
        string="this string will match because the first word starts with th",
    )
