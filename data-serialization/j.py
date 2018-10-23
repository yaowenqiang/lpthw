import json

a = json.dumps({'isbn':'9780262510875','title':'Structure and Interpretation of Computer Programs - 2nd Edition'})
print(a)
b = json.loads('{"isbn":"9780262510875","title":"Structure and Interpretation of Computer Programs - 2nd Edition"}')
print(b)


