import re

text = "The quick brown fox"
pattern = r"quick"
match = re.match(pattern, text)
if match:
    print("Mach found:", match.group())
else:
    print("No mach")