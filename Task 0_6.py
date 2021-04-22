def maximum(*arg):
    max_number = arg[0]
    for i in range(len(arg)):
        if max_number < arg[i]:
             max_number = arg[i]
    return max_number

def main():
    print(maximum(10,2,53,4,51,67,7,50))

if __name__ == "__main__":
    main()