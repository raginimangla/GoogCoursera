def greeting(gender, age):
    if age < 18:
        if gender == "Male" or gender == "M":
            return "Hello Young Sir!"
        elif gender == "Female" or gender == "F":
            return "Hello Young Miss!"
    elif age >=18:
        if gender == "Male" or gender == "M":
            return "Hello Sir!"
        elif gender == "Female" or gender == "F":
            return "Hello Miss!"

print(greeting("Male", 20))
print(greeting("M", 15))
print(greeting("Female", 10))
print(greeting("F", 65))