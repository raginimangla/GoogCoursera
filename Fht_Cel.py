def fht_cel(fhtemp): #fhtemp = temperature entered in degree celcius
    if fhtemp <= -459.4:
        return "Invalid input"

    else:
        return ((fhtemp - 32) // 1.8)

print(fht_cel(80))
print(fht_cel(-459.4))