"""
This challenge starts with a little joke. You have to replace the html URL with a php URL.
The hints are:
1. The title is "follow the chain".
2. The picture shows a chainsaw according to its filename and it is linked to site ending with "nothing=12345".
3. The page from hint 2 says "the next nothing is 44827".
4. The page source code contains an information that 400 nothings are enough.


So the solution here is pretty simple:
Just follow the chain by changing the URL based on the next nothing and follow the instructions.
"""

from urllib import request

nextNothing = "12345"
for counter in range(0, 400):
    # Get the comment
    with request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nextNothing) as response:
        content = response.read().decode("utf-8")
        print(content)
        if "next nothing is" in content:
            nextNothing = content.split("next nothing is ")[1]  # Extract next nothing
            continue
        elif "Divide by two" in content:  # After some nothings there is a prompt to divide the number by to
            # nextNothing is a string. To divide it, it must be converted into an integer
            # and then back into a string for use in the URL.
            nextNothing = str(int(nextNothing) / 2)
            continue
        else:
            solution = content
            break

# The solution already contains ".html"
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution))
