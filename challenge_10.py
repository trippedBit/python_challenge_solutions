"""
The page title is "what are you looking at?".
The picture shows a standing and a laying cow.
There is the hint "len(a[30] = ?")
The standing cow is linked to http://www.pythonchallenge.com/pc/return/sequence.txt.

The solution here is understand how the sequence works, calculate the 30th element and get its length.
"""

import re

"""
The sequence.txt says "a = [1, 11, 21, 1211, 111221, ", no additional information.
Search for it, you will find https://en.wikipedia.org/wiki/Look-and-say_sequence.
1
11
21
1211
111221
312211
"""

numberString = "1"
res = re.findall("(\\d)(\\1*)", "1211")
print(res)
"""
The line above returns the following:
[('1', ''), ('2', ''), ('1', '1')]

Based on the wiki page linked above we know, the next number should be:
"one 1, one 2, two 1" = 111221

The tuples show us:
- There is one 1
- There is one 2
- There are two 1

So this can be used to build the next number.
Start is an empty string ("")       -> Result string = ""
Append len(i+j) = len("1"+"") = 1   -> Result string = "1"
Append i itself = 1                 -> Result string = "11"
Append len(i+j) = len("2"+"") = 1   -> Result string = "111"
Append i itself = 2                 -> Result string = "1112"
Append len(i+j) = len("1"+"1") = 2  -> Result string = "11122"
Append i itself = 1                 -> Result string = "111221"
"""
print("".join(str(len(i+j))+i for i,j in re.findall("(\\d)(\\1*)", "1211")))

# To get the 30th number and its length, just start with "1" as input and repeat the function 30 times
for i in range(30):
    numberString = "".join(str(len(i+j))+i for i,j in re.findall("(\\d)(\\1*)", numberString))

solution = str(len(numberString))
print("The URL for the next challenge is: http://www.pythonchallenge.com/pc/return/" + str(solution) + ".html")