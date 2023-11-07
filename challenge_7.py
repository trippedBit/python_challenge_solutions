"""
The page title is "smarty".
The picture shows lake or river and line of grey/black squares.

The solution here must be in the grey/black squares.
1. Download the picture.
2. Read the image and get some basic information.
3. Get the middle row and find out that each R, G, B, A information repeats 7 times.
4. Reduce the information to just occurence for each information.
5. Remove the pixel information at the end, which does not repeat 7 times.
6. Map the pixel information to characters to get a hint.
7. Convert the numbers given as string (e.g. '123') in the hint into numbers ('123' becomes 123)
8. Map the numbers to characters to get the solution.
"""

import os
from PIL import Image
import re
from urllib import request

# Download the picture
with request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png") as response:
    content = response.read()
    with open("oxygen.png", "wb") as file:
        file.write(content)
        file.close()

image = Image.open("oxygen.png")

# Get basic information
imageWidth = image.width
imageHeight = image.height
print(str(imageWidth) + ", " + str(imageHeight))

# Get middle pixel row which is also part of the grey/black pixels.
middleRow = [image.getpixel((x, imageHeight / 2)) for x in range(imageWidth)]
# print(middleRow)
# The print above should show that every information is there 7 times, therefore reduce it to just one occurence.
middleRow = middleRow[::7]

# Remove the pixels at the end which do not repeat
middleRowCleaned = [r for r, g, b, a in middleRow if r == g == b]  # R, G, B are the same for each relevant pixel.
# print(middleRowCleaned)

image.close()

print("".join(map(chr, middleRowCleaned)))  # Assuming the numbers can be mapped to characters.

# The last print showed a hint
numbers = re.findall("\\d+", "".join(map(chr, middleRowCleaned)))
print(numbers)

solution = "".join(map(chr, map(int, numbers)))  # Finally map the numbers to integers to map the integers to characters.
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution) + ".html")

# Clean up
os.remove("oxygen.png")
