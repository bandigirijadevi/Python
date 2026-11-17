import re

str = "Hello_123!"
result = re.findall(r'\w', str)
print(result)