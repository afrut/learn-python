# Unicode is a character set. Each character is converted to a decimal number.
# utf-8 is an encoding scheme that converts the decimal representation to
# the bits/bytes format used by the machine.
# Python defaults to using utf-8 to represent strings.
# u"some string" is a Unicode string.
# b"some string" is a byte string.
from random import randint
from printAttr import printAttr
if __name__ == "__main__":
    # ord() returns the decimal representation of a character
    print("Decimal representation of a: {}".format(ord("a")))

    # chr() returns the Unicode character given the decimal representation.
    print("Unicode character of 97: {}".format(chr(97)))

    # Convert a string to bytes using an encoding scheme.
    str1 = "The quick brown fox jumps over the lazy dog"
    enc1 = str1.encode("ascii")
    print("str1: {}".format(str1))
    print("Byte representation of str1 using ascii: {}".format(enc1))
    print("Decimal representation enc1 byte 0: {}".format(enc1[0]))
    print("Binary representation enc1 byte 0: {:08b}".format(enc1[0]))
    print("Character set representation of enc1 byte 0: {}".format(chr(enc1[0])))

    # The letters ab in bytes expressed as a hex literals.
    enc2 = b"\x61\x62"
    print("The letters a and b decoded using ascii: {}".format(enc2.decode("ascii")))

    # Up and down arrows in bytes specified as decimals.
    enc3 = bytes([226, 134, 145]) + bytes([226, 134, 147])
    print("Up and down arrows decoded using utf-8: {}".format(enc3.decode("utf-8")))

    # Left and right arrows in bytes specified as binary literal bytes.
    enc4 = bytes([0b11100010,0b10000110,0b10010000]) + bytes([0b11100010,0b10000110,0b10010010])
    leftright = enc4.decode("utf-8")
    print("Left and right arrows decoded using utf-8: {}".format(leftright))

    # Try to encode left-right arrows in ascii
    try:
        leftright.encode("ascii")
    except UnicodeError:
        print("Cannot convert {} to ascii bytes".format(leftright))
