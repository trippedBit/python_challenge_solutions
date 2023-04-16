"""
The page title is "now there are pairs".
The picture shows pants with an open zipper.
There is a comment "zip" in the source code.

The solution here is to change the URL from .html to .zip and download the file.
It contains a lot of txt files with the already known "next nothing is" game.
First, let's check the files' content.
Second, follow the hints to get a temporary solution from the comments.
Third, follow the last hint to get the final solution.
"""

import os
import shutil
from urllib import request
import zipfile

# Download the zip file
with request.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip") as response:
        content = response.read()
        with open("channel.zip", "wb") as file:
            file.write(content)
            file.close()

# Extract zip file
with zipfile.ZipFile("channel.zip", "r") as zipContainer:
    zipContainer.extractall("channel_extracted")
    zipContainer.close()

# Check the files' content
for entry in os.listdir("channel_extracted"):
    # Get the comment
    if entry == "." or entry == "..":
        continue

    with open("channel_extracted\\" + entry, "r") as file:
        content = file.read()
        file.close()
        # print(content)

"""
Now there are two hints:
hint1: start from 90052
hint2: answer is inside the zip
"""

nextNothing = "90052"
for counter in range(0, len(os.listdir("channel_extracted"))):
    # Get the comment
    with open("channel_extracted\\" + nextNothing + ".txt", "r") as file:
        content = file.read()
        file.close()
        # print(content)
        if "Next nothing is" in content:
            nextNothing = content.split("Next nothing is ")[1]  # Extract next nothing
            continue

"""
New hint: Collect the comments
And there is still: answer is inside the zip
"""

# Get the zip file comment
with zipfile.ZipFile("channel.zip", "r") as zipContainer:
    comment = zipContainer.comment.decode("utf-8")
    zipContainer.close()
    print(comment)  # The comment is empty

# Now try the individual files
comments = []
nextNothing = "90052"
with zipfile.ZipFile("channel.zip", "r") as zipContainer:
    # Get the individual file's comment
    while True:
        comments.append(zipContainer.getinfo(nextNothing + ".txt").comment.decode("utf-8"))
        content = zipContainer.read(nextNothing + ".txt").decode("utf-8")
        if "Next nothing is" in content:
            nextNothing = content.split("Next nothing is ")[1]  # Extract next nothing
            continue
        else:
            break

print("".join(comments))

"""
Using the collected comments as results leads to a new hint:
it's in the air. look at the letters.
Looking at the letters of the collected comments: O X Y G E N --> oxygen
"""

solution = "oxygen"
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution) + ".html")

# Clean up
os.remove("channel.zip")
shutil.rmtree("channel_extracted")