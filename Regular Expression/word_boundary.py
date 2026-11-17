import re

str = "cat category dog"
result = re.findall(r'\bcat\b', str)
print(result)