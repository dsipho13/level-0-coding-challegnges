def triangleArea(x,y,r):
    semiparam = (x + y + r)/2 
    area = (semiparam * (semiparam - x)*(semiparam - y)*(semiparam -r) )**(0.5) #Heron's formula
    return area 

def main():
    print(triangleArea(3,3,3))

if __name__ == "__main__":
    main()

