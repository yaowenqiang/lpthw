my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 100 # lbs
my_eyes = 'Blue'
my_teath = 'White'
my_hair = 'Brown'


print(f"Let's talk about {my_name}.") # not work on python 2 f stand for format
print(f"He's {my_height} inches tall.") 
print("He's {my_height} inches tall.")  # won't print the variable
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teach are usually {my_teath} depending on the coffee.")

# this line is tricky,try to get it exactly right

total = my_age + my_height + my_weight


print(f"If I add {my_age}, {my_height}, and {my_weight} I got {total}")
