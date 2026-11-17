import re
phone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone.search("My number is thr 123-345-5678")
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups()) # output tuple
