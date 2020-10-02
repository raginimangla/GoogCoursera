def greeting(gender):
    if gender == "Male" or gender == "M":
        return "Hello Sir!"
    elif gender == "Female" or gender == "F":
        return "Hello Miss!"
    else:
        return "Hello there!"

print(greeting("Male"))
print(greeting("M"))
print(greeting("Female"))
print(greeting("F"))