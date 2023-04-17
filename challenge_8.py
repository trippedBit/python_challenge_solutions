"""
The page title is "working hard?".
The picture shows a bee and flowers.
The picture is linked to a site which needs username and password.
There is a text "Where is the missing link?"
There is a comment with "un" and "pw" in the source code.

The solution here is to know that username and password are bz2 compressed. 
"""

import bz2

usernameDecompressed = bz2.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
print(usernameDecompressed)

passwordDecompressed = bz2.decompress(b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
print(passwordDecompressed)

solution = "good"
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/def/" + str(solution) + ".html")