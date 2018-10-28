print("Let's practice everything!")
print("You'd need to know \"bout escapes with \\ that do:")
print('\n newlines and \t tabs')
poem = """
\tThe lovely word
with logic so firmly planted
cnanot discern \s the needs of lovenor comprehend passion from intution
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6
print(f"This should be five:{five}")

def secrect_formula(started):
    jelly_beans = started * 509
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

started_point = 10000
beans, jars, crates = secrect_formula(started_point)

print("With a starting point of {}".format(started_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
started_point = started_point / 10
print("We can also do that this way.")
formula = secrect_formula(started_point)
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
