import re

str = "Hello@123!"
result = re.findall(r'\W', str)
print(result)