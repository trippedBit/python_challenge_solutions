"""
The picture shows some character shifts, e.g. K becomes M.
The shift for all three character pairs is 2.
And there is a hint one should think twice.

So the solution here is to first shift all characters in the given text.
The result tells you to apply the same action to the url.
"""

def shift_text(text: str,
               shift: int) -> str:
    newString = ""
    for element in text:
        if element in abc:
            if abc.index(element) <= 23:
                newString = newString + abc[abc.index(element) + shift]
            elif abc.index(element) == 24:
                newString = newString + abc[0]
            elif abc.index(element) == 25:
                newString = newString + abc[1]
        else:
            newString = newString + element
    return newString

givenString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

abc = ["a", "b", "c", "d", "e",
       "f", "g", "h", "i", "j",
       "k", "l", "m", "n", "o",
       "p", "q", "r", "s", "t",
       "u", "v", "w", "x", "y",
       "z"]

shift = 2

result1 = shift_text(givenString, shift)
print("New string: " + result1 + "\n")

# The previous print told us to apply the action to the current URL which is "map"
result2 = shift_text("map", shift)
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(result2) + ".html")
