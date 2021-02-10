def func(i):
    j = i / 60
    hour = j // 1
    hour = int(hour)
    minute = (j - hour) * 10
    minute = int(minute)
    strhour = " hour"
    strmin = " minute"
    if( hour != 1):
        strhour += "s"
    if( minute != 1):
        strmin += "s"
    print(str(hour) + strhour +" and " + str(minute) + strmin)

time = int(input("Please enter a number"))

func(time)
