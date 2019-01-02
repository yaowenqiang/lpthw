import re
m = re.search("(?<=abc)def", "abcdef")
print(m.group(0))
n = re.search('\\\\', '\\')
print(n.group(0))

p = re.compile("ab*")
dir(p)
