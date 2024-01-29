import re

text = "apple,banana,oringe,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)