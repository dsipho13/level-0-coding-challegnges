def maximum(*arg):
    largest = arg[0]
    for i in range(len(arg)):
        if largest < arg[i]:
            largest = arg[i]
    return largest


def main():
    print(maximum(10, 2, 53, 4, 51, 67, 7, 50))


if __name__ == "__main__":
    main()
