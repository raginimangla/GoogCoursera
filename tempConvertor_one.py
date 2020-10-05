def temp_convert(temp):
    if temp.endswith("C"):
        inttemp = int(temp[0:-1])
        if inttemp <= -273:
            return "Invalid input"

        else:
            return ((inttemp  * 1.8) + 32)

    if temp.endswith("F"):
        inttemp = int(temp[0:-1])
        if inttemp <= -459.4:
            return "Invalid input"

        else:
            return ((inttemp - 32) // 1.8)


print(temp_convert("0C"))
print(temp_convert("75F"))
