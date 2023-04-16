"""
The page title is "peak hell".
The picture shows a green hill.
The hint is "pronounce it".
There is a file "banner.p" mentioned in the source code.

The solution here is to use a module called pickle which sounds a bit like "peak hell".
First, use pickel on the content of banner.p.
Second, see the resulting list of paired characters and numbers.
Third, print the characters as often as given by the numbers.
"""

import pickle
from urllib import request

# Get the banner and use pickle on it
with request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p") as response:
    pickleString = pickle.load(response)

# Print the character k v times
for line in pickleString:
    print("".join([k * v for k, v in line]))

solution = "channel"  # The print in the line above should show this.
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution) + ".html")