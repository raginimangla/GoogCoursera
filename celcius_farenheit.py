def cel_fht(celtemp): #celtemp = temperature entered in degree celcius
    if celtemp <= -273:
        return "Invalid input"

    elif celtemp > -273:
        return ((celtemp * 1.8) + 32)



print(cel_fht(25))
print((cel_fht(-273)))