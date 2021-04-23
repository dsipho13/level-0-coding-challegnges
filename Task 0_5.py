def triangle_area(length,height,width):
    semiparam = (length + height + width)/2 
    area = (semiparam * (semiparam - length)*(semiparam - height)*(semiparam -width) )**(0.5) #Heron's formula
    return area 

def main():
    print(triangle_area(3,3,3))

if __name__ == "__main__":
    main()

