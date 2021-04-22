def toFarenheit(temperature):
    farenheit = (9/5)*temperature + 32
    return farenheit

print(toFarenheit(28))

def toCelcius(temperature):
    celcius = (temperature - 32)*(5/9)
    return int(celcius)

def main():
    print(toCelcius(toFarenheit(28)))

if __name__ == "__main__":
    main()