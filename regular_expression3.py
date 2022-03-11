import re
string = "Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation"
pattern=re.compile('natural')
a=pattern.search(string)
print(a)
b=pattern.findall(string)
print(b)
c=pattern.fullmatch(string)
print(c)
d=pattern.match(string)
print(d)