def to_farenheit(temperature):
    farenheit = (9 / 5) * temperature + 32
    return farenheit


def to_celcius(temperature):
    celcius = (temperature - 32) * (5 / 9)
    return celcius


def main():
    print(to_farenheit(28))
    print(to_celcius(to_farenheit(28)))


if __name__ == "__main__":
    main()
