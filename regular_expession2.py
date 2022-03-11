import re
string= 'Hello, Good Afternoon!!! Go to sleep!!!'
a=(re.search('sleep', string))
print(a.span())
print(a.start())
print(a.group())