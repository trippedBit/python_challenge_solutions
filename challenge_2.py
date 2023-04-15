"""
The picture shows some book pages, but nothing readable.
The hint says, the characters might be in the page source.

So the solution here is to first check the source code and get this comment.
As a second step, one creates a dictionary to count the amount of each character in the comment.
The last step is to build a string using all characters which appear only once.
"""

from urllib import request

# Get the comment
with request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html") as response:
    content = response.read().decode("utf-8")
lastCommentIndexStart = content.rfind("<!--\n") + 5  # Plus for to skip "<!--\n"
lastCommentIndexEnd = content.rfind("\n-->")
commentToCheck = content[lastCommentIndexStart:lastCommentIndexEnd]

# Create the dictionary
characterDictionary = {}
for character in commentToCheck:
    if character not in characterDictionary.keys():
        characterDictionary[character] = 1
    else:
        characterDictionary[character] = characterDictionary.get(character) + 1
print(characterDictionary)

solution = ""
for char, value in characterDictionary.items():
    if value == 1:
        solution = solution + char

print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution) + ".html")