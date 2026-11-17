import re

str = "Hello World"
result = re.findall(r'\AHello', str)
print(result)