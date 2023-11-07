"""
The picture is an example of how the solution should look like.
The hint is very important here: Exactly 3 big somethings, 1 small something, 3 big somethings; e.g. aXXXbYYYc.
There cannot be 4 big somethings on the left or right side.
The page title is "re" which might point to the re module to use regular expressions.

So the solution here is to first check the source code and again get a comment from it.
As a second step, one searches for all parts of the comment matching the criteria.
The last step is to concatenate the results.
"""

import re
from urllib import request

# Get the comment
with request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html") as response:
    content = response.read().decode("utf-8")
lastCommentIndexStart = content.rfind("<!--\n") + 5  # Plus for to skip "<!--\n"
lastCommentIndexEnd = content.rfind("\n-->")
commentToCheck = content[lastCommentIndexStart:lastCommentIndexEnd]

"""
Find all entries matching the criteria.
Some hints:
[A-Z] allows the characters A-Z, but only capital characters
[A-Z]{3} is like [A-Z] but expects 3 characters in sequence
[^A-Z] allows every character except A-Z, e.g. lower case characters or number
Therefore the used pattern searches for a sequence of characters which
1. Starts with anything but capital A-Z
2. Followed by exactly 3 capital A-Z
3. Followed by 1 lower a-z
4. Followed by exactly 3 capital A-Z
5. Followed by anything but capital A-Z
"""
result = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", commentToCheck)
if result is not None:
    # Finally concatenate everything
    solution = "".join(result)
    print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution) + ".html")
else:
    print("No result")
