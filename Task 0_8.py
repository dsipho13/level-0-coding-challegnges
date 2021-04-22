def toHours(time):
    hour = time // 60
    minute = time - (hour * 60)
    strhour = " hour"
    strmin = " minute"
    if( hour != 1):
        strhour += "s"
    if( minute != 1):
        strmin += "s"
    print(f"{hour} {strhour} and {minute} {strmin}")

def main():
    toHours(121)

if __name__ == "__main__":
    main()
