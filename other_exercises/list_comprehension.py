numbers = [1, 2, 3, 4, 5]
# lambda function = {new_item for item in items}
new_number = {n+1 for n in numbers}
print(new_number)

# Strings
user_name = "Fernando"
# lambda function = {new_item for item in items}
name_character = [letter for letter in user_name]
print(name_character)

# challenge 1: Double the value in a range

# 5 is exclusive [1,2,3,4]
my_range = range(1, 5)
# lambda function = {new_item for item in items}
doble_my_range = [n * 2 for n in my_range]
print(doble_my_range)
# second alternative
print([n * 2 for n in range(1, 5)])

# Conditional List comprehension
names_list = ["John", "Felix", "McNeal", "Thompson", "David", "Lee"]
shortname_list = [name for name in names_list if len(name) < 5]
print(shortname_list)

# challenge #2
cap_longname_list = [name.upper() for name in names_list if len(name) > 5]
print(cap_longname_list)
