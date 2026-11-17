import re

str = "Hello World"
result = re.findall(r'\S', str)
print(result)