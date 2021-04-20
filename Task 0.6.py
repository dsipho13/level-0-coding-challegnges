def maximum(*arg):
    length = len(arg)
    count = 0
    max_number = arg[0]

    while count < length - 1:
        count =  count+1
        if max_number < arg[count]:
             max_number = arg[count]
    return max_number

print(maximum(11,7,5))
print(maximum(10,2,53,4,51,67,7,50))
