def convertToF(temperature):
    farenheit = (9 / 5) * temperature + 32
    return farenheit


def convertToC(temperature):
    celcius = (temperature - 32) * (5 / 9)
    return celcius


def main():
    print(convertToF(28))
    print(convertToC(convertToF(28)))


if __name__ == "__main__":
    main()
