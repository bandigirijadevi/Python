import re

str = "Hello123"
result = re.findall(r'\D', str)
print(result)