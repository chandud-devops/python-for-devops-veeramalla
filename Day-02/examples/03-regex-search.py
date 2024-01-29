import re

text = "the quick brown fox"
pattern = r"quick"

search = re.search(pattern, text)
if search:
    print("Pattern is found:", search.group())
else:
    print("Pattern is not found")