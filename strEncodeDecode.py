# Python defaults to using utf-8 to represent strings.
# u"some string" is a Unicode string.
# b"some string" is a byte string.
# watchFiles -Command python -FileFilters ".+\.py" -Clear -Clear
from random import randint
from printAttr import printAttr
from sys import byteorder   # Machine's "endianness". big or little endian
import re # Regular expressions module

# Return the character represented by an in using utf-16
def intToChar16(x: int):
    # byte order is the machine's endian-ness
    return int.to_bytes(x, 2, byteorder).decode("utf-16")

# Remove all unicode characters by attempting to encode into ascii
def toAsciiReplace(x: str) -> tuple:
    # Try to encode to ascii
    _bytes = x.encode("ascii", errors = "xmlcharrefreplace")

    # Find all instances of replaced characters
    prog = re.compile("&#(\d+); ?")
    result = list(re.finditer(prog, str3))

    # For all matches, store the character, their locations and remove from
    # original string
    retStr = ""
    i = 0
    lsChars = list()
    lsInd = list()
    for mch in result:
        # Decimal that represents the character in utf-16
        dec = int(mch.group(1))

        # Store the actual unicode character
        lsChars.append(int.to_bytes(dec, 2, byteorder).decode("utf-16"))

        # Store the start and stop indices
        lsInd.append((mch.start(), mch.end()))

        # Slice original string to obtain string without unicode characters.
        str4 = str4 + str3[i:mch.start()]

        # Update the start of the next slice to be the end of the current regex match.
        i = mch.end()

    return (str4, tuple(lsChars), tuple(lsInd))


if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    print("  Basics")
    print("----------------------------------------------------------------------")
    # An integer and its decimal, binary and hex representations
    someInt = 0x54  # in hexadecimal
    print("Decimal: {:d}".format(someInt))
    print("Hexadecimal: {:#x}".format(someInt))
    print("Binary: {:#b}".format(someInt))
    print("Octal: {:#o}".format(someInt))
    print("")

    print("----------------------------------------------------------------------")
    print("  Bytes")
    print("----------------------------------------------------------------------")
    # 1 byte = 8 bits; has range in decimal 0 - 255
    # The bytes functions takes a list of int and returns a string of bytes
    # A byte can be thought of as an int between 0 - 255
    bytes1 = bytes([x for x in range(10)])
    print(f"bytes1 = {bytes1}")
    print('')

    print("----------------------------------------------------------------------")
    print("  Characters")
    print("----------------------------------------------------------------------")
    # Characters are represented by a byte or series of bytes.
    # Unicode is a set of characters.
    # utf-8 is an encoding scheme that maps a character to a series of bytes.
    # Take a byte and return the character it represents.
    char1 = bytes([97]).decode("utf-8")
    print(f"A single byte with value 97 represents the character \"{char1}\"")

    # A character can be encoded into a series of bytes using an encoding scheme.
    # Encode a character using utf-8.
    bytes2 = "b".encode("utf-8")
    print("Character \"b\" has utf-8 representation {:d}".format(bytes2[0]))

    # Python uses utf-8 by default. When the object bytes is printed,
    # Python decodes the bytes using utf-8.
    print(f"bytes2 = {bytes2}")

    # ord() returns an int representing the character
    print("Int representing a: {}".format(ord("a")))

    # chr() returns the Unicode character given the decimal representation.
    print("Unicode character of 97: {}".format(chr(97)))

    print("----------------------------------------------------------------------")
    print("  Strings")
    print("----------------------------------------------------------------------")
    # Strings are ultimately a series of bytes.
    bytes3 = bytes([97, 98, 99])
    print(f"bytes3 = {bytes3}")
    print("bytes3 decoded = {}".format(bytes3.decode())) # utf-8 is default

    # Strings can also be converted to the bytes that represent it.
    str1 = "some string"
    bytes4 = str1.encode() # utf-8 is default
    print(f"str1 = {str1}")

    # Get a list of bytes from the bytes object.
    lsbytes1 = list(bytes4)

    # Get a string that represents the series of bytes in hexadecimal.
    hexstr1 = ",".join("{:#x}".format(byte) for byte in bytes4)
    print(f"\"some string\" = {hexstr1}")
    print('')

    print("----------------------------------------------------------------------")
    print("  Unicode and Ascii")
    print("----------------------------------------------------------------------")
    # utf-8 and ascii are both encoding schemes.
    # Sometimes a string contains a unicode character
    # The 3 bytes 226, 134, 145 represent the up arrow in utf-8.
    str2 = "another " + bytes([226, 134, 145]).decode() + "string" +\
        " with more " + int.to_bytes(8734,2,byteorder).decode("utf-16") +\
        " unicode characters" + int.to_bytes(176,2,byteorder).decode("utf-16")
    print(f"str2 = {str2}")

    # Attempting to encode this in a format that is not compatible will result
    # in an error.
    try:
        str2.encode("ascii")
    except UnicodeEncodeError:
        print(f"ERROR: Cannot encode \"{str2}\" in ascii!")

    # A number of options exist for handling encoding errors.
    # Replacing with a question mark is not as useful
    bytes5 = str2.encode("ascii", errors="replace")
    print(f"bytes5 = {bytes5}")

    # ------------------------------
    # Replacing with HTML numeric code is better
    # ------------------------------
    # See toAsciiReplace() for a function that does similar things.
    # The pattern is "&#(int);". The unicode character can be retrieved from this
    # int by converting it to bytes in little endian endian and
    # decoding it using utf-16. See intToChar16().
    bytes6 = str2.encode("ascii", errors="xmlcharrefreplace")
    str3 = bytes6.decode("ascii")       # Get the ascii string
    print(f"bytes6 = {bytes6}")
    print(f"str3 = {str3}")

    # Use regex can be used to extract these characters and clean the string.
    prog = re.compile("&#(\d+); ?")

    # Return a list of match objects of every match.
    result = list(re.finditer(prog, str3))

    # Remove the unicode characters from the original string
    str4 = ""
    i = 0
    for mch in result:
        # Decimal that represents the character in utf-16
        dec = int(mch.group(1))

        # The actual unicode character
        char = int.to_bytes(dec, 2, byteorder).decode("utf-16")

        # Slice original string to obtain string without unicode characters.
        str4 = str4 + str3[i:mch.start()]

        # Update the start of the next slice to be the end of the current regex match.
        i = mch.end()
    print(f"String without unicode characters str4 = {str4}")

    # Same as xmlcharrefreplace but with \\u(int) that represents the int in hexadecimal.
    bytes7 = str2.encode("ascii", errors="backslashreplace")
    print(f"bytes7 = {bytes7}")

    # Replace with character name.
    bytes8 = str2.encode("ascii", errors="namereplace")
    print(f"bytes8 = {bytes8}")

    # Purged cached regular expression that were passed to re.compile().
    re.purge()
