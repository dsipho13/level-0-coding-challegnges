def maximum(*arg):
    maxnumber = arg[0]
    for i in range(len(arg)):
        if maxnumber < arg[i]:
            maxnumber = arg[i]
    return maxnumber


def main():
    print(maximum(10, 2, 53, 4, 51, 67, 7, 50))


if __name__ == "__main__":
    main()
