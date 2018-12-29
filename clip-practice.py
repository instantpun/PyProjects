## string practice
import pyperclip
# import re

clipSource = pyperclip.paste()
clipPrune1 = clipSource.replace("\r", " ")
clipPrune2 = clipPrune1.replace("\newline", " ")
# clipPrune3 = clipPrune2.("\newline")

print(clipPrune1)

# clipTokens = clipSource.split("\r\n")

# print(clipTokens.strip("\r"))