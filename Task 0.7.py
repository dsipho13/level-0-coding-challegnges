def cel_to_far(x):
    farenheit = (9/5)*x + 32
    return farenheit

print(cel_to_far(28))

def far_to_cel(y):
    celcius = (y - 32)*(5/9)
    return int(celcius)

print(far_to_cel(cel_to_far(28)))
