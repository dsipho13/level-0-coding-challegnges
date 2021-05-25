def convert_to_farenheit(temperature):
    farenheit = (9 / 5) * temperature + 32
    return farenheit


def convert_to_celcius(temperature):
    celcius = (temperature - 32) * (5 / 9)
    return celcius


def main():
    print(convert_to_farenheit(28))
    print(convert_to_celcius(convert_to_farenheit(28)))


if __name__ == "__main__":
    main()
