def maximum(*arg):
    x = list(arg)
    length = len(x)
    count = 0
    max_number = x[0]

    while count < length - 1:
        count =  count+1
        if max_number < x[count]:
             max_number = x[count]
    return max_number

print(maximum(11,7,5))
print(maximum(10,2,53,4,51,67,7,50))
