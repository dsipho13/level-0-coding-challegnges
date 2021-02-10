def celcius_to_farenheit(x):
    """ a function that converts celcius to farenheits
    """
    farenheit = (9/5)*x + 32
    return farenheit

print(celcius_to_farenheit(28))

def farenheit_to_celcius(y):
    """ a function that converts farenheits to celcius
    """
    celcius = (y - 32)*(5/9)
    return int(celcius)

print(farenheit_to_celcius(celcius_to_farenheit(28)))
